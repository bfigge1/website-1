"""
Build interactive Leaflet map of CPC and abortion provider expansion
in North and South Carolina, 1970-2020.

Outputs a self-contained HTML file for embedding in a Hugo blog post.

Usage:
    python scripts/build_leaflet_map.py

Requires: pandas, pyreadstat, folium
"""

import pandas as pd
import json
from pathlib import Path

# === CONFIG ===
DATA_PATH = Path(__file__).parent.parent / "data" / "geo_mapping_clinic_cpc.dta"
# Fallback to uploads path if data dir doesn't exist
if not DATA_PATH.exists():
    DATA_PATH = Path("/sessions/amazing-bold-pasteur/mnt/uploads/geo_mapping_clinic_cpc.dta")

OUTPUT_PATH = Path(__file__).parent.parent / "content" / "post" / "cpc-expansion-carolinas" / "leaflet_map.html"

# Bounding box for NC/SC (filter out geocoding errors)
LAT_MIN, LAT_MAX = 32.0, 36.6
LNG_MIN, LNG_MAX = -84.5, -75.4

# Time periods matching the paper's maps
PERIODS = {
    "Early 1990s (1990-1995)": (1990, 1995),
    "Early 2000s (2000-2005)": (2000, 2005),
    "Early 2010s (2010-2015)": (2010, 2015),
    "Late 2010s (2015-2020)": (2015, 2020),
}

# === LOAD DATA ===
df = pd.read_stata(str(DATA_PATH))

# --- CPCs ---
cpcs = df[df["cpc_lat"].notna()].copy()
cpcs = cpcs[
    (cpcs["cpc_lat"] >= LAT_MIN) & (cpcs["cpc_lat"] <= LAT_MAX) &
    (cpcs["cpc_lng"] >= LNG_MIN) & (cpcs["cpc_lng"] <= LNG_MAX)
].copy()

# --- Clinics (abortion providers) ---
clinics = df[df["clinic"] == 1].copy()
clinics = clinics[
    (clinics["clinic_lat"] >= LAT_MIN) & (clinics["clinic_lat"] <= LAT_MAX) &
    (clinics["clinic_lng"] >= LNG_MIN) & (clinics["clinic_lng"] <= LNG_MAX)
].copy()


def is_open(open_yr, close_yr, period_start, period_end):
    """Check if a facility was open during any part of the period."""
    if pd.isna(open_yr):
        return False
    if open_yr > period_end:
        return False
    if pd.notna(close_yr) and close_yr < period_start:
        return False
    return True


# === BUILD HTML ===
# We'll build a custom HTML file with Leaflet + a time slider,
# rather than using folium, for more control over the slider UX.

# Prepare data as JSON for embedding
cpc_data = []
for _, row in cpcs.iterrows():
    entry = {
        "lat": round(row["cpc_lat"], 4),
        "lng": round(row["cpc_lng"], 4),
        "name": str(row.get("name_location", "CPC")),
        "county": str(row.get("county_name_location", "")),
        "state": str(row.get("state_location", "")),
        "open": int(row["opening_year_location"]) if pd.notna(row["opening_year_location"]) else None,
        "close": int(row["closing_year_location"]) if pd.notna(row["closing_year_location"]) else None,
    }
    cpc_data.append(entry)

