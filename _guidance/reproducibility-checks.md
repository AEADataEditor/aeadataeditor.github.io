---
title: Guidance on testing replicability of code
toc: true
date: 2021-04-08
---



The code and data that have been archived should be reproducible and replicable. How do we test that?

## Generic guidance

Generic guidance is provided at the [Social Science Data Editors' Guidance](https://social-science-data-editors.github.io/guidance/) website. 

## At the AEA

We use **[this template](https://github.com/AEADataEditor/replication-template/blob/master/REPLICATION.md)** to guide our replicators. 

- [Example 1](sample-report.md)

We assess 

- software availability
- data availability and data citations
- code availability and clarity
- needed computational resources
- time needed to acquire or use all of the above, and conduct the reproducibility check

If we have, or can acquire in a reasonable time, all of the resources needed, then we conduct a computational check. If not, we conduct only a visual inspection of the code, but may test the described data access or data provenance description (could we get the data?). 

## What if we don't have the resources

When some of the conditions are not met with our own resources, we may ask others to conduct a reproducibility exercise for us. 

- Our [PROTOCOL](https://www.aeaweb.org/journals/data/policy-third-party) describes how we might request reports.
- [Sample report 1](sample-report-3rd-1.md)
- We may ask others to do so because
  - They are experts
  - They have access to the software
  - They have access to the data
  - They have access to computational resources needed

- **No reproducibility check is discarded out of hand**

## Outcomes

We classify the outcome of the verification as follows:

### Accept

Authors receive the report by the AEA Data Editor via ScholarOne.

No further changes are needed to either manuscript or replication package. The manuscript is sent to the copy-editors by the editorial office, the replication package is ready to be published. The process is finished on ScholarOne, and authors will receive  all further communication from the editorial office. 

### Accept with changes

Authors receive the report by the AEA Data Editor via ScholarOne.

There are some minor changes that will need to be made to manuscript and/or replication package. No major impediments to publication of either.

- Changes to the manuscript (typically missing or erroneous data citations, or minor numerical differences in a small number of table cells) will be made during the copy-editing process. Authors should pay attention to the proofs! All communication regarding the manuscript (and the online appendix) come from the editorial office.

- Changes to the replication package are handled separately on openICPSR by the AEA Data Editor's staff. Typical issues are:
  - minor fixable bugs in code (fix the code)
  - missing code that is not critical (provide the code)
  - incomplete data provenance information (update the README)
  - missing information on software (update the README and any setup files)

Authors are expected to fix the issues on ICPSR in a timely manner, [submit an updated replication package](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submitting-to-the-data-editor) on ICPSR, and to reply to the Data Editor with a brief description of any changes made.

### Conditional Accept

Authors receive the report by the AEA Data Editor via ScholarOne.

There are major changes needed to achieve compliance with the [AEA's Data and Code Availability Policy](https://www.aeaweb.org/journals/data/data-code-policy). The report will outline the steps needed to achieve compliance.

Authors are expected to 

- make all changes to the replication package in the existing ICPSR deposit in a timely manner, 
- [submit the updated replication package](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html#submitting-to-the-data-editor) on ICPSR, 
- re-submit manuscript and a letter to the Editor and the Data Editor outlining changes made in a detailed fashion. The manuscript and letter should be submitted on ScholarOne (not ICPSR). 

Once received, the AEA Data Editor will check compliance with any requests, and creates a revised report. 

### Revise-and-resubmit


Authors receive the report by the AEA Data Editor via ScholarOne, but will also receive direct correspondence from the AEA Data Editor. 

A "revise-and-resubmit" means that the reproducibility check has identified critical shortcomings that might affect the Editor's decision regarding acceptance of the paper. This may be due to significant numerical differences that possibly change the conclusions of the paper, inadequacies of the data description that are materials to the paper, or some other reasons.

The AEA Data Editor and the journal editor responsible for the manuscript will make an assessment, and work with the authors to remediate the issue. 

Procedurally, the manuscript *may* go back to referees from the previous round (this has never happened), and may receive a second "conditional acceptance" by the editor. Usually, the process proceeds as for "[Conditional Accept](#conditional-accept)".

