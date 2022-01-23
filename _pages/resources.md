---
title: "Resources - AEA Data Editor"
layout: splash
permalink: /resources/
date: 2022-01-23
excerpt: "The AEA Data Editor provides a variety of textual and technical resources to further the goals of transparency, reproducibility and future replicability of AEA publications."
intro: 
  - excerpt: 'The AEA Data Editor provides a variety of textual and technical resources to further the goals of transparency, reproducibility and future replicability of AEA publications.'
feature_row:
  - image_path: /images/noun-talk-3836230.png
    alt: "Image: Ilham Fitrotul Hayat from the Noun Project"
    title: "Discussion"
    excerpt: "Informative [posts](/year-archive/) and [talks](/talks/)by the AEA Data Editor."
    btn_label: "Find blog posts"
    btn_class: "btn--primary"
    url: "/year-archive/"
  - image_path: /images/noun-help-3836213.png
    alt: "Image: Ilham Fitrotul Hayat from the Noun Project"
    title: "Read"
    url: "/aea-de-guidance/FAQ.html"
    excerpt: "Find answers to some frequently asked questions asked by authors."
    btn_label: "Read More"
    btn_class: "btn--primary btn--center"
  - image_path: /images/noun-setting-3836204.png
    alt: "Image: Ilham Fitrotul Hayat from the Noun Project"
    title: "Technical tools"
    excerpt: "Data, code, containers, templates, for and by the Data Editor."
    btn_label: "Read more"
    btn_class: "btn--primary"
    btn_id: "btn--toggle"

feature_row2:
  - title: "Data resources"
    excerpt: 'The AEA Data Editor team sometimes makes general-purpose preservation archives available for re-use by the (economics) community. Find some at the [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/search/aea/studies) and at the [auxiliary repository at Zenodo](https://zenodo.org/communities/aeajournals/). '
    url: "https://www.openicpsr.org/openicpsr/search/aea/studies"
    image_path: /images/icpsr-plus-zenodo.png
    btn_label: "Go to ICPSR"
    btn_class: "btn--primary"
  - title: "Code resources"
    excerpt: 'Much useful code - for researchers starting new projects, or those just about to submit - can be found on the Data Editor Github.'
    url: "https://github.com/AEADataEditor/"
    image_path: /images/github-frontpage.png
    btn_label: "Go there now"
    btn_class: "btn--primary btn--center"
  - title: "Compute containers"
    excerpt: 'Compute containers - docker, singularity - are useful and being used by the Data Editor. Find pre-compiled containers at [dataeditors Docker Hub](https://hub.docker.com/u/dataeditors), project-specific containers at [aeadataeditor Docker Hub](https://hub.docker.com/u/aeadataeditor), and at [Sylabs.io library](https://cloud.sylabs.io/library/vilhuberlars/dataeditors/stata17)'
    url: "https://hub.docker.com/u/dataeditors"
    image_path: /images/docker-frontpage.png
    btn_label: "Go to Docker Hub"
    btn_class: "btn--primary"
---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

<div id="hideme" class="hidable">

{% include feature_row id="feature_row2" %}

</div>

{% include hidable.html %}
