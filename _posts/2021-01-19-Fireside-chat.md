---
title:  "Follow-up to Fireside Chat"
layout: single-withtoc
date: 2021-01-19
tags:
  - FAQ
  - Twitter
  - Fireside Chat
---

In this post, I'll pick up questions that have been asked over Twitter or during the [2021-01-19 Fireside chat](https://aeadataeditor.github.io/talks/2021-01-19-cswep), in long form (Twitter is not always the best medium). Over time, you might see some of these questions and answers be migrated to FAQ and/or best practices documents.

<!-- more -->

## Starting a project

> [Judy Chevalier](https://twitter.com/judy_chevalier/status/1346259253955354624) What do I do before I even start the project? What do I do if I am accessing a big public dataset and it is always at risk of being changed or cleaned or updated?

Answer coming. Short answer: Keep track of what you do. Set up the project correctly. See  <https://aeadataeditor.github.io/aea-de-guidance/step-by-step.html> - in particular the first part <https://aeadataeditor.github.io/aea-de-guidance/preparing-for-data-deposit.html> can be done at any time!

## IRB, consent, and distributing sensitive data

> [David Cutler](https://twitter.com/Cutler_econ/status/1346261440899018752) IRB rules are becoming more complex over time. It would be good for economists to understand them better.

> [Adam Sacarny](https://twitter.com/asacarny/status/1346262290354614274) I strongly second this point! Knowing a bit about the Common Rule and HIPAA has saved me a lot of time. For example, sometimes the IRB requests waivers etc. that are not needed. Or sometimes you can make minor changes to make your research exempt rather than expedited…

Excellent points. Longish answer during Fireplace Chat.

## Code Persistence or Code Rot

> [John Horton](https://twitter.com/johnjhorton/status/1346260871429971970): If you are relying on lots of open source packages subject to change, how do we prevent “code rot”? Might it make sense for AEA to collect & store docker images or virtual machines?

There are two assumptions embedded within the question, which I'll address at the end. The easy answer to this is: We already have a mechanism to store code, docker images, and virtual machines, it's called the "[AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/search/aea/studies)" where all replication packages are stored.

The two assumptions are: "open source packages" and "researcher-provided docker images/VMs". Most economics code is written in Stata or Matlab, which are not open-source software, but which often have open-source (or imprecisely licensed) add-ons (packages, etc.) (I will address "packages" later). The best practice we have found is for copies of those packages to be distributed with the replication package, pre-installed, for two key reasons: Stata package repositories ([SSC](https://ideas.repec.org/s/boc/bocode.html)) are not versioned (old versions disappear), Matlab has no package repository, and Github (often used as an alternative, in particular for a small subset of Stata packages) is not persistent in the same way the "[AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/search/aea/studies)" is. The AEA guidelines may require this in the future, but currently only suggest it.

The second assumption is that researchers provide Docker images and VMS. **They don't**. Not in the social sciences. It is beyond the scope of what we do to create it for them, at this point (we are looking into ways of doing that, though). 

## Proprietary Data from Unknown Sources

> [John Horton](https://twitter.com/johnjhorton/status/1346261392983285761) For proprietary data where the source of the data is not disclosed but known to the authors, is there a way to facilitate access for other researchers to the data without divulging source publicly?

This is an excellent idea, variants of which we have investigated before. It hinges primarily on the willingness of the original data provider to entertain this. We don't actually have many cases where the provider is anonymous. I can think of two right now: one has a researcher-mediated access mechanism via a Non-disclosure Agreement - a group of researchers maintains the data, protects anonymity, but is willing to provide access to the data for replication and possibly for research purposes. A second one implemented an email-moderated mechanism that hides the identity of the data provider. In both cases, the persistence of the data, and of the access mechanism is not guaranteed. 

The ideal scenario is for researchers to obtain approval from the data provider to deposit data under a restrictive access mechanism mediated by a third party. [ICPSR](https://www.icpsr.umich.edu/web/pages/ICPSR/access/restricted/) is one such entity, and there are not many others. A grander scenario are industry-specific restricted-access data centers, such as [PCRI](http://www.privatecapitalresearchinstitute.org/research.php), where access is possible, and the identity of (multiple) data providers is hidden.

The key, however, is the willingness of the data provider to participate. The AEA can mediate and provide guidance to such arrangements, and I am happy to consult with any researcher who wants to go down that path, but will not, in general, become data custodian itself.

## Data citations - how to do it

> [Elizabeth Weber Handwerker](https://twitter.com/ElizWebHand/status/1347602931210739718) I'm trying to create a bibtex entry for a dataset (the journal says to "reference datasets" and can't find any examples of how to do this. 

Try these examples: 

- <https://zotero.org/groups/2245704/fsrdc>, <https://github.com/ncrncornell/cms-to-bib/blob/master/cms.bib> for confidential data, 
- <https://github.com/larsvilhuber/MobZ/blob/master/data.bib> for a variety of different data. 

Standard AEA bib style does not show URLs properly, use <https://github.com/AEADataEditor/aea-de-guidance/blob/master/citations/aea-mod.bst> or the "econ" style. The quick solution: use @techreport
{} in a Bibtex file. [doi.org/10.5281/zenodo.4073995](https://doi.org/10.5281/zenodo.4073995), starting around pg. 37, discusses the basic ideas. Short take-away: It's simple. (and @techreport or @misc
 has all the necessary fields).

Some examples:

```
@techreport{bea_table30_2019,
  title = {Table 30:  {Economic Profile}  by  {County} , 1969-2018},
  author = { {Bureau of Economic Analysis} },
  year = {2019},
  institution = { {U.S. Department of Commerce  [producer]} },
  url = {https://apps.bea.gov/regional/zip/CAINC30.zip},
  timestamp = {2020-09-08T00:42:24Z},
  type = {[Datafile]}
}

@misc{BLS_QCEW_2020,
  title = {Quarterly {Census} of {Employment} and {Wages} -- {Data Files} },
  shorttitle = { {QCEW Data Files} },
  author = { {Bureau of Labor Statistics} },
  year = {2020},
  publisher = { {Department of Labor [distributor]} },
  url = {https://www.bls.gov/cew/downloadable-data-files.htm},
  urldate = {2020-09-20},
  abstract = {Quarterly Census of Employment and Wages -- Data Files},
  language = {en},
  number = {1990-2019},
  timestamp = {2020-09-20T19:26:12Z},
  type = {[Datafiles]}
}
```


## How to bring solved problems to the next generation?

> [John Horton](https://twitter.com/johnjhorton/status/1346262118904029184) Many of the code & data problems are essentially solved software engineering problems (version control, makefiles, unit tests, etc) - how do we incorporate these practices into PhD education so next generation is better than us?

Good question... Efforts at [BITSS](https://bitss.github.io/ACRE/), [Carpentries](https://carpentries.org/), various data-science oriented classes, [my own efforts at Cornell](https://labordynamicsinstitute.github.io/computing4economists/web/#/) only scratch the surface. They train a minority of volunteering students. I would actually argue that these best practices should be taught at the undergraduate level, and should be a compulsory part of graduate education the same way we require math proficiency. But we are a long way off of that.

## Time capsules and other data access options

> [John Horton](https://twitter.com/johnjhorton/status/1346263273432354816) Could AEA help credibly create “time capsule” data agreements where it will release a public dataset X years in the future? Some companies are willing to share data but not until it has lost its competitive value. A long lived institution like AEA is well positioned for this.

Answer coming soon.

## Accessing data

> [Chris Conlon](https://twitter.com/conlon_chris/status/1346473098518773760) Several boilerplate data agreements that meet AEA requirements?

> [Chris Conlon](https://twitter.com/conlon_chris/status/1346474319283593218) negotiate terms with some of the commonly used data ACADEMIC data providers (WRDS? Kilts?).

Ongoing ([Kilts](https://marketingdata.chicagobooth.edu/Anonymous/Welcome), [German SOEP](https://www.diw.de/en/diw_02.c.238223.en/soep_conditions.html#614607), [German Scientific Use Files](https://fdz.iab.de/en/FDZ_Data_Access/FDZ_Scientific_Use_Files.aspx)). Repeatedly requesting ([DHS](https://dhsprogram.com/data/), [Afrobarometer](https://www.afrobarometer.org/)) One issue is that data providers tend to have project-specific permissions, and none have a blanket approval for replicators at academic journals (not just AEA). 

Typical answer: "We have not had a request like yours. I will need to speak with the director and potentially [data provider/counsel/lawyers]." 

## Gazillion files

> (via email) We have 26,000 files in our deposit. How should we proceed (openICPSR only handles up to 1,000 files)?

We get this question regularly. There are multiple partial answers:

- When the data provider has assigned a DOI, no need to provide the data. An example is the TERRA/MODIS climate data is such an example, see <https://dx.doi.org/10.5067/MODIS/MOD08_M3.061>. 
- If the data provider has not assigned a DOI, we encourage authors to ask their data provider to do so. This is the right approach... but it is unlikely to yield a result prior to publication. Fallback solutions below.
- If you have the interest and time to provide a public good, deposit the data separately, thus creating a DOI. While the AEA uses openICPSR to handle its replication packages, you can deposit the pure data deposit anywhere. A good option (as of January 2021) is [Zenodo](https://zenodo.org), which has an excellent API allowing to download metadata and large quantities of files. You would describe the data, and publish a deposit, thus creating a DOI. No need to then provide the data as part of the AEA Replication package - just cite it. Bonus: use the API to read-in the data for your own research.
- If all else fails, it is acceptable to ZIP up files by sub-directory (e.g., "zip -rp weather_CPCG.zip weather_CPCG/*" and then describe, as part of setup/processing, how and where to unzip the files. Caution: ZIP files on different platforms include addtional directory levels sometimes, so be precise about the directory structure you want. Also, the default Windows and Linux zip utilities can only handle ZIP archives up to 2GB, whereas modern macOS archives can handle larger ZIP packages. We suggest using 7zip, which is free and cross-platform.

## Verifying papers with restricted-access data

> (via email) It would be great to know more about best practice for papers based on administrative data that cannot be made available publicly. What are the AEAs recommendations – is there a planned “standard way” of doing things in this case? One way would be to require an independent review of national colleagues (eg in DK) to review the code and provide comments/run the analyses on their/similar data.

Longish answer coming in the Fireside Chat. Short answer: we already do this on a regular basis (successful in the past year: Washington State data, Wisconsin state data, French customs data, Brazilian firm and worker admin data (3x), Swedish register data (2x), IRS tax data (2x), etc.) in more or less the way you describe it. That being said, we do not yet have a mechanism on soliciting / finding replicators - but are working on that. For now, that mechanism is called "my memory" and a database of data citations.

> [Elizabeth Weber Handwerker](https://twitter.com/ElizWebHand/status/1346258970827218946) I'm a government economist, working with some data outside researchers can access only through an application process, and some data they can't access at all (Massachusetts QCEW, etc.). What do AEA requirements for data & code look like in each case?

Answer coming live during Fireside Chat. Short answer: The same. 

See talk at the [University of Waterloo / Canadian Research Data Center](https://doi.org/10.5281/zenodo.4250890). I have also had talks with Census Bureau folks, and have ongoing private and public talks with institutions that have access to restricted-data.

## Replicability and Reproducibility in Institutions

> [@fibbyccino](https://twitter.com/fibbyccino/status/1346262249854275585) What would you recommend to an organisation looking to introduce internal replicability standards for code and data for the first time?

Requires a longish answer (live), but is something I have been talking to various organizations about, see slides for my talk at [Brookings](https://doi.org/10.5281/zenodo.4311917) and [St. Louis Fed](https://doi.org/10.5281/zenodo.4281633) (also [video](https://research.stlouisfed.org/conferences/beyond-the-numbers/).
