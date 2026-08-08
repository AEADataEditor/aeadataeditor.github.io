---
title: "The Same Code, a Different Answer: Stata Convergence Across Platforms"
categories: dataeditor
date: 2026-07-24
mastodon:
bluesky: https://bsky.app/profile/aeadata.bsky.social/post/3mreaq7ll4k2v
tags:
  - data editor tips
  - reproducibility
  - replication packages
  - Stata
  - Code
---

A recent replication came to a halt on a first-stage regression. The authors' code ran fine on the authors' computer. It failed on ours. Same code, same data, same software package — different answer. Here is what it took to find out why, and some thoughts (lessons?).

<!-- more -->

## First: do not hide the output!

The immediate problem was not the regression itself. It was that we could not see the regression output, and thus the error.

The offending line was, in essence:

```stata
quietly do regression_55.do
```

`quietly` suppressed exactly the output that would have explained the failure. The code simply stopped completing, with nothing on screen to say why. Diagnosing it meant unwinding the suppression before we could even start on the econometrics.

## It's not exactly the code

After some back and forth, the authors provided (credible) evidence that the code did run on their system. So we reduced their several hundred lines to a minimal working example of about two dozen, and sent it to Stata support, who responded promptly!

## It is not the operating system

Our first hypothesis was the obvious one. We had run on Windows Server (StataNow 19) and Linux (StataNow 19); the authors had run on Windows Enterprise (Stata 19). Operating system, then. Or version.

That was not enough. Stata's technical staff ran the example across their internal collection of hardware and software, and reported:

> convergence on Windows box running Stata 18 MP32 and Stata 19 MP8, but `set processors` to any number less than 8 cause not converging….Mac mini Apple M2 pro/ S19MP16 NOT…Linux/S19MP16, S19SE, S18MP2, S17MP2, S16MP2, NOT converged for any number of processors

One should take particular note of this fact: On the _same_ Windows machine, with the _same_ Stata, the model converges or does not converge depending on how many processors you let it use. The authors, it turned out, had run Stata 19 MP10 — one of the **few** combinations in which the model converged at all.

The determining variable was not the operating system, and not the Stata version. It was the number of processors.

## What was actually wrong

Stata's statisticians examined the code and the data, and the answer is that it's not "a bug." Mostly. Quoting from their reply:

> Stata, like any other software package, has fixed criteria to convergence declaration. It's not foolproof. There will be always cases where convergence will be "declared" and it shouldn't.

> This is why we insist on the importance of examining the output and make sure that it makes sense. I looked at the output it shows several problems.

Three symptoms, all visible in the output that `quietly` had been hiding:

> 1) there are missing standard errors. ... an indication that there is a problem with the Hessian (either it has missing values, or for some reason it can't be inverted), so you can't trust your results.
>
> 2) There are huge confidence intervals,... coefficients are poorly identified."
> 3) The problem is the matrix of second derivatives, that
is non invertible. In the cases where we get 'convergence',
we get huge or missing standard errors, meaning that it can't really be inverted."

The mechanism is worth spelling out, because it explains the platform sensitivity. Stata declares convergence when the scaled gradient satisfies `g*inv(H)*g' < nrtolerance()`, with a default of `1e-5`. That criterion _requires inverting the Hessian_. When the Hessian is numerically singular, the criterion cannot be evaluated in a meaningful way — and whether it happens to be evaluated as satisfied comes down to floating-point details that differ with the number of processors, the BLAS in use, and the order in which sums are accumulated (my words, not theirs).

They continued.

> On Mac, I don't get convergence by default, but I get it if I disable the `nrtolerance`, meaning that this is the tolerance that the model fails to meet.

> If I write `shownrtol` option instead, I will see that (the "minimum" of all tolerances) is 0, but exact zero means that something can't be computed, in this case the nrtol (which requires inverting the Hessian).


So the model was not identified on any platform. On most configurations Stata correctly refused to declare victory. On a few — including the authors' — it declared convergence it should not have.

## Why this matters beyond one paper

Two observations:

This was one regression out of many dozens in the paper. The rest converged. _How well_ they converged we did not investigate — that remains for the authors, and for future replicators.

More importantly, consider what would have happened had our replication machines been configured slightly differently. **We only detect some of these issues.** If we happen to land on the same sweet-spot hardware and software configuration as the authors, we never see a discrepancy, and the paper passes. The non-identification is still there; we just never trip over it. And it is genuinely hard for authors to diagnose on their own, unless they happen to maintain the same museum of hardware and software versions that Stata does.


## Lessons

I will not pronounce on the econometrics — that is the authors' problem, and for future replicators (who have a reproducible package to work with!) But two things are general:

**Know your regressions.** Missing standard errors and implausibly wide confidence intervals are not cosmetic blemishes to be tidied up in the table. They are the software telling you the model is not identified. Look at the output.

**Do not suppress your output.** In Stata, that means thinking twice about `quietly`. The equivalents elsewhere are just as effective at hiding a problem: `source()` without `echo=TRUE` in R, or a stray `;` in MATLAB. Silence during a long run feels tidy. It is not tidy — it is a diagnostic you have thrown away, and you will want it back at precisely the moment it is gone.

Thanks to [@stata.bsky.social](https://bsky.app/profile/stata.bsky.social), whose helpdesk responded quickly and then very thoroughly, and did a fantastic job diagnosing this.

Good night, and good computing!

---

_This post is adapted from [a thread](https://bsky.app/profile/aeadata.bsky.social/post/3mreaq7ll4k2v) originally posted on Bluesky._
