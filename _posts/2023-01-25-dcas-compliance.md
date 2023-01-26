---
title:  "DCAS v1.0 Compliance Self-Assessment"
date: 2023-01-25
toc: true
mastodon: 
tags:
  - standards
  - reproducibility
  - provenance
  - dcas
---

![DCAS Logo](https://datacodestandard.org/assets/img/logo-800.png)
On 2022-12-15, various data editors, including myself, [launched the Data and Code Availability Standard (DCAS)](2022-12-15-launching-dcas).  In this post, I will do a self-assessment of my claim that the AEA's Data and Code Availability Policy (DCAP) complies with DCAS. The assessment is based on [DCAS V1.0 rules](https://github.com/social-science-data-editors/DCAS/blob/4b68868d3ecd9ac331f9add6813dae4ffe9b8d87/_data/rules.csv), compared to the [DCAP as of January 2023](https://www.aeaweb.org/journals/data/data-code-policy).


{% for row in site.data.DCAS-compliance-v1 %}
  <!-- group,topic,description,Relate to AEA DCAP,Comment by Data Editor -->

{% if row["group"] %}

---

## Section: {{ row["group"] }} 

{% endif %}

### {{ row["topic"]}}

<table>
<thead>
<tr><td>What the DCAS says</td><td>What the AEA DCAP says</td>
</tr></thead>

<td width="35%">{{ row["description"] }}</td>
<td>{{ row["Relate to AEA DCAP"] }}</td>

</table>

{% if row["Comment by Data Editor"] %}

> Comment: {{ row["Comment by Data Editor"] }}

{% endif %}

  {% endfor %}


## A few last notes

The current AEA policy was created before the release of the Data and Code Availability Standard. As the AEA and other journals align on a common standard, we will likely more closely adjust how our policy is expressed with the standard, making compliance by authors less well versed in these things easier.

I welcome any feedback.