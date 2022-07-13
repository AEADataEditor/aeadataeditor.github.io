---
title: Display Guidelines for Trusted Repositories (other than AEA Data and Code Repository)
toc: true
layout: single
date: 2022-07-13
---

The AEA accepts replication packages from any trusted repository (see [list](https://social-science-data-editors.github.io/guidance/Requested_information_hosting.html#trusted-repositories)), as long as they meet certain display criteria, and otherwise satisfy the reproducibility criteria as per the AEA Data and Code Availability Policy. The default trusted repository is the [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/search/aea/studies). If you have doubts about whether a particular repository qualifies as a "trusted" repository, contact the AEA Data Editor before unnecessarily duplicating the deposit. 

If depositing at other trusted repositories, please follow these guidelines. 

## Title

The **title** should clearly distinguish paper and replication package. 

- The AEA requires "`Data and Code for: TITLE OF PAPER`" when both data and code are part of the replication package, with variants for data-only, code-only, and additional data packages ("`supplemental data`") that may be created to allow for different licensing (for instance, see [this guide on creating a separate data deposit](creating-separate-data-deposit))
- Other repositories may offer to automatically prefix the paper title with "`Replication package for: TITLE OF PAPER`". That is acceptable.
- Simply repeating the title of the paper is not acceptable.
- Prefixing the title of the paper with "`Data for:`" when the replication package actually contains code is not acceptable.

## README

The **README** must use the  [template README for social science replication packages](https://social-science-data-editors.github.io/template_README/).


## ZIP files

  - if possible, expand all ZIP files, so that individual files can be downloaded.
  - under no circumstances should it be necessary to download a (possibly) very large ZIP file to read the README.
  - if ZIP files must be used, the visual display of the trusted repository should allow to inspect ZIP files
    - for instance, the filenames in a ZIP file can be viewed on Zenodo, but are not browsable on Dataverse or ICPSR.
    - when ZIP files cannot be inspected before downloading, the deposit must be amended to "expand" the ZIP file. Exceptions to this rule should be requested from the AEA Data Editor.
## Contents

The **contents** of the deposit must, of course, satisfy all other requirements for AEA replication packages.

## Updating a Pre-Existing Deposit

If your pre-existing deposit does not satisfy all of these rules, you can generally create a new version of the existing deposit. Such a new version is preferable to depositing at the AEA repository, but is your choice. In some cases, a new DOI is assigned (e.g., Zenodo or ICPSR), and you must communicate the DOI of the updated deposit to the AEA Data Editor in a timely fashion.

These rules may be amended from time to time.