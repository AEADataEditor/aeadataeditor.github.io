---
title: "Step 3: Dependencies"
toc: true
date: 2026-02-16
---

[◀ Back to Checklist](preparing-replication-package) | [Back to Details](preparing-replication-package-details) | [◀ Previous: Step 2](preparing-replication-package-step2)

## Stata packages

Stata users frequently use user-written packages, which are made available to the Stata community via the [Stata Journal](https://www.stata-journal.com/), [SSC](https://ideas.repec.org/s/boc/bocode.html), or Github. They are typically installed using a small number of variants of the `net install` command (including `ssc install`).

Replicators need to have the same versions of these packages installed. Stata does not (currently) provide a way to install older versions of packages, and a regular occurrence of reproducibility failure is due to changes in packages over time. We have some simple solutions to this problem.

First, use an environment to permanently install-project specific packages once and for all.


**Define the environment** in your main file, after setting `$rootdir`:


> Reference: <https://larsvilhuber.github.io/self-checking-reproducibility/12-environments-in-stata.html> and <https://github.com/AEADataEditor/replication-template/blob/master/template-config.do#L129>.


```stata
/* install any packages locally */
di "=== Redirecting where Stata searches for ado files ==="
capture mkdir "$rootdir/ado"
adopath - PERSONAL
adopath - OLDPLACE
adopath - SITE
sysdir set PLUS     "$rootdir/ado/plus"
sysdir set PERSONAL "$rootdir/ado"       // may be needed for some packages
sysdir
```

From this point on, all installed packages will be installed into `$rootdir/ado`, and Stata will look there first when loading packages.

**Install packages once** if not present, but don't reinstall if already present.


> Reference: <https://gist.github.com/larsvilhuber/d8b643a408d425ef2a80385b6377870d#file-part2_of_main-do-L14>, though you should be able to just use your own install code as well, if it worked before.

```stata
*** Add required packages from SSC to this list ***
local ssc_packages ""
    // Example:
    // local ssc_packages "estout boottest"
    //
    display in red "============ Installing packages/commands from SSC ============="
    display in red "== Packages: `ssc_packages'"
    if !missing("`ssc_packages'") {
        foreach pkg in `ssc_packages' {
            capture which `pkg'
            if _rc == 111 {
               dis "Installing `pkg'"
                ssc install `pkg'
            }
            which `pkg'
        }
    }
 ado
```

**Some special cases** (usually not necessary)

*For some packages, the package name is not the same thing as the command name.* Example: `moremata`. For these packages, the above code does not work. Use this code:[^unconditional-packages]

[^unconditional-packages]: A more customized setup might check for a package-specific file in the `ado` directory, such as the `<package>.pkg`, but this is more complex and may not always work.


> Reference: <https://gist.github.com/larsvilhuber/d8b643a408d425ef2a80385b6377870d#file-part2_of_main-do-L27>

```stata
    // If you have packages that need to be unconditionally installed (the name of the package differs from the included commands), then list them here.
    // examples are moremata, egennmore, blindschemes, etc.
local ssc_unconditional ""
/* add unconditionally installed packages */
    display in red "=============== Unconditionally installed packages from SSC ==============="
    display in red "== Packages: `ssc_unconditional'"
    if !missing("`ssc_unconditional'") {
        foreach pkg in `ssc_unconditional' {
            dis "Installing `pkg'"
            cap ssc install `pkg'
        }
    }
 ado
```

*Packages that are not on SSC may need to be `net install`ed from other sources,* including Github and personal websites. Again, this does not neatly work with a specific command check, and thus you may need to unconditionally install them. Use this code:


```stata
    // If you have packages that need to be unconditionally installed from other sources (not SSC), then list them here.
    // Example: grc1leg
  net install grc1leg, from("http://www.stata.com/users/vwiggins/")
    // Example when net install is not an option
  cap mkdir "$rootdir/ado/plus/e"
  cap copy http://www.sacarny.com/wp-content/uploads/2015/08/ebayes.ado "$rootdir/ado/plus/e/ebayes.ado"
 ado
```

***Adding to replication package***

The following files should be included in your replication package:

```bash
code/ado/*
```

## R packages

For R packages, we suggest that users use `renv`, and do not set a specific CRAN mirror. We refer users to the [renv documentation](https://rstudio.github.io/renv/articles/renv.html) for details, but in a nutshell, for an existing R project that is not using `renv`, the following commands should be run in the R console:

```r
install.packages("renv")  # only once
renv::init()               # only once per project
renv::snapshot()           # only once per project, after all packages are installed. You should choose to install all packages detected, then snapshotting.
renv::status()             # to check status
```

This will create a file `renv.lock` in the top-level directory of your project.

***Adding to replication package***

The following files should be included in your replication package:

```bash
.Rprofile
renv.lock
renv/activate.R
renv/settings.json
```

Do not include the entire `renv` directory, in particular not the `renv/library` subdirectory, as it is platform-specific (of no use to other platforms), and can be very large.

---

[![Next: Step 4](/images/next-button-step4.png)](preparing-replication-package-step4)
