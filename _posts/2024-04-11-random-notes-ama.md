---
title:  "Random notes from the AMAs"
date: 2024-04-11
mastodon: 
twitter:
bluesky: https://bsky.app/profile/aeadata.bsky.social/post/3kppyo5fj7v2g
tags:
  - data editor tips
  - replication packages
---

In the AMAs ([see past and future AMAs](https://aeadataeditor.github.io/talks/)), we talked about many things. No transcript, but here's a raw dump of the various websites that were used. 

<!-- more -->

## AEA Data and Code Availability Policy

[https://www.aeaweb.org/journals/data/data-code-policy](https://www.aeaweb.org/journals/data/data-code-policy), and if revising a package, [https://www.aeaweb.org/journals/data/revisions-policy](https://www.aeaweb.org/journals/data/revisions-policy)

## Restricted data

To access restricted data, the author and Editor may start here: [https://aeadataeditor.github.io/aea-de-guidance/sharing-restricted-data/](https://aeadataeditor.github.io/aea-de-guidance/sharing-restricted-data/)

If the AEA Data Editor cannot access the data, but somebody else can, we follow the "third party" policy [https://www.aeaweb.org/journals/data/policy-third-party](https://www.aeaweb.org/journals/data/policy-third-party)

## Common documentation by Social Science Data Editors

- "The" README: 
[https://social-science-data-editors.github.io/template_README/template-README.html](https://social-science-data-editors.github.io/template_README/template-README.html)

- The common policy guidelines:
[https://datacodestandard.org/](https://datacodestandard.org/)

## Better code and READMEs

Example of graphical interface to select data (and the difficulty of describing how to do that concisely):

[https://databank.worldbank.org/source/world-development-indicators](https://databank.worldbank.org/source/world-development-indicators)

Stata package to do the same much more succinctly: 

- [https://datahelpdesk.worldbank.org/knowledgebase/articles/889464-wbopendata-stata-module-to-access-world-bank-data](https://datahelpdesk.worldbank.org/knowledgebase/articles/889464-wbopendata-stata-module-to-access-world-bank-data) 
- [Package on RePEc](https://ideas.repec.org/c/boc/bocode/s457234.html)

Similar tension between the FRED graphical interface [https://fred.stlouisfed.org/](https://fred.stlouisfed.org/) and the FRED API, which can be used via 

- Stata  [https://www.stata.com/manuals/dimportfred.pdf](https://www.stata.com/manuals/dimportfred.pdf)
- MATLAB  [https://www.mathworks.com/help/datafeed/fred.fetch.html](https://www.mathworks.com/help/datafeed/fred.fetch.html) 
- R [https://cran.r-project.org/web/packages/fredr/vignettes/fredr.html](https://cran.r-project.org/web/packages/fredr/vignettes/fredr.html)

## Difficult data citations

Example of restricted access data with DOI, and a long list of DOIs (problems with data citations):

[https://www.casd.eu/source/statistique-structurelle-annuelle-dentreprises-issue-du-dispositif-esane/](https://www.casd.eu/source/statistique-structurelle-annuelle-dentreprises-issue-du-dispositif-esane/)

and a [possible solution](https://social-science-data-editors.github.io/guidance/addtl-data-citation-guidance.html#many-related-datasets).


## Versioning of Stata packages 

[https://github.com/labordynamicsinstitute/ssc-mirror/](https://github.com/labordynamicsinstitute/ssc-mirror/)

## Improving yourself

Draft tutorial on how to self-check reproducibility (and also how to ensure it in the first place), still quite preliminary right now:

[https://larsvilhuber.github.io/self-checking-reproducibility/](https://larsvilhuber.github.io/self-checking-reproducibility/)

## Crediting others (software citations)

R package to generate a bibliography file (bib, etc.) from all the citable packages used in an R-based replication package:  [https://github.com/Pakillo/grateful](https://github.com/Pakillo/grateful)