---
title: Display Guidelines for Trusted Repositories (other than AEA Data and Code Repository)
toc: true
layout: single
date: 2022-07-13
---

The AEA accepts replication packages from any **trusted** repository (see [list](https://social-science-data-editors.github.io/guidance/Requested_information_hosting.html#trusted-repositories)), as long as they meet certain display criteria, and otherwise satisfy the reproducibility criteria as per the AEA Data and Code Availability Policy. The default trusted repository is the [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/search/aea/studies). If you have doubts about whether a particular repository qualifies as a "trusted" repository, contact the AEA Data Editor before unnecessarily duplicating the deposit. 

If depositing at other trusted repositories, please follow these guidelines. 

## Why deposit at a different repository

There are two main reasons why authors may want to deposit at a different repository:

- They may have already created a deposit (for instance, when releasing a working paper). Deposits should remain where they are, reducing duplication and ambiguity (but see below for changes that may need to be made).
  - Some institutions or research labs habitually create deposits. Example: [J-PAL's Dataverse](https://dataverse.harvard.edu/dataverse/jpal)
- Certain repositories may have additional features that are not available on the AEA's repository at openICPSR.
  - As of 2022, openICPSR struggles with data deposits that have more than 1,000 files or more than 30GB of content.
  - Harvard Dataverse offers up to **1TB** for free. An **API** is available.
  - Zenodo offers **50GB** per default, but can easily be expanded to more than **200GB** upon request. An API to download individual files is available.

## Title

The **title** should clearly distinguish paper and replication package. 

- The AEA requires "`Data and Code for: TITLE OF PAPER`" when both data and code are part of the replication package, with variants for data-only, code-only, and additional data packages ("`supplemental data`") that may be created to allow for different licensing (for instance, see [this guide on creating a separate data deposit](creating-separate-data-deposit))
- Other repositories may offer to automatically prefix the paper title with "`Replication package for: TITLE OF PAPER`". That is acceptable, but not preferred, as it obfuscates what the deposit actually contains.
- Simply repeating the title of the paper is not acceptable.
- Prefixing the title of the paper with "`Data for:`" when the replication package actually contains code is not acceptable.

## README

The **README** must use the  [template README for social science replication packages](https://social-science-data-editors.github.io/template_README/) if the deposit is for a full replication package. If the deposit is for data-only, a simplified README is acceptable, but should 

- describe salient characteristics of the data,
- the source of the data
- license information

## Summary / Abstract

The summary should be short, but informative. It can include the abstract of the article itself. It should not include information on the related article (which has its own field). 

## Additional fields / metadata

Some repositories have the ability to provide related articles (most) or other related information. 

Authors will need to return to these sites to update these fields with

- the DOI of the published manuscript
- the DOI of any related deposits 

This ensures that the information is findable in both directions, not just from the article to the data and code.

> NOTE: In any repository other than the AEA's openICPSR repository, this action must be undertaken by the **author**, **after** the publication of the article. It cannot be done by AEA staff.

## ZIP files

- if possible, expand all ZIP files, so that individual files can be downloaded.
- under no circumstances should it be necessary to download a (possibly) very large ZIP file to read the README.
- if ZIP files must be used, the visual display of the trusted repository should allow to inspect ZIP files
  - for instance, the filenames in a ZIP file can be viewed on Zenodo, but are not browsable on Dataverse or ICPSR.
  - when ZIP files cannot be inspected before downloading, the deposit must be amended to "expand" the ZIP file. Exceptions to this rule should be requested from the AEA Data Editor.

## Contents

The **contents** of the deposit must, of course, satisfy all other requirements for AEA replication packages.

### Uploading large quantities of files

Some repositories allow for the upload of files via API or import from online services. This may be useful for particularly large data deposits.

- Zenodo: See [documentation for the Zenodo API](https://developers.zenodo.org/). An example for a simple uploader in Python is on the [AEA Github repository](https://github.com/AEADataEditor/Upload-to-Zenodo). The [zenodo_get](https://pypi.org/project/zenodo-get/) Python package allows to download entire packages. The API can also be used to download individual files from Zenodo.
- Dataverse: See [documentation for Dataverse API](https://guides.dataverse.org/en/5.12/api/index.html). A R package `[dataverse-client-r](https://github.com/IQSS/dataverse-client-r)` can download individual files or complete packages. [pyDataverse](https://pydataverse.readthedocs.io/en/latest/) is Python code  to interface with Dataverses.

## Publishing, saving, and sharing

Some repositories offer the ability to share the contents of the deposit prior to publishing it. Authors are encouraged to avail themselves of this opportunity.

Otherwise, authors must publish the repository, and communicate the DOI to the AEA Data Editor as part of the [Data and Code Availability Form](https://www.aeaweb.org/journals/forms/data-code-availability).

- Zenodo: pre-publication sharing not available
- Dataverse: See [Private URL to Review Unpublished Dataset](https://guides.dataverse.org/en/5.12/user/dataset-management.html#)

## Special notes

### Zenodo

When editing the metadata, depositors should add the "American Economic Association" community. The AEA Data Editor will be notified, and will verify compliance, then accept the request.

![Communities field on Zenodo](/images/zenodo-community-empty.png)


![Selecting AEA in the Communities field on Zenodo](/images/zenodo-community-select.png)


![AEA selected in the Communities field on Zenodo](/images/zenodo-community-aea.png)

## Updating a Pre-Existing Deposit

If your pre-existing deposit does not satisfy all of these rules, you can generally create a new version of the existing deposit. Such a new version is preferable to depositing at the AEA repository, but is your choice. In some cases, a new DOI is assigned (e.g., Zenodo or ICPSR), and you must communicate the DOI of the updated deposit to the AEA Data Editor in a timely fashion.

> NOTE: Unless the chosen repository can be shared prior to publication (Dataverse), all such changes are public and visible to others.

## Examples

### Zenodo

Good examples can be found in the [AEA Journal Community](https://zenodo.org/communities/aeajournals/), for instance:

- U.S. Geological Survey, & Brooks, Leah. (2022). USGS National Map 3DEP 1 Arc-second Digital Elevation Models (DEMs): Full Coverage for U.S. Interstate Highway System [Data set]. Zenodo. [https://doi.org/10.5281/zenodo.5830968](https://doi.org/10.5281/zenodo.5830968) (83GB)
- Ministerio de Desarrollo Productivo Argentina, Daruich, Diego, Kozlowski, Julian, & Vilhuber, Lars. (2022). Precios Claros (2016-05 - 2018-03) [Data set]. In American Economic Journal: Macroeconomics. Zenodo. [https://doi.org/10.5281/zenodo.6568295](https://doi.org/10.5281/zenodo.6568295) (44GB, about 1,200 files)

## Note

These rules may be amended from time to time.