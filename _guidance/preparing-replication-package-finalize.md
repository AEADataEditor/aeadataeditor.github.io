---
title: "Finalize README"
toc: true
date: 2026-02-16
---

[◀ Back to Checklist](preparing-replication-package) | [Back to Details](preparing-replication-package-details) | [◀ Previous: Step 5](preparing-replication-package-step5)

### Finalize README

> Reference: <https://social-science-data-editors.github.io/template_README/template-README.html>

This step is usually not necessary, but you want to just make sure that your README has the necessary information that help set expectations about computational feasibility, based on the steps above. 

- [**Software**:](https://social-science-data-editors.github.io/template_README/template-README.html#software-requirements) If you used a container, specify which container you used (name and tag, e.g., `dataeditors/stata18_5-mp:2025-02-26`). Be precise when describing the StataMP version - the number of cores matters! (`StataMP-4` may not behave the same way as `StataMP-8`.)
- [**Hardware**:](https://social-science-data-editors.github.io/template_README/template-README.html#memory-runtime-storage-requirements) Verify that the description of your computer (CPU, number of cores, RAM, disk space) is accurate.
- [**Run time**:](https://social-science-data-editors.github.io/template_README/template-README.html#memory-runtime-storage-requirements) Provide an estimate of the expected run time, however trivial it might be. It matters to the replicator!

**Examples:**

```
- OS: "openSUSE Leap 15.6"
- Processor:  13th Gen Intel(R) Core(TM) i7-1365U, 12 cores
- Memory available: 30GB memory
- Docker version 28.4.0-ce, build 249d679a6 
- stata version 18-mp-i (Docker image dataeditors/stata18-mp-i:2024-12-18) (born date: "18 Dec 2024") with 32 core license

Code ran for about 35 hours.
```

```
- OS: Windows Server AMD EPYC 7763 64-Core Processor 2.44 GHz, 128GB
- Stata/MP4 19.5 ("21 May 2025")
- MATLAB R2025a

Code runs about 10 minutes for Stata portion, and about 5 days for MATLAB portion.
```


### Submitting

You can now submit your replication package to the Data Editor, along with the completed checklist from above, and the generated `main.log`/`main.Rout` as evidence.