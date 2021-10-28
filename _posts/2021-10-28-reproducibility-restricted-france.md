---
title:  "When a reproducibility check turns into a replication exercise"
date: 2021-10-28
tags:
  - restricted-access
  - AEJ:Micro
  - CASD
  - cascad
---

I wanted to highlight a particular interesting article in the latest [AEJ: Microeconomics](https://www.aeaweb.org/journals/mic) from the perspective of replicability and reproducibility. 

<!-- more -->

> Piveteau, Paul. 2021. "An Empirical Dynamic Model of Trade with Consumer Accumulation." *American Economic Journal: Microeconomics*, 13 (4): 23-63. [https://doi.org/10.1257/mic.20190051](https://doi.org/10.1257/mic.20190051)

![AEJ:Micro 20190051](/images/aejmicro-2021-10-piveteau.png)

[Paul](https://paulpiveteau.com/) uses granular (firm-level) French customs data to estimate a model with trade flows. The detailed but confidential French customs data were obtained by Paul many years ago, directly from the French administration. However, by the time the replication package was sent to the AEA Data Editor (me), the French customs agency had (very recently) signed an agreement with [CASD (Centre d'accès sécurisé aux données)](https://www.casd.eu/), the French system for academic use of restricted-access data, making more generalized access to the customs data feasible for future researchers and replicators.[^1] Furthermore, several years ago, [Christophe Perignon](https://people.hec.edu/perignon/) (HEC Paris, [@christoperignon](https://twitter.com/christoperignon) and [Christophe Hurlin](https://sites.google.com/view/christophe-hurlin/home) (Université d'Orléans, [@churlin1804](https://twitter.com/churlin1804)) created [*cascad*](https://www.cascad.tech/), an organization dedicated to conducting reproducibility checks, including within the confines of the secure environment at CASD.[^2]

We therefore requested that *cascad* conduct a reproducibility check for the AEA, using the full confidential French customs data available within CASD.[^3] And... the first attempt at reproducing even basic statistics failed. The data deposited by the customs agency at CASD many years later were subtly different in several dimensions. While the replicators worked hard to adapt the code to the data structure available to them, we ultimately turned to Paul for help. In the end, pure computational reproducibility was not possible, but a replication using the more recently extracted customs data was feasible.

Jointly, but mostly through Paul's efforts, the team succeeded in adapting the cleaning and preparation code to the newer data, and ran most of the code successfully. As should be expected when data are somewhat different, some of the results were different, though generally not in a substantial way.  However, some results were not replicable:

> However, this replication exercise highlighted some numerical fragilities in the algorithm developed to estimate the dynamic model in the paper. In particular, the estimation of the model on the sample of wood exporters (appendix C) could not be performed.

But instead of either resolving this via (private) correspondence between editors and authors, or letting future replicators find this out the hard way, Paul adopted what I believe is the best approach: acknowledging the limits of the computational reproducibility. 

And you do not need to rely on my hearsay - you can read all about it in the summary in [Appendix H of the online appendix, page 77](https://assets.aeaweb.org/asset-server/files/15530.pdf#page=36) (from which the quote above is pulled), with the full replication report and all replicated tables and figures by *cascad* available at in the "[Replication_Fall20](https://doi.org/10.3886/E120070V1-100007)" folder in the public replication package.[^4]

No future replicator can access the data that Paul originally had obtained. But many future replicators (subject to certain conditions) can access the confidential customs data available through CASD. And can request such access with the assurance that the baseline analysis can be replicated (and the replication reproduced), making such requests - costly in time, effort, and money - worth a researcher's while.

The final outcome is, in my opinion, more transparent than it would have been in many other scenarios, and verified to be more robust than if we had only relied on Paul's original materials. 

We thank Paul for his patience and assistance, and Christophe, Christophe, and Olivier Akmansoy (the replicator at *cascad*) for their help in conducting this reproducibility check plus replication exercise.

Authors interested in communicating with us about ways to verify reproducibility when the data are confidential can consult our [step-by-step guide](https://aeadataeditor.github.io/aea-de-guidance/preparing-for-data-deposit.html#structure-in-the-presence-of-confidential-unpublished-data).


## Notes

[^1] Full disclosure: I (Lars Vilhuber) happen to serve as [chair of the scientific advisory board](https://www.casd.eu/nomination-de-lars-vilhuber-en-tant-que-president-du-conseil-scientifique-du-casd/). However, access to the customs data, and to the services of *cascad* are open to anyone, and no privileged access or treatment was necessary to obtain the outcomes of this post.

[^2] Pérignon, Christophe, Kamel Gadouche, Christophe Hurlin, Roxane Silberman, and Eric Debonnel. 2019. “Certify Reproducibility with Confidential Data.” Science 365, no. 6449: 127–28. [https://doi.org/10.1126/science.aaw2825](https://doi.org/10.1126/science.aaw2825).

[^3] As of the writing of this post, the customs data are not yet listed in the CASD data catalog at [https://www.casd.eu/les-sources-de-donnees-disponibles-au-casd/](https://www.casd.eu/les-sources-de-donnees-disponibles-au-casd/).

[^4] Piveteau, Paul. 2021. "Data and Code for: An Empirical Dynamic Model of Trade with Consumer Accumulation: Replication_Fall20." *American Economic Association [publisher]*,  *Inter-university Consortium for Political and Social Research [distributor]*. [https://doi.org/10.3886/E120070V1-100007](https://doi.org/10.3886/E120070V1-100007).