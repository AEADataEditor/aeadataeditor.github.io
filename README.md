See aeadataeditor.github.io


## Images for talks

Talks in `_talks/` can use the theme's standard `header` front matter. No layout changes are needed:

```yaml
header:
  image: /images/my-talk-hero.jpg        # shown above the talk (page hero)
  image_description: "Alt text"          # optional, defaults to the title
  caption: "Photo credit"                # optional
  teaser: /images/my-talk-thumbnail.jpg  # thumbnail in grid archives
```

Put the image files in `images/`. The lars.vilhuber.com mirror copies them and maps `header.image` and `header.teaser` to its own `hero` and `thumbnail` fields.
