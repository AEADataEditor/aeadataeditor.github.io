---
title: "Creating separate linked data archives"
toc: true
layout: single
date: 2021-07-08
---


Every time we see that a lot of effort went into creating a data resource, we don't want to have that sit hidden in a replication package. We want to give data packages with significant value-added their own deposit, separately cited, and with much better discoverability. This is also relevant for situations where some or all of the data may be **restricted**, but the code is meant to be public (such as to ensure compliance with the [AEA Data and Code Availability Policy](https://www.aeaweb.org/journals/data/data-code-policy)).

## Who should read this

The present guidance is most useful for **individual researchers** and **small research groups** who do not have a dedicated data manager. While the information may also be useful for data managers at medium and large research groups and institutions, the issues, options, and solutions may be different for them.

## Websites and Persistence

Many researchers and small research groups have built very informative **websites** dedicated to their research project, which provide rich background information and often access to data. However, in general, such websites lack a key attribute important in the realm of academic publishing: *persistence*. Personal websites, whether truly at a personal site or at a university department, can and do disappear, or are "reorganized" away. Project websites may depend on hosting providers, free or paid, that may go away, for a variety of reasons.

Trusted repositories excel at persistence - it is their primary raison-d'être. They are not so great, in general, at flexibility and design. As we will describe below, project websites can be combined with data stored at trusted repositories to obtain the best of both worlds. 

## Searching and finding data

