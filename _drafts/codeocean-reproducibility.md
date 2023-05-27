---
title:  "Using CodeOcean as a primary or secondary replication package for AEA Journals"
date: 2022-05-26
tags:
  - self-checks
  - CodeOcean
  - openICPSR
  - R
  - Stata
  - Matlab
---

A while back, I posted about [how to use Docker for reproducibility](https://aeadataeditor.github.io/posts/2021-11-16-docker). This post is about how to use one particular (commercial) online Docker-based system to prepare replication packages for AEA journals. Two scenarios will be explored: CodeOcean (henceforth: CO) as the primary replication package (optionally with a backup archive on openICPSR), and CO as a secondary (partial) replication package (and I will explain why that might be useful).

<!-- more -->

## What is CodeOcean

CodeOcean is a commercial company offering web-based ([codeocean.com](https://codeocean.com)) "compute capsules" using open technology. Behind the scenes, capsules use Docker, a container technology. See my [previous post](https://aeadataeditor.github.io/posts/2021-11-16-docker) and references therein for more information. Importantly, CO has (a) a preservation policy [^1]

https://help.codeocean.com/en/articles/1120151-code-ocean-s-verification-process-for-computational-reproducibility-quality

https://help.codeocean.com/en/articles/1310182-updating-published-compute-capsules

## CodeOcean as a primary

The closest to a full openICPSR copy of a CO capsule I have is

Rossi, Barbara. Data and Code for: “Forecasting in the Presence of Instabilities.” Nashville, TN: American Economic Association [publisher], 2021. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2021-10-26. https://doi.org/10.3886/E147225V1

For that case, we deposited the full CO capsule export into openICPSR, modified REPRODUCING.md, and published it.
You can see the REPRODUCING.md that is a lightly modified version of the default CodeOcean one. 
The "REPRODUCING.md" is automatically downloaded when you "export" a capsule. If we stick to JUST CO, you would need to do nothing (but for clarity, the README might reference the REPRODUCING.md file, since many folks will otherwise be confused - they typically won't know how to download/export a capsule).



One change I would make is to add a reference to where to find the README with detailed code instructions, which is in code/README.{pdf,md}.

But you can start with this, and I'll review.

A more "partial" approach (which I don't think you need to follow) is

Jonathan Roth (2022) Compute Capsule for: Pre-test with Caution: Event-study Estimates After Testing for Parallel Trends [Source Code]. https://doi.org/10.24433/CO.0353633.v1

where the openICPSR deposit is complete, and contains all the code, whereas the CO only contains part of the code, and a back reference to the openICPSR deposit.

## Variants


we remove the "precomputed" folder.
we run the full analysis (bhm = 1)
we publish this Capsule (V1)

    it will contain in "results" the Stan-computed stuff

we then add the STan-computed stuff back to "pre-computed"
we adjust the README to say that pre-computed results (stemming from DOI for V1) are included, and are used because bhm=0

    Instructions are also included where to turn bhm=1 and what the expected variability is in the outcomes due to uncontrollable randomness

we run the bhm=0 analysis
we publish V2. 

[^1] https://help.codeocean.com/en/articles/2443989-code-ocean-s-preservation-plan