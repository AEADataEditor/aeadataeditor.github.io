---
title: Preparing your replication package for Papers and Proceedings
toc: true
date: 2025-02-26
---

Much of the preparation for the replication packages for papers published in [Papers and Proceedings](https://www.aeaweb.org/journals/pandp) is the same as for the AEA journals, see [Step 1](preparing-for-data-deposit.html) and [Step 2](data-deposit-aea.html). 

> However, our compliance check is more limited than the checks conducted for peer-reviewed papers. Your replication package must nevertheless be fully compliant with the [AEA Data and Code Availability Policy](https://www.aeaweb.org/journals/data/data-code-policy). Should a reader or user of your replication package find errors or omissions at a later stage, you will be asked to remedy the situation in line with our [Policy on Revisions of Data and Code Deposits](https://www.aeaweb.org/journals/data/revisions-policy).

We will send you a filled-out checklist, verifying compliance with each item. This page provides a bit of guidance on how to get a perfect score.

> The use of the [AEA Data and Code Repository](https://www.openicpsr.org/openicpsr/aea) is strongly encouraged. Other repositories and archives considered to be "trusted" may be acceptable (Github is not a "trusted" archive). Other repositories may not  support a specific item in the checklist, it is fine to skip. These special features are denoted by a **\***.

A printable checklist is available [here](/assets/pdfs/pandp2025-checklist.pdf).

## List of required items

### Title

Suggested: “Data and code for: (NAME OF PAPER)”	

### Principal Investigators	

This corresponds to the authors of the article; however, these need not be in the same order as in the article.  

Please ensure that all authors have affiliations; if not affiliated, 
use "Independent Researcher".

### Summary

Suggested: The abstract from the article and/or a note that this is 
data and/or code accompanying the article.

### JEL Classification	**\***

May be the same JEL codes as the article.

### Manuscript ID	**\***

Manuscript tracking numbers in the format  "PandP-2021-xxxx"

### No ZIP Files **\***

No visible ZIP files. Use "Import from ZIP" on openICPSR. This is supported on Dataverse deposits, but not on Zenodo and some others.

### README Format

Must be PDF, TXT, or MD. DOCX generally not accepted, unless the relevant repository allows for Web preview without download of DOCX files.

### README Content	

The README content must contain all the required elements as per the [AEA Data and Code Availability Policy](https://www.aeaweb.org/journals/data/data-code-policy#dcas-13). A good starting point is the [Template README](https://social-science-data-editors.github.io/template_README/), which provides guidance on what to provide for each of the required elements.

We check that at least the following sections must be present to be compliant:

- Data Availability and Provenance Statements
- Details on Each Data Source (sufficient for others to obtain the same data from the original source)
- Computational Requirements
- Instructions to Replicators. 

### Code

Deposits must always contain code, even if data cannot be included. The provided code must be **complete**, including for construction 
of the analysis data from raw data, and for appendix tables and 
figures, and all inline numbers.

### Data

Please only include data that you are allowed to publish. The README should provide instructions for any data that you are not allowed to publish. For large deposits, contact the AEA Data Editor. Maximum of 20GB. 

### Survey/Experimental materials 

These must be provided, if the manuscript references an experiment, an RCT, or a survey, in line with the [Policy for Papers Conducting Experiments and Collecting Primary Data](https://www.aeaweb.org/journals/data/policy-experimental-surveys). 

The replication package must contain any computer programs, 
configuration files, or scripts used to run the experiment or 
develop the survey instrument, e.g., z-Tree code, Qualtrics, 
SurveyCTO, LimeSurvey.

## List of suggested (metadata) items

The following items are suggested for better findability of the replication package by searches.

- Subject Terms, e.g., “Machine Learning”, “Randomized Control Trial”, ...
- Geographic Coverage **\***, e.g, “United States”, “Florida, U.S.”, “Indonesia”, ...
- Time Period(s) **\***, e.g., “1982-2008” 
- Funding Sources	
- Collection Dates **\***
- Data Types	
- Data Sources
- Unit of Observation
