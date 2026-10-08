---
title: "Limits of Cross-Platform Code"
categories: dataeditor
date: 2026-10-08
mastodon:
bluesky:
tags:
  - data editor tips
  - reproducibility
  - replication packages
  - computational requirements
  - Code
  - Python
  - MacOS
  - Linux
---

<!--
Bluesky version (each paragraph < 300 characters):

1/ The authors' README: "Runs in 12h40m on a Mac with 24 GB of RAM." Our Linux server: crashed out of memory. With 64 GB. With 180 GB. With 1,000 GB. Same code, same data. A thread on the limits of cross-platform code. 🧵

2/ The crash: same line every time, factoring one large sparse matrix with SciPy's splu (SuperLU). Peak ~150 GB, with 1,000 GB available. Reload the same matrix from disk: same error after 2 min, at <3 GB. SuperLU gives up; the RAM isn't full.

3/ We (with AI help) ruled out six suspects: Python version, stale caches, wasted zeros in the matrix, the ordering heuristic, integer limits, MKL. Each change: same crash.

4/ On a 64 GB Mac, the unmodified code got through that step 9 times. Process memory looks like <50 GB, but macOS is compressing ~92 GB of data into ~38 GB of RAM. The Mac doesn't need less memory. It hides it, and pays in time.

5/ Same code. Same NumPy, SciPy, JAX versions on Mac and Linux. But the layers underneath differ: SciPy's bundled SuperLU sits on Apple's Accelerate on the Mac, on OpenBLAS on Linux. "Portable" code stops at those layers.

6/ Lessons: report memory needs for the platform you used, and say so. If you can, test on a second OS. And, for us: computational requirements are measurements on one system, not guarantees for others.

https://aeadataeditor.github.io/dataeditor/memory-across-platforms
-->

A recent replication package came with a throw-away description in the README of one minor part of the processing: a Python notebook running in about 12 hours and 40 minutes on a MacBook Pro with 24 GB of RAM. We tried it first on a shared Windows machine with 128 GB, and it failed with some memory error. That happens all the time (too many people on the machine), so we switched to our Linux HPC cluster. One of the nodes has 1,000 GB. Surely that would solve that little problem.

Nothing worked.

Here is what we learned about the limits of "cross-platform" code.[^claude]

<!-- more -->

## The setup

