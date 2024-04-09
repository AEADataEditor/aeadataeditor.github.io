---
title:  "Some remarks on coding when data are confidential"
date: 2024-04-09
mastodon: 
twitter:
bluesky:
tags:
  - confidential data
  - complex projects
---

I have been asked a few times about guidance for replication packages that use confidential data in research data centers, e.g., the  Federal Statistical Research Data Centers (FSRDCs) and others. Here are some examples and guidance.

<!-- more -->

## The problem

The data, and sometimes (only sometimes) pieces of code, are confidential. If this is something you encounter, read on.

## This is not new

See my [earlier post almost exactly two years ago](https://aeadataeditor.github.io/posts/2022-04-13-coding-confidential) and this [2022 tutorial](https://larsvilhuber.github.io/reproducibility-confidential-fsrdc/) that I developed from that.

## General Guidance

- https://social-science-data-editors.github.io/guidance/DCAS_Restricted_data.html#us-census-bureau-and-fsrdc
- https://social-science-data-editors.github.io/guidance/Requested_information_hosting.html#self-generated-repositories

## Examples!

Two excellent examples:

### Example 1: Berger, Herkenhoof, and Mongey (2022)

> Berger, David, Herkenhoff, Kyle, and Mongey, Simon. Data and Code for: Labor Market Power. Nashville, TN: American Economic Association [publisher], 2022. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2022-12-07. [https://doi.org/10.3886/E154241V2](https://doi.org/10.3886/E154241V2)

Not only code, but faces the problem that IRS data cannot have variables revealed. Workarounds galore.

### Example 2: Yeh, Macoluso, and Hershbein (2022)

> Yeh, Chen, Macaluso, Claudia, and Hershbein, Brad. Code for: “Monopsony in the U.S. Labor Market.” Nashville, TN: American Economic Association [publisher], 2022. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2022-11-28. https://doi.org/10.3886/E162581V1

### Example 3: Fort (2017)

This replication package is a bit older, but is an excellent example that I have repurposed as guidance for others:

> Teresa C. Fort, Technology and Production Fragmentation: Domestic versus Foreign Sourcing, The Review of Economic Studies, Volume 84, Issue 2, April 2017, Pages 650–687, [https://doi.org/10.1093/restud/rdw057](https://doi.org/10.1093/restud/rdw057)

and the [copy of the README](https://social-science-data-editors.github.io/guidance/copies/Fort2016-Readme.pdf).

Note that this package was created before the installation of the current generation of data editors, so relied on none of that (official) expertise!


Many more out there. 

## Ask the research data center

The US Census Bureau has procedures in place to review code (it's actually part of the release system), as do many other systems. Some parts of the code will need to be redacted, but you can get very functional code released (see the [2022 tutorial](https://larsvilhuber.github.io/reproducibility-confidential-fsrdc/) on how to set this up from the start).

## But: Don't take "No" for an answer!

There are sometimes some old practices in place in restricted-access environments that do not have 100s of researchers flowing through (for instance, smaller countries, places with newer centers, etc.). Sometimes, you need to push back. You can rely on the Data Editors - me, others - to help you do that. I have successfully educated data custodians, who justifiably fear releasing too much confidential data, on what can be done reliably and robustly, at least with code.

## Dotting the i's and crossing the t's

We usually require that an **internal** archive be created at the institution holding the data, so that regardless of how much or how little is released, internally, a fully reproducible archive exists, accessible for those with permission to access. The permissions necessary , and permission granted in the replication package so that others, with appropriate access, can access those files. See the first example above for an excellent example of that, and [this guidance](https://social-science-data-editors.github.io/guidance/Requested_information_hosting.html#self-generated-repositories) on how to do so in the absence of a formal internal archive.