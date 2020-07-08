---
title: Step by step guidance
layout: mermaid
---

The following steps outline what you should expect after conditional acceptance of your manuscript, in compliance with the [AEA Data and Code Availability Policy](https://www.aeaweb.org/journals/policies/data-code):

1. [Prepare your data and code replication package](preparing-for-data-deposit.md) (including data citations and provenance information)
2. [Provide metadata and upload the replication package](data-deposit-aea.md), for verification and subsequently publication.
3. Submit the [Data and Code Availability Form] together with your manuscript native files as instructed, and as per guidelines at your journal (for example, [AER guidelines](https://www.aeaweb.org/journals/aer/submissions/accepted-articles/styleguide)).
4. The editorial office assigns the manuscript to the AEA Data Editor.
5. The AEA Data Editor team downloads materials, [conducts reproducibility checks](https://social-science-data-editors.github.io/guidance/Verification_guidance.html) , writes [report](https://github.com/AEADataEditor/replication-template/blob/master/REPLICATION.md).
6. The report is communicated to the editorial office and the Editor of the journal.
   - If accepted, the manuscript is copy-edited, and published together with the data deposit as provided by the author.
   - If changes need to be made, the report is communicated to the authors, who make changes, until the replication package is accepted.


```mermaid
sequenceDiagram;
    autonumber;
    participant Author;
    participant ICPSR;
    participant Editorial Office;
    participant Data Editor;
    activate Author;
    note left of Author: Add Data Citations<br>to manuscript;
    note left of Author: Prepare replication package;
    deactivate Author;
    rect rgba(252,141,98, .3)
      Author->> ICPSR: Create new deposit;
      Author-->> ICPSR: Enter metadata;
      Author-->> ICPSR: Upload replication package;
    end;
    Author->> Editorial Office: Send manuscript native files;
    Author->> Editorial Office: Send data and code availability form;
    Editorial Office ->>+ Data Editor: Assign manuscript;
    activate Data Editor;
    rect rgba(141,160,203,.1)
    loop until acceptance;
       ICPSR -->> Data Editor: Downloads replication package;
       note right of Data Editor: conduct <br>reproducibility<br> check;
       Data Editor -->> Editorial Office: Sends report;
       Editorial Office -->> Author: Sends report;
       Author -->> ICPSR: uploads corrections;
       Author -->> Editorial Office: Sends response;
       Editorial Office -->> Data Editor: Re-assigns manuscript;
       end;
    end;
    deactivate Data Editor;
    Data Editor -->> Editorial Office: Accepts replication package;
    note right of Editorial Office: copyediting;
    Editorial Office -->> ICPSR: Publishes deposit;

```

