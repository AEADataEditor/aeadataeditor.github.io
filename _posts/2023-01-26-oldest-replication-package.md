---
title:  "The oldest AEA replication package"
date: 2023-01-26
toc: false
mastodon: 
tags:
  - migration
  - reproducibility
---

We were recently discussing among data editors what the oldest replication package (in Econ and Political Science) might be.

<!-- more -->

I actually don't know the answer to that. But the oldest replication package we have in the (migrated) AEA archives is:

> Frankel, Jeffrey A., and Romer, David H. Replication data for: Does Trade Cause Growth? Nashville, TN: American Economic Association [publisher], 1999. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2019-10-12. [https://doi.org/10.3886/E113211V1](https://doi.org/10.3886/E113211V1).

which accompanies this article:

> Frankel, Jeffrey A, and David Romer. “Does Trade Cause Growth?” American Economic Review 89, no. 3 (June 1999): 379–99. [https://doi.org/10.1257/aer.89.3.379](https://doi.org/10.1257/aer.89.3.379).

Find out yourself: a (fully reproducible) way to verify this (there are better ways, of course)

```r
library(readr)
library(tidyverse) # I'm lazy

baseurl <- "https://github.com/AEADataEditor/aea-supplement-migration/raw/master/data/acquired"
# alternatively, if running locally
# baseurl <- "data/acquired"
aea_article_data  <- read_csv(file.path(baseurl,
                                        "aea_article_data.csv.gz"))
aea_issue_data    <- read_csv(file.path(baseurl,
                                        "aea_issue_data.csv.gz"))
aea_icpsr_mapping <- read_csv(file.path(baseurl,
                                        "aea_icpsr_mapping.20191014.txt"),
                              col_names = c("icpsr_doi","zipfile"))  %>% 
                    mutate(zipfile = str_remove(zipfile,
                                                fixed("Original Zip: ")))
aea_deposits <- left_join(aea_article_data,aea_icpsr_mapping,
                          by=c("icpsr_package_name"="zipfile")) %>% 
  left_join(aea_issue_data,by=c("issue_id"))
# oldest package
aea_deposits %>% filter(year==min(aea_deposits$year)) %>% 
  select(doi,title,journal,volume,issue, year,icpsr_doi)

```

([source](https://github.com/AEADataEditor/aea-supplement-migration/blob/ab235cbf1e0e1965a71263d15e1d0f3983fdba9c/programs/oldest-package.R))