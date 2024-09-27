---
title: Creating a Restricted Data Deposit  for AEA Publications
toc: true
layout: single
date: 2023-01-23
---

> THIS GUIDE IS OUTDATED, AND SHOULD NOT BE FOLLOWED. IT IS KEPT FOR HISTORICAL REASONS.


This guide describes how to create a restricted-access data deposit at ICPSR, associated with an AEA publication. The guide also describes what authors should expect in terms of timelines and process. This reflects current practice as of July 2022, but may change. The process of creating restricted-access data deposits remains a highly interactive process, and authors should always reach out to the AEA Data Editor with questions. 

> If authors have created a restricted-access data deposit elsewhere, they probably do not need to duplicate that effort. Contacting the AEA Data Editor is the best way to ensure compliance with the AEA Policy.

### Preliminaries

All restricted-access deposits should ONLY include materials that absolutely need to be restricted. In general, that implies that all code, and any non-sensitive data, must be [separately deposited](data-deposit-aea) under an open license. 

### Special notes on preparation

The README should be focused on sources and documentation of the data for the data provided here, useful once access has been obtained. The README is not accessible separately from the data (it is subject to the same access control conditions), and thus should not contain information about sources and access that is critical to understanding whether it is useful to actually request access to the data. It may thus be useful or necessary to duplicate the information from the restricted README in the (unrestricted) replication package. 

The unrestricted replication package should clearly identify how the data were collected or created, and importantly, under what conditions the data can be redistributed: any IRB approvals and conditions on redistribution, or data use agreements that the authors engaged in and that permit for redistribution.

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

NOTE: *The AEA Data Editor is able to access the submitted but unpublished restricted deposit. If you need a signed DUA, NDA, or other document, please contact the AEA Data Editor immediately.*

### Next steps

#### Contact the AEA Data Editor

For all restricted deposits, please alert the AEA Data Editor directly of the deposit. Mention the manuscript number, as well as the desired distribution method as outlined at [ICPSR's page](https://www.icpsr.umich.edu/web/pages/ICPSR/access/restricted/). 

#### Choice of methods 

All access options require an **application**, a **secure computer or room**, and **IRB approval**. As of the time of writing of this page, the following options are available:

- **Secure Download**: Approved researchers can securely download to the secure location specified in an application.
- **Virtual Data Enclave (VDE)**:  Approved researchers access the data in a secure remote desktop (Windows) on ICPSR’s servers. They are unable to remove files from the system. To obtain output, ICPSR conduct a disclosure review on requested files. This is similar in technology and process to files available through NORC (which provides services to the Bureau of Labor Statistics and the Economic Research Service of the Department of Agriculture) and various European access mechanisms.
  - For more information on the VDE, see [ICPSR VDE website](https://www.icpsr.umich.edu/VDE/)
- **Physical Data Enclave (PDE)**: The researcher must travel to Ann Arbor, MI, and access the data in a secure room on ICPSR's premises.

The AEA will support any of these access methods. 

#### ICPSR Ingest Workflow

For all restricted deposits, the AEA will add them to ICPSR's "quick curation workflow." The deposit you just created will NOT be separately published (as has been done in the past), avoiding duplicate DOIs and possible confusion. 

ICPSR's "quick curation workflow" ingests the data you deposited into the general ICPSR (not the openICPSR) data warehouse. 

This will affect primarily findability: When searching on the web site of the general data warehouse, packages at both ICPSR and openICPSR can be found. When searching on the [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/search/aea/studies), only packages on openICPSR will be listed. Your restricted data package will not be listed amongst the AEA packages.

Even the "quick curation workflow" can take several months, depending on other workloads at ICPSR. You do not need to wait for completion of the process to proceed with other actions related to the manuscript. In particular, it may happen that the restricted data may become available only after publication of the manuscript. This is not of (immediate) concern.

#### Wrapping up

Once ICPSR has started to prepare the deposit for publication, a DOI will be assigned. The AEA will add this DOI to the online manuscript, and link it to the (unrestricted) replication package. The AEA *may* ask the authors to amend the README in the (unrestricted) replication package (leading to an update to the replication package, typically `V2`). See guidelines for the [Revision Policy](https://www.aeaweb.org/journals/data/policy-revisions) for instructions on how to amend the README.


### Possible questions

#### When will the restricted-data deposit become available to the public?

We do not know at the time of deposit, but we endeavor to make it public as soon as possible. As we get more information on the process, we, or the ICPSR curators, will contact you.

#### Are there any specific pieces of information that authors should provide to speed up the process? 

We do not know yet. Please check back.

#### General ICPSR deposits are  "available only to ICPSR members". Is that true for my deposit as well?

No, your deposit will be available to anybody, subject to the distribution restrictions.

#### Can depositors access their own data deposit?

The unpublished deposit remains accessible to the depositor. They can assign "Download" rights to any person, who can then download, but not otherwise modify the data deposit. To do so, go to the "Share Project" button in your deposit:

![Share Project](/images/openicpsr-restricted-share.png)

Add the sharee's email to the correct field, and select "`Allow user to download contents`"

![Sharing for download onlyh](/images/openicpsr-restricted-share3.png)

This should update the list of users with certain permissions:

![Permissions view](/images/openicpsr-restricted-share4.png)

Note that you take full responsibility for sharing. At any point, the permission can be removed by clicking on the trash can next to the user name.

#### This process is too complicated for my data

We are looking into other options. In order to satisfy our requirements, the approval process must be disconnected from the original authors (authors cannot be gatekeepers, unless unavoidable). This severely limits the options.

Please talk to us if you know of other options that you think might satisfy the following conditions:

- the approval process does not involve the author
- the approval process can be maintained for a minimum of five years after publication of the manuscript
- the approval process respects the conditions imposed on data access by the author as well as the author's data providers (i.e., must be compliant with the particular DUA, contract, or IRB protocol governing access to the author's data)

Currently known options:

- Dataverse allows for a guestbook, which also requires acknowledgement of any license-specific questions. See [instructions](https://guides.dataverse.org/en/4.13/user/dataverse-management.html). Untested, but likely to meet certain criteria. Unlikely to be compliant if IRB approval is required.

Known not be acceptable:

- Zenodo allows for "restricted access" but always requires approval by the depositor. This does not satisfy our criteria.