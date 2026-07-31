---
title: Preparing your code for computational verification
toc: true
date: 2025-12-04
---

> The steps in this document are being used in a pilot project. 

This document describes how to prepare your code for verification, taking into account some of the most frequent issues that the Data Editor and his team have encountered in submitted replication packages.


> ⚠️❗ **IMPORTANT:** At this point, you should only be seeing this page if you were asked by the Data Editor team to do so. If using multiple software in the replication package, you must be able to split the processing into a reasonably small set of single-software master scripts (see [SIVACOR documentation](https://docs.sivacor.org/docs/step0-prepare/#your-replication-package-only-uses-a-single-software-application-per-step)). Only a limited set of software are feasible at this time (see [Step 5 section: authorized containers](#authorized-containers)). 
>
> You do NOT need to know how Docker or similar software works, nor do you need to be able to run containers on your own computer (though it helps). See [Step 5 section: Using the SIVACOR website](#using-the-sivacor-website).

## Overview

We will describe a few checks and edits you should make to your code, in order to ensure maximum reproducibility. We then describe how to test for reproducibility before submitting to the Data Editor. All steps have been tested by undergraduate replicators, and should be easy to implement. Whether they take a lot of time depends on your specific code, but generally, these adjustments can be made by somebody with good knowledge of the code base very quickly.

Much more extensive guidance on the issues addressed here is available at <https://larsvilhuber.github.io/self-checking-reproducibility/>. We reference specific chapters there at each of the steps.

> ⚠️❗ **IMPORTANT:** All but the last steps can be done by anybody, no special system requirements required, and independent of your ability to share confidential data. 
>
> However, the last step (online or offline validation) may not be possible in some circumstances: You should not upload sensitive data to the SIVACOR system we describe, and you may not be able to run a container-based validation in an institution that does not allow you to install container software (Docker, OrbStack, etc.). Nevertheless, do still implement the first steps, and let the Data Editor know if you cannot do the final step.

<div style="page-break-after: always;"></div>

## Using an AI assistant

You can use an AI assistant (such as Claude, ChatGPT, or GitHub Copilot) to guide you through this checklist. Give your AI the following instruction:

> Use <https://aeadataeditor.github.io/aea-de-guidance/preparing-replication-package.agent.md> to review my replication package and help me prepare it for submission to the AEA Data Editor.

The AI will work through each step with you, identify issues, and suggest specific fixes.

## Checklist

Print off (as PDF or on paper) the following checklist, and tick off each item as you complete it. Provide the completed checklist as part of the replication package.

- [ ] [**Step 1: Main file**](preparing-replication-package-step1): A single main file is provided that runs all code.  [Details](preparing-replication-package-step1)
- [ ] [**Step 2: Path names**](preparing-replication-package-step2): All paths in code use `/` (forward slashes) relative to a single top-level project directory (`$rootdir`, `$basedir`, etc.). The top-level project directory is set dynamically, not hard-coded (explanations below).  [Details](preparing-replication-package-step2)
- [ ] [**Step 3: Dependencies**](preparing-replication-package-step3): All packages/libraries/dependencies are installed via code once.  [Details](preparing-replication-package-step3)
  - [ ] For Stata, these packages are installed into a subdirectory in the project (`$rootdir/ado`, `$basedir/adofiles`, etc.), and used by the code.
  - [ ] For R, `renv` is used (exceptions made for other package management systems if such a system is explained).
  - [ ] For Python, environments are used (native `venv` or `conda`), and the necessary top-level requirements specified (no OS-specific dependencies are included).
- [ ] [**Step 4: Displays**](preparing-replication-package-step4): All figures and tables are written out to clearly identified external files, and the authors' versions, as used in the manuscript, are provided.  [Details](preparing-replication-package-step4)
- [ ] [**Step 5: Testing on AEA-maintained website**](preparing-replication-package-step5): After all changes were made, the code was run  using the referenced website, a certified ZIP file was created, and is provided instead of the original replication package (alternatives exist for certain situations).  [Details](preparing-replication-package-step5)
- [ ] (usually not necessary) [**Finalize**](preparing-replication-package-finalize): Update the README with the necessary information about computer specifications, Docker image used, memory and disk space requirements, and expected runtime. 



## Submitting

You can now submit your replication package to the Data Editor, along with the completed checklist from above, and the generated `main.log`/`main.Rout` as evidence.

## Problems?

If you run into problems at any step, please reach out. If you only run into problems in Step 5, no worries, simply submit all the files as modified in Steps 1-4, along with the completed checklist, and we will handle the remaining issues.

[![Gory Details](/images/next-button-details.png)](preparing-replication-package-details)
