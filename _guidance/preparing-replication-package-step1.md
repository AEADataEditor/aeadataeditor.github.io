---
title: "Step 1: Main file"
toc: true
date: 2026-02-16
---

[◀ Back to Checklist](preparing-replication-package) | [Back to Details](preparing-replication-package-details)

> You may or may not have a main file. The following should be adapted to your circumstances. You do not need to create a file that is called `main.do` if you already have one, but you may need to update your existing main file.

> Reference: <https://larsvilhuber.github.io/self-checking-reproducibility/02-hands_off_running.html>

Creating a single main file is straightforward. However, you will want to make some minor edits depending on where, in the above template setup, the file is located:

## Scenario A: `main` is in the `code` directory

The most frequent scenario we see (which we call **Scenario A**) amongst economists is that the main file is in the `code` directory:

```
README.pdf
data/
...
code/
  main.do
  01_readcps.do
  02_readfred.do
...
```

In this case, the following generic main file will work, with `scenario` set to `"A"`.

```stata
local scenario "A"          // Scenario A: main is in code directory
local pwd : pwd                     // This always captures the current directory

if "`scenario'" == "A" {             // If in Scenario A, we need to change directory first
    cd ..
}
global rootdir : pwd                // Now capture the directory to use as rootdir
display in red "Rootdir has been set to: $rootdir"
cd "`pwd'"                            // Return to where we were before and never again use cd

// Now run the rest of the code
do "$rootdir/code/01_readcps.do"
do "$rootdir/code/02_readfred.do"
do "$rootdir/code/03_table1-5.do"
do "$rootdir/code/04_figures1-4.do"
```

## Scenario B: `main` is in the top-level directory

More common in other computational sciences, but also present amongst economists, is that the main file is in the top-level directory:


```
README.pdf
main.do
data/
...
code/
  01_readcps.do
  02_readfred.do
...
```


In this case, the following generic main file will work, with `scenario` set to `"B"`(though see [Step 3 Dependencies](preparing-replication-package-step3))

```stata
local scenario "B"          // Scenario B: main is in project top-level directory
local pwd : pwd                     // This always captures the current directory

if "`scenario'" == "A" {             // If in Scenario A, we need to change directory first
    cd ..
}
global rootdir : pwd                // Now capture the directory to use as rootdir
display in red "Rootdir has been set to: $rootdir"
cd "`pwd'"                            // Return to where we were before and never again use cd

// Now run the rest of the code
do "$rootdir/code/01_readcps.do"
do "$rootdir/code/02_readfred.do"
do "$rootdir/code/03_table1-5.do"
do "$rootdir/code/04_figures1-4.do"
```

## Important

> In neither scenario did we hard-code the path to our project directory `/my/computer/users/me/project`. This is not an omission, and it is important, because it allows the code to be run on any computer, without modification.

Finally, you should not hard-code your `rootdir`. Set the **project root directory dynamically**:

```stata
global rootdir : pwd
// Example
datadir   = "$rootdir/data/raw"
outputdir = "$rootdir/data/clean"
```

```r
# if using the here package:
rootdir <- here::here()
# or the rprojroot package
rootdir <- rprojroot::find_root_file("README.pdf")  # or other marker file
# Example
datadir   = file.path(rootdir, "data", "raw")
outputdir = file.path(rootdir, "data", "clean")
```

```python
import os
from pathlib import Path

# Set directories
code_dir = Path(__file__).resolve().parent
rootdir = code_dir.parent
# Example
datadir   = rootdir / "data" / "raw"
outputdir = rootdir / "data" / "clean"
```

> IMPORTANT: your code MUST contain the line (Stata) `global rootdir : pwd` (or equivalent) to set the project root directory dynamically.

## Creating directories programmatically

If your code uses directories that may start out empty, or may not exist on the replicators' computers, you must create them programmatically. 


```stata
cap mkdir "$outputdir"
```

```r
dir.create(outputdir, showWarnings = FALSE, recursive = TRUE)
```

```python
outputdir.mkdir(parents=True, exist_ok=True)
```

---

[![Next: Step 2](/images/next-button-step2.png)](preparing-replication-package-step2)
