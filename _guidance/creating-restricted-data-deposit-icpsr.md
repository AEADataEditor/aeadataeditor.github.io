---
title: Depositing Restricted Data at ICPSR for AEA Publications
toc: true
layout: single
date: 2022-07-13
---

This guide describes how to create a restricted-access data deposit at ICPSR, associated with an AEA publication. The guide also describes what authors should expect in terms of timelines and process. This reflects current practice as of July 2022, but may change. The process of creating restricted-access data deposits remains a highly interactive process, and authors should always reach out to the AEA Data Editor with questions. 

> If authors have created a restricted-access data deposit elsewhere, they probably do not need to duplicate that effort. Contacting the AEA Data Editor is the best way to ensure compliance with the AEA Policy.

### Preliminaries

All restricted-access deposits should ONLY include materials that absolutely need to be restricted. In general, that implies that all code, and any non-sensitive data, must be [separately deposited](data-deposit-aea.md) under an open license. 

### Special notes on preparation

We strongly suggest here to include a license file that describes the access conditions. The file should be uploaded in TXT or PDF format, and called "LICENSE.pdf". Alternate names, like "Terms of Use", are acceptable. The license should only be as restrictive as necessary. In particular, it must allow for reproducibility checks without restrictions, in order to comply with AEA policy. We also strongly suggest that the license allow for more general re-use of the data, for instance in novel publications, subject to any of the restrictions that are imposed on the data. Note that the license may change as ICPSR takes custodianship of these data, but always involves a discussion with the author.

The README should also be focused on sources, restrictions, and access conditions for the data provided here, and not duplicate the information in the (unrestricted) replication package. It should clearly identify how the data were collected or created, and importantly, under what conditions the data can be redistributed: any IRB approvals and conditions on redistribution, or data use agreements that the authors engaged in and that permit for redistribution.

### Depositing data

You should follow the [generic preparation and upload guidelines](data-deposit-aea.md) up to the submission questions. 


### Submitting to the Data Editor

Once you are satisfied that all data files are present, are complete, and all metadata is satisfactory, including all required elements filled out, you should **submit** the deposit, by changing the **status** of the deposit:

![submit project](/images/project-submit.png)

Choose "Submit to AEA" (or "Resubmit") under "Change Status".

#### Submission questions

You will be presented with a page to confirm that you are going through with the submission. You will then be presented with a page, asking various questions. 

> You should answer these questions in regards to the data in the deposit you are submitting. This is where you indicate that the data is sensitive and that access should be restricted. 

Contact the Data Editor if you have any questions or concerns.

##### Can individuals be identified?

![Identification question 1](/images/icpsr-submit-q1.png)

The normal answer to this question is "No," even when the data can be deemed sensitive. However, if for some reason, there are direct identifiers included, such as names or precise addresses for individuals, the answer here should be "Yes". A "Yes" will always lead to the data deposit being classified as "restricted".

##### Are the data sensitive?

![Sensitivity question 2](/images/icpsr-submit-q2.png)

Even when the answer to the previous question is "No", the data may still be deemed sensitive. This may be due to your own assessment, or may be required by IRB or ethics board. If you are reading this guide, the likely answer to this question is "Yes."

##### Distribution question

![Distribution question](/images/icpsr-submit-q3.png)

"Restricted access" means that data will be distributed through ICPSR's [Restricted Data Access Mechanism](https://www.icpsr.umich.edu/web/pages/ICPSR/access/restricted/). If the data are not to be restricted, you are on the wrong page.

#### Choose a license

![License question](/images/icpsr-submit-q4-license.png)

You should choose "Other" from the drop-down menu, since none of the licensing options are appropriate for a restricted-access repository. See our [Licensing Guidance](Licensing_guidance).


#### Finalizing

Press "submit." Should you have forgotten something, you can "recall" the submission, fix the issue, and re-submit. 

### Next steps

#### Contact the AEA Data Editor

For all restricted deposits, please alert the AEA Data Editor directly of the deposit. Mention the manuscript number, as well as the desired distribution method as outlined at [ICPSR's page](https://www.icpsr.umich.edu/web/pages/ICPSR/access/restricted/). The AEA Data Editor is able to access the submitted but unpublished restricted deposit. If you need a signed DUA, NDA, or other document, please contact the AEA Data Editor immediately.

#### AEA and ICPSR Workflow

For all restricted deposits, the AEA will add them to ICPSR's "quick curation workflow." The deposit you just created will NOT be separately published (as has been done in the past), avoiding duplicate DOIs and possible confusion.

Even the "quick curation workflow" can take several months, depending on other workloads at ICPSR. You do not need to wait for completion of the process to proceed with other actions related to the manuscript. In particular, it may happen that the restricted data may become available only after publication of the manuscript. This is not of (immediate) concern.

Once ICPSR has started to prepare the deposit for publication, a DOI will be assigned. The AEA will add this DOI to the online manuscript, and link it to the (unrestricted) replication package. The AEA *may* ask the authors to amend the README in the (unrestricted) replication package. 

### Possible questions

#### When will the restricted-data deposit become available to the public?

We do not know at the time of deposit, but we endeavor to make it public as soon as possible. As we get more information on the process, we, or the ICPSR curators, will contact you.

#### Are there any specific pieces of information that authors should provide to speed up the process? 

We do not know yet. Please check back.

#### General ICPSR deposits are  "available only to ICPSR members". Is that true for my deposit as well?

We do not know yet. Please check back.