Visibility comes through findability, and trusted repositories have that built in, in ways that go beyond a mere Google or Bing search. Whether you are using [openICPSR](https://www.openicpsr.org/openicpsr/), [Dataverse](https://dataverse.harvard.edu/), [Zenodo](https://zenodo.org/), or any other one of many [trusted repositories](https://social-science-data-editors.github.io/guidance/Requested_information_hosting.html#trusted-repositories), they share a number of key characteristics

- be trustworthy
- be accessible to others, at least in terms of the metadata 
- be persistent, for instance through a continuity plan, but also to disallow deletion of objects
- guarantee some level of data integrity
- have version control
- be properly indexed and findable

The latter point is reflected in being able to find deposits made at deposits through a variety of mechanisms, such as on-site search (e.g. [ICPSR search](https://www.icpsr.umich.edu/web/pages/)), federated search (e.g. [Data-PASS](http://www.data-pass.org/call.html), DOI search (e.g., [DataCite Search](https://search.datacite.org/)),or search engines (e.g. [Google Dataset Search](https://datasetsearch.research.google.com/)). By assigning DOIs, they also contribute to citation statistics. 

## Permission

Of course, you should only do this if the original data provider's license allows you to redistribute their original data, and the derived data. You might need to explicitly obtain those rights, the original data may be in the public domain (e.g., US Government data), or the original data may be out of copyright (varies across countries). You are the one who knows this best!

## What data is in scope

Suppose that, as part of your research, you have created a "data asset" - something that has independent value, can be re-used outside of the context of your current article. This could be

- a broad survey, which your current article only partially describes and uses
- a clean, usable version of otherwise complex, costly, or messy data
- a usable version of historically available, but not digitized data

It may also be the case that you are able to redistribute the sensitive data you have collected, but need to ensure that subsequent users get appropriate IRB approval. 

## What you should do: Creating and using a separate data deposit

1. Create a separate (new) deposit at one of the trusted repositories. This is separate from your article's replication package. We'll call this the "DATA deposit."
    - See for example [a tutorial by the Harvard Astrophysics Library for Zenodo](https://library.cfa.harvard.edu/data-archiving-and-sharing) and for [DataLumos](creating-datalumos-deposit) on this site.
    - The title would be something meaningful like "Historical FERC Form 714 submissions."
    - Authors should be you, and possibly the original agency (the latter enhances findability).
    - Provide the raw data files (if not archived elsewhere - but that's the point, most often).
    - Create a simple **README** that summarizes the processing - does not need to be long, but should be complete.
    - Choose a **license**, which might include a requirement to cite your paper which first uses these data (also see our [licensing guidance](Licensing_guidance)). For data deposits like this, we suggest CC-BY (standard on many trusted repositories), or CC-BY-NC (no commercial use). The license should be broad enough to allow others to re-use the data, specific enough to have them give you credit (if you so desire). (see below for **possible restrictions**) Note that a license is just a default permission - parties that wish to use the data but who do not conform to your license (e.g. commercial entities) can still contact you, and you retain the right to give them a custom license that is in addition to the default license. Consult your university's counsel if in doubt. 
    - If the deposit is meant to be **restricted** in some way, you may need to check certain options to select a **distribution** method (download, virtual data enclave, something else), and/or an approval method (by the archive, by a third-party, or -- if no other method is available -- by you). Not all trusted repositories offer all methods.
    - Also provide any scripts you used for data collection or data cleaning, if any. If some of the processing was manual, describe the manual processing in the README, including possibly providing instructions to RAs or staff. This is about transparency, and users will use your data if they trust that you did the "right thing". 
      - Note however that the scripts provided here will usually be subject to the same distribution restrictions as the data. Thus, if accessing the code in the DATA repository requires asking for permission, you may need to provide the code in the CODE repository, without such restrictions, to satisfy journal requirements.
    - Upload the cleaned files as well - this is the value-added data you created! Remember to label/document each variable, to remove unnecessary (temporary processing) variables. 
2. Then publish the DATA deposit:
    - This provides you with a DOI, and a citation.
    - Your data archive is now permanent!

3. Back in your current paper and CODE replication package, do NOT provide any of the files you just uploaded to the "DATA deposit" (except possibly some scripts, as noted).  Rather, cite the DATA deposit (in paper, in README), and name the files that a user should use (i.e., "all the files in "cleaned/").

Examples:

- [https://doi.org/10.3886/E117464V1](https://doi.org/10.3886/E117464V1) - raw data + cleaned data
- [https://doi.org/10.3886/E100274V1](https://doi.org/10.3886/E100274V1) - derived data not directly connected to a paper
- [https://doi.org/10.3886/E100616V1](https://doi.org/10.3886/E100616V1) - nearly unmodified raw data

## Additional thoughts

### Project websites and archives 

Some researchers keep separate websites for their long-running projects, including providing data on those websites. While the stylistic freedom of a free-standing website is certainly important, we suggest that the data provided via those websites (e.g., `www.fabdata.org/data/superdata.zip`), be archived in a trusted repository, and that the primary download link point to those repositories.

- Maintain as usual your project website "www.fabdata.org"
- When producing data, proceed as outlined above, depositing in a trusted repository, and obtaining a DOI "10.1234/5678.abc"
- The links on "www.fabdata.org/data" point to the DOI at the repository, and provide appropriate citations.

Example:

- [Startup Cartography](https://www.startupcartography.com/) (Guzman, Stern, and others) stores data at [https://doi.org/10.7910/DVN/BMRPVH](https://doi.org/10.7910/DVN/BMRPVH)
- [Census Linking Project](https://censuslinkingproject.org/) (Abramitzky, Boustan, and many others) allows to select data on their [website](https://censuslinkingproject.org/), but stores (preserves) the data at [https://dataverse.harvard.edu/dataverse/censuslinkingproject](https://dataverse.harvard.edu/dataverse/censuslinkingproject)

In addition, you might want to save the website to the [Internet archive](archive.org) to make a permanent copy of the front end web pages.

### Collections and Communities

Some trusted repositories offer the option to make what are called "collections", "communities", "dataverses", or similar. This can be used for single projects, entire institutes, or journals

- [openICPSR](https://www.openicpsr.org/openicpsr/repository/) offers branded repositories. However, these are not free.
  - Example: [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/aea) hosts the AEA's replication packages
  - Example: [DataLumos](https://www.datalumos.org/datalumos/) preserves "valuable government data resources"
- [Zenodo Communities](https://zenodo.org/communities): "Communities created and curated by Zenodo users"
  - The [AEA Community on Zenodo](https://zenodo.org/communities/aeajournals/) collects replication packages and supplementary data for AEA journals that are deposited on Zenodo. 
  - Example: [Labor Dynamics Institute](https://zenodo.org/communities/labordynamicsinstitute/) collects presentations and data related to their activities on Zenodo
  - Example: [Economic Journal Community](https://zenodo.org/communities/ej-replication-repository) stores replication packages for articles published in the Economic Journal
- [Harvard Dataverse](https://dataverse.harvard.edu): "*Organize datasets and gather metrics in your own repository. A dataverse is a container for all your datasets, files, and metadata.*"
  - Example: [Bracero data](https://dataverse.harvard.edu/dataverse/bracero) stores both raw data and cleaned data within a "dataverse"
  - Tutorial: [IQSS Tutorial](https://youtu.be/5l4VZ-T2WYE?t=3780)

### Curation vs. Preservation

Most of the free or low-cost resources mentioned here provide preservation of the deposited materials, but are essentially self-serve websites with included preservation. No professional archivist or curator will inspect data, or work to improve the data quality. However, in some cases, it may make sense to work with a professional archivist to further improve the quality of the archived materials. 

Example:

- As part of the work for her AER article “[Cities in Bad Shape: Urban Geometry in India](https://doi.org/10.1257/aer.20171673),” Mariaflavia Harari made georeferenced digital historical maps of India and Pakistan. These were delivered to professional archivists at ICPSR, and published as "Historical Maps of India and Pakistan, 1955-1963" (ICPSR 37937, [https://doi.org/10.3886/ICPSR37937.v1](https://doi.org/10.3886/ICPSR37937.v1)). The core replication files are independent of this archive, and can be found at [https://doi.org/10.3886/E116003V1](https://doi.org/10.3886/E116003V1).

- [Harari (2020)](https://doi.org/10.1257/aer.20171673) Paper
- [Code and replication data](https://doi.org/10.3886/E116003V1)
- [Curated raw data](https://doi.org/10.3886/ICPSR37937.v1)

A note that such curation can take significant time (several months). It may also carry a cost, depending on, for instance, membership of an author's institution in ICPSR.

### Restrictions

When creating a separate DATA deposit because of ethical or legal requirements, you may want to enforce an application process and/or provide a more restricted license. 

> The AEA requires that such licenses permit at least the publication of reproducibility checks, encourages licenses that permit broader re-use, and strongly encourages that the approval process be as simple and objective as possible, ideally not involving the original authors.

The following example uses two linked deposits. All code is available for unrestricted download,  the data is available broadly, but with restrictions (IRB approval and computer security plan, subject to approval):

- [Deryugina, Shurchkov, and Stearns (2021)](https://doi.org/10.1257/pandp.20211017) Paper
- [Code deposit](https://doi.org/10.3886/E131761V1): this deposit can be freely downloaded
- [Deposit of restricted-access data](https://doi.org/10.3886/E139263V1): this deposit contains the sensitive data, and requires that interested parties apply, and demonstrate IRB approval. It is, however, available to anybody who qualifies.

To learn more about how to create restricted DATA deposits for AEA (and other) journals, visit [our guide to depositing restricted data at ICPSR](creating-restricted-data-deposit-icpsr).
