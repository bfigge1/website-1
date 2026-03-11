# Blog Visualization Handoff

## Status
- Leaflet map built and working (`content/post/cpc-expansion-carolinas/leaflet_map.html`)
- CPC/clinic markers render correctly on the Leaflet tile map
- Blog post embeds map via `{{< include-html "leaflet_map.html" >}}` shortcode
- Three blog posts written and live (expansion maps, age heterogeneity, IV methodology)
- Placeholder PNGs in place for coefficient plot, event study, Monte Carlo figures

## Known Issue
CPC and clinic lat/lng coordinates don't align well with county shapefiles. The point locations are correct on the Leaflet tile basemap but would be misplaced if overlaid on a shapefile-based choropleth. This needs investigation before adding the abortion rate choropleth layer.

## What's Next
1. **Fix coordinate alignment.** The geo_mapping_clinic_cpc.dta lat/lng may use a different CRS than the county shapefiles. Check projections (likely NAD83 vs WGS84, or geocoding quirks). Work in the Clinics_CPC research project folder to diagnose.
2. **Add county choropleth.** Once alignment is fixed, overlay county-level abortion rates as a choropleth behind the point markers. Need the county-year abortion rate data file for this.
3. **Plotly coefficient plot.** Convert the age-group 2SLS coefficient plot to interactive Plotly (hover for exact estimates/CIs). Data is hardcoded approximations in `scripts/export_figures_for_blog.R`; swap in actual estimates.
4. **Plotly event study.** Convert event study to Plotly with dropdown to toggle age groups. Source PDF is in uploads.
5. **Plotly Monte Carlo.** Convert the 3x3 kernel density grid to Plotly with toggle buttons per DGP scenario.

## File Locations
- Website repo: `/Users/lepus/Documents/GitHub/website-1/`
- Research project: Clinics_CPC folder (user will specify path)
- Data file used: `geo_mapping_clinic_cpc.dta` (286 CPCs, 46 clinics, with lat/lng and open/close years)
- Map builder script: `scripts/build_leaflet_map.py`
- R figure script: `scripts/export_figures_for_blog.R`
- Python featured image generator: `scripts/generate_featured_images.py`
- Hugo shortcode: `layouts/shortcodes/include-html.html`

## Config Changes Made
- Fixed Twitter icon pack (ai -> fab) in `content/authors/admin/_index.md`
- Uncommented CV icon link
- Linked JMP PDF (`url_pdf: 'uploads/figge_jmp.pdf'`)
- Enabled posts widget, renamed to "Writing", added to nav menu
- Added featured images to JMP publication and all three blog posts
