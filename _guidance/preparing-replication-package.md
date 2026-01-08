---
title: Preparing your code for computational verification
toc: true
date: 2025-12-04
---

> The steps in this document are being used in a pilot project. 

This document describes how to prepare your code for verification, taking into account some of the most frequent issues that the Data Editor and his team have encountered in submitted replication packages.


> ⚠️❗ **IMPORTANT:** At this point, you should only be seeing this page if you were asked by the Data Editor team to do so, and if your replication package relies on a single software. Admissible containers are listed in the [Step 5 section: authorized containers](#authorized-containers). We are not currently attempting to generalize this to multi-software replication packages, though [it](https://github.com/AEADataEditor/docker-r-gurobi) [is](https://github.com/AEADataEditor/docker-aer-2022-0276) [possible](https://github.com/AEADataEditor/docker-aer-2023-0505) [to do so](https://github.com/AEADataEditor/docker-aer-2023-0700).

## Overview

We will describe a few checks and edits you should make to your code, in order to ensure maximum reproducibility. We then describe how to test for reproducibility before submitting to the Data Editor. All steps have been tested by undergraduate replicators, and should be easy to implement. Whether they take a lot of time depends on your specific code, but generally, these adjustments can be made by somebody with good knowledge of the code base very quickly.

Much more extensive guidance on the issues addressed here is available at <https://larsvilhuber.github.io/self-checking-reproducibility/>. We reference specific chapters there at each of the steps.

> ⚠️❗ **IMPORTANT:** All but the last steps can be done by anybody, no special system requirements required, and independent of your ability to share confidential data. However, the last step may not be possible in an institution that does not allow you to install container software (Docker, OrbStack, etc.), and does not have such technology installed on a Linux cluster. We provide a public website where you can leverage containers for verification, but you should not use it for confidential data. In that case, please do all the other steps. 

<div style="page-break-after: always;"></div>


## Checklist

Print off (as PDF or on paper) the following checklist, and tick off each item as you complete it. Provide the completed checklist as part of the replication package.

- [ ] [**Step 1: Main file**](preparing-replication-package-details#step-1-main-file): A single main file is provided that runs all code.
- [ ] [**Step 2: Path names**](preparing-replication-package-details#step-2-path-names-and-case): All paths in code use `/` (forward slashes) relative to a single top-level project directory (`$rootdir`, `$basedir`, etc.). The top-level project directory is set dynamically, not hard-coded (explanations below).
- [ ] [**Step 3: Dependencies**](preparing-replication-package-details#step-3-dependencies): All packages/libraries/dependencies are installed via code once. 
  - [ ] For Stata, these packages are installed into a subdirectory in the project (`$rootdir/ado`, `$basedir/adofiles`, etc.), and used by the code.
  - [ ] For R, `renv` is used (exceptions made for other package management systems if such a system is explained).
  - [ ] For Python, environments are used (native `venv` or `conda`), and the necessary top-level requirements specified (no OS-specific dependencies are included).
- [ ] [**Step 4: Displays**](preparing-replication-package-details#step-4-displays): All figures and tables are written out to clearly identified external files, and the authors' versions, as used in the manuscript, are provided. 
- [ ] [**Step 5: Testing on AEA-maintained website**](preparing-replication-package-details#step-5-testing-in-containers): After all changes were made, the code was run  using the referenced website, a certified ZIP file was created, and is provided instead of the original replication package (alternatives exist for certain situations).
- [ ] (usually not necessary) [**Finalize**](preparing-replication-package-details#finalize-readme): Update the README with the necessary information about computer specifications, Docker image used, memory and disk space requirements, and expected runtime. 



## Submitting

You can now submit your replication package to the Data Editor, along with the completed checklist from above, and the generated `main.log`/`main.Rout` as evidence.

## Problems?

If you run into problems at any step, please reach out. If you only run into problems in Step 5, no worries, simply submit all the files as modified in Steps 1-4, along with the completed checklist, and we will handle the remaining issues.

[![Gory Details](/images/next-details-red.png)](preparing-replication-package-details)
