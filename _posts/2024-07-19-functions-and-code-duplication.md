---
title:  "On the use and reuse of within-project code"
date: 2024-07-19
mastodon: 
twitter:
bluesky: 
tags:
  - data editor tips
  - replication packages
  - code
  - function libraries
---

We often see researchers handle variants of their analysis by copying and pasting code, or by copying code files into separate directories, and making only minimal modifications. Some folks do this for robustness checks - same data, different analysis method, or a variant of the dependent variable - others for simulation of various scenarios - an economy without banks, an economy with credit-constrained banks, an economy with unconstrained banks. I won't point to particular examples, to protect the (somewhat) innocent, but this is not a good idea.

<!-- more -->

It introduces lots of failure points - not necessarily in the final package, but in the development process. 

## The example

Consider that you are halfway through your project. You have a base model, and three variants thereof. Each of which is the base model, copied into three different directories, with minimal modifications in the code. For sake of clarity, and with no loss of generality intended:

```
code/
    base-model/
            base-model.m
    robustness-check-1/
            base-model.m
    robustness-check-2/
            base-model.m
    robustness-check-3/
            base-model.m
```

where a `diff` between `base-model.m` and `robustness-check-1/base-model.m` would show only a few lines changed:

```diff
diff code/base-model/base-model.m code/robustness-check-1/base-model.m
13073c13073
< a=1;
---
> a=2;
```

> Note: the change would appear to be in line 13073, which is awfully subtle... this is inspired by real-life examples!

## The problem

Now imagine that your thesis advisor, or a reviewer, identifies a key problem in the implemented algorithm. You fix it in `base-model.m`, but now need to fix it in all the other modified copies too. Will there be any typos when you implement the patch? What if there are not three robustness checks, but 30? Or 300 different parameterizations of a simulation?

The techy programmer might decide to do this with `patch` in conjunction with `git`, but that already counts as advanced functionality (I probably lost a lot of readers with the first part of that sentence...)


```bash
# create a patch from the updates to the base model
git diff d362f6..3bd22 > patch.diff
# apply the patch to the robustness check
patch code/robustness-check-1/base-model.m < patch.diff
```

but that is not a robust solution that scales to the 30 or 300 robustness checks.

## A possible solution

The core solution is to apply elementary best programming practices: **write functions**.[^functions]

[^functions]: See for instance <https://medium.com/@josueparra2892/20-best-programming-practices-407df688b96e>, but this will be repeated many times. I was personally influenced by reading the (very accessible, but 900 pages!) "[Code Complete](https://bookshop.org/p/books/code-complete-steve-mcconnell/12551815?ean=9780735619678)" by Steve McConnell. Desirable internal design characteristics include "minimal complexity" (KISS), "ease of maintenance", and "reusability"

So should one go about the above problem? My rule of thumb is: 

- Copy code once, fine, don't do it again. 
- Copy it twice, stop, and create a function.
- Copy it three times: don't even go there!


Assuming that you are using MATLAB (where we seem to see this often), you should treat the core model code as a "function" (even if you do not explicitly program it that way), and then call that "function" multiple times. In a nutshell:

```
code/
    core-simulation/
            parametrized-simulation.m
    base-model.m
    robustness-check-1.m
    robustness-check-2.m
    robustness-check-3.m
```

where

```matlab
% base-model.m

% We set the base model to have the following parameters,
% as per Section 2 of the paper:
a=1;
b=2;
c=3;

% We then call the core simulation code
parametrized-simulation
```

will call the code in "parametrized-simulation.m" with parameters `a,b,c` already set. The simulation itself assumes those parameters are set.[^proper-function]

[^proper-function]: In a proper function, you would pass the parameters as arguments, and validate that they are the right ones, etc.: `core-model(a,b,c)`. Read the programming language specific manual on how to properly write functions: [Stata](https://www.stata.com/manuals/u17.pdf), [R via Hadley](https://adv-r.hadley.nz/functions.html#functions), [MATLAB](https://www.mathworks.com/help/matlab/ref/function.html), etc.

The robustness checks might then have 

```matlab
% robustness-check-1.m

% We set the model to have the following parameters,
% as per Section 3 of the paper:

a=2; % This differs from the base model
b=2;
c=3;

% We then call the core simulation code
parametrized-simulation
```

or go through a loop of multiple values:

```matlab
% robustness-check-2.m


% We set the model to have the following parameters,
% as per Section 4 of the paper:

b=3;
c=4;

% We now explore the space of a within this context.
for a = 1:10
    parametrized-simulation
end

% Summarize results from exploration

summarize-results

```


## Other languages

Is that a MATLAB-specific problem? No. We see similar issues in Stata, R, Python, and other languages. The core solution is the same: write functions, and call them multiple times, instead of copying code around, and hard-coding parameters. 

## Other situations

The above example had continuous (well, kind of) parameter spaces. What if they are discontinuous? You can still loop over a whole set of specifications by storing them in a file - yes, an Excel file is fine! - and reading them in (in MATLAB, [`readtable`](https://www.mathworks.com/help/matlab/import_export/ways-to-import-spreadsheets.html)). For example,

```matlab
% Read the Excel spreadsheet
[num, txt, raw] = xlsread('your_spreadsheet.xlsx');

% Get the number of rows in the data
[numRows, ~] = size(raw);

% Loop over each row, starting from the second row (assuming first row is header)
for i = 2:numRows
    % Extract values from columns A, B, and C
    a = raw{i, 1};  % Column A
    b = raw{i, 2};  % Column B
    c = raw{i, 3};  % Column C
    
    % Call the function something() with the extracted values
    result = something(a, b, c);
    
    % You can do something with the result here if needed
    % For example, store it in an array or print it
    disp(['Result for row ', num2str(i), ': ', num2str(result)]);
end
```
(straight from [Claude AI](https://claude.ai/))


## Summarizing it and creating tables

Of course, you now also have  to properly capture all those results, store them, and be able to summarize them, and create tables from them. That's another story.