The relevant part of the code is a [Jupyter](https://jupyter.org/) notebook using Python that solves a large dynamic model. It uses the standard scientific Python stack: [NumPy](https://numpy.org/), [SciPy](https://scipy.org/), and [JAX](https://docs.jax.dev/). Python, NumPy, and SciPy are all widely considered portable. You write the code once, and it runs anywhere.

The authors ran it on an Apple Silicon Mac with 24 GB of RAM.

## Windows: out of memory

Our first attempt was on a Windows server with 128 GB of RAM. It failed at the dynamic solve step:

```text
JaxRuntimeError: INTERNAL: Error dispatching computation: Out of memory allocating 146669667649 bytes.
```

For those who do not read long numbers, that's about 147 GB. Far more than the server has, and more than the code supposedly uses.

## Linux: same result, but a more complicated story emerges

We moved to a Linux compute cluster. Our [cluster](https://biohpc.cornell.edu/Default.aspx) has nodes from 128 GB to 1,000 GB. That should work. Or so we thought. The RA submitted [SLURM](https://biohpc.cornell.edu/lab/userguide.aspx?a=bioslurm) jobs reserving (for exclusive use) 24 GB. Then 64 GB. Then 180 GB, 240 GB, and finally 1,000 GB. Every run failed with some sort of memory error, though not always the same. The initial runs failed because the SLURM manager declared [OOM](https://en.wikipedia.org/wiki/Out_of_memory) and killed the job. But at 180 GB, a different error emerged: a `MemoryError` inside [`scipy.sparse.linalg.splu`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.splu.html), while factoring one large sparse matrix (the Hessian of the optimization problem, 204,200 rows and columns). Each run climbed for **about an hour**, to a peak of roughly **147-150 GB**, and died at the same line. Note that the peak is very close to the 147 GB that JAX wanted on Windows.

That happened even with 1,000 GB available, suggesting that it is NOT just "the computer ran out of memory." Indeed, beyond 180 GB, the job was never killed by the operating system or the cluster scheduler. The error was persistently occurring within "SuperLU", and Python itself was now reporting `MemoryError`.

AI-assisted debugging[^AI2] pinpointed some additional info. Take the same matrix, saved to disk by the code, load it into a fresh Python session and call `splu` on it with the same options. It failed with the same error, but after about **two minutes**, having used **less than 3 GB**.

## Ruling out some cases

With help from an AI coding assistant, we went through the plausible suspects one at a time:

1. **The Python version.** The initial Python version was the stock Python provided by the cluster (3.12). We rebuilt the environment with Python 3.14, which is the version recorded in the notebook's metadata. We used [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) to do so, but installed [PyPI](https://pypi.org/) packages. Same crash.
2. **Stale cached files.** The code caches intermediate results. We deleted them and started fresh. Same crash.
3. **Wasted space in the matrix.** AI determined that a helper function was storing about 77% of the (sparse) matrix entries as explicit zeros (338 million stored entries, where the true density was 0.19%). Dropping them cut the stored entries to 79 million. But fixing it did not change the peak memory at the crash.
4. **The ordering heuristic.** AI told me that sparse factorization reorders the matrix to limit "fill-in", the new non-zero entries created during factorization. Switching SuperLU's ordering from the default (`COLAMD`) to an alternative (`MMD_AT_PLUS_A`) produced an identical crash: same line, same ~148 GB, same runtime.
5. **Integer limits.** SciPy's SuperLU indexes matrices with 32-bit integers, which can overflow on very large problems. This matrix is comfortably within range.
6. **Back to conda: MKL.** We tried to use the Intel MKL version of SciPy installed via conda, instead of the pip-installed version. Same crash.

We did not go and try to refactor the code. That is a different problem for future users of this replication package. Nothing within the scope of purportedly cross-platform code worked.

## Back to a Mac

The authors ran this on "Apple M4 Pro, 24 GB RAM" for around 12h, according to their README. We then found a Mac Studio with "Apple M4 Max, 64 GB of RAM." After more than 21 hours, it had not crashed, but also had not finished. AI analysis showed that it had gone through the `splu` factorization that killed every Linux run, and did so nine times, for different matrices, about 1h20m per case.

How much memory is it using? That depends on how you count:

- The process's resident memory (RSS) is typically 15-27 GB, and peaked (in our 30-second sampling) at 48.5 GB.
- Swap to disk (SSD) fluctuates between 2 and 13 GB.
- But RSS on macOS does not count _compressed_ memory. The AI checked: macOS's memory compressor (system-wide, but this job is by far the largest thing running) was holding about **92 GB of data, squeezed into about 38 GB of physical RAM**.


## Why does it fail?

The Python code is identical on all systems. Even the versions of the key Python packages are identical between the Mac and Linux runs. What is _not_ identical is everything underneath:

|                     | Our Mac                                   | Our Linux                                           |
|---------------------|-------------------------------------------|-----------------------------------------------------|
| Hardware            | Apple M4 Max (ARM), 64 GB                 | Intel Xeon (x86_64), up to 1,000 GB                 |
| Python              | 3.12.13 (pip)                             | 3.14.8 (conda-forge); earlier also 3.12.7 (pip)     |
| NumPy / SciPy / JAX | 2.5.3 / 1.18.1 / 0.11.2                   | 2.5.3 / 1.18.1 / 0.11.2                             |
| Sparse LU           | SuperLU, bundled with SciPy               | SuperLU, bundled with SciPy                         |
| BLAS/LAPACK         | Apple Accelerate (version not reported)   | OpenBLAS 0.3.x, bundled with NumPy and SciPy        |
| Result at `splu`    | Succeeds (9 times so far, ~1h20m each)    | `MemoryError`, after ~1h at ~150 GB, or after 2 min at <3 GB |

**Some notes**

- **SuperLU is bundled.** The function that fails, `splu`, is a wrapper around [SuperLU](https://portal.nersc.gov/project/sparse/superlu/), a C library for sparse LU factorization. SciPy includes and compiles its own copy. Same `scipy` package, same `superlu`. That is good for consistency. But it also means that making system-level changes to numerical libraries is not a way out. We tried forcing Python to recognize MKL by installing it via `miniconda` (which includes it) vs. PyPI, which does not, but that did not work.[^minicondamkl]
- **Linear algebra underneath differs by platform.** But does it matter? SuperLU relies on BLAS routines for dense sub-blocks. On Apple Silicon, recent NumPy and SciPy builds use Apple's [Accelerate](https://developer.apple.com/documentation/accelerate) framework. On Linux (and Windows), the NumPy and SciPy packages include a copy of OpenBLAS. The AI tells me that these differ in floating-point details, and in a sparse factorization, small differences in which pivot gets picked can lead to very large differences in fill-in, and thus in memory.
- **The operating system manages memory differently.** macOS aggressively compresses memory and swaps to fast SSD storage. Windows also compresses memory by default; Linux can (via zswap or zram), but this is usually not enabled on HPC compute nodes. All three can swap to disk. If swap is used, speed declines. Our Mac run saw 92 GB compressed into 38 GB – which should fit in memory - and yet saw some swap usage as well. Almost certainly, the authors' run also used swap. Linux on a compute cluster, managed by a scheduler like [SLURM](https://slurm.schedmd.com/), does not need to compress memory this way. In our case, the job was provided with far more memory than it used at the point of failure. Is that somehow hard-coded into `superlu`/`scipy`?


This echoes an [earlier post]({% post_url 2026-07-24-stata-convergence-across-platforms %}), where the same Stata code converged or not depending on the number of processors used. Different software, different symptom, same lesson: "the code is the same" is not the same as "the computation is the same."

## Lessons

**For authors:**

- **Report computational requirements as measurements, and say where you measured them.** "24 GB of RAM" is a fact about one Mac, with its memory compression and its swap. See also [Florian Oswald's post](https://jpedataeditor.github.io/posts/20261001-ram-usage/). Measuring **actual** usage is important.
- **If you can, try a second platform.** Even a partial run, up to the most demanding step, would have revealed this problem (in fact, the Linux run can be made to fail very quickly). Many universities have Linux clusters available.
- **Provide the full list of dependencies with versions.** It eliminates one set of suspects, but it will not solve platform differences: in our case, identical package versions worked on one platform and failed on the other.

**For replicators (us included):**

- **"Portable" has limits.** Python, R, Julia, MATLAB code can be portable at the source level and still behave very differently at the level of the numerical libraries they call. When something fails on one platform, it is worth trying another before concluding the package is broken.
- **Memory requirements do not transfer across operating systems.** We will be more careful about how we read, and how we ask authors to report, memory requirements.


## About the AI assistance

[Editorial note by the AI: Lars made me write this...]

Three separate [Claude Code](https://claude.com/claude-code) sessions contributed to this post and to the work behind it. They did not share context. The drafting session asked the other two for technical details; the Mac session replied directly, and we relayed the Linux session's answer by hand.

| Session          | Role                                                                                       | Models                                   | Wall time  | Active (API) time | Cost   |
|------------------|--------------------------------------------------------------------------------------------|------------------------------------------|------------|-------------------|--------|
| Linux cluster    | Set up environments, submitted jobs, tested the six hypotheses, wrote up diagnostics (146 lines of code added, 51 removed) | Claude Sonnet 5 (most), Claude Opus 5, Claude Haiku 4.5 | 1d 3h 46m  | 38m 31s           | $11.50 |
| Mac | Monitored the running job without interfering; collected memory statistics and software stack details | Claude Sonnet 5.5 (most), Claude Haiku 4.5 | 21h 24m | 25m 29s | $10.51 |
| This post | Drafted the post from our replication notes and the other two sessions' reports | Claude Opus 5.5 | n/a | n/a | $1.80 (estimated, via ccusage) |

Costs are as reported by Claude Code itself, except for the drafting session, which ran in an editor that does not report them; that figure is an estimate from [ccusage](https://github.com/ryoppippi/ccusage), which came within about 7% of Claude Code's own figure for the Linux session. Most of the wall time is waiting: for cluster jobs to fail, and for the Mac job to run. The time the models actually spent working is a small fraction of that.

[^claude]: With assistance from Claude Code; see [About the AI assistance](#about-the-ai-assistance) at the end of this post. The Windows run was done manually by one of our replicators. The decisions about what to test, and the final text, are mine, as are any remaining errors.

[^AI2]: Claude ran various diagnostics on the Linux cluster and the Mac, collecting memory usage statistics and software stack details for both platforms.

[^minicondamkl]: We rebuilt the environment with `miniconda`. We only tried a simple test (load cached matrix → `splu` directly). The first conda build  resolved to OpenBLAS (reported generically via pkg-config,  confirmed as OpenBLAS by `conda list`). We then also tried with an MKL build. pip/OpenBLAS (job 865), conda-forge/OpenBLAS (job 866), and conda defaults/MKL (job 867, confirmed MKL 2025.0.0, defaults channel) completed, same result: `MemoryError`: Not enough memory to perform factorization, ~2.5GB peak RSS, ~1m28s. BLAS backend (OpenBLAS vs. MKL) makes no difference either, for this particular code path . See <https://gist.github.com/larsvilhuber/de88073e7416f2009e38a0fdac745126>.