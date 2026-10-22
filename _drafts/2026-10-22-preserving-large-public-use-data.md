# Case 1

In total, the data for the project are approximately 115 GB before compression.

## Me 

That being said, for big auxiliary data that are not your own to start with, I usually suggest creating a secondary archive with just those data, see https://aeadataeditor.github.io/aea-de-guidance/preparing-for-data-deposit.html#creating-a-separate-data-deposit. Usually, Zenodo is a good place to put those data, see the examples (including some weather data) on the Zenodo community. 

All code and the main README should still be in the openICPSR primary deposit. You reference the (future) DOI of the secondary deposit in your README, and provide instructions (or code) to replicators on how to combine the two pieces again. 

## Author

Our project uses multiple large data sources that create file size and file count issues, including pollution data, wildfire smoke data, and weather data. Given the size and number of files across these sources, it sounds like creating a secondary Zenodo deposit for the data may be the cleanest approach. We would then keep all code and the main README in openICPSR, reference the Zenodo DOI in the README, and provide instructions for combining the Zenodo data with the openICPSR files in the README.

## Me

here's R code that iterates over a certain extension (Rds files, in this case, could be a ZIP file) and downloads them all. The key is the JSON file that the Zenodo API coughs up.

 

https://github.com/larsvilhuber/aej-applied-replications-public/blob/master/programs/01_download_replication_data.R#L1-L29

 

For Dataverse, there is an R package https://cran.r-project.org/web/packages/dataverse/index.html

 

In Python, you could import things from the https://github.com/dvolgyes/zenodo_get package. For dataverse, there is https://pydataverse.readthedocs.io/en/latest/.

 

We actually use our own Python  tools within the Replication Lab, but they can easily be integrated into other things:

 

https://github.com/AEADataEditor/replication-template/blob/master/tools/download_dv.py

https://github.com/AEADataEditor/replication-template/blob/master/tools/download_zenodo_public.py

 

but you can also test prior to publication

 

https://github.com/AEADataEditor/replication-template/blob/master/tools/download_zenodo_draft.py

# Case 2

## author

| Source | Size |
|---|---:|
| DIME (23 files) | 132.220 GB |
| Voter data (6 files) | 62.991 GB |
| Data source 3 | 5.390 GB |
| Data source 4 | 2.437 GB |
| Data source 5 | 1.353 GB |

## Me

### so a few quick thoughts:

- the obvious candidate to "offload" is [DIME](https://data.stanford.edu/dime) data - but they store their files on Dropbox, so that's not acceptable from a preservation perspective. I will come back to that below.
-  the next candidate are the voter records: they have a legitimate novelty, are not preserved elsewhere. One could "offload" them.


### What I mean by offload is

-   create a Zenodo deposit for JUST that data. That gives you DOI and preservation. Makes Data Editors' happy.
-  then include in your code a fragment to download that data from Zenodo, programmatically.

You could also include such a Zenodo archive for the other data sources data. For each, look at a small number of files, either natively, if there are a few but large files, or logically if they can be collected by sub-data source, month/year as a ZIP file. 

Each data source would be its own deposit - so that the metadata can be accurate and informative.

Some guidance is here: https://aeadataeditor.github.io/aea-de-guidance/guidelines-other-repositories

Some very good examples of the kind are https://doi.org/10.5281/zenodo.17676746 or https://doi.org/10.5281/zenodo.10408818 , which are there for the exact same reason that you are running into. 


### Why not DIME

The reason I'm not sure DIME is a good candidate for that is that they already have a sort of research-oriented archive - they just don't do it right. But creating a Zenodo copy would be somewhat treading on their feet. That does not apply to the NC voter data.

### Sample code in R

https://github.com/larsvilhuber/aej-applied-replications-public/blob/master/programs/01_download_replication_data.R

You can include that in your "00_unzip.R". Technically, you don't need to unzip them, you can iterate over a JSON manifest that Zenodo provides, and download individual files. But you already have the unzip code.



