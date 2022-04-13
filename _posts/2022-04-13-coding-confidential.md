---
title:  "Some remarks on coding when data are confidential"
date: 2022-04-13
tags:
  - confidential data
  - complex projects
---

Back in the fall, I made a few notes regarding how to prepare replication packages when data are confidential ([here](https://aeadataeditor.github.io/posts/2021-11-08-replication-pkg-confidential)). What I did not address, and what comes up regularly, is how to **write code** when some code and/or data are confidential.


<!-- more -->

## What is confidential code, you say? 

- In the United States, some variables on IRS databases are considered super-top-secret. So you can't name that-variable-that-you-filled-out-on-your-Form-1040 in your analysis code of same data. (They are often referred to in jargon as "Title 26 variables"). Not sure why that continues to be perceived as a problem, but until the law changes, that's one possible constraint.
- Your code contains the random seed you used to anonymize the sensitive identifiers. This might allow to reverse-engineer the anonymization, and is not a good idea to publish.
- You used a look-up table hard-coded in your Stata code to anonymize the sensitive identifiers (`replace anoncounty=1 if county="Tompkins, NY"`). A really bad idea, but yes, you probably want to hide that.
- Your IT specialist or misguided disclosure officer thinks publishing the exact path to your copy of the confidential 2010 Census data, e.g., "/data/census/2010", is a security risk and refuses to let that code through.
- You have adhered to disclosure rules, but for some reason, the precise minimum cell size is a confidential parameter.

So whether reasonable or not, this is an issue. How do you do that, without messing up the code, or spending hours redacting your code?

## Example 

This will serve as an example throughout this post. I'm focusing on Stata, because so many economists use Stata, but none of this is specific to Stata, and the solutions for R, Python, Julia, Matlab, etc. are all quite similar. Assume that variables `q2f` and `q3e` are considered confidential by some rule, and that the minimum cell size `10` is also confidential.

```{stata}
set seed 12345
use q2f q3e county using "/data/economic/cmf2012/extract.dta", clear
gen logprofit = log(q2f)
by county: collapse (count)  n=q3e (mean) logprofit
drop if n<10
graph twoway n logprofit
```


## Do not do this

A bad example, because literally making more work for you and for future replicators, is to manually redact the confidential information with text that is not legitimate code:

```{stata}
set seed NNNNN
use <removed vars> county using "<removed path>", clear
gen logprofit = log(XXXX)
by county: collapse (count)  n=XXXX (mean) logprofit
drop if n<XXXX
graph twoway n logprofit
```

The redacted program above will no longer run, and will be very tedious to un-redact if a subsequent replicator obtains legitimate access to the confidential data.

## Better

Simply replacing the confidential data with replacement that are valid placeholders in the programming language of your choice is already better. Here's the confidential version of the file:

```{stata}
//============ confidential parameters =============
global confseed    12345
global confpath    "/data/economic/cmf2012"
global confprofit  q2f
global confemploy  q3e
global confmincell 10
//============ end confidential parameters =========
set seed $confseed
use $confprofit county using "${confpath}/extract.dta", clear
gen logprofit = log($confprofit)
by county: collapse (count)  n=$confemploy (mean) logprofit
drop if n<$confmincell
graph twoway n logprofit
```

and this would be the released file, part of the replication package:

```{stata}
//============ confidential parameters =============
global confseed    XXXX    // a number
global confpath    "XXXX"  // a path that will be communicated to you
global confprofit  XXX     // Variable name for profit T26
global confemploy  XXX     // Variable name for employment T26
global confmincell XXX     // a number
//============ end confidential parameters =========
set seed $confseed
use $confprofit county using "${confpath}/extract.dta", clear
gen logprofit = log($confprofit)
by county: collapse (count)  n=$confemploy (mean) logprofit
drop if n<$confmincell
graph twoway n logprofit
```

While the code won't run as-is, it is easy to un-redact, regardless of how many times you reference the confidential values, e.g., `q2f`, anywhere in the code.

## Best

Note that you have to re-run the entire code to obtain a modified graph, e.g., if you want to add some reference line, or change colors. But if the data presented in the graph is non-sensitive (i.e., disclosable), then the data underlying it is as well. Thus, and this is a more general approach, we can provide code that automatically detects if the confidential data is there, and only then will it run the data preparation part, but it will always run for the graphing ("analysis") part of the code. 

We also introduce the use of a separate file for all the confidential parameters, which may be more convenient, since now, no redaction is needed - the confidential file is simply dropped (but should be documented).

Main file `main.do`:

```{stata}
//============ confidential parameters =============
capture confirm file "include/confparms.do"
if _rc == 0 {
    // file exists
    include "include/confparms.do"
} else {
    di in red "No confidential parameters found"
}
//============ end confidential parameters =========

//============ non-confidential parameters =========
global safepath "releasable"
cap mkdir "$safepath"

//============ end parameters ======================

// ::::  Process only if confidential data is present 

capture confirm "${confpath}/extract.dta"
if _rc == 0 {
   set seed $confseed
   use $confprofit county using "${confpath}/extract.dta", clear
   gen logprofit = log($confprofit)
   by county: collapse (count)  n=$confemploy (mean) logprofit
   drop if n<$confmincell
   save "${safepath}/figure1.dta", replace
} else { di in red "Skipping processing of confidential data" }

//============ at this point, the data is releasable ======
// ::::  Process always 

use "${safepath}/figure1.dta", clear
graph twoway n logprofit
graph export "${safepath}/figure1.pdf", replace
```

Auxiliary file `include/confparms.do` (not released)

```{stata}
//============ confidential parameters =============
global confseed    12345
global confpath    "/data/economic/cmf2012"
global confprofit  q2f
global confemploy  q3e
global confmincell 10
//============ end confidential parameters =========
```

Auxiliary file `include/confparms_template.do` (this is released)

```{stata}
//============ confidential parameters =============
global confseed    XXXX    // a number
global confpath    "XXXX"  // a path that will be communicated to you
global confprofit  XXX     // Variable name for profit T26
global confemploy  XXX     // Variable name for employment T26
global confmincell XXX     // a number
//============ end confidential parameters =========
```

And after a successful run, the files `releasable/figure1.dta` and `releasable/figure1.pdf` are available, and can be reviewed and released.

Thus, the replication package would have:

```
main.do
README.md
include/confparms_template.do
releasable/figure1.dta
releasable/figure1.pdf
```

Voilà! The resulting non-confidential package will run to produce the analysis (`figure1.pdf`) based on the distributable, non-confidential analysis file (`analysis.dta`). It can also be very simply brought back into the confidential environment, where either the replicator creates a new `confparms.do`, or copies the confidential `confparms.do` from the original author into their own working area.

