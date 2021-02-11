---
title:  "Reproducible GIS"
layout: single-withtoc
date: 2021-02-10
tags:
  - FAQ
  - Twitter
  - GIS
---

A note on reproducible GIS by economists: it's mostly absent. Here are some tips.

<!-- more -->

## Reproducibility and GIS

Reproducibility means that the inputs and methods can be repeated by a (somewhat) knowledgeable person. For GIS, that *might* (should) mean code, but it *definitely* means at least SOME instructions. Even if they are manual....

Maps are data. While your typical Stata/Matlab/R/Julia graph is data projected into Cartesian coordinates, maps are data projected into geographic coordinates. So at a minimum, we need to know what the inputs to the map are, same as we need to know inputs to graphs.

So "data + code" + "`graph twoway scatter x y`" -&gt; 📈📉, 

![](https://pbs.twimg.com/media/Et31MkpXcAQg8Nw.png)

and "data + code" + "`maptile x, geo(state)`" -&gt; 🗺️. Or "data + code" + "*instructions(ArcGIS)*" -&gt; 🗺️. 

![](https://pbs.twimg.com/media/Et3048TXcAIx20f.png)	

Note that for a map, "data" includes shapefiles (including provenance of the shapefile) 

##  Checklist for reproducible maps

- ✅ data (+ provenance)
- ✅ code (manipulates data)
- ✅ shapefile (provides coordinates)
- ✅ code (preferred) or instructions (sufficient)

## Resources

A few tentative resources are collected at <https://social-science-data-editors.github.io/guidance/guidance-reproducible-gis-analysis.html> (please suggest improvements!), with some other links below:

### Stata

[Stata FAQ on maps](https://www.stata.com/support/faqs/graphics/spmap-and-maps/), including the [spmap package](https://ideas.repec.org/c/boc/bocode/s456812.html) and the [maptile package](https://michaelstepner.com/maptile/) by [@michaelstepner](https://twitter.com/michaelstepner)

### R

The core [sf library](https://r-spatial.github.io/sf/), [reproducible GIS practices in R](https://staff.washington.edu/phurvitz/r_gis/)  and interactions with GIS software (and integrated as a dependency into many great packages)
### Python

[GeoPandas](https://geopandas.org/) and others

### ArcGIS

ArcGIS can also be scripted (via python) and now [integrates Jupyter-like notebooks](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/pro-notebooks.htm)

### QGIS

Staying #opensource: [QGIS](https://www.qgis.org/) has "[Graphical Modeler](https://docs.qgis.org/3.10/en/docs/user_manual/processing/modeler.html)", and look for tutorials on "[Automating GIS Workflows](https://courses.spatialthoughts.com/)" 

## Summary

Please try to create scripted maps, but always describe what data you are mapping, and where you got the shapefiles from (note: copyrights might apply, permissions might need to be obtained!)

## PS

And for those exceptions from scripting: a 2-3 sentence description of what you did would be sufficient. And for the unscripted ArcGIS which you did before you learned how to script stuff: a 4-5 sentence description may be sufficient as well.

## Follow the conversation

Slightly modified from 
<https://twitter.com/AeaData/status/1359516297990701057>