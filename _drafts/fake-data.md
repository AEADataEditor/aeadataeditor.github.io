# I'd like to post a replication package for a paper ... uses proprietary data ... favorite packages that will "simulate" data to step in?

- [synthpop](https://cran.r-project.org/package=synthpop) ([paper](https://doi.org/10.18637/jss.v074.i11)) @SCADR_data - used frequently in statistics, well-maintained
  - (untested) Python version https://github.com/hazy/synthpop @hazy_ai
- [fakeR](https://cran.r-project.org/package=fakeR)
- [fabricatr](https://cran.r-project.org/package=fabricatr) (see also [DeclareDesign](https://declaredesign.org/r/fabricatr/)) "designs" data
- [corr2data](https://www.stata.com/manuals/dcorr2data.pdf) to create a dataset with specified correlation structure
```
use https://www.stata-press.com/data/r16/auto
qui sum 
local obs `r(N)'
regress weight length trunk
matrix accum R = weight length trunk, nocons dev means(M)
matrix V = corr(R)
corr2data x y z, n(`obs') cov(R) means(M)
regress x y z
```
- [Synthetic Data Vault](https://github.com/sdv-dev/SDV) in Python