clinic_data = []
for _, row in clinics.iterrows():
    entry = {
        "lat": round(row["clinic_lat"], 4),
        "lng": round(row["clinic_lng"], 4),
        "name": str(row.get("city_clinic", "Clinic")),
        "county": str(row.get("county_name_clinic", "")),
        "state": str(row.get("state_clinic", "")),
        "open": int(row["opening_year_clinic"]) if pd.notna(row["opening_year_clinic"]) else None,
        "close": int(row["closing_year_clinic"]) if pd.notna(row["closing_year_clinic"]) else None,
    }
    clinic_data.append(entry)

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CPC Expansion in the Carolinas</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #fafafa; }}
  #map {{ width: 100%; height: 520px; border-radius: 8px; border: 1px solid #e0e0e0; }}
  .controls {{
    padding: 16px 0;
    max-width: 100%;
  }}
  .slider-container {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 12px;
  }}
  .slider-container label {{
    font-size: 14px;
    font-weight: 600;
    color: #333;
    min-width: 50px;
  }}
  #yearSlider {{
    flex: 1;
    height: 6px;
    -webkit-appearance: none;
    appearance: none;
    background: #ddd;
    border-radius: 3px;
    outline: none;
  }}
  #yearSlider::-webkit-slider-thumb {{
    -webkit-appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #2b4c7e;
    cursor: pointer;
    border: 2px solid white;
    box-shadow: 0 1px 4px rgba(0,0,0,0.3);
  }}
  #yearDisplay {{
    font-size: 28px;
    font-weight: 700;
    color: #2b4c7e;
    min-width: 60px;
    text-align: right;
    font-variant-numeric: tabular-nums;
  }}
  .counts {{
    display: flex;
    gap: 24px;
    font-size: 14px;
    color: #555;
  }}
  .counts .cpc-count {{
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .counts .clinic-count {{
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .dot-cpc {{
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: rgba(192, 112, 112, 0.8);
    border: 1px solid rgba(192, 112, 112, 1);
  }}
  .dot-clinic {{
    display: inline-block;
    width: 0;
    height: 0;
    border-left: 7px solid transparent;
    border-right: 7px solid transparent;
    border-bottom: 12px solid rgba(43, 76, 126, 0.9);
  }}
  .play-btn {{
    background: #2b4c7e;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
  }}
  .play-btn:hover {{ background: #1d3557; }}
  .play-btn.playing {{ background: #8b2323; }}
  .ratio-bar {{
    margin-top: 8px;
    font-size: 13px;
    color: #666;
  }}
  .ratio-bar .bar-bg {{
    width: 100%;
    height: 8px;
    background: #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
    margin-top: 4px;
  }}
  .ratio-bar .bar-fill {{
    height: 100%;
    border-radius: 4px;
    transition: width 0.3s ease;
  }}
</style>
</head>
<body>

<div class="controls">
  <div class="slider-container">
    <button class="play-btn" id="playBtn" onclick="togglePlay()">&#9654; Play</button>
    <input type="range" id="yearSlider" min="1975" max="2020" value="1990" step="1">
    <span id="yearDisplay">1990</span>
  </div>
  <div class="counts">
    <div class="cpc-count"><span class="dot-cpc"></span> CPCs open: <strong id="cpcCount">0</strong></div>
    <div class="clinic-count"><span class="dot-clinic"></span> Abortion providers: <strong id="clinicCount">0</strong></div>
  </div>
  <div class="ratio-bar">
    <span id="ratioText">Ratio: 0 CPCs per provider</span>
    <div class="bar-bg">
      <div class="bar-fill" id="ratioBar" style="width: 0%; background: linear-gradient(90deg, rgba(43,76,126,0.7), rgba(192,112,112,0.8));"></div>
    </div>
  </div>
</div>

<div id="map"></div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
const cpcData = {json.dumps(cpc_data)};
const clinicData = {json.dumps(clinic_data)};

// Initialize map centered on NC/SC
const map = L.map('map', {{
  zoomControl: true,
  scrollWheelZoom: true,
}}).setView([34.8, -80.0], 7);

L.tileLayer('https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
  attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
  subdomains: 'abcd',
  maxZoom: 19
}}).addTo(map);

// Layer groups
let cpcMarkers = L.layerGroup().addTo(map);
let clinicMarkers = L.layerGroup().addTo(map);

function isOpen(item, year) {{
  if (item.open === null || item.open > year) return false;
  if (item.close !== null && item.close < year) return false;
  return true;
}}

function updateMap(year) {{
  cpcMarkers.clearLayers();
  clinicMarkers.clearLayers();

  let cpcCount = 0;
  let clinicCount = 0;

  // Add CPCs
  cpcData.forEach(d => {{
    if (isOpen(d, year)) {{
      cpcCount++;
      const marker = L.circleMarker([d.lat, d.lng], {{
        radius: 6,
        fillColor: 'rgba(192, 112, 112, 0.75)',
        color: 'rgba(160, 80, 80, 0.9)',
        weight: 1,
        fillOpacity: 0.75,
      }});
      marker.bindPopup(
        '<strong>' + d.name + '</strong><br>' +
        d.county + ', ' + d.state + '<br>' +
        'Opened: ' + d.open + (d.close ? '<br>Closed: ' + d.close : '')
      );
      cpcMarkers.addLayer(marker);
    }}
  }});

  // Add clinics (abortion providers) - larger, triangular appearance via DivIcon
  clinicData.forEach(d => {{
    if (isOpen(d, year)) {{
      clinicCount++;
      const marker = L.marker([d.lat, d.lng], {{
        icon: L.divIcon({{
          className: '',
          html: '<div style="width:0;height:0;border-left:8px solid transparent;border-right:8px solid transparent;border-bottom:14px solid rgba(43,76,126,0.9);filter:drop-shadow(0 1px 1px rgba(0,0,0,0.3));"></div>',
          iconSize: [16, 14],
          iconAnchor: [8, 14],
        }})
      }});
      marker.bindPopup(
        '<strong>Abortion Provider</strong><br>' +
        d.county + ', ' + d.state + '<br>' +
        d.name + '<br>' +
        'Opened: ' + d.open + (d.close ? '<br>Closed: ' + d.close : '')
      );
      clinicMarkers.addLayer(marker);
    }}
  }});

  document.getElementById('cpcCount').textContent = cpcCount;
  document.getElementById('clinicCount').textContent = clinicCount;

  // Update ratio bar
  const ratio = clinicCount > 0 ? (cpcCount / clinicCount).toFixed(1) : '—';
  document.getElementById('ratioText').textContent =
    'Ratio: ' + ratio + ' CPCs per abortion provider';
  const barPct = Math.min((cpcCount / Math.max(cpcCount + clinicCount, 1)) * 100, 100);
  document.getElementById('ratioBar').style.width = barPct + '%';
}}

// Slider
const slider = document.getElementById('yearSlider');
const display = document.getElementById('yearDisplay');

slider.addEventListener('input', function() {{
  const year = parseInt(this.value);
  display.textContent = year;
  updateMap(year);
}});

// Play/pause animation
let playing = false;
let playInterval = null;

function togglePlay() {{
  const btn = document.getElementById('playBtn');
  if (playing) {{
    clearInterval(playInterval);
    btn.innerHTML = '&#9654; Play';
    btn.classList.remove('playing');
    playing = false;
  }} else {{
    // If at end, reset to start
    if (parseInt(slider.value) >= 2020) {{
      slider.value = 1975;
    }}
    btn.innerHTML = '&#9646;&#9646; Pause';
    btn.classList.add('playing');
    playing = true;
    playInterval = setInterval(() => {{
      let val = parseInt(slider.value);
      if (val >= 2020) {{
        clearInterval(playInterval);
        btn.innerHTML = '&#9654; Play';
        btn.classList.remove('playing');
        playing = false;
        return;
      }}
      slider.value = val + 1;
      display.textContent = val + 1;
      updateMap(val + 1);
    }}, 400);
  }}
}}

// Initial render
updateMap(1990);
</script>
</body>
</html>
"""

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text(html)
print(f"Wrote {OUTPUT_PATH}")
print(f"CPC records (in bounds): {len(cpcs)}")
print(f"Clinic records (in bounds): {len(clinics)}")
