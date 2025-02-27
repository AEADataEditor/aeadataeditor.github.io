---
title:  "On access to restricted data by journals and others"
date: 2025-02-18
mastodon: 
twitter:
bluesky: 
tags:
  - data editor tips
  - replication packages
  - restricted data
  - access to data
---

Much of the data (though not a majority) in economics is in some way restricted. This can range from data that anybody can download, but not redistribute, to data that is so sensitive that you need to walk into a box in a room in a university to access it. 
I want to highlight a particular mechanism that provides some privileged access to journals in order to be able to conduct a reproducibility check that is **better** than what arbitrary other researchers might encounter.

<!--more-->

## The landscape for geocoded survey data (very briefly)

The US [General Social Survey](https://gss.norc.org/) (GSS)[^gss], like many other surveys, applies various disclosure avoidance measures before releasing data to the public, in order to protect respondent privacy. One data point frequently filtered in this way is geography, which in the publicly accessible files is generally either omitted (strictly speaking, coarsened to the national level), but is of high interest to researchers. Thus, the GSS also makes [GSS Sensitive Data Files](https://gss.norc.org/content/dam/gss/get-documentation/pdf/other/ObtainingGSSSensitiveDataFiles.pdf) available upon request. Obtaining such data for new research requires a research plan, IRB clearance, and a data protection plan (i.e., use of special, secure computers), as well as a fee (as of this writing, $1500). Similar mechanisms exist for other surveys, such as [NLSY](https://www.nlsinfo.org/content/getting-started/accessing-data) in the US and the German [SOEP](https://www.diw.de/en/diw_01.c.683748.en/regional_data.html), which both also have even more detailed geographic information available for in-person on-site visits.

## Caveat!

This is all fine - except that data editors never pay for access to data, and doing a full ethics-approval and secure computer setup is a bit more onerous than we mostly do for a reproducibility check. In my case, I have an opinion from my own IRB that what data editors do is not "research" (we audit, but do no new research), therefore does not qualify as "human subjects **research**" under the Common Rule that governs US IRBs. 

## Solution

It turns out that at least the GSS actually has thought this through.[^jeremy]

> In order to support the important work of reproducibility in academic journals, the GSS has an alternate process to facilitate journals getting temporary access to GSS sensitive data to replicate analyses ahead of publication. We do so through a data use agreement (DUA) that requires no fee [and no separate IRB approval].[^email]

While I still need to conduct the analysis within a secure environment (I will probably use Cornell's [Regulated Research Environment](https://socialsciences.cornell.edu/computing-and-data/regulated-research-environment)), and my university will still need to sign a Data Use Agreement, this is terrific support for reproducibility.

## More generally

More generally, of course, the editorial privilege that I and others in this situation enjoy allows for faster and credible verification. More importantly, though, is that there is a process for others to get access to the same data, albeit at a price. The mechanism is in place to ensure respondent confidentiality, as promised by the folks who conduct the survey, and is manageable by most researchers, though for some, $1500 may be a barrier. 



[^gss]: The GSS run by NORC is the US variant. There are several other surveys called "GSS" in other countries. For instance, Statistics Canada runs a "[General Social Survey](https://www150.statcan.gc.ca/n1/en/catalogue/89F0115X)" as well.

[^jeremy]: It may help that one of the big proponents of reproducibility in sociology and overall, [Jeremy Freese](https://sociology.stanford.edu/people/jeremy-freese), is a Principal Investigator of the GSS.

[^email]: Email from GSS staff to me, 2025-02-11. My addition in square brackets, as implicit in the process.