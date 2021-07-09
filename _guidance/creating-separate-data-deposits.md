---
title: "Creating separate linked data archives"
toc: true
layout: single
date: 2021-07-08
---


Every time we see that a lot of effort went into creating a data resource, we don't want to have that sit hidden in a replication package. We want to give data packages with significant value-added their own deposit, separately cited, and with much better discoverability.

## Searching and finding data

Visibility comes through findability, and this is what trusted repositories excel at. Whether you are using [openICPSR](https://www.openicpsr.org/openicpsr/), [Dataverse](https://dataverse.harvard.edu/), [Zenodo](https://zenodo.org/), or any other one of many [trusted repositories](https://social-science-data-editors.github.io/guidance/Requested_information_hosting.html#trusted-repositories), they share a number of key characteristics

- be trustworthy
- be accessible to others, at least in terms of the metadata 
- be persistent, for instance through a continuity plan, but also to disallow deletion of objects
- guarantee some level of data integrity
- have version control
- be properly indexed and findable

The latter point is reflected in being able to find deposits made at deposits through a variety of mechanisms, such as on-site search (e.g. [ICPSR search](https://www.icpsr.umich.edu/web/pages/)), federated search (e.g. [Data-PASS](http://www.data-pass.org/call.html), DOI search (e.g., [DataCite Search](https://search.datacite.org/)),or search engines (e.g. [Google Dataset Search](https://datasetsearch.research.google.com/)). By assigning DOIs, they also contribute to citation statistics. 

## Permission

Of course, you should only do this if the original data provider's license allows you to redistribute their original data, and the derived data. You might need to explicitly obtain those rights, the original data may be in the public domain (e.g., US Government data), or the original data may be out of copyright (varies across countries). You are the one who knows this best!

## What should you do

Suppose that, as part of your research, you have created a "data asset" - something that has independent value, can be re-used outside of the context of your current article. This could be

- a broad survey, which your current article only partially describes and uses
- a clean, usable version of otherwise complex, costly, or messy data
- a usable version of historically available, but not digitized data

## Creating and using a separate data deposit

1. Create a separate (new) deposit at one of the trusted repositories. This is separate from your article's replication package. We'll call this the "DATA deposit."
    - The title would be something meaningful like "Historical FERC Form 714 submissions"
    - Authors should be you, and possibly the original agency (the latter enhances findability)
    - Provide the raw data files (if not archived elsewhere - but that's the point, most often)
    - Create a simple README that summarizes the processing - does not need to be long, but should be complete.
    - Choose a license, which might include a requirement to cite your paper which first uses these data. For data deposits like this, we suggest CC-BY (standard on many trusted repositories), or CC-BY-NC (no commercial use). The license should be broad enough to allow others to re-use the data, specific enough to have them give you credit (if you so desire). Note that a license is just a default permission - parties that wish to use the data but who do not conform to your license (e.g. commercial entities) can still contact you, and you retain the right to give them a custom license that is in addition to the default license. Consult your university's counsel if in doubt. 
    - Also provide any scripts you used, if any. If some of the processing was manual, describe the manual processing in the README, including possibly providing instructions to RAs or staff. This is about transparency, and users will use your data if they trust that you did the "right thing". 
    - Upload the cleaned files as well - this is the value-added data you created. Remember to label/document each variable, to remove unnecessary (temporary processing) variables. 
2. Then publish:
    - This provides you with a DOI, and a citation.
    - Your data archive is now permanent!

3. Back in your current paper and replication package, do NOT provide any of the files you just uploaded to the "DATA deposit."  Rather, cite the deposit (in paper, in README), and name the files that a user should use (i.e., "all the files in "cleaned/").

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

In addition, you might want to save the website to the [Internet archive](archive.org) to make a permanent copy of the front end web pages.

### Collections and Communities

Some trusted repositories offer the option to make what are called "collections", "communities", "dataverses", or similar. This can be used for single projects, entire institutes, or journals

- [Harvard Dataverse](https://dataverse.harvard.edu): "*Organize datasets and gather metrics in your own repository. A dataverse is a container for all your datasets, files, and metadata.*"
  - Example: [Bracero data](https://dataverse.harvard.edu/dataverse/bracero) stores both raw data and cleaned data within a "dataverse"
- [Zenodo Communities](https://zenodo.org/communities): "Communities created and curated by Zenodo users"
  - Example: [Labor Dynamics Institute](https://zenodo.org/communities/labordynamicsinstitute/) collects presentations and data related to their activities on Zenodo
  - Example: [Economic Journal Community](https://zenodo.org/communities/ej-replication-repository) stores replication packages for articles published in the Economic Journal
- [openICPSR](https://www.openicpsr.org/openicpsr/repository/) offers branded repositories. However, these are not free.
  - Example: [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/aea) hosts the AEA's replication packages
  - Example: [DataLumos](https://www.datalumos.org/datalumos/) preserves "valuable government data resources"

### Curation vs. Preservation

Most of the free or low-cost resources mentioned here provide preservation of the deposited materials, but are essentially self-serve websites. No professional archivist or curator will inspect data, or work to improve the data quality. However, in some cases, it may make sense to work with a professional archivist to further improve the quality of the archived materials. 

Example:

- As part of the work for her AER article “[Cities in Bad Shape: Urban Geometry in India](https://doi.org/10.1257/aer.20171673),” Mariaflavia Harari made georeferenced digital historical maps of India and Pakistan. These were delivered to professional archivists at ICPSR, and published as "Historical Maps of India and Pakistan, 1955-1963" (ICPSR 37937, [https://doi.org/10.3886/ICPSR37937.v1](https://doi.org/10.3886/ICPSR37937.v1)). The core replication files are independent of this archive, and can be found at [https://doi.org/10.3886/E116003V1](https://doi.org/10.3886/E116003V1).

A note that such curation can take significant time (several months). It may also carry a cost, depending on, for instance, membership of an author's institution in ICPSR.

