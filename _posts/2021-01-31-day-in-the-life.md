---
title:  "A Day in the Life of a Data Editor"
layout: single-withtoc
date: 2021-01-31
tags:
  - FAQ
  - Twitter
  - Tasks
---

I wanted to illustrate the range of the various topics that a Data Editor might face, by taking a fairly random day (2021-01-29) and listing all the various (distinct) activities that are in-scope for my job at the AEA. 


<!-- more -->

All in all, I worked on 15 different papers - some for quite a while, others only briefly. 
Naturally, I signed off on a few reports - some were first round (yes!), some were second round. I'm late on quite a few, because ...

I've spent a good chunk of the week onboarding a cohort of 11 new RAs. We wrapped up 15 hours of lecture and hands-on training. They did really well!

I sent off a reminder to an author. Deposit was withdrawn, because it contained data in infringement of his DUA. The data provider contacted us ("take down request"), we are waiting for the author to update deposit so we can republish.
![Unpublished study](/images/openICPSR-study-unpublished.png)

I contacted a commercial data provider to request permission to post a data extract provided by author. Author had not asked for permission. I believe we will not get permission. This avoids a "take down request" later.

Can a Data Editor (or any data-oriented referee) be considered a "consultant" with "material participation/engagement" for the purposes of a confidentiality and data use agreement? Question sent to IRB (thanks to the author for bringing this up early!)

How do you cross-list replication packages or data from a trusted repository that is not the journal's repository? We would like to be able to search "all the journal's packages" even when they are legitimately deposited elsewhere? Backend technical.

Identified one new request for replication (with restricted-access data) that I can delegate to a third-party replicator. Handled getting them started. <https://aeadataeditor.github.io/aea-de-guidance/protocol-3rd-party-replication.html>

First paper that uses Google Colab to run and disseminate package - guide RA, and figure out response to authors, since we still need a copy of the Jupyter notebooks in the archive (they did not provide a README). <https://social-science-data-editors.github.io/template_README/>

Assigned additional resources (extended reservation) for the Linux Cluster so the job that another RA is running can finish.  Note that we are skipping the part that uses 2000 nodes (as per README) in the interest of time (and $$).

Assessed whether we need to boot up the (pre-configured) Windows VM to run a Matlab + Dynare job, or whether we can run it on the existing Cornell Windows cluster.

Helped RA debug a problem where Matlab interfaces with an external (Fortran-compiled) binary that is not producing output - the code contained no checks for that situation, and gave a misleading error message several steps later. 

Alerted the journal editor to an issue where even the authors' revision still leads to numerical discrepancies, despite authors' greatly improved efforts to specify exactly how to run (and our standard setup is fully compliant). Is this another Stata bug?

Used a Docker image to run revised R code from author team. The revised README now specifies exactly the version of R, and Docker happens to be the best way to compartmentalize the whole package (the authors did not use Docker). <https://github.com/AEADataEditor/docker-r-starter>

Never a dull day!


