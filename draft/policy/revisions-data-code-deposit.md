---
layout: withtoc
title: "Policy on Revisions of Data and Code Deposits in the AEA Data and Code Repository"
---

Once an article has been published in an [AEA journal](https://www.aeaweb.org/journals/), the associated code and data deposit will also have been published in the [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/search/aea/studies). Both publications are considered permanent. 

It may become necessary or desirable to update the code and data deposit associated with a published manuscript. Reasons may include

- the code or the data have been updated to more accurately reproduce the results in the manuscript
- the code or instructions have been updated to more easily reproduce the results in the manuscript
- data which previously could not be made available is now redistributable 
- the data availability statement can be updated
- the data are found to contain confidential or copyrighted materials

This policy describes principles and practical matters related to such an update.

## Policy

### No Replacement

All previously published deposits will remain available, except when [privacy or copyright infringements](#infringement) have been identified. Each deposit has a version number (`V1`,`V2`, etc.). When updating and publishing a deposit, a new version is created. All versions connect to each other: If a user finds the `V1` version, there is an indication that a `V2` exists, and vice-versa.

### Infringement 

Should a data and code deposit be found to be in infringement of copyright, confidentiality, or other data use agreements, it may be "unpublished." The repository will continue to display metadata, including filenames, but the infringing files will no longer be downloadable.

### Identifying that the Deposit has been Updated

All data and code deposits are required to have a README. For updates, the README should clearly state (within the first paragraph, or as a banner), that it was updated after publication. Suggested language:

> The data and code in this deposit have been updated after publication of the article. For changes made, see below.

After an introductory paragraph, a clearly identified section or paragraph called "Changes made" should also be added. This should briefly and succintly describe the changes made. Examples:

> The code has been simplified, and better instructions provided. All results are the same.

> Permission was obtained by the data provider to post additional data. Figures 5, 8, and 10 are now reproducible with this archive.

### Minimal Modifications

Authors should update only those files that need to be added, edited, or removed. Wholesale replacement of the entire archive is not allowed.

### Review and Approval

In all cases, the AEA Data Editor will need to review the updated materials provided.

The AEA Data Editor will review the metadata associated with the new version. However, we are not currently able to provide the same level of pre-publication verification of computational reproducibility afforded to new submissions, except in select cases.

### Version of Record and Linking

The version of record is immutable. However, the AEA manuscript landing page and associated metadata will link to an updated deposit if

- the changes are minimal (e.g. clarity of documentation in README or code)
- unambiguously do not affect the computation of the tables and figures in the manuscript

The AEA manuscript landing page and associated metadata will link to the original version of record if

- any new data or code is provided, even if it improves the overall reproducibility of the package
- any modification to code or data has the potential to change tables and figures, even if it improves the overall reproducibility of the package

However, in all cases, the version of record on the AEA Data and Code Repository will identify, without prejudice, any later versions that may exist.

## Practical Considerations

### Prerequisites: Deposit Ownership

If the materials were deposited with the AEA prior to the [announcement](https://www.aeaweb.org/news/member-announcements-july-16-2019) of the [2019 Data and Code Availability Policy](https://www.aeaweb.org/journals/policies/data-code), the "owner" of the deposit is the AEA Data Editor. When updating the deposit, authors should [request that the AEA Data Editor share the deposit with them](mailto:dataeditor@aeapubs.org?subject=Request%20for%20access%20to%20prior%20deposit).

If the deposit was made after July 2019, one of the authors retains the ability to publish updates. No intervention by the AEA Data Editor is needed. 

### Uploading Changes

Authors should consult the generic [AEA Deposit Instructions](https://www.openicpsr.org/openicpsr/aea/deposit-instructions) and [supplementary guidance](data-deposit-aea-guidance.md). In particular, we encourage authors to update and enrich any metadata previously not entered, such as geographic scope and time periods covered by the data.

- If replacing files, you will first need to delete the original file.
- We strongly suggest not to replace anything that does not need replacing (surgical replacement rather than bulldozer replacement)
- Do not upload ZIP files. All files need to be expanded. Authors can use the "Import from ZIP" functionality. 

### Publishing Changes

When publishing a deposit, a new version number is automatically assigned. In addition, a `version title` can be provided. Suggested:

> Post-publication update fixing various issues

or

> Post-publication update providing additional data

### Identifying Updated Supplemental Materials

We are still exploring how to accurately reflect such updates on the article landing page at the [AEA journals](https://www.aeaweb.org/journals/) website.
