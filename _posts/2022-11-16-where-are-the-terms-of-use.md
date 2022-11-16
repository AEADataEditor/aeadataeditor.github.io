---
title:  "What is this LICENSE thing"
date: 2022-11-16
tags:
  - license 
  - terms of use
  - copyright
  - reproducibility
  - provenance
---

The [template README](https://social-science-data-editors.github.io/template_README/) required by various econ journals asks for a statement about the rights to RE-distribute data. Many economists are confused by this: "*But the data is publicly available.*" Let me try to disentangle that somewhat.

<!-- more -->

## The statement about rights

The statement says

> I certify that the author(s) of the manuscript have documented 
> permission to redistribute/publish the data contained within this 
> replication package. Appropriate permission are documented in the 
> LICENSE.txt file.

Two questions arise: what does this mean, and what is an author supposed to do with the LICENSE.txt file? And then of course, how to cite it all.

### Questions and some answers

Here are a few questions that arise

> Do you require licensing information for all the data that we are using, or just the specific data that is provided in the replication package? 

Many econ papers use data from multiple sources, including data that are clearly confidential. Some data sources are not confidential, but are subject to copyright or licensing agreements. The replication package should ONLY contain data that can be redistributed, and the statement ONLY pertains to such data. It does not pertain to data not included within the replication package. 

Of course, a good chunk of the README is spent describing ALL the data sources, including the confidential ones, the non-confidential ones that are copyrighted, the non-confidential ones that are proprietary, or otherwise subject to redistribution restrictions. ALL data provenance must be described, sufficient for a replicator to start from scratch, ignoring even the data provided within the replication package. That description should contain the licensing information for every dataset as well, at least in summary. It should list pertinent conditions and restrictions, for instance: application process, required residency or citizenship, etc. The LICENSE.txt is more likely to contain a long text in legalese, the formal permission to use the data that is in fact *included* in the package.

> Why can't I redistribute this data, since it is publicly available?

I'll take the IPUMS CPS and the S&P 500 as an example. 

"Publicly available" does not mean that you have the rights to distribute. For instance, you can use the [S&P 500 data distributed by FRED](https://fred.stlouisfed.org/series/SP500), but you are not allowed to re-distribute that data, as noted on the page there. You would describe that in the README, but the license would not be in the LICENSE.txt, because you are not, in fact, including the data!

Turning to the CPS: When CPS data is pulled directly from the [US Census Bureau website](https://www.census.gov/programs-surveys/cps.html), it is in the "public domain," i.e., not subject to copyright (Note that this is not clear from the Census Bureau's website, which simply assumes that you know that! Check the [USA.gov](https://www.usa.gov/government-works) website for an explanation.) 

But when you obtain it through other sources ([CEPR](https://ceprdata.org/), [EPI](https://www.epi.org/data/), [IPUMS](https://www.ipums.org/projects/ipums-cps)), you have to read the terms of use, since by re-packaging the data, the **files** containing the data​ are subject to copyright by the redistributor... . 

If you are using the IPUMS data, the terms of use describe what you can do with the data: [https://www.ipums.org/about/terms](https://www.ipums.org/about/terms). As it turns out, you can​ redistribute an extract from their database, and that​ is what you should list in the LICENSE.txt. 

Note that other licenses are "sticky" - if you obtain data that is under a [CC-BY](https://creativecommons.org/licenses/by/4.0/) (Creative Commons) license, then you can do with the data what you want - but you must include the CC-BY license and the original source attribution. In essence, that part of your data is also under a CC-BY license.

> What goes into the LICENSE.txt?

![LICENSE txt image](/images/openicpsr-license.png)

This is straightforward if you have a single source. It should state the permissions and conditions that are attached to that file. If the data you obtained has a LICENSE.txt (some do), then simply include that with your deposit. Licenses can be long - they are written in legalese, because they are, in fact, legal permission to do something with the data.

If you created or collected the primary data yourself, you define the LICENSE. By default, deposits on openICPSR have a CC-BY license. We have a small discussion of how to choose licenses at the [AEA Data Editor's website](https://aeadataeditor.github.io/aea-de-guidance/Licensing_guidance) and the [Social Science Data Editors' website](https://social-science-data-editors.github.io/guidance/Licensing_guidance.html). 

If you have multiple data sources, it becomes a bit more complicated. The LICENSE.txt can be a simple collation of the various terms of use/ licenses/etc. So you could have:

```
For IPUMS CPS files, IPUMS' Standard Redistribution Terms 
apply (https://www.ipums.org/about/terms#redistribution)

    You will not redistribute the data without permission. You may 
    publish a subset of the data to meet journal requirements for 
    accessing data related to a particular publication. Contact us for
    permission for any other redistribution; we will consider requests
    for free and commercial redistribution. 

Applies to: AHTUS, ATUS, CPS, GeoMarker, HigherEd, IHGIS, MEPS, MTUS, NHGIS, NHIS

For UNCTAD TRAINS data:

The TRAINS Terms of Use at https://trainsonline.unctad.org/disclaimer state that users

   are not allowed to disseminate the data or parts of the 
   database in other dissemination tools unless written 
   permission is given by the Chief of UNCTAD's Trade 
   Information Section, Trade Analysis Branch, Division on 
   International Goods and Commodities. 

We have obtained such permission via email correspondence on 16 November 2022. 
```

> OK, so how do I cite the data?

Thank you for that question, since most researchers in economics do NOT cite the data. See this [extensive discussion](https://social-science-data-editors.github.io/guidance/addtl-data-citation-guidance.html) over on the Social Science Data Editor website, consult the [AEA Style Reference](https://www.aeaweb.org/journals/policies/sample-references), and remember that not all data distributors provide suggested citations that satisfy the [Data Citation Principles](https://force11.org/info/joint-declaration-of-data-citation-principles-final/). If they ask you to cite a working paper, do so, but **also** cite the data correctly.

> Most of this data was collected in 2016, but the [IPUMS AHTUS data citation page](https://www.ahtusdata.org/ahtus/citation.shtml) only lists the 2018 version. I am unable to find a historic example of this specific citation. 

IPUMS doesn't make it easy, I know.  There is a not-so-obvious list of versions of the data at this URL: [https://www.ipums.org/projects/ipums-time-use](https://www.ipums.org/projects/ipums-time-use). The IPUMS Time Use Revision history page](https://www.ahtusdata.org/ahtus-action/revisions) does NOT list the DOIs for the various version. So as far as I can deduce from that, you would have used V1.0 of the AHTUS data, which has DOI **10.18128/D061.V1.0**. You can use https://citation.crosscite.org/, or simply adapt their suggested citation accordingly.

Data providers have not all adapted to a world where data citations are ubiquitious, or should be. Sometimes it takes a little extra work.

Note that data citations should appear both in the manuscript (upon first mention of the data) and in the README (properly formatted as in the manuscript).