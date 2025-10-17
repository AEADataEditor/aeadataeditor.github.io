---
title: Guidance on how to deposit data at the AEA Data and Code Repository
toc: true
layout: single
date: 2021-09-06
modified: 2023-09-07
---

### Tutorial

For a video tutorial on this process, see [this Youtube video](https://www.youtube.com/watch?v=wRytQcotLGc).

> If you are depositing at a different trusted repository, please be sure that your deposit complies with our [Display Guidelines for Trusted Repositories](guidelines-other-repositories)


### Assistance

If, in the process of uploading your replication package, you have questions that are not addressed by these guidelines, please contact us:

- We are on [BlueSky](https://bsky.app/profile/aeadata.bsky.social), [Mastodon](https://mstdn.social/@aeadata/).
- Contact us via the AEA's [Contact form](https://www.aeaweb.org/contact)
- Reach out to the editor handling your paper, who knows how to reach us (but might also have the answer).
- Reach out to us directly (you know how to find us).

In some cases, the [openICPSR helpdesk](https://www.openicpsr.org/openicpsr/contactUs) may be able to help you, but with any content matter, please contact us, not them. 

### Start the deposit process


[![Start deposit](/images/icpsr-start-your-deposit-v2.png)](https://www.openicpsr.org/openicpsr/workspace?create=true&archive=aea)



Go to the [AEA Data and Code Repository](https://www.icpsr.umich.edu/sites/aea/home), and start the process. 
Once there, click on the "Share Data" link:

[![Start process](/images/icpsr-start-process-share-data-v2.png)](https://www.icpsr.umich.edu/sites/aea/home)

You will be taken to a page explaining some of the technical details. Click on the "[Start Your deposit](https://www.openicpsr.org/openicpsr/workspace?create=true&archive=aea)" button to initiate the deposit process itself. 


---

### Checklist for Metadata

#### Required

- [ ] **Title** (Either: "*Data and Code for: (NAME OF PAPER)*" or "*Code for: (NAME OF PAPER)*")
  - If only data, or only code are provided, adjust accordingly.
- [ ] "**Principal Investigators**" (=Authors)
  - These need not be in the same order as on the paper. 
  - These need not be the same people as on the paper (more, or less, is OK)
  - Please ensure that all authors have affiliations (if not affiliated: "Independent Researcher")
- [ ] **Summary** (Suggested: The abstract from the article and/or a note that this is data and/or code accompanying the article)
  - Do not cite, or mention, the article, or include "forthcoming".
- [ ] **Subject Terms** (e.g., "Machine Learning", "Randomized Control Trial", "Nudges", ...)
- [ ] **JEL Classification** (can be the same as article)
- [ ] **Manuscript Number** (your manuscript tracking number as assigned by the editorial office, e.g., "AER-2019-0000")

#### Conditionally required

*Most deposits will also need to provide the following metadata elements. In some cases, it may not make sense to fill out (for instance, a laboratory experiment may have no meaningful "geographic coverage"). These elements contribute to better inclusion in search engines.*

- [ ] Geographic coverage (e.g, "United States", "Florida, U.S.", "Indonesia", ...)
- [ ] Time period(s)  (e.g., "1982-2008")
- [ ] Collection date(s) 
- [ ] Universe (e.g., "All households in Canada", "Manufacturing establishments in Indonesia", ...)
- [ ] Data Type(s) 

#### Suggested

*The following elements are suggested for certain types of data, and may not apply to all types of data.*

- [ ] Data Source 
- [ ] Units of Observation 
- [ ] Any additional metadata elements

---

Start by providing the metadata (descriptors) for the data and code you are uploading.


### Details on Filling Out Metadata


#### Describe the project

![screenshot of project description](/images/project-description-icpsr.png)

  - The **title** should be "`Data and Code for: [Title of article]`" if it contains both data and code. If only one or the other are included, then "`Data for: [Title of article]`" or "`Code for: [Title of article]`". In some cases, when data is split across multiple deposits, one might use "`Supplementary Data for: [Title of article]`". Do not use the uninformative "Replication files for...", nor "Data for ..." when the deposit contains code.
  - The **authors** should be those who compiled the data and code. The names, and order of the names, may differ (if necessary) from the article. 
  - The **summary** might be short. It should always be informative. It can include the **abstract** of the article itself. It should not include information on the related article (which has its own field). If data is included, the summary/abstract should describe the data. 
  - Identify any **funding sources** here - the information can be queried by some funders, and can assist with your award reporting.


#### Scope of project section

To fill out the required metadata elements **Subject Terms**, **JEL Classification**, and **Manuscript Number**, open the "Scope of Project" section:

![metadata of project](/images/project-metadata-icpsr.png)

**Click on each + to open the related section:**


![scope of project](/images/project-scope-of-project-icpsr.png)

  - Authors **MUST** provide additional subject terms (keywords). You do not need to repeat JEL codes.
  - Authors **MUST** provide JEL codes (under "Scope of Project")
  - Authors **MUST** provide the **Manuscript Number**,  (your manuscript tracking number as assigned by the editorial office, e.g., "AER-2019-0000") as this will allow us to properly connect the repository with the manuscript.
  - Where appropriate, authors are **REQUIRED** to define 
      - the geographical scope(s)
      - the time period(s)
      - the universe(s)
      - data type(s)
  - Most fields are repeatable, please enter as many values as needed. For instance, if subsets of the data cover different periods (e.g., `1999-2019` and `2004-2019`). Just click "add value" next to the time period field for each time period.
  - This information can also be provided when only code is made available.
  - When only code is produced, authors should choose `data type = program source code`: ![program source code](../../images/project-data-type-icpsr.png)

#### Methodology section

  ![methodology section](/images/project-methodology-icpsr.png)
  
  - Methodology is particularly relevant for survey or experimental data:
    - response rates, sampling rates, etc.
  - We ENCOURAGE all authors to define
    - the unit of observation (e.g. individual, firm, establishment, county, country)

#### Related publications section

![related publications](/images/project-related-icpsr.png)

- The AEA editorial office will provide an entry for this field that links back to the **published manuscript** - authors do not need to add any reference to the manuscript anywhere in the deposit form (other than the Manuscript Number)
- Authors are encouraged to link back to **working papers** or related publications that have or will use this (same!) data. 
- If code is derived from or continues to be updated on a Git repository (**Github, Gitlab, Bitbucket**, etc.), authors can link to it here.
- Future functionality will automatically list articles (including articles by third parties) that cite the data.



### Uploading

Once the metadata is completed, authors can upload files. 

Upload files in the way you expect the files to be organized in order to run the code. 

---

#### Checklist for Uploading

- [ ] README is in PDF or TXT format 
- [ ] Do not upload a ZIP file - [IMPORT IT](#importing-zip-files)! 
- [ ] Do not upload manuscripts, appendices, responses to editors, etc.
- [ ] Directory structure does not contain redundant/ superfluous directories
- [ ] Do not upload data that you do not have the rights to publish! (This includes PII that is not authorized by your IRB)
- [ ] Do not upload confidential data!

---

### Some caveats and tips

#### Importing ZIP files

We said it above: 

> **Do not upload a ZIP file** - IMPORT IT! 

![screenshot of upload and import options](/images/upload-import-icpsr.png)

- It is possible to **IMPORT a ZIP file** (do **NOT** upload a ZIP file - no ZIP files should be visible in the deposit). Replicators will be downloading a ZIP file that preserves the directory structure.
  - See the [tutorial](https://www.youtube.com/watch?v=wRytQcotLGc?t=135)
  - A well prepared ZIP file has NO folder in the root
  - macOS users should [see our FAQ on this topic](https://aeadataeditor.github.io/aea-de-guidance/FAQ.html#what-is-that-__macosx-folder-which-seems-to-contain-a-second-copy-of-all-the--replication-files-i-am-not-sure-why-this-folder-exists)
  - Instructional videos: [macOS](https://www.youtube.com/watch?v=fCfVu55YsJg), [Windows](https://www.youtube.com/watch?v=wRytQcotLGc?t=135)
- The Import functionality can handle ZIP files, but cannot handle other compression formats (RAR,7z, etc.). Please convert to ZIP before importing.


#### File size and count

- If the **UNCOMPRESSED** contents of the deposit (the **UNZIPPED** size of the ZIP file) are larger than **30GB**, please send an email to the AEA Data Editor to request an increase in the quota. Reasonable requests will be authorized, though we may also suggest other, more suitable repositories. Size of the deposit is **never** a reason not to provide materials, as we have found solutions for every single case so far.
- If you have **more than 1,000 files** in your deposit, please read [the guidance in the previous Step 1](/aea-de-guidance/preparing-for-data-deposit.html#structure-in-the-presence-of-more-than-1000-files), and if that doesn't solve it, [talk to us](#assistance) before uploading, 


#### Restricted-access data

> **DO NOT UPLOAD data that you do not want published!** 

- **Contact the AEA Data Editor** if you are able to share data for reproducibility checks that cannot be published.

> - Consult the [Sharing restricted-access data with the AEA Data Editor](sharing-restricted-data) page.
> - See [instructions in previous Step 1](/aea-de-guidance/preparing-for-data-deposit.html#structure-in-the-presence-of-confidential-unpublished-data)
> - Be sure to only include PII data that you are allowed to publish (f.i., politicians' names, etc.). We recommend using the J-PAL maintained PII-Scan for R <https://github.com/J-PAL/PII-Scan> or PII-Scan for Stata <https://github.com/J-PAL/stata_PII_scan> to get an idea of potential PII in your dataset.

⚠️ 📢 You remain ultimately responsible for ensuring that no **unauthorized** PII is included in the published replication package.

- If you can share the data more broadly, but want to control access, you **must** create a separate deposit for the parts of the data that are sensitive  while keeping the code, and any non-sensitive data, in the "primary" deposit as described on the present page. Your README must describe how to combine the two deposits.

> - Consult the [Creating separate linked data archives](creating-separate-data-deposit) page for details on how and where to create a separate data deposit.
> - See the "[Depositing Data for the Greater Good](https://social-science-data-editors.github.io/guidance/sample-depositing-data-for-greater-good.html)" page at the Social Science Data Editors website.
> - Consult the [Accessing Restricted Data Through openICPSR](https://www.openicpsr.org/openicpsr/accessRD) page about the process at openICPSR, but other repositories may be acceptable.

**TL;DR version:**

- [ ] Choose where to upload any restricted data (but not HERE)
- [ ] If you are able to provide the data to the Data Editor, select the appropriate checkbox on the [DCAF](https://www.aeaweb.org/journals/forms/data-code-availability) but **DO NOT** upload the data here (even temporarily). You will be sent a secure upload form.
- [ ] Be sure to answer the [Submission questions](#submission-questions) with respect to the data that you **have** deposited, not data withheld or deposited elsewhere
- [ ] proceed as usual as outlined below

#### Tips

- Please upload the README (in PDF or TXT) as the very first file - ensuring that it can be found easily by browsers of the archive.
  - It is OK to upload Markdown or Word documents in addition to, but not instead of the PDF or TXT version
- Please upload the README to the root of the repository - any data and code can be in subdirectories, but it is easier to find the README if it is not in subdirectories.
  - There should be no duplicate README files in the repository

#### Ideal structure

Your deposit should have

- [ ] no redundant directories: the first thing you should see is the README and any subdirectories
- [ ] there should be no ZIP files!
- [ ] the structure should be as you last ran the code

> [NOTE] The AEA staff will not re-arrange or otherwise restructure your deposit in any way. What you see in the deposit interface is what others will see once it is published.

You should see something like this:
```
data_directory/
prog_directory/
README.pdf
LICENSE.txt
```
(the `LICENSE.txt` is optional if you want to adopt one of the standard openICPSR licenses upon publication. See [our licensing guidance](Licensing_guidance) for other options).

### Submitting to the Data Editor

Once you are satisfied that all (publishable) data files are present, are complete, and all metadata is satisfactory, including all required elements filled out, you should **submit** the deposit, by changing the **status** of the deposit:

![submit project](/images/project-submit.png)

Choose "Submit to AEA" (or "Resubmit") under "Change Status".

#### Submission questions

You will be presented with a page to confirm that you are going through with the submission. You will then be presented with a page, asking various questions. 

> You should answer these questions in regards to the **data in the deposit** you are submitting. The answer should NOT consider any other data that may have been used as part of the manuscript's analysis, but that are not present in this particular deposit. 

Contact the Data Editor if you have any questions or concerns.

##### Can individuals be identified?

![Identification question 1](/images/icpsr-submit-q1.png)

The normal answer to this question is "No." If you would answer "Yes" to this question, go back to [Restricted-Access data](#restricted-access-data), or contact the Data Editor for clarification.

##### Are the data sensitive?

![Sensitivity question 2](/images/icpsr-submit-q2.png)

The normal answer to this question is "No." If you would answer "Yes" to this question, go back to [Restricted-Access data](#restricted-access-data), or contact the Data Editor for clarification.

##### Distribution question

![Distribution question](/images/icpsr-submit-q3.png)

You should answer this one as a function of the earlier answers. "Public download" means users will be registered users of openICPSR and consent to the license (next question), without further controls. "Restricted access" means that data will be distributed through ICPSR's [Restricted Data Access Mechanism](https://www.icpsr.umich.edu/web/pages/ICPSR/access/restricted/). Every replication package must have AT LEAST ONE deposit that is unrestricted. If you are uncertain, go back to [Restricted-Access data](#restricted-access-data), or contact the Data Editor for clarification.

#### Choose a license

![License question](/images/icpsr-submit-q4-license.png)

You should choose a license from the drop-down menu, or, if you have a custom license as part of the deposit, select "Other". See our [Licensing Guidance](Licensing_guidance).


#### Finalizing

Press "submit." Should you have forgotten something, you can "recall" the submission, fix the issue, and re-submit. 


### Citing Your Deposit

At present (2020), the openICPSR repository does not display the Digital Object Identifier (DOI) that will be associated with your deposit. However, it can be deduced easily.

- Each openICPSR project has a number (e.g., "109622"), that might show up on the right panel:

 ![Image of number](/images/project-number.png) 

- if the openICPSR project has not been published, then the DOI will be "http://doi.org/10.3886/E" + number + "V1" (e.g. **http://doi.org/10.3886/E109622V1**)
- if the project has already been published before, and you are updating it, then the "V1" will be incremented. See [our FAQ](FAQ.md)
- You should then cite your deposit as follows (see [AEA Sample References](https://www.aeaweb.org/journals/policies/sample-references)):


|                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|
| **Romer, Christina D., and David H. Romer**. 2010. "Replication data for: The Macroeconomic Effects of Tax Changes: Estimates Based on a New Measure of Fiscal Shocks." *American Economic Association* [publisher], Inter-university Consortium for Political and Social Research [distributor]. https://doi.org/10.3886/E112357V1. |
|                                                                                                                |

- Note that the DOI **will not work** until (at the very end of the review process) the deposit is published. This is **normal**.
- You do **not** need to add your replication package citation to the manuscript's **list of references**, as it will be added automatically. However, you do need to add the in-text citation, ideally the first time you mention the data, in particular the data you collected.

#### Give it a try

{% include deposit-doi.html %}

### Ready to submit manuscript

Once you have completed the deposit, you are now ready to submit the manuscript native files, together with the [Data and Code Availability Form](https://www.aeaweb.org/journals/forms/data-code-availability), as per the journal's guidelines ([AER guidelines here](https://www.aeaweb.org/journals/aer/submissions/accepted-articles/styleguide)).

