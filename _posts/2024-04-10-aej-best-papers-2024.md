---
title:  "AEJ Best Papers 2024 and replication packages"
date: 2024-04-10
classes: wide
datatable: true
mastodon: 
twitter:
bluesky:
tags:
  - best papers
  - replication packages
---

The annual **American Economic Journal (AEJ) Best Paper Awards** highlight the best paper published in each of the American Economic Journals: Applied Economics, Economic Policy, Macroeconomics, and Microeconomics over the last three years. Nominations are provided by AEA members, and winners are selected by the journals' Boards of Editors. More information, including links to the papers, at  [https://www.aeaweb.org/about-aea/honors-awards/aej-best-papers](https://www.aeaweb.org/about-aea/honors-awards/aej-best-papers).

The decision process is on the overall scientific merit. On this page, I list the replication packages for each of these. 

<!-- more -->

  <!-- manually constructing table -->
  <!-- "Journal","Title","Authors","DOI","Date","Package DOI","Requires confidential or proprietary data","Data Editor ran","Notes" -->

{% for row in site.data.aej-best-papers-2024 %}
## {{ row["Journal"] }} 

>  {{ row["Authors"] }}. "{{ row["Title"] }}" *{{ row["Journal"] }}* ({{ row["Date"] }}). [{{ row["DOI"] }}](https://doi.org/{{ row["DOI"] }}) 
  
- Replication package: [{{ row["Package DOI"] }}](https://doi.org/{{ row["Package DOI"] }})
- Does the replication package require confidential or proprietary data? **{{ row["Requires confidential or proprietary data"] }}**
- Did the Data Editor run the package? **{{ row["Data Editor ran"] }}**
- Additional notes:    *{{ row["Notes"]}}*


{% endfor %}


