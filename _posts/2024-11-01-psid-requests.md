---
title:  "How to respond to data provider requests for data removal (take-down requests)"
date: 2024-11-01
mastodon: 
twitter:
bluesky: 
tags:
  - data editor tips
  - replication packages
  - terms of use
---

The [AEA Data and Code Availability Policy](https://www.aeaweb.org/journals/data/data-code-policy) asks that authors provide access to all data used in a published paper. But it also acknowledges that there are cases where data cannot be shared. This may be due to privacy concerns, proprietary rights to the data that are not the author's, or terms of use that prohibit the sharing, redistribution, or publication of data. 

So what happens when an author inadvertently does share such data, and the data provider finds out, and is not happy? Let's call this a "take-down request." The data provider asks that the author remove the data from the replication package. But the author is committed (by [signing an agreement](https://www.aeaweb.org/journals/forms/data-code-archive-agreement)) to not withdrawing the replication package. How to proceed? Read on!

<!-- more -->

## In a nutshell

The gist of the solution is the following, for AEA manuscripts (which I obviously know well), but probably similarly for other journals:

- Remove the infringing data from V1 of the replication package.
- [Ideally] Create a new, separate deposit that is in compliance with the data provider's terms of use.
- Document the new location of the now absent data in the README of the replication package.
- Submit the revised replication package to the journal.
- The journal publishes V2 of the replication package, which is now compliant.


## An example: PSID data

For years, I as Data Editor have alerted authors when I detected data that infringes on terms of use. Two of the most frequent cases are the Panel Study of Income Dynamics (PSID) and the UNSD's Comtrade data. We even have an [FAQ entry dedicated to the PSID case](https://www.aeaweb.org/journals/data/faq#psid) and a [copy-and-paste entry in our "most frequent errors" document](https://github.com/AEADataEditor/replication-template/blob/master/sample-language-report.md?plain=1#L243).

But what if PSID data does end up in a deposit, either because I missed it (believe it or not, I'm not perfect), or because the replication package was published before the Data Editor was appointed?[^1] In fact, on November 1, 2024, the folks at PSID did just that: Contacted a large number of authors that had included PSID data in their replication packages, asking them to remove the data. 

It is worth reminding that the [PSID terms of use](https://simba.isr.umich.edu/U/CondUse.aspx), which everybody agrees to when downloading the data, are quite clear: 

> 4. Not transfer PSID public data that has been downloaded from the website, including user-created data extracts, to any third parties...

[^1]: I was appointed as Data Editor position  in 2018, and we started verification of packages in 2019. We also only do a cursory review of Papers and Proceedings, though they remain subject to the same Data and Code Availability Policy.

> So what can authors do?

### Preliminary steps

The first steps involve getting access to your own replication package. This may differ by when the replication package was published.[^2]

[^2]: The dividing line is approximately Oct 1, 2019. In 2019, [we migrated approximately 2,500 older replication packages into openICPSR](https://aeadataeditor.github.io/aea-supplement-migration/programs/aea201910-migration.html). Authors were not involved in this process, and so do not have operational access to the replication package. They do, however, have ownership of the deposit, and can request access to it.


- For authors with papers published before 2019 (approximately)
  - All authors will need to get an openICPSR login, which will serve them both for the changes to the AEA and for creating the new PSID deposit.
  - They will need to request access to the deposit. The [openICPSR helpdesk](https://www.openicpsr.org/openicpsr/contactUs) may be able to help with that. The authors should mention the URL or DOI, and the openICPSR login they want the deposit associated with. 

- For authors with more recent papers:

  - They will need to re-create an ICPSR account **with the same email as previously used** since [ICPSR changed their login system in Feb 2024](https://researcherpassport.icpsr.umich.edu/help). The [openICPSR helpdesk](https://www.openicpsr.org/openicpsr/contactUs) may help with that.
  - They need to then [create a new version](https://www.aeaweb.org/journals/data/revisions-policy#createnewversion).

![Create a new version](/images/icpsr-create-new-version.png)]

### Rules that apply to revisions of replication packages

Here are a few simple rules:

- The modified package should differ only as necessary from the original package. Less work for the author, greater clarity for replicators, everybody wins.
- Journal-specific policies may apply. For instance, the AEA has a [Policy on Revisions of Data and Code Deposits in the AEA Data and Code Repository](https://www.aeaweb.org/journals/data/revisions-policy). Among other things, it requires that all changes be clearly identified. 

### Fixing the problem

Once the preliminaries are done, here's what authors need to do to remain compliant with AEA policy (similar rules may apply at other journals):

- PSID actually has a way to properly and openly preserve the user-created extracts in compliance with their terms of use. It is the [PSID Repository on openICPSR](https://www.openicpsr.org/openicpsr/psid).  
- For sake of discussion, the "original replication package" is V1. The replacement replication package will be V2.

![Image of PSID repository](/images/psid-repository.png)

- For sake of discussion, consider the case where V1 contains a single file `psid.dta`.

#### PSID deposit

- Authors should [create a new deposit at the PSID repository](https://www.openicpsr.org/openicpsr/psid/deposit-instructions) with title "**Supplementary data** for: [NAME OF THE MANUSCRIPT]". 
  - Put into it ONLY the PSID data `psid.dta`. Do not put other things into this deposit.
  - You might want to add the **DOI** of V1 and the **DOI** of the manuscript in the "Related publications" section  (use the `Import from DOI` functionality, choose `is supplemented by` for the `Relationship` field)
  - Publish it. 
  - Remember the DOI (not the URL). Call this the "[PSID DOI]". Replace this with the **actual** DOI everywhere it is mentioned below!

#### Back in the AEA deposit

- Log on to the V1 deposit. You should be in "Modifying" mode.
- Remove (delete) the same PSID data (`psid.dta`) you just uploaded into the PSID deposit, from the openICPSR AEA deposit V1. 
- Update the README with "PSID data for this package can be obtained from [PSID DOI]" in an appropriate location. The ideal README follows the [Template README published by the Social Science Data Editors](https://doi.org/10.5281/zenodo.7293838), but make only minimal changes to the README in this deposit.
  - Delete the old README (*completely*),
  - Upload the new README (in PDF format) to the same location the original one was
- [Create a `CHANGES.txt`.](https://www.aeaweb.org/journals/data/revisions-policy#identifying)  Identify changes made. E.g. "V2: Moved PSID data to [PSID DOI]".  It should look something like this:

```
V1: Original deposit
V2: PSID data moved to [PSID DOI]
```
- Upload the `CHANGES.txt`.
- Link to the [PSID DOI] in the "Related publications" section of the deposit (use the `Import from DOI` functionality, choose `is supplemented by` for the `Relationship` field)
- You *may* have to add the "manuscript number" to the metadata, see [this link](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#scope-of-project-section). Use the last part of the DOI of the paper, e.g. if the paper DOI is `https://doi.org/10.1257/aer.p20161120` then the "manuscript number" should be `aer.p20161120`.
- [Re-Submit to the AEA](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submitting-to-the-data-editor)
- Contact the [openICPSR helpdesk](https://www.openicpsr.org/openicpsr/contactUs) and ask them to "Unpublish" the V1 deposit.	

![(Re-)Submit to the AEA](/images/project-submit.png)

### The end state

After all the fixes,

- V1 is still visible, but can no longer be downloaded. 

![Unpublished deposit shows banner](/images/openICPSR-study-unpublished.png)

- the PSID deposit is now available. Users who want to download the data have to agree to the PSID's terms of use. You are now in compliance with the PSID's terms of use!
- V2 is published, contains no PSID data, links to the PSID deposit, and remains otherwise available to replicators. You are still in compliance with the AEA publication agreements and your obligations as an AEA author!

### An example

Fran Blau and Larry Kahn had a JEL article (with replication package!) back in 2016:

> Blau, Francine D., and Lawrence M. Kahn. “The Gender Wage Gap: Extent, Trends, and Explanations.” Journal of Economic Literature 55, no. 3 (September 2017): 789–865. <https://doi.org/10.1257/jel.20160995>.

The relevant original replication package was migrated to openICPSR in 2019, and its contents can still be viewed here, **but not downloaded**:

> Blau, Francine D., and Kahn, Lawrence M. Replication data for: The Gender Wage Gap: Extent, Trends, and Explanations. Nashville, TN: American Economic Association [publisher], 2017. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2019-10-12. <https://doi.org/10.3886/E113913V1>

The amended replication package is now available, and linked from the earlier one (note the V2, and the later publication date):

> Blau, Francine D., and Kahn, Lawrence M. Replication data for: The Gender Wage Gap: Extent, Trends, and Explanations. Nashville, TN: American Economic Association [publisher], 2024. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2024-11-14. <https://doi.org/10.3886/E113913V2>

The required `CHANGES.txt` reads

```
V1: Original version
V2: Moved PSID data to https://doi.org/10.3886/E210483V1 and updated README.
```

and the new PSID deposit is referenced there, in the related publications, and in the README.

> Kahn, Lawrence, and Francine Blau. “Supplementary for: Francine D. Blau and Lawrence M. Kahn, ‘The Gender Wage Gap: Extent, Trends, and Explanations’, Journal of Economic Literature , 55 ,3 (Sept 2017): 789-865.” ICPSR - Interuniversity Consortium for Political and Social Research, 2024. <https://doi.org/10.3886/E210483V1>.[^note]

[^note]: A shorter and perfectly acceptable name would have been "Supplementary for: The Gender Wage Gap: Extent, Trends, and Explanations". The supplementary data could also be linked back to the original replication package, for clarity.

### Conclusion

The problem outlined above is not unique to the PSID. We have seen "takedown" requests from the German Socio-Economic Panel and others, and I have prevented inadvertent publication of UNSD Comtrade data, Compustat data, commercial data, PII-laden data, etc. The PSID is relatively unique in that it has a mechanism to actually preserve the author-created extracts. A few other such mechanisms exist, but they are by no means universal. Most "takedown" requests can only be satisfied with the deletion of data, and the inclusion of detailed information on how others can obtain the data from the original data provider - an error-prone and not ideal process. 

Authors should feel free to reach out to their journal's data and reproducibility editor with questions about the available options. 
