---
title:  "AEJ Best Papers 2024 and replication packages"
date: 2024-04-10
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


<table class="display">
  {% for row in site.data.aej-best-papers-2024 %}
    {% if forloop.first %}
    <thead>
    <tr>
      {% for cell in row %}
        {% if forloop.last %}
          {% continue %}
        {% else %}
        <th>{{ cell[0] }}</th>
        {% endif %}
      {% endfor %}
    </tr>
    </thead>
    {% endif %}

  <!-- manually constructing table -->
  <!-- "Journal","Title","Authors","DOI","Date","Package DOI" -->
  <tr>
    <td> {{ row["Journal"] }} </td>
    <td> {{ row["Title"] }} </td>
    <td> {{ row["Authors"] }} </td>
    <td> {{ row["Date"] }} </td>
    <td> <a href="{{ row["DOI"] }}" alt="Link to article DOI">{{ row["DOI"] }}</a></td>
    <td> <a href="{{ row["Package DOI"] }}" alt="Link to Replication Package">{{ row["Package DOI"]</a></td>
  </tr>
  {% endfor %}
</table>

