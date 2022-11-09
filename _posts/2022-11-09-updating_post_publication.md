---
title:  "A short example of how to update a replication package"
date: 2022-11-09
tags:
  - updating 
  - improvement
  - reproducibility
---

The AEA Data and Code Availability does not just require that authors publish a replication package - it also encourages authors to improve upon the replication package. Here is an example.

<!-- more -->

> [NOTE] I am posting about this update with permission by the author.

### Links

- [Data and Code Availability Policy](https://www.aeaweb.org/journals/policies/data-code)
- [Revision Policy](https://www.aeaweb.org/journals/data/policy-revisions)'
- [Instructions how to create a new version on openICPSR](https://aeadataeditor.github.io/aea-de-guidance/FAQ.html#i-was-wondering-whether-and-how-i-can-update-the-published-repository-for-our-paper-i-was-contacted-by-a-researcher-who-is-doing-a-replication--couple-of-minor-issues--forgotten-to-include-two-auxiliary-datasets-in-the-repository-without-which-one-of-the-programs-does-not-run-successfully)

### TLDR

In a nutshell, when authors, or replicators, or somebody on the internet, identifies an issue with a package, they have a few options to identify and publish a solution for it, so that others can benefit the update.

They can submit a comment to the journal, when the issue is a scientific one that materially affects the outcome and the conclusions.

They can write a new article, triggered by an issue identified through the reproduction or replication attempt. This can be an original new article, or a replication-specific article ((for instance, at the Journal of Applied Econometrics)[https://onlinelibrary.wiley.com/page/journal/10991255/homepage/News.html#replication]).

They can record the issue on platforms such as the [Social Science Reproduction Platform](https://www.socialsciencereproduction.org/) or the [Replication Wiki](https://replication.uni-goettingen.de/).

Or, if the issue is really minor, or is simply an improvement, authors can post a revision of replication package according to the **[AEA Revision Policy](https://www.aeaweb.org/journals/data/policy-revisions)**.

This post describes the latter.

### Timeline

- Oct 2019: Replication package was submitted to Data Editor (one of the first 200 cases). A first report was sent back to the author (they were simpler back then...), the author revised the package, and re-submitted an improved package.
- Nov 2019: The revised package was accepted (after 1 round). We were unable to access all data, but improved the documentation of the data sources.
- April 2020: Publication of the manuscript: [https://doi.org/10.1257/aer.20171732](https://doi.org/10.1257/aer.20171732), and of the replication package: [https://doi.org/10.3886/E112121V1](https://doi.org/10.3886/E112121V1). ![article page](/images/revpolicy-article1.png) ![replication package v1](/images/revpolicy-data1.png)
- Sometime in 2020: a replicator, with access to the data, reports to the author various small issues, in particular missing files.
- Jan 2021: Author reaches out to AEA Data Editor,  and wants to correct the data deposit, so that future replicators can access the missing files. A case is created by the AEA Data Editor to follow up. 
- *Life intrudes* 🤷‍♂️
- Oct 2022: Author updates the replication package, together with a Changelog (as required by policy), creating a V2. The revised package is published: [https://doi.org/10.3886/E112121V2](https://doi.org/10.3886/E112121V2), and the V1 now has a banner identifying that a newer version is available. ![revised data package](/images/revpolicy-data2.png)

### Notes

- The original deposit - the version of record - remains available, and downloadable.
- The article page continues to link to the original deposit (V1) because it is the version of record.
- The original deposit has a banner indicating that a newer package is available, and directs to that newer deposit.
- The original deposit and the revised deposit contain cross-links.

### Conclusion

This is a great example of how the ability to update replication packages is a key part, previously underexploited and not transparent, in improving science. Such updates happen for a variety of reasons multiple times a year. Sometimes, they happen for less happy reasons, such as a data provider requests that a file be removed because posting the file is not compliant with their terms of use. In other cases, authors simply post a better README, after having received feedback from students or replicators. 

Revisions and new versions can be created on all regularly used repositories, such as [openICPSR](https://www.openicpsr.org/openicpsr/search/aea/studies), [Zenodo](https://zenodo.org/communities/aeajournals/), and [Dataverse](https://dataverse.harvard.edu/). 

When authors publish their replication packages prior to submission, such revisions allow them to incorporate the changes made during the editorial process, whether related to the scientific or the computational content of the paper.



<!-- Ref: AEAREP-228 -->
