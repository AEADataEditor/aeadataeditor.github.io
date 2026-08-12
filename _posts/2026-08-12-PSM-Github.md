---
title: "PSM: Please be precise when using Github as input to scientific articles."
categories: dataeditor
date: 2026-08-12
mastodon:
bluesky: 
tags:
  - data editor tips
  - reproducibility
  - data citation
  - Github
  - licenses
---

If you use Github as an deposit for your scientific output, or you are re-using somebody else's Github deposit, please be precise. I have some thoughts...


<!-- more -->

From a recent (draft) replication package:

> Data on Kelly et al. (2021)'s patent indicator are downloaded from the authors’ GitHub repository. A copy of the data is provided as part of this archive. The data are in the public domain. To download, visit at https://github.com/KPSS2017, click the pinned repository named "Measuring-Technological-Innovation-Over-the-Long-Run-Extended-Data," and download "PatentSimilarityImportanceBreakthrough_forPost2022.csv.zip".

A few things, first for those re-using the data, and then for those providing the data.

## For re-users

### Citing

If using the Github data, and not the replication package to the original article, the Github data must be cited. Here, that would be 

> Kelly, B., Papanikolaou, D., Seru, A. and Taddy, M. 2023. *Updates and Extension of Measuring Technological Innovation Over the Long Run*. https://github.com/KPSS2017/Measuring-Technological-Innovation-Over-the-Long-Run-Extended-Data, version from November 2023.

On the [Github README](https://github.com/KPSS2017/Measuring-Technological-Innovation-Over-the-Long-Run-Extended-Data/blob/main/README.md), the authors actually say 

> The version released on Sept 29, 2023 is the latest.

but the [commits](https://github.com/KPSS2017/Measuring-Technological-Innovation-Over-the-Long-Run-Extended-Data/commits/main/) on the Github actually tell a different story: there are September and November updates to the deposit. Whether those are materially different is not clear (these are ZIP files), but as a re-user, you should identify the version you ACTUALLY used.

Note that the authors ask that their published article be cited as a source. That is fine, as long as the re-user ALSO cites the actual source of the data, which is Github.

### Downloading

The very verbose description is actually not the best way. First, the actual Github repository has a direct link. The *pinned* repositories can change over time, without any reason. Re-users should not rely on that. In fact, as I mentioned above, there are multiple commits. Unless the Github owners manipulate those commits (possible), the specific commit is what should be identified, possibly in the citation, but definitely in the download instructions. Here is the same verbose instructions expressed as a single URL:

> Download 
> <https://github.com/KPSS2017/Measuring-Technological-Innovation-Over-the-Long-Run-Extended-Data/blob/42f283517d72d90272f151867bb7b22744e23b2f/PatentSimilarityImportanceBreakthrough_forPost2022.csv.zip>

which preserves the metadata (it doesn't directly download the data, but rather, allows you to see the context in which you are downloading the data). Much simpler.

### Distributing

The quote I provided mentions "data are in the public domain." That is incorrect. The data are downloadable by anybody without registration. However, "public domain"  is a legal term that means that nobody has the copyright on the data. Possibly because the entity producing the data is legally excluded from claiming copyright (oversimplifying somewhat, in the US, the federal government), or because the person producing the data has explicitly relinquished this (often under a "CC0"  license). 

But in the absence of true "public domain", the data are copyrighted by the original authors. Fair-use is fine (so using the data is likely the intent of posting it on the internet here), but re-purposing the data may not be. Copyright = all rights reserved does not need an explicit mention! So strictly speaking, you need the authors' permission to redistribute the data, or you might have to claim "fair use" explicitly. We usually send the re-users to ask permission, which is cleaner.

## For authors

All of the above can be greatly simplified if authors (those posting on Github) followed some simple best practices:

### Define a license

Authors should clearly specify the license under which the data are released. Common licenses include Creative Commons (CC) licenses, which allow for various levels of reuse of data, or open-source software licenses like MIT or GPL, which might be more relevant for code. A dual-license setup can work. See [guidance](https://aeadataeditor.github.io/aea-de-guidance/Licensing_guidance) on my website. The license should be expressed as a `LICENSE.txt` or `LICENSE.md` file in the root of the repository, it will be picked up and displayed in the sidebar by Github.

If authors do NOT want to provide a general license, that is also fine, but they should likely explicitly say it, to be clear, although that may not be legally required: "Copyright John Doe and Alice Smith, all rights reserved. Permission to redistribute or reuse this data must be obtained from the authors." 

### Versioning

Rather than having re-users guess at versions, and have long commit-based URLs, create tags or releases. Very easy to do in both `git`  and on Github. That would allow for much simpler URLs:

> Download [https://github.com/KPSS2017/Measuring-Technological-Innovation-Over-the-Long-Run-Extended-Data/blob/ **v1.1** /PatentSimilarityImportanceBreakthrough_forPost2022.csv.zip](https://github.com/KPSS2017/Measuring-Technological-Innovation-Over-the-Long-Run-Extended-Data/blob/v1.1/PatentSimilarityImportanceBreakthrough_forPost2022.csv.zip)

(OK, that's not much shorter in this case, because of the long repository and file names, but it is easier to read).

### Citation

Authors in general prefer that you cite the article, because under current academic norms (at least in economics), is the only thing that counts. Nevertheless, if the article is published in 2021, and the data in 2023, re-users are misleading their readers because they materially reference data that does not exist at the cited location (the article, or its replication package), and cannot be easily linked. The solution is to cite both. 

And to make that easy, use the [CITATION.cff](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) file. It, too, is highlighted by Github in the right panel. 

### Preserving

And finally, if you have license and citation all tidied up, why not preserve it, and get a DOI to boot? This does away with the fragility of deposits and commits (anybody can delete their Github repo forever, in 30 seconds flat), and simplifies citation as well. You can do so nearly automatically (if creating releases) [via Zenodo](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content), or to [Dataverse](https://github.com/marketplace/actions/dataverse-uploader-action). 

Re-users can then simply use the Zenodo version, which has a DOI, and is guaranteed to be preserved. 