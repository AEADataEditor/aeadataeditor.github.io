---
title:  "Thoughts on the unnecessary complexity of AI-generated code"
date: 2026-08-28
mastodon: 
bluesky: 
tags:
  - data editor tips
  - replication packages
  - AI
  - Makefile
---


Original replicaiton package used `make`. I love me a nice `Makefile`, but... 50% of authors are on Windows, this fraction is even higher in "industry", and the solution to "to run on Windows, install Linux"  is a bit facetious... and is not possible in many corporate environments. (I would like to hear back from folks on that, actually).

Authors proposed for Windows users to manually do the following

```ps1

   python Replication\Data\code\download_dataverse_trade_data.py --server="https://dataverse.harvard.edu" --persistent-id="doi:10.1234/DVN/XYZABC" --start="2010-01-01" --end="2027-12-31" --imports-dir="Replication\Data\outputs\raw_zips" --exports-dir="Replication\Data\outputs\raw_zips_exports"
   Rscript Replication\Data\code\build_data.R --start=2010-01-01 --end=2027-12-31 --series=naics,enduse
   Rscript Replication\Data\code\cache_imports.R
   Rscript Replication\Data\code\build_sectors_table.R
```

which of course could be put into `main.ps1`  and run from the Powershell terminal. That would be a platform-specific solution for Windows-only. My own preference is to express it in Bash, and then run that even on Windows, because of course everybody has Git installed, which comes with Git Bash. But I realize that's exactly the same kind of assumption that "just install WSL" does.

But there is a much simpler solution: Write a single R script. R handles the translation to platforms so you do not have to.  When I asked an LLM to suggest options, one answer was

> Option B — true source() pipeline (one R process)
>
> To actually source() the R scripts you must get parameters into them without a command line. The scripts currently call something like commandArgs(trailingOnly = TRUE). Two sub-options:
>
> B1 — shadow commandArgs before each source() (no edits to sub-scripts, but a bit hacky):

When your AI tells you that something is "hacky", you should probably avoid it...

Version 1 of its suggestsion was a pure R script that shelled out to Python:

```r
#!/usr/bin/env Rscript
CODE_DIR <- file.path("Replication", "Data", "code")

# Step 1 still has to shell out — it's Python
system2(Sys.getenv("PYTHON", "python3"), c(
  file.path(CODE_DIR, "download_dataverse_trade_data.py"),
  "--server=https://dataverse.harvard.edu",
  "--persistent-id=doi:10.7910/DVN/XYXABC",
  "--start=2010-01-01", "--end=2027-12-31",
  "--imports-dir=Replication/Data/outputs/raw_zips",
  "--exports-dir=Replication/Data/outputs/raw_zips_exports"))

source_with_args <- function(path, args = character()) {
  commandArgs <<- function(trailingOnly = FALSE) args   # shadow in globalenv
  on.exit(rm(commandArgs, envir = globalenv()), add = TRUE)
  source(path, local = new.env(parent = globalenv()), chdir = FALSE)
}

source_with_args(file.path(CODE_DIR, "build_data.R"),
                 c("--start=2010-01-01", "--end=2027-12-31", "--series=naics,enduse"))
source_with_args(file.path(CODE_DIR, "cache_imports.R"))
source_with_args(file.path(CODE_DIR, "build_sectors_table.R"))
```

I actually think that the last proposed solution aligns most cleanly with the way I have learned to do this, back in the day when I was a floppy-haired Ph.D. student, and which I have tried to teach collaborators and students ever since: use a config file!

> B2 — refactor the scripts to read a config (cleanest long-term): give each R script a header like

```r
if (!exists("PARAMS")) {
  # standalone invocation: parse the command line
  library(optparse)
  PARAMS <- parse_args(OptionParser(option_list = list(
    make_option("--start"), make_option("--end"), make_option("--series"))))
}
# ... use PARAMS$start, PARAMS$end, PARAMS$series ...
```

> Then the master file just sets `PARAMS <- list(start = "2010-01-01", ...)` once and `source()`s each script. Each script still runs standalone from the command line unchanged.

Or, the way I would have done it: stick a bunch of globals into `config.R` and source that at the top of each script, or once in the master, with the only complexity being how to call out to Python in a platform-agnostic way.:

```r
# config.R
datadoi <- "doi:10.1234/DVN/XYZABC"
startdate <- "2010-01-01"
enddate <- "2027-12-31"
pypath <- reticulate::py_exe()          # absolute path to the configured interpreter

```r
# master.R

rootdir <- here::here()
codebuild <- file.path(rootdir,"Replication","Data","code")

source(file.path(rootdir,"config.R"), echo =TRUE)

# build args here
processx::run(pypath, args, echo = TRUE, error_on_status = TRUE)
source(file.path(codebuild,"build_data.R"), echo =TRUE)
source(file.path(codebuild,"cache_imports.R"), echo =TRUE)
source(file.path(codebuild,"build_sectors_table.R"), echo =TRUE)
```

Easy-peasy, straightforward (except for the Python dependency), and platform-agnostic. No WSL needed, no Make needed. It will not resolve dependencies as cleanly as `make` does - but if you have completed your development work on the paper, there should be no issue with that. You want to convey the economics of it in as simple a fashion, not show off your task-management skills. The simpler the better, and the more likely it is to be used by others.
