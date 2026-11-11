---
title:  "Creating a restricted-access Zenodo deposit for data that cannot go into the openICPSR replication package"
date: 2026-11-11
mastodon: 
bluesky: 
tags:
  - data editor tips
  - replication packages
  - terms of use
  - private data
  - Zenodo
---

Sometimes, authors have data that they are allowed to share, but **not publicly**. The data use agreement may say that the data can be given to other researchers who agree to certain conditions, but not posted for anybody to download. Or the data may contain information that is too sensitive for an open deposit, but not so sensitive that it needs to sit in a secure enclave. Such data cannot go into the primary replication package on openICPSR, which is public. But it should not just sit on the author's laptop either.

This post describes one solution: a **restricted, but shareable** deposit on [Zenodo](https://zenodo.org/), which is linked to the main replication package.

<!-- more -->

## When is this the right solution?

The [AEA Data and Code Availability Policy](https://www.aeaweb.org/journals/data/data-code-policy) asks that authors provide access to all data used in a published paper, and acknowledges that some data cannot be shared openly. In earlier posts, I described what to do with [data from unnamed providers](2026-05-08-private-data) and with [data containing PII](2026-05-05-pii). A restricted Zenodo deposit fits a specific case in between:

- the **author** has the right to redistribute the data, but only under conditions (e.g., "for non-commercial research only", "users must agree not to re-identify respondents", "users must cite the original source");
- the conditions can be **checked by somebody other than the author**, based on what the requester provides (a statement of intended use, an institutional affiliation, an IRB approval);
- the data are small enough for Zenodo (currently 50 GB and 100 files per record; check the [current limits](https://help.zenodo.org/docs/deposit/manage-files/)).

It is **not** the right solution when:

- the data are licensed from a third party that does not allow redistribution at all (then the data are not yours to deposit; document how to obtain them from the provider instead);
- the data are so sensitive that they require a secure environment (enclave, FSRDC, or a curated archive with restricted-use agreements, such as ICPSR's restricted data services);
- the data can in fact be published openly (then they belong in the openICPSR deposit).

When in doubt, talk to your data librarian, and to the Data Editor, **before** creating the deposit.

## In a nutshell

1. Create a new upload on Zenodo, containing only the data that cannot be in the openICPSR deposit (plus a short README).
2. Set the **files** to "Restricted", keep the **metadata** public.
3. Enable **access requests**, and write clear, objective conditions for access.
4. Link the Zenodo record to the openICPSR deposit and to the article, and vice versa.
5. Publish the Zenodo record, and create a **share link** for the Data Editor so we can verify reproducibility with the restricted data.
6. Document everything in the README of the openICPSR deposit.

The rest of this post goes through each step.

## Step by step

### Prepare the files

Separate the data that must be restricted from everything else. Everything that **can** be public (code, public data, documentation, codebooks, even variable lists for the restricted data) stays in the openICPSR deposit. The Zenodo deposit should contain only:

- the restricted data files, in the same directory structure as expected by the code (e.g., `data/raw/restricted/`), so that a user can simply drop them into the replication package;
- a short `README` that describes the files, points back to the main replication package, and repeats the terms of use;
- if the data come with their own license or data use agreement text, a copy of it.

Do **not** put code in the restricted deposit. Code goes into the main replication package, where everybody can see it.

### Create the Zenodo upload

Log in to Zenodo, and click on "New upload".

<!-- TODO: link to Zenodo "New upload" and screenshot -->
![Zenodo new upload](/images/zenodo-new-upload.png)

Fill in the usual metadata: title, authors, description, resource type ("Dataset"), and a license. A few recommendations:

- **Title**: make it obvious that this is a supplement, e.g., "Restricted data for: *Title of the article*".
- **Description**: this is **public**, even if the files are not. Describe what the data are, why they are restricted, and what the conditions for access are. Mention the main replication package by DOI.
- **License**: choose a license that is consistent with the restrictions. Do not use CC-BY or similar open licenses for data that are not, in fact, open.
- **DOI**: let Zenodo reserve a DOI ("Get a DOI now!"), so you can reference it in the openICPSR README before the record is published.

### Restrict the files

In the "Visibility" section, keep the **record** public, but set the **files** to "Restricted". This means that anybody can find the record and read its description, but only people you grant access to can download the files.

<!-- TODO: screenshot of Visibility section with "Restricted" files -->
![Zenodo visibility settings](/images/zenodo-visibility-restricted.png)

Do not use an embargo for this purpose. An embargo makes the files public automatically on a set date, which is probably not what the data use agreement says.

### Enable access requests

Once the record exists, go to the record's "Share" menu, and open the "Settings" (or "Access requests") tab. Enable access requests, so that users can ask for access from the record's landing page. Write the conditions in the field provided ("Conditions" or "Accept conditions"); requesters will see that text and must agree to it.

<!-- TODO: screenshot of the access request settings -->
![Zenodo access request settings](/images/zenodo-access-requests.png)

Good conditions are **objective**, so that anybody could apply them consistently. For instance:

> Access is granted to researchers affiliated with an academic or non-profit research institution, for non-commercial research purposes. Requesters must state their affiliation and intended use, and agree not to attempt to re-identify any individual or firm, and not to redistribute the data.

Poor conditions are ones that depend on the author's discretion ("access at the discretion of the authors"). The AEA strongly prefers that access not depend on the author's personal approval, which is likely to become unavailable once the author moves on or retires.

### Make sure somebody other than you can approve requests

By default, access requests go to the owner of the record, i.e., you. To make sure requests continue to be handled when you change jobs, change email addresses, or are simply on vacation, share **management** rights for the record with at least one other person: a co-author, and ideally somebody at your institution whose job it is to do this (a data librarian, a research data services unit). This is done in the same "Share" menu, under "People" (or "Groups"), with the "Can manage" permission.

<!-- TODO: screenshot of sharing with "Can manage" -->
![Zenodo share with people](/images/zenodo-share-people.png)

Document in the description who handles access requests, and a fallback contact (e.g., the institution's data services email address, not a personal email).

### Link the deposits

Both deposits should point to each other, and to the article.

- **On Zenodo**: under "Related works", add the DOI of the openICPSR deposit with relation "Is supplement to", and the DOI of the article (once known) with relation "Is supplement to" as well.
- **On openICPSR**: in the "Related publications" section, use "Import from DOI" with the Zenodo DOI, and choose `is supplemented by` for the `Relationship` field.

<!-- TODO: screenshots of Zenodo "Related works" and openICPSR "Related publications" -->
![Zenodo related works](/images/zenodo-related-works.png)

### Publish, and share with the Data Editor

Publish the Zenodo record. Note that once published, you cannot change the files without creating a new version, so double-check them first. The metadata (including the conditions) can still be edited later.

Then, in the "Share" menu, under "Links", create an **access link** with "Can view" permission. Anybody with that link can download the restricted files, so treat it like a password. Send it to the Data Editor through the channel we indicate (not in the public README, and not in the openICPSR deposit). We will use it to verify computational reproducibility with the restricted data. You can set an expiration date on the link, or delete it once we are done.

<!-- TODO: screenshot of creating an access link -->
![Zenodo access link](/images/zenodo-access-link.png)

### Document in the README

In the README of the **openICPSR** deposit (ideally following the [Template README](https://doi.org/10.5281/zenodo.7293838)), in the "Data Availability and Provenance Statements" section:

- name the restricted files, and say where they are (the Zenodo DOI);
- state the conditions for access, and how to request access (via the Zenodo record's "Request access" button);
- say where the files need to be placed for the code to run (e.g., `data/raw/restricted/`);
- describe which results can, and which cannot, be reproduced without the restricted data. Ideally, the code checks for the presence of the restricted data and skips (with a clear message) the parts that need it, so that the rest of the package still runs.

The Zenodo record's own README should, in turn, point back to the openICPSR deposit, since that is where the code and full documentation live.

## The end state

At the end:

- The openICPSR deposit is public, contains all code and all non-restricted data, and its README explains how to obtain the rest.
- The Zenodo record is public and findable, with a DOI and a clear description, but its files are only available to users who request access and agree to the conditions.
- More than one person can approve access requests, and the conditions do not depend on the author's discretion.
- The Data Editor has verified reproducibility using the restricted data.

## Final comments

This is one of several options, not the only one. Your institution may have a repository that offers similar functionality, possibly with better long-term guarantees and curation, and ICPSR has its own options for restricted data. Authors should feel free to reach out to the Data Editor with questions about which option fits their situation.
