---
title: Step-by-Step tutorial on how to deposit data at DataLumos
toc: true
layout: single
date: 2025-02-14
---

DataLumos is an ICPSR archive for crowd-sourced deposits of government data resources. This tutorial shows how to create a deposit at DataLumos. You should read the [Tips for Using DataLumos](https://www.datalumos.org/datalumos/static/tips) on their website first. 

## When  and what to deposit

U.S. Government data are freely available. In fact, they are in the [public domain](https://en.wikipedia.org/wiki/Copyright_status_of_works_by_the_federal_government_of_the_United_States) within the US (the situation outside of the US is a bit more ambiguous). However, unless these data are preserved at the [Library of Congress](https://www.loc.gov/) or the [National Archives and Records Administration](https://www.archives.gov/), they can be deleted or re-organized at any time, and data might be lost.[^1]

[^1]: Some agencies have exceptions, where archives are separately created and DOI assigned. Always check first.

You should deposit public domain or otherwise freely available data (e.g., [CC-BY](https://creativecommons.org/licenses/by/4.0/))

- when you first use them
- if they are not preserved elsewhere

If you are not in the US and depositing non-US data, you should preferentially use your local archives, such as

- [Swedish National Data Service](https://snd.se/en)
- [GESIS in Germany](https://www.gesis.org/en/landingpage/data-gesis)
- or more generally, [re3data.org](https://www.re3data.org/)

## Before depositing

Search existing holdings to see if the data have already been deposited:

- [ICPSR](https://www.icpsr.umich.edu/web/pages/) (will search openICPSR and DataLumos as well)
- [Dataverse](https://dataverse.harvard.edu/) (the Harvard Dataverse will also search through federated dataverses)
- [DataCite](https://commons.datacite.org/) a registry for dataset DOIs
- [Google Dataset search](https://datasetsearch.research.google.com/)


## Start the deposit process

Go to the [DataLumos](https://www.datalumos.org/datalumos/), and choose `Add Data Now`:

[![Start process](/images/datalumos-10.png)](https://www.datalumos.org/datalumos/workspace).

You may need to create an ICPSR account first.

## Create a new project

Then, create a new project:

![Create new project](/images/datalumos-11.png)

## Name the project

![Name the project](/images/datalumos-12.png)

Title the project accurately and descriptively, preferably using the exact title provided by the agency originally issuing the data. This will help others find the data, and connect it with its original location.

Do not add your name, your paper, etc.

## Describe the project

You should now provide additional information in the `Project Description`:

![screenshot of project description](/images/datalumos-1.png)

### Data Producer (Government agency)

Data produced by or associated with a specific US government agency should list the agency as the author of the data in the `Government Agency/Principal Investigator(s)` field. Click on the `+ add value` and switch to the `Organization/Agency` tab of the pop-up window.

![Organization/Agency tab](/images/datalumos-13.png)

You should start typing, typically with the full name of the department without acronyms. In the example screenshot, while the agency is typically referred to as "OPM", it was found by typing `United States Office of P` before the type-ahead found the agency. Try to avoid creating new variants of the name. However, if you cannot find it, simply write the name of the agency as accurately as possible. 

![Name of the Agency](/images/datalumos-2.png)

### Summary field

You should provide ideally relevant information taken verbatim from the original website. You can then add information on when the data were downloaded or scraped, and if you wish, who did this. 

### Original Distribution URL

Provide the URL where the data were originally found. 

- Try to remove tracking parameters from the URL (anything after a `?`)
- If the URL is very long, try to find a shorter one that goes to the same location.
- If the data are found on a page with multiple datasets, provide the URL of that page. You can then add more information in the summary field.

![Original URL](/images/datalumos-7.png)

### Additional information (metadata)

- Try to capture a PDF or a screenshot of the website as it was when you downloaded it. This can be useful. The PDF can be uploaded as part of the next step.
- Also try to identify any additional documentation, such as codebooks.


## Upload data files

### Importing a ZIP file

You should try to preserve the data in its original arrangement, with any subdirectories. The best way to achieve this is to compile a ZIP file of the preserved data.

You then `Import from ZIP`, which will expand the ZIP file, preserving the directory structure. This makes it easier for others to download individual files.[^2]

> The Import functionality can handle ZIP files, but cannot handle other compression formats (RAR,7z, etc.). Please convert to ZIP before importing.


[^2]: Future users will still be able to download the entire collection as a ZIP file, using the download facility of the DataLumos site.

![Importing from ZIP](/images/datalumos-9.png)

> ⚠️ WARNING: The process of both uploading and unpacking the ZIP file can take some time, depending on the size of the file. Be patient!

### Uploading individual files

For other files, they can be added individually. Use the `Upload Files` button.

![Upload files](/images/datalumos-3.png)

You can now choose, or drag-and-drop, the files to be uploaded. While files are being uploaded, others can be added

> ⚠️ WARNING: Files are immediately uploaded!

![Uploading files](/images/datalumos-4.png)

![Uploading more files](/images/datalumos-5.png)

> In the example, we also uploaded (not imported) a more comprehensive ZIP file that contained a complete mirror of the website. However, the core data files were `imported`, and show up in the `Files` folder.

![Uploaded files](/images/datalumos-8.png)

> ⚠️ WARNING: The process of uploading and then subsequently checking the files can take some time, depending on the size of the file. Be patient! ⏱️

Files that are still being checked are indicated with `File not available for download 🗑️`. 

## Publishing the deposit


### Start the publishing workflow

When everything is ready, on the right-hand side is a `📣 Publish Project` button.

![Publish project](/images/datalumos-14.png)

You can review the information as it will be published again:

![Review information](/images/datalumos-15.png)


### Submission questions

You will then be presented with a page, asking various questions. 

> You should answer these questions in regards to the **data in the deposit** you are submitting. The answer should NOT consider any other data that have not been uploaded. Usually, if you downloaded it from a public website without registration requirements, the answer to the first two questions is "No".

##### Can individuals be identified?

![Identification question 1](/images/icpsr-submit-q1.png)

The normal answer to this question is "No." 

##### Are the data sensitive?

![Sensitivity question 2](/images/icpsr-submit-q2.png)

The normal answer to this question is "No." 

##### Distribution question

> If both previous answers are `No`, this question does not appear.

![Distribution question](/images/icpsr-submit-q3.png)

You should answer this one as a function of the earlier answers. "Public download" means users will be registered users of openICPSR and consent to the license (next question), without further controls. "Restricted access" means that data will be distributed through ICPSR's [Restricted Data Access Mechanism](https://www.icpsr.umich.edu/web/pages/ICPSR/access/restricted/).

#### Delayed Dissemination

Usually, you would answer this with `No`. 

#### Choose a license

![License question](/images/icpsr-submit-q4-license.png)

You should choose a license from the drop-down menu. If depositing data that came from a U.S. government website, you would normally choose "Public Domain mark".

#### Read the agreement and consent

Reminder that you should always read the agreements that you consent to!

#### Finalizing

Press "Publish data." It might take a while for the data to be published.

## Final outcome

Back in the workspace, you should now see, bottom right, a list of the `Published Versions`:

![Published version workspace](/images/datalumos-16.png)

If you click on the version number, you will be taken to the published version:

[![Published version](/images/datalumos-17.png)](https://doi.org/10.3886/E219172V1)

## Citing the deposited data

Remember to cite the data in any publication that uses these data. You should use the provided `Project Citation`, adapted to your citation style. 

> United States Office of Personnel Management (OPM). Fedscope Datasets Available from OPM. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2025-02-13. https://doi.org/10.3886/E219172V1

Remember to use the DOI, and not the visible URL in your browser bar. To learn more about how to cite data, see [ICPSR guidance](https://www.icpsr.umich.edu/web/pages/datamanagement/citations.html) and [Guidance by Social Science Data Editors](https://social-science-data-editors.github.io/guidance/addtl-data-citation-guidance.html).