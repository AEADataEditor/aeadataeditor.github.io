---
title:  "On the use and redistribution of data"
date: 2024-04-29
mastodon: 
twitter:
bluesky: 
tags:
  - data editor tips
  - replication packages
  - terms of use
  - licenses
---

Many researchers are confused by the difference between "use" and "(re-)distribution" of data. In a nutshell, just because you are able to freely use the data for your own research purposes does not give you the right to distribute the data to others. The devil is in the details.

<!-- more -->

## A scenario

You are happily browsing along the internet, and find an fabulous dataset you think you can use for your awesome idea. Download, analyze, submit, publish, ... all good. But then the pesky journal asks for a replication package. Easy, right? Wrap up the code, the data, upload, ... all good? Maybe. Possibly not.

## The problem

Many data used by economists stems from other data sources. Most of these data sources are on the internet. Anybody can use data that's on the internet and do with it what they want, right?

As the discussion surrounding copyright and artificial intelligence shows, the answer is complex.[^nytai][^silverman] There is a concept of "fair use" in US copyright law, and in particular, it has been used to allow for legal webscraping.[^webscraping] 

But that applies primarily for "use". If you want to publish the data you obtained from elsewhere, that is no longer necessarily considered (fair) "use", it falls under "redistribution" or "publication". 

[^nytai]: New York Times has sued OpenAI and Microsoft for having used their texts, see [https://www.washingtonpost.com/technology/2024/01/04/nyt-ai-copyright-lawsuit-fair-use/](https://www.washingtonpost.com/technology/2024/01/04/nyt-ai-copyright-lawsuit-fair-use/).

[^silverman]: Sarah Silverman and other authors have sued OpenAI over the use of their texts, but parts of that lawsuit have been dismissed, see [https://www.reuters.com/legal/litigation/openai-gets-partial-win-authors-us-copyright-lawsuit-2024-02-13/](https://www.reuters.com/legal/litigation/openai-gets-partial-win-authors-us-copyright-lawsuit-2024-02-13/).

[^webscraping]: See [https://techcrunch.com/2022/04/18/web-scraping-legal-court/](https://techcrunch.com/2022/04/18/web-scraping-legal-court/).

## The solution

In principle, the solution is for data providers to establish clear terms of use and licenses. And many do, especially in the commercial space. In general, you will find that "terms of use" restrict certains uses and rights, and "licenses" allow or grant certain uses and rights.

Historically, it was software that was licensed, and "open source" licenses have a long history. Many such licenses are listed at the "[open source initiative](https://opensource.org/licenses)". 

For data, a popular set of licenses are the "[Creative Commons](https://creativecommons.org/licenses/)" licenses. These licenses are designed to be easy to understand and to use, and allow for a wide range of uses - including **redistribution**. The CC-BY license is abundantly clear about what it allows:

> [CC By 4.0 DEED](https://creativecommons.org/licenses/by/4.0/): 
>
>  You are free to:
>
>  - Share — copy and redistribute the material in any medium or format for any purpose, even commercially. 
> [...]
> 

Other data licenses exist that allow for redistribution explicitly:

- [Open Data Commons Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/)
- various government "open data" licenses, such as the [UK Open Government License](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) and Statistics Canada's [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/reference/licence).

(often times, the differences are minor between these licenses). 



## The problem, part 2

The problem is that many (academic) data providers still do not show or apply these licenses, and have no terms of use, or ones that are hidden. It thus becomes difficult for researchers to know what they can and cannot do with the data they find, leading to avoidable confusion. 

Sometimes, these are identified at the time of downloading the data. For instance, the widely-used [World Values Survey](https://www.worldvaluessurvey.org/WVSDocumentationWV6.jsp) displays four conditions to researchers who (after registering) download the data:

![WVS download conditions](/images/wvs-download-screenshot-20240429.png)

It otherwise mentions the "non-redistribution license" or that "data redistribution is prohibited" in multiple places, but there is no single "Terms of Use" page, or a "WVS License" page that is easily accessible and referenceable. 

Even when terms of use are provided, permissions and restrictions are not necessarily linked together. For instance, the fabulous [DHS Program](https://dhsprogram.com/) states on many of its pages

> The DHS Program is authorized to distribute, at no cost, unrestricted survey data files for legitimate academic research. 

but one has to search for the [Terms of Use](https://dhsprogram.com/data/Terms-of-Use.cfm), tucked in between "Contraceptive Calendar Tutorial" and "DHS Github Code Share", which state (also very clearly)

> Conditions of Use for The DHS Program datasets 
> (applies to all datasets downloaded from The DHS Program website: www.dhsprogram.com)
> 
> [...]
>  -  Agree that the datasets **will not be shared** with other researchers without the written consent of The DHS Program.

(emphasis added). Many researchers include DHS data in their replication packages, and active data editors like myself have to remind them to remove the data from the replication package.


## The takeaways

### Data providers

- Data providers should have a clear "Terms of Use" page, or a "License" page, that is easily accessible and referenceable. 
- They should also include the license and conditions in every download.
- When data formats that allow for annotation (Stata, SAS), embed the license information in the dataset itself.

### Researchers

- Always record the terms of use and license when you download the data. 
- Search for "terms of use" or "license" on data providers' websites.
- If the website asks for registration, it is highly likely that there are redistribution restrictions.
- Request that data providers make their terms of use and licenses more visible and accessible.
- Consult (and update) the [Social Science Data Editors' Terms of Use database](https://social-science-data-editors.github.io/reference/TermsOfUse.html).



