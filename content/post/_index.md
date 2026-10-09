---
# Section taken offline: do not render or list posts.
_build:
  render: never
  list: never
cascade:
  _build:
    render: never
    list: never
title: Posts
cms_exclude: true

# View.
#   1 = List
#   2 = Compact
#   3 = Card
view: 2

# Optional header image (relative to `static/media/` folder).
header:
  caption: ""
  image: ""
---
