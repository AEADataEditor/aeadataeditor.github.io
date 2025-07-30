---
title: Display Guidelines for Trusted Repositories (other than AEA Data and Code Repository)
toc: true
layout: single
date: 2023-01-23
modified: 2023-09-08
---

The AEA accepts replication packages from any **trusted** repository (see [list](https://social-science-data-editors.github.io/guidance/Requested_information_hosting.html#trusted-repositories)), as long as they meet certain display criteria, and otherwise satisfy the reproducibility criteria as per the AEA Data and Code Availability Policy. The default trusted repository is the [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/search/aea/studies). If you have doubts about whether a particular repository qualifies as a "trusted" repository, contact the AEA Data Editor before unnecessarily duplicating the deposit. 

If depositing at other trusted repositories, please follow these guidelines. 

## Why deposit at a different repository

There are two main reasons why authors may want to deposit at a different repository:

- They may have already created a deposit (for instance, when releasing a working paper). Deposits should remain where they are, reducing duplication and ambiguity (but see below for changes that may need to be made).
  - Some institutions or research labs habitually create deposits. Example: [J-PAL's Dataverse](https://dataverse.harvard.edu/dataverse/jpal)
  - The [Zenodo-Github](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) integration may have been used; see notes about [Title](#title), below.
- Certain repositories may have additional features that are not available on the AEA's repository at openICPSR.
  - As of 2022, openICPSR struggles with data deposits that have more than 1,000 files or more than 30GB of content.
  - Harvard Dataverse offers up to **1TB** for free. An **API** is available.
  - Zenodo offers **50GB** per default, but can easily be expanded to more than **200GB** upon request. An API to download individual files is available.
  - Codeocean offers 2GB per capsule, but allows for easy in-the-cloud computing, i.e., replicators can immediately [duplicate a capsule](https://help.codeocean.com/en/articles/1217599-duplicating-a-compute-capsule?q=export) and start running it. 


## Title

The **title** should clearly distinguish paper and replication package. 

- The AEA requires "`Data and Code for: TITLE OF PAPER`" when both data and code are part of the replication package, with variants for data-only, code-only, and additional data packages ("`supplemental data`") that may be created to allow for different licensing (for instance, see [this guide on creating a separate data deposit](creating-separate-data-deposit))
- Other repositories may offer to automatically prefix the paper title with "`Replication package for: TITLE OF PAPER`". That is acceptable, but not preferred, as it obfuscates what the deposit actually contains.
- Simply repeating the title of the paper is not acceptable.
- Prefixing the title of the paper with "`Data for:`" when the replication package actually contains code is not acceptable.
- Users of the Zenodo-Github integration may want to use the [CITATION.cff] file in their Github repository, see [citation-file-format.github.io/](https://citation-file-format.github.io/), [Github documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files), and the [Citation File generator](https://citation-file-format.github.io/cff-initializer-javascript/)

## README

The **README** must conform to the  [template README for social science replication packages](https://social-science-data-editors.github.io/template_README/) if the deposit is for a full replication package. If the deposit is for data-only, a simplified README is acceptable, but should 

- describe salient characteristics of the data,
- the source of the data
- license information

The README must be present in PDF format (other additional formats are acceptable). The README should be able to be viewed and/or downloaded independently from the rest of the deposit, i.e., it should not be part of a single ZIP file.

> If the platform allows, select the README as the default file to display.

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

- if possible, expand all ZIP files, so that individual files can be downloaded, while preserving directory structure (may not be possible on all platforms)
- under no circumstances should it be necessary to download a (possibly very large) ZIP file to read the README. The README should be available as a separate file.
- if ZIP files must be used, the visual display of the trusted repository should allow to inspect ZIP files
  - for instance, the filenames in a ZIP file can be viewed on Zenodo, but are not browsable on Dataverse or ICPSR.
  - when ZIP files cannot be inspected before downloading, the deposit must be amended to "expand" the ZIP file. Exceptions to this rule should be requested from the AEA Data Editor.

## Contents

The **contents** of the deposit must, of course, satisfy all other requirements for AEA replication packages.

### Uploading and downloading large quantities of files

Some repositories allow for the upload of files via API or import from online services. This may be useful for particularly large data deposits.

- Zenodo: See [documentation for the Zenodo legacy API](https://developers.zenodo.org/). An example for a simple uploader in Python is on the [AEA Github repository](https://github.com/AEADataEditor/Upload-to-Zenodo). 
- Zenodo: The legacy API can also be used to download individual files from Zenodo. The [zenodo_get](https://pypi.org/project/zenodo-get/) ([Github source](https://github.com/dvolgyes/zenodo_get)) Python package allows to download entire packages. 

>  Zenodo: The legacy API is being deprecated. Once newer guidance and tools are available, we will update this page. For now, Zenodo points to [InvenioRDM](https://inveniordm.docs.cern.ch/reference/rest_api_index/) for API guidance (2023)

- Dataverse: See [documentation for Dataverse API](https://guides.dataverse.org/en/5.12/api/index.html). A R package [`dataverse-client-r`](https://github.com/IQSS/dataverse-client-r) can download individual files or complete packages. [pyDataverse](https://pydataverse.readthedocs.io/en/latest/) is Python code  to interface with Dataverses.

## Additional repository-specific guidance

### Zenodo

The AEA has a "community" on Zenodo: [https://zenodo.org/communities/aeajournals](https://zenodo.org/communities/aeajournals)

On Zenodo, you should use the "Submit for review" functionality if you do not already have a public deposit:

- Only draft deposits can be submitted for review
- Both the uploader (you) and the curator (the AEA Data Editor) can modify metadata and files

> Zenodo [Create new upload](https://help.zenodo.org/docs/deposit/create-new-upload/), but do NOT publish!
>
> - We strongly suggest not uploading a ZIP file, unless you need to preserve folder structure.
> - The README must be individually uploaded and [selected as the file to display](https://help.zenodo.org/docs/deposit/manage-files/#preview).

> Zenodo [Submit for Review](https://help.zenodo.org/docs/share/submit-for-review/)

If you already have a published deposit, you can "Submit to community". 

- Only published deposits can be submitted for inclusion in a community
- Only metadata can be edited (any revision to files can only be handled by creating a new version)

> Zenodo [Submit to community for inclusion](https://help.zenodo.org/docs/share/submit-to-community/)

At the time of writing, [Zenodo allows](https://help.zenodo.org/docs/deposit/manage-files/) for "up to 50GB per record with a maximum of 100 files." To the extent possible (conditional on preserving directory structure), you should unzip as many files as possible. 

### Codeocean

If you can publish your data freely, and the data is less than 2GB, you can construct your entire replication package on CodeOcean. If on the other hand your replication package requires future replicators to download data, then you will not be able to use Codeocean.

You can deduce the presumptive DOI on Codeocean from the capsule number, visible in the address bar of your browser, e.g.,

> `https://codeocean.com/capsule/1234567/tree`

You can compute the DOI in the following way:

{% include deposit-doi-codeocean.html %}


## Publishing, saving, and sharing

Some repositories offer the ability to share the contents of the deposit prior to publishing it. Authors are encouraged to avail themselves of this opportunity.

Otherwise, authors must publish the repository, and communicate the DOI to the AEA Data Editor as part of the [Data and Code Availability Form](https://www.aeaweb.org/journals/forms/data-code-availability).

- Zenodo: see [link sharing](https://help.zenodo.org/docs/share/link-sharing/) or [submit for review](https://help.zenodo.org/docs/share/submit-for-review/)
- Dataverse: See [Private URL to Review Unpublished Dataset](https://guides.dataverse.org/en/5.12/user/dataset-management.html#)
- Codeocean: Invite the AEA Data Editor as a [collaborator to the capsule](https://help.codeocean.com/en/articles/1052886-sharing-capsules).

## After publication of the manuscript

Once the AEA has published your manuscript, the manuscript DOI will be locked in place. At this time, there is one final small step that needs to be done: The author should     adjust the "backlink" to the published manuscript (the link pointing from the deposit to the manuscript). While the AEA publication staff handle the "forward link" (from the manuscript to the replication package), and handle the backlink for any deposit in the AEA Data and Code Repository, they are unable to do so for any other trusted repository (including PSID and similar non-AEA repositories at ICPSR).

Here are some guidelines on how to do that update:

### Adding manuscript DOI to CodeOcean capsule

Authors will need to email Codeocean support ([support@codeocean.com](mailto:support@codeocean.com)), providing them with the capsule number and the DOI to be linked from the capsule. Support will update the capsule metadata. 

Normally, this should not generate a new version (`V2`), but rather, a `V1.1`. The DOI of the deposit should not change. 

![Updated CodeOcean after adding manuscript DOI](/images/codeocean-update-link-doi.png)

### Adding manuscript DOI to other openICPSR repositories

Authors will need to edit the metadata under the "Related Publications" heading:

- Log in to openICPSR 
- Navigate to your deposits, and select the right one.
- Do NOT create a new version!
- Scroll down to the "Related publications" section.

![related publications](/images/openicpsr-metadata-related-publications.png)

- In the modal, select "`Import via DOI`":

![import via DOI](/images/project-related-icpsr-modal1.png)

- Enter the DOI as per instructions

![enter the DOI](/images/project-related-icpsr-modal2.png)

- From the relationship dropdown, select "`is supplemented by`":

![Select relationship](/images/project-related-icpsr-modal3.png)

- Select `Save and Apply`. The change will take effect immediately, there is no need to go through the publication process.

### Adding related manuscript to Dataverse

This should be applicable to any Dataverse instance.

- Log in to your Dataverse account
- Under profile name, click on "`My Data`", wait for information to load
- Then click on the correct dataset / code / replication package
- Click on `Edit Data > Metadata`
- scroll down to "`Related publication`"
- choose DOI under "`Identifier Type`"
- paste the DOI provided
- You may need to remove an older (obsolete) entry
- Save and then don't forget to publish 

> Contributed by Charlotte Cavaillé.

### Adding related manuscript to Zenodo

- See [Edit published records](https://help.zenodo.org/docs/deposit/manage-records/#edit) for details on how to edit the metadata of a deposit (a "record")
- Go to [My Uploads](https://zenodo.org/me/uploads) and find the record.
- Click `Edit`
- Scroll down to `Related works`
- Choose "`Add related work`" 
- Then 
  - Choose `is supplement to` as `Relation`. 
  - Enter the DOI of the published article into the field `Identifier`
  - Choose `DOI` as `Scheme`
  - Choose "Publication/Journal article" as `Resource type`
- Optionally choose `Preview`, then `Publish`. 

This does NOT create a new version. Do not change any files.

## Special notes

None at present.

## Updating a Pre-Existing Deposit

If your pre-existing deposit does not satisfy all of these rules, you can generally create a new version of the existing deposit. Such a new version is preferable to depositing at the AEA repository, but is your choice. In some cases, a new DOI is assigned (e.g., Zenodo or ICPSR), and you must communicate the DOI of the updated deposit to the AEA Data Editor in a timely fashion.

> NOTE: Unless the chosen repository can be shared prior to publication (Dataverse), all such changes are public and visible to others.

## Examples

### Zenodo

Good examples can be found in the [AEA Journal Community](https://zenodo.org/communities/aeajournals/), for instance:

- U.S. Geological Survey, & Brooks, Leah. (2022). USGS National Map 3DEP 1 Arc-second Digital Elevation Models (DEMs): Full Coverage for U.S. Interstate Highway System [Data set]. Zenodo. [https://doi.org/10.5281/zenodo.5830968](https://doi.org/10.5281/zenodo.5830968) (83GB)
- Ministerio de Desarrollo Productivo Argentina, Daruich, Diego, Kozlowski, Julian, & Vilhuber, Lars. (2022). Precios Claros (2016-05 - 2018-03) [Data set]. In American Economic Journal: Macroeconomics. Zenodo. [https://doi.org/10.5281/zenodo.6568295](https://doi.org/10.5281/zenodo.6568295) (44GB, about 1,200 files)

### Codeocean

Some examples of replication packages on CodeOcean are:

- Ryan Chahrour, Robert Ulbricht (2022) Compute Capsule for: Robust Predictions for DSGE Models with Incomplete Information [Source Code]. [https://doi.org/10.24433/CO.5177698.v1](https://doi.org/10.24433/CO.5177698.v1)
- Mónica García-Pérez, José Fernandez, Sandra Orozco-Aleman (2024) Compute Capsule for: Unraveling the Hispanic Health Paradox [Source Code]. [https://doi.org/10.24433/CO.7234900.v1](https://doi.org/10.24433/CO.7234900.v1)

### Dataverse

- Cavaillé, Charlotte, 2022, "Replication Code for "Immigration and Support for Redistribution: Lessons from Europe"", [https://doi.org/10.7910/DVN/6WTDRH](https://doi.org/10.7910/DVN/6WTDRH), Harvard Dataverse, V3 

## Note

These rules may be amended from time to time.
