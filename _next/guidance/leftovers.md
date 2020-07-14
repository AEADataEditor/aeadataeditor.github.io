---
title: Leftovers
layout: mermaid
---

Process for R&R
===============

<div class="mermaid">
sequenceDiagram;
    autonumber;
    participant Author;
    participant ICPSR;
    participant Editorial Office;
    participant CoEditor;
    participant Data Editor;
    CoEditor ->> Author: promising R&R decision (letter A)
    activate Author;
    rect rgba(252,141,98, .3)
      Author ->> Author: revise manuscript;
      Author->> ICPSR: Create new deposit;
      Author-->> ICPSR: Upload replication package;
    end;
    Author->> Editorial Office: Send manuscript native files;
    Author->> Editorial Office: Send data and code availability form;
    deactivate Author;
    Note right of Editorial Office: Send out to referees;
    activate Data Editor;
    rect rgba(141,160,203,.1);
      Editorial Office ->>+ Data Editor: Assign manuscript ("as referee");
      note right of Data Editor: conduct <br>reproducibility<br> check;
      Data Editor ->> CoEditor: Sends report;
    end;
    deactivate Data Editor;
    CoEditor ->> Author: Sends decision;
    rect rgba(141,160,203,.1);
       note right of Editorial Office: Normal process
    end;
</div>



For more information, see the [Frequently Asked
Questions](https://www.aeaweb.org/journals/policies/data-code/faq)
(<[https://www.aeaweb.org/journals/policies/data-code/faq](https://www.aeaweb.org/journals/policies/data-code/faq)>).