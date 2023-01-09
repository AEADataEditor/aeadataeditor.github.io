---
title: Guidance on how to prepare a comment based on a replication
toc: true
layout: single
date: 2021-09-29
---

You may have found an issue in a published article related to some of the computations therein, and are preparing a comment. This note describes how you should prepare the replication package that accompanies the comment, to ensure clarity and transparency of your replication package.

### Provide a strong link to the original replication package

Your comment may start off with different data, augmented data, more up-to-date data, or the same data the original authors used. If you are pointing out issues with data processing or analysis methods, ideally use the same data the original authors used. Put simply, start with a reproduction of the original article! 

> If you are unable to computationally reproduce the original article, despite having all materials as described by the original authors, please let us know immediately, regardless of whether you are writing a more complete article or not.

You should

- [ ] provide  the DOI of the original replication package, and the associated data citation.

You need not

- [ ] provide the original replication package - rather, instruct the authors to download it, and unpack it into a specific location

You should 

- [ ] not rename or otherwise modify the original files

### Provide reproducible code

Your code should itself be reproducible. 

### Provide a README

You should provide a clear README that outlines the requirements for your comment's replication package. You should be precise (more precise, in general) then the original authors in outlining the computational requirements (for instance, software versions), so that any spurious discrepancy can be ruled out.

> There are various ways to use older versions of Stata, Matlab, R. We encourage you to reach out to us to explore options.

You do not need to make the main point using the same software as the original authors, but you should avoid any ambiguity that it is only the software that is causing you to obtain different results from the authors.

