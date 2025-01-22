# Data provenance descriptions

Data provenance and access modes should be detailed enough to understand what the associated mechanisms of access are, what the rights and access restrictions associated with the data are, and potentially any costs.

## Just good enough

### Example

> FRED tickers UNRATE, PCEPI, FEDFUNDS, and Romer
Romer Shock as updated by Johannes Wieland:
https://www.openicpsr.org/openicpsr/project/1357
41/version/V1/view

In the references:

> - Board of Governors of the Federal Reserve System (US), Federal Funds Effective
Rate [FEDFUNDS], retrieved from FRED, Federal Reserve Bank of St. Louis;
https://fred.stlouisfed.org/series/FEDFUNDS, December 10, 2024.
> - U.S. Bureau of Economic Analysis, Personal Consumption Expenditures: Chain-type
Price Index [PCEPI], retrieved from FRED, Federal Reserve Bank of St. Louis;
https://fred.stlouisfed.org/series/PCEPI, December 10, 2024.
> - U.S. Bureau of Labor Statistics, Unemployment Rate [UNRATE], retrieved from
FRED, Federal Reserve Bank of St. Louis;
https://fred.stlouisfed.org/series/UNRATE, December 10, 2024.
> Wieland, Johannes. Updated Romer-Romer Monetary Policy Shocks. Ann Arbor, MI:
Inter-university Consortium for Political and Social Research [distributor], 2021-03-
23. https://doi.org/10.3886/E135741V1

### Why

- The source of the data in each case is properly listed in the references, albeit not correctly cited in the usage description.
- No rights or license information is provided:
  - The FRED retrieved information is actually in the public domain (but FRED does not say that)
  - The Wieland files are under a CC-BY license, but requires a login in order to record agreement with those terms.
 
### Better

> FRED tickers UNRATE [3], PCEPI [2], FEDFUNDS [1], and Romer
Romer Shock as updated by Johannes Wieland [4]. The first three are in the public domain, the latter is CC-BY, login required to agree to terms.

In the references, use the numbered citation style instead of standard Chicago style to make the citations more succinct. Note that the citation style used in the README does not need to be the same as in the manuscript.

