---
title:  "What can Data Editors do when authors have data that you cannot publish?"
date: 2026-09-23
mastodon: 
bluesky: 
tags:
  - data editor tips
  - replication packages
  - terms of use
  - private data
  - data publication
---

Quite a substantial fraction of data sources in economics are, for various reasons, not public. They might be proprietary, they might contain personally identifying information (PII), or business identifying information (BII). While we ask authors to publish data that they have control over, many of these unpublishable data are under somebody else's control, writ large (that somebody else might be the respondent, who is promised privacy!). 


<!-- more -->

## Related topics

I have written on similar and related issues before:

- [When data are so private, the provider cannot be named](2026-05-08-private-data.md)
- [When data should be private, but leaked into the published data (PSID version)](2024-11-01-psid-requests.md)
- [When data should be private, but leaked into the published data (PII version)](2026-05-05-pii.md)
- [When you should think about creating a separate data deposit](https://aeadataeditor.github.io/aea-de-guidance/creating-separate-data-deposit), including when that might allow for tighter access control then you want to have on the data.

## The AEA's policy on non-publishable data


The [AEA Data and Code Availability Policy](https://www.aeaweb.org/journals/data/data-code-policy) asks that authors provide access to all data used in a published paper. But it also acknowledges that there may be cases where data cannot be shared. 

> If providing the data publicly is not possible despite the authors' best efforts and due to valid constraints outside the authors' control, authors must ...

and in the [implementation guidance](https://www.aeaweb.org/journals/data/data-code-policy#non-public-data),

> If raw or analysis data cannot be published as part of a replication package or in an openly accessible trusted data repository, the reason(s) must be provided in the Data Availability Statement. Examples include confidential data with identifying information of persons or businesses and data subject to data use agreements or copyrights that prohibit redistribution. It is generally not acceptable that data be provided "upon request" if the request must be approved by the authors themselves. For non-public data, the author should indicate to the AEA Data Editor (in a form provided by the editorial office when requesting final manuscript files) whether a private (not to be published) version of the data can be provided directly to the Data Editor and/or a designated third-party replicator.

## How often does this happen?

Quite a large fraction of papers use this kind of data. When authors provide the information about their code and data (upon conditional acceptance), data access is classified into five categories: included (fully open data), and four categories of restricted access, going from "very easy to access" to "very difficult".[^dcaf] 

![Data access classification](/images/figure_access_provision.png)


[^dcaf]: The first pass at this is made by authors self-classifying their data, on the [Data and Code Availability Form](https://www.aeaweb.org/journals/forms/data-code-availability). We may revisit this once we've seen the replication package, and will recode this in our internal database. The data tabulated refer to 2025, and are published in Vilhuber, Lars. 2026. "Report of the AEA Data Editor." AEA Papers and Proceedings 116: 890–904. <https://doi.org/10.1257/pandp.116.890>.

## What do we then do?

### Data provision

In a nutshell, our first preference is that authors are allowed to share the data with us, but **not-for-publication**. This means that we will have access to the data, and can run code against the data, but won't publish the data.[^nopub] 

[^nopub]: To be clear, **we** actually never publish data or code regardless of when or how authors have provided it. The authors publish their data and their code, but in a space that we make available. We never touch their draft deposits, only review them, and we certainly never add anything to it. In some rare cases, we may help the authors by removing files that should not be there (obvious junk files).

We provide a secure upload link, different from the draft deposit.[^email] Of course, authors should check with their data provider if provision of data is OK. We can also sign a non-disclosure agreement (NDA) if necessary (referenced in the email), but we stand by our word, and most authors take us up on that.

[^email]: Readers can view our template email with which we reach out to authors at [here](https://aeadataeditor.github.io/LDI-Research-Aide/docs/emails/Request-Restricted-Access-Data.html). 

In some cases, we have standing or regularly renewed agreements with data providers to have the authors transfer otherwise restricted data to us ([Wharton Research Data Service](https://wrds-www.wharton.upenn.edu/), WRDS; or [IPUMS full-count files](https://usa.ipums.org/usa/full_count.shtml)[^ipums].).

[^ipums]: For some IPUMS datasets, inclusion is permitted as per the [Terms of Use](https://usa.ipums.org/usa/terms.shtml), but the full count (100%) files cannot.

### Data acquisition

We can also go out and get a copy of the data ourselves, primarily for the "very easy to obtain" category. For instance, you are not allowed to share the [PSID](https://simba.isr.umich.edu/), [Demographic and Health Surveys](https://dhsprogram.com/) (DHS), [World Value Survey](https://www.worldvaluessurvey.org/) (hosted in Spain) or certain UK Data Service files (for instance, [this one](http://doi.org/10.5255/UKDA-SN-2131-1)), as well as, in certain instances, the aforementioned IPUMS Full Count data (preferably via the API!). In all these cases, it is not very onerous to go through the process ourselves (it's a great learning experience for undergraduates!) 

Sometimes, this can be a longer process, and for a random sample, we will still go through the process. For instance, at the time of this writing, we are navigating obtaining a ["scientific use file" from the IAB-FDZ](https://doi.org/10.5164/IAB.SIAB-R7521.de.en.v1), and we have in the past arranged for FTP transfer of an [embargoed file from the UK Data Service](http://doi.org/10.5255/UKDA-SN-4560-1).

### Access to computing infrastructure

In some cases, the authors (or data providers) make the data available to us on their computing infrastructure. This can be very time intensive! I currently have pending some sort of access request to Chilean tax data on a Swiss server, welfare data from an experiment on a US AWS server, and have recently accessed data on a secure Bank of Spain server, after ID verification, cryptographic certificate generation, shipment of a chip card and a chip card reader, and onboarding onto their systems. We routinely access data that are available on the secure NBER servers.

### Third party replicators

We may reach out to [third-party replicators](https://www.aeaweb.org/journals/data/policy-third-party) who **do** have access to the data, when we do not. We distinguish between **independent replicators**, and **arms-length replicators**. 

**Independent replicators** are individuals and institutions who are not directly connected to the researchers. Examples of independent replicators are cascad.tech (a research entity in France, with access to French and other secure data), or independent graduate students (a UK student accessed Swedish data for us, a Finnish student ran code on the secure Finnish data enclave). We also consider as "independent" when staff at the secure data enclave themselves run code that hosted researchers had used in papers. Examples here are the Central Bank of Chile (ongoing) and the German IAB; cascad.tech is kind of the "house replicator"  for the French secure data enclave CASD. 

**Arms-length replicators** have some sort of connection to the authors: They may work for the same company, they may be a student working for the author. Recent examples are researchers at Microsoft, the OECD, and  a British Energy company. We usually try to ensure that there is no direct reporting chain, but that is not always the case. Any such connection is disclosed to me. They then have access to the same data, and run the code for us (or attempt to do so).
They mostly succeed. Such replicators are not perfect substitutes. But in some cases, in particular when the data are in secure data enclaves, there are 100s of other researchers who could also access the data, even when we cannot. 

## Conclusion

As an author, you should not assume that we cannot access the data: There is a good chance that we can. Build into your data access a possibility for somebody in the future to review your code (and running code is one kind of review), before you publish. We are also working with various data centers to make such a process smoother. If you are working in a secure data center where other economists also work, ask the data provider if there is a mechanism for somebody else to vet your code. In some cases, this might even happen before we data editors ever see your code, though you should still expect us to scrutinize your code as well.