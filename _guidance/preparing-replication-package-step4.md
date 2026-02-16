---
title: "Step 4: Displays"
toc: true
date: 2026-02-16
---

[◀ Back to Checklist](preparing-replication-package) | [Back to Details](preparing-replication-package-details) | [◀ Previous: Step 3](preparing-replication-package-step3)

Displays (figures and tables) should be written out to external files, and the authors' versions, as used in the manuscript, should be provided. In the prototypical replication package structure above, these files would be in the `results` directory.

> Reference: <https://larsvilhuber.github.io/self-checking-reproducibility/03-automatically_saving_figures.html> and <https://github.com/labordynamicsinstitute/replicability-training/wiki/How-to-output-tables-and-figures>

## Figures

- All figures can be written out to files. Journals like `pdf` and `eps` files, but `png` are convenient. You can output multiple formats.
- Whenever you have displayed a figure, also `export`it to a file. It's a simple command.

### Stata

```stata
// Example for PNG
graph export "$rootdir/results/figure1.png", replace width(1200) height(800)
// Example for PDF
graph export "$rootdir/results/figure1.pdf", replace
```

### R

```r
# Example for PNG if using standard R
png(filename = file.path(rootdir, "results", "figure1.png"), width = 1200, height = 800)
plot(x, y)  # your plotting code here
dev.off()
# Example if using ggplot2
ggsave(filename = file.path(rootdir, "results", "figure1.png"), plot = myplot, width = 12, height = 8, units = "in", dpi = 100)
```

### More complex figures

For more complex figures, it may be easier to simply write out the data underlying the figure to an Excel sheet, and create the figure there. See <https://github.com/labordynamicsinstitute/replicability-training/wiki/How-to-output-tables-and-figures#arbitrary-data-to-excel>  on how to write out the underlying data. **You would then include the Excel file that maps the data into a figure with your replication package.**


## Tables

Tables may be more complex. Simple tables can be written out using various tools:

### Stata

`esttab` or `outreg2`, also `putexcel`. For fancier stuff, treat tables as data, use `regsave` or `export excel` to manipulate.

### R

`xtable`, `stargazer`, others.

### More complex tables

For more complex tables, it may be easier to simply write out entire matrices, or individual numbers, to an Excel sheet, and compose the table there. See <https://github.com/labordynamicsinstitute/replicability-training/wiki/How-to-output-tables-and-figures#examples> for an example, especially if you have already been compiling your tables in Excel. **You would then include the Excel file that maps the data into your preferred table layout with your replication package.**

---

[![Next: Step 5](/images/next-button-step5.png)](preparing-replication-package-step5)
