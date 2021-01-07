---
title:  "An example of reproducibility checking when data is restricted-access"
date: 2020-06-30
tags:
  - restricted-access
  - AEJPolicy
---

I wanted to highlight a recently (2020-04-30) published article in the [AEJ:Economic Policy](https://www.aeaweb.org/journals/pol) as an example of reproducibility checking when data is restricted-access.


> Leung, Pauline, and Christopher O'Leary. 2020. "Unemployment Insurance and Means-Tested Program Interactions: Evidence from Administrative Data." American Economic Journal: Economic Policy, 12 (2): 159-92. [https://doi.org/10.1257/pol.20170262](https://doi.org/10.1257/pol.20170262)

![AEJ:Policy 20170262](/assets/aejpolicy-2020-05-leung.png)

This manuscript was part of our earliest reproducibility checks - it was assigned to us in early April 2019. But with one caveat that I'll hold till the end, it is an excellent example of a well-documented, and as it turns out, reproducible article. Even if the data is confidential and restricted-access!

The data underlying the analysis is administrative data from various state agencies in Michigan, and it would have been difficult and time-consuming for us replicators to request access.

![AEJ:Policy 20170262 README](/assets/aejpolicy-2020-05-leung-readme.png)

We reached out to the authors and asked whether they would be able to add a 3rd-party to their research protocol - either a member of our team or somebody at their institution ([@Upjohninstitute](https://www.upjohn.org)) who was not involved in the original research.

The authors connected us with a research associate at their institution who had legal access to the data. The procedure happened, as much as possible, at arms-length: the 3rd-party replicator followed only written instructions that are publicly available, as per our [protocol](https://aeadataeditor.github.io/aea-de-guidance/protocol-3rd-party-replication.html).

In fact, all information and code came from the researchers' replication archive at openICPSR, which is now available at [https://doi.org/10.3886/E109704V1](https://doi.org/10.3886/E109704V1). However, the replicator had access prior to publication of the archive, and what you see now is not what they had access to. 

![AEJ:Policy 20170262 openICPSR](/assets/aejpolicy-2020-05-leung-openicpsr.png)

That's because the replicator identified and suggested multiple (small, but meaningful) edits to README and programs, to make the replication easier for subsequent replicators. 

They also identified (minor) various numerical discrepancies, typically at the 3rd decimal place, that we tracked down to  differences in the versions of the Stata package [`rdrobust`](https://sites.google.com/site/rdpackages/rdrobust). After discussions with `rdrobust` authors and manuscript authors, the replication package now contains the exact version of `rdrobust` used for the analysis. 

Overall, the report received from the 3rd party replicator was useful confirmation that the code that anybody can see would work well on the data that few people can see, and materially improved the replication package. 

Take-away message: While we cannot do reproducibility checks on restricted-access data in a timely fashion for all papers that use restricted-access data, there are still many opportunities to do so, and we will always attempt to do so.

In fact, since that paper was reproduced, we have been able to make similar attempts at reproduction for about a dozen other papers, for which we reached out to various individuals or institutions. We have also signed NDA or DUA for various datasets, to obtain copies ourselves. Not all attempts succeed, but expect to see more such verifications in the future.

Caveat I alluded to: We were still refining our various checks and guidance documents. While the authors did an excellent job citing various data sources (in the [online appendix](https://www.aeaweb.org/doi/10.1257/pol.20170262.appx)), we did not ask them to add a data citation for the core confidential data. That would be different today.
