---
title: "Step 2: Path names and case"
toc: true
date: 2026-02-16
---

[◀ Back to Checklist](preparing-replication-package) | [Back to Details](preparing-replication-package-details) | [◀ Previous: Step 1](preparing-replication-package-step1)

Two issues:

- Windows computers use `\` (backslashes) in path names, while Mac and Linux computers use `/` (forward slashes). The use of `\` (backslashes) in path names breaks code on Mac and Linux computers.

- Windows and Mac computers use case-insensitive file systems, while Linux computers use case-sensitive file systems.

Both of these issues need to be addressed. You are helped by a straightforward but often forgotten (or unknown) observation:


- **Every statistical programming language can use generic path names using `/` (forward slashes).** This ensures wide reproducibility.

About 40% of replication packages in economics appear to be submitted by researchers using computers running MacOS or Linux. With a bit of simplified math, if we believe that is representative of what future replicators will do, that means that 40% of users will not be able to run 60% of replication packages without some potentially widespread edits, because of those backslashes.

You should thus **replace all path names in your code to use `/` (forward slashes)**, or appropriate functions, and take care to write **case-sensitive file and path names**. This is straightforward:

## Stata

```stata
// Instead of
use "data\analysis\combined_data.dta", clear
// Use
use "data/analysis/combined_data.dta", clear
// or better
use "$rootdir/data/analysis/combined_data.dta", clear
```

## R

```r
# Instead of
data <- read.csv("data\\analysis\\combined_data.csv")
# Use
data <- read.csv("data/analysis/combined_data.csv")
# or better
data <- read.csv(file.path(rootdir, "data", "analysis", "combined_data.csv"))
```

and similarly for other languages.


## Implementing

In many cases, you can just globally replace all `\` with `/` in your code files. Caution however is warranted if your code explicitly writes out $LaTeX$ code, which also (legitimately) uses `\`. In that case, you will need to be more careful.

## Expert tip

If using a (Bash or Zsh) terminal, you likely have the `sed` command available. You can use it to replace all backslashes with forward slashes in all `.do` files in the `code` directory as follows:

```bash
sed -i 's+\\+/+g' code/*.do
```

---

[![Next: Step 3](/images/next-button-step3.png)](preparing-replication-package-step3)
