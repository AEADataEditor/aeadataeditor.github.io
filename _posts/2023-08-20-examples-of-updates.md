---
title:  "Details on how to update a replication package post-publication"
date: 2023-08-20
mastodon: 
tags:
  - updating 
  - improvement
  - reproducibility
---

I have previously posted about [how to update a replication package, after initial publication](). We do get more than a dozen such updates a year (see my annual reports).I'll describe a few examples.

<!-- more -->

## When to update

You should update your replication package if

- there is an error in one of the code or data files that was detected subsequent to publication. 
- you are aware of an improvement in accessibility of the replication package (data in more robust data formats, additional data documentation, more efficient code)
- you are made aware of some other issue with the replication package that needs to be addressed

Only the original authors can make these changes, but anybody can detect such changes. We field change requests coming from students attempting to replicate a package, researchers with access to restricted data that we did not have access to, or authors themselves who noticed, or were made aware of, issues with their deposit. In all cases where the initial notice does not involve the author, the Data Editor, or the Co-editor responsible for the article, will contact the author. 

## Whom to contact

For changes that do not affect the results in the actual manuscript, it is sufficient to contact the Data Editor (I may still reach out to the Editor in charge). For any corrections that affect manuscript or online appendix tables, figure, results, or conclusions, please contact the Editor in charge first, as these may require a corrigendum, erratum, or other corrections. 

> The remainder of this post will only address the changes made to the replication package, not to any other published materials.

## How to update

In a nutshell, this is described in the [policy](https://www.aeaweb.org/journals/data/policy-revisions), you should

Our general policy about how to update is posted here:

- Do **NOT** make a new deposit; edit the old deposit ([contact us](mailto:dataeditor@aeapubs.org) if you don't remember who  last accessed the deposit, or if your email has changed), creating a new version.

![Create a new version on openICPSR](/images/icpsr-create-new-version.png)

- Prepare the changes: Download the **published** archive (not your private copy of it), and make changes to code and/or data.
- Create a new version (on openICPSR, or elsewhere - procedures may differ for other systems)
- Edit the README and possibly create a "Changes.txt" or "Changelog.txt".
- In the deposit, delete the INDIVIDUAL files that need to be changed, then re-upload them (openICPSR does not allow you to simply replace by uploading... sorry)
- Make changes to **NO** other files. 
- [Re-submit](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submitting-to-the-data-editor) to the Data Editor.

## What happens after update

After you have submitted the update to the replication package, 

- the Data Editor will review the deposit for compliance with the  [policy](https://www.aeaweb.org/journals/data/policy-revisions). Changes may be requested.
- the Data Editor will publish the revised replication package (usually, this becomes **V2**). A new DOI is assigned. 
- Depending on the type of change being made, the "version of record" (linked from the article page) is adjusted (see [what the policy has to say about that](https://www.aeaweb.org/journals/data/policy-revisions#version)). NOTE: Usually, the version of record is NOT modified.
- In all cases, accessing the original deposit (**V1**) will show a banner at the top, directing interested parties to the new version.

![Redirect on openICPSR page](/images/icpsr-version2-banner.png)

## Examples

- [https://doi.org/10.3886/E148361V1](https://www.aeaweb.org/journals/data/policy-revisions#version) - [https://doi.org/10.3886/E148361V2](https://doi.org/10.3886/E148361V2) - only the README was updated (clarified), see top of the (revised) README. For this one, we updated the version of record - see link at [https://doi.org/10.1257/aeri.20210201](https://doi.org/10.1257/aeri.20210201) - because no code was impacted, and the change was a clarification. The change was initiated by the authors.

- [https://doi.org/10.3886/E172902V1](https://doi.org/10.3886/E172902V1) - [https://doi.org/10.3886/E172902V2](https://doi.org/10.3886/E172902V2) - A (small) piece of code was corrected. Since this affected the functionality of the code (though no output from the code), this did NOT change version of record - see the link to the replication package at [https://doi.org/10.1257/aer.20200961](https://doi.org/10.1257/aer.20200961). A researcher contacted the Data Editor, who then contacted the authors.

- [https://doi.org/10.3886/E184461V1](https://doi.org/10.3886/E184461V1) - [https://doi.org/10.3886/E184461V2](https://doi.org/10.3886/E184461V2) - A data-related issue (copyright and terms of use) required us to remove some data files from the deposit. This is one of the few cases where a replication package was "de-accessioned" -- the original deposit is still viewable (the list of files is still there), but cannot be downloaded. In this case, **V2** became the version of record because (a) **V1** is no longer functional (b) the impact does not affect the results of the (successful) reproduction, though it is now clear that part of the package needs proprietary data.

## Some helpful links

- [The replication package revision policy at the AEA](https://www.aeaweb.org/journals/data/policy-revisions)
- [Guidance on how to re-submit](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submitting-to-the-data-editor) (hint: it's much like the initial submission...)

