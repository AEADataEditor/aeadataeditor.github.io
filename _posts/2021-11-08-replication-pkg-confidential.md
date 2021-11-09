---
title:  "How to prepare replication packages for papers that used confidential data"
date: 2021-11-08
tags:
  - restricted-access
  - administrative 
  - replication package
---

On a tangent: we get this question regularly - how to prepare replication packages for papers that used confidential data (here: by statistical agencies). A really [short thread](https://twitter.com/AeaData/status/1457815800438562828). 

<!-- more -->

![inquiry](/images/img-2021-11-08-1.png)

The very general answer is: The guidance is the same as for any other paper, including with public data: 

> describe where the data came from, describe how others can get the data, provide all the code, describe how to run code, create README for it all.

The only part that's different is that getting access to the data WAS complicated for you, and MIGHT be a tad complicated/long/costly/impossible for others. Details, details...

But concretely, here are a few pointers. 

1. First, start with our [fabulous template README](https://social-science-data-editors.github.io/template_README/). Really, it helps! Available at [https://social-science-data-editors.github.io/template_README/](https://social-science-data-editors.github.io/template_README/)


[![README](/images/img-2021-11-08-2.png)](https://social-science-data-editors.github.io/template_README/)


2. In order to describe data availability, split into two: 
  - how did YOU get access to the data, and 
  - how can OTHERS get access to the same data. 
  - The two are not always the same, but are both relevant. 
  
Examples include [this excellent description](https://social-science-data-editors.github.io/guidance/DCAS_Restricted_data.html#us-census-bureau-and-fsrdc) from a paper by [Teresa Fort](https://faculty.tuck.dartmouth.edu/teresa-fort/) ([@Tfpiasecki](https://twitter.com/Tfpiasecki)). Or [this description](https://social-science-data-editors.github.io/guidance/Requested_information_dcas.html#example-for-confidential-data) by Fadlon and Nielsen about Danish data

Note: That's for the data which you *cannot* share - because it is not yours to share. In general, the statistical agencies, or other providers, control access. You, the author, can only share information about *how* to access.

Furthermore,  you should also make an archive *WITHIN* the secure computing facility - of anything that cannot be shared, to the extent permissible, and as long as possible. And then provide information about it in the README.

3. Code: **All** code needs to be provided - no exceptions! Redactions for security/privacy are OK. Requesting code is standard practice in most secure computing facilities, but might take some time, so do it as soon as possible if you have not already done so.

In the unlikely event that you get push back from whatever agency provided you with the data, contact your favorite data editor.

4. All public use data you might have introduced to the secure computing facility are expected to be provided in the replication package, including where they came from. You probably had to describe the provenance anyway in order to import them (most secure computing facilities, such as the US FSRDC or the Canadian CRDCN, require such documentation).

5. Do not forget to cite data! See our [Guidance on Data Citation](https://social-science-data-editors.github.io/guidance/Data_citation_guidance.html)


And if you have questions, contact us! 