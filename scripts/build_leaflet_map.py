"""
Build interactive Leaflet map of CPC and abortion provider expansion
in North and South Carolina, 1970-2020.

Outputs a self-contained HTML file for embedding in a Hugo blog post.

Usage:
    python scripts/build_leaflet_map.py

Requires: pandas, pyreadstat
"""

import pandas as pd
import json
from pathlib import Path

# === CONFIG ===
DATA_PATH = Path(__file__).parent.parent / "data" / "geo_mapping_clinic_cpc.dta"
# Fallback to Dropbox path
if not DATA_PATH.exists():
    # Try common locations for the research data
    for base in [Path("/Users/lepus"), Path("/sessions/upbeat-charming-bardeen/mnt/lepus")]:
        candidate = base / "Dropbox (Personal)" / "GSU" / "Clinics_CPC" / "JPE Submission and Replication" / "Replication" / "Data" / "Processed" / "geo_mapping_clinic_cpc.dta"
        if candidate.exists():
            DATA_PATH = candidate
            break

OUTPUT_PATH = Path(__file__).parent.parent / "content" / "post" / "cpc-expansion-carolinas" / "leaflet_map.html"

# Bounding box for NC/SC (filter out geocoding errors)
LAT_MIN, LAT_MAX = 32.0, 36.6
LNG_MIN, LNG_MAX = -84.5, -75.4

# NC/SC state boundary GeoJSON (NAD83, same CRS as point coordinates)
NC_SC_GEOJSON = '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{"NAME":"North Carolina","STATEFP":"37"},"geometry":{"type":"Polygon","coordinates":[[[-84.2866,35.2058],[-84.2832,35.2266],[-84.2237,35.2691],[-84.1785,35.2407],[-84.0975,35.2474],[-84.0291,35.2921],[-84.0235,35.2958],[-84.0381,35.3484],[-84.0076,35.3717],[-84.0218,35.4074],[-83.9732,35.4526],[-83.9589,35.4579],[-83.9532,35.46],[-83.9168,35.4736],[-83.8485,35.5193],[-83.7717,35.5621],[-83.6629,35.5678],[-83.6532,35.5683],[-83.5878,35.567],[-83.4983,35.563],[-83.4524,35.6029],[-83.4216,35.6112],[-83.3473,35.6605],[-83.2972,35.6578],[-83.2647,35.7031],[-83.2561,35.7151],[-83.2554,35.7162],[-83.1983,35.7255],[-83.1615,35.7634],[-83.0972,35.7761],[-83.0485,35.7877],[-82.9784,35.7826],[-82.9666,35.7954],[-82.9374,35.8273],[-82.8997,35.8746],[-82.9106,35.9269],[-82.8938,35.9339],[-82.8607,35.9474],[-82.8161,35.924],[-82.7875,35.9522],[-82.7794,35.9925],[-82.7251,36.0182],[-82.6284,36.0621],[-82.6057,36.0372],[-82.5955,36.026],[-82.6109,35.9744],[-82.5579,35.9539],[-82.508,35.982],[-82.4646,36.0065],[-82.4169,36.073],[-82.4095,36.0834],[-82.3469,36.1152],[-82.2977,36.1335],[-82.2657,36.1276],[-82.2203,36.1538],[-82.2113,36.159],[-82.1408,36.1362],[-82.1271,36.1044],[-82.0811,36.1057],[-82.0801,36.1057],[-82.0287,36.1243],[-81.9601,36.2281],[-81.9344,36.2647],[-81.9184,36.2874],[-81.9081,36.302],[-81.8332,36.3473],[-81.769,36.341],[-81.706,36.3385],[-81.7254,36.3897],[-81.7343,36.4133],[-81.6953,36.4679],[-81.7,36.5368],[-81.6775,36.5881],[-81.4998,36.5798],[-81.3532,36.5762],[-81.1767,36.5719],[-81.0619,36.567],[-80.9017,36.5618],[-80.9017,36.5618],[-80.8402,36.5619],[-80.7048,36.5623],[-80.6122,36.5582],[-80.4401,36.5506],[-80.4316,36.5502],[-80.2952,36.544],[-80.0535,36.5426],[-80.0273,36.5425],[-80.0273,36.5425],[-79.8917,36.542],[-79.7149,36.5414],[-79.5136,36.5407],[-79.5106,36.5407],[-79.4701,36.5408],[-79.3431,36.5411],[-79.2185,36.5414],[-79.1383,36.5416],[-78.942,36.5421],[-78.7963,36.5418],[-78.7341,36.5416],[-78.51,36.5411],[-78.4573,36.5414],[-78.3237,36.5424],[-78.1329,36.5438],[-78.0462,36.5442],[-77.8998,36.5449],[-77.7671,36.5454],[-77.7497,36.5455],[-77.2988,36.546],[-77.1902,36.5462],[-77.1643,36.5462],[-76.9173,36.546],[-76.916,36.5461],[-76.9157,36.5461],[-76.7383,36.551],[-76.542,36.5508],[-76.4915,36.5507],[-76.3133,36.5506],[-76.3132,36.5506],[-76.1223,36.5506],[-76.0268,36.5506],[-75.867,36.5508],[-75.8384,36.4349],[-75.7964,36.2904],[-75.7707,36.2321],[-75.7183,36.1137],[-75.6585,36.0204],[-75.5698,35.8633],[-75.519,35.7691],[-75.4961,35.7285],[-75.4587,35.5966],[-75.4868,35.3917],[-75.5336,35.2258],[-75.6355,35.2203],[-75.7496,35.1856],[-75.7579,35.1831],[-75.913,35.1196],[-76.0131,35.0619],[-76.1373,34.9879],[-76.2331,34.9055],[-76.3102,34.8523],[-76.3868,34.7846],[-76.4505,34.7144],[-76.5359,34.5886],[-76.5538,34.6283],[-76.6187,34.6726],[-76.727,34.6967],[-76.9063,34.6828],[-77.113,34.6381],[-77.1368,34.6329],[-77.241,34.5875],[-77.3225,34.5356],[-77.4629,34.4714],[-77.5152,34.4374],[-77.635,34.3596],[-77.7135,34.2902],[-77.764,34.2456],[-77.8292,34.1626],[-77.8855,34.0382],[-77.9155,33.9717],[-77.9348,33.9205],[-77.9602,33.8533],[-78.0068,33.8587],[-78.0187,33.8883],[-78.137,33.9122],[-78.2761,33.9124],[-78.384,33.9019],[-78.5411,33.8511],[-78.6159,33.9155],[-78.6509,33.9451],[-78.8117,34.081],[-79.0712,34.2992],[-79.0712,34.2993],[-79.0713,34.2993],[-79.3583,34.5454],[-79.4503,34.6206],[-79.4618,34.63],[-79.6753,34.8047],[-79.6929,34.805],[-79.9247,34.8078],[-79.9274,34.8079],[-80.0772,34.8097],[-80.3208,34.8136],[-80.5617,34.8175],[-80.5617,34.8175],[-80.797,34.8239],[-80.782,34.9358],[-80.8406,35.0015],[-80.9035,35.0721],[-80.9062,35.0752],[-80.935,35.1074],[-81.0415,35.0447],[-81.058,35.0732],[-81.0368,35.1226],[-81.0423,35.1468],[-81.0429,35.1492],[-81.3281,35.1623],[-81.3676,35.1641],[-81.4943,35.1699],[-81.7681,35.1797],[-81.8744,35.1835],[-81.9694,35.1869],[-82.0397,35.1894],[-82.0484,35.1896],[-82.216,35.1933],[-82.2954,35.195],[-82.3532,35.1987],[-82.4113,35.2025],[-82.4556,35.1774],[-82.5326,35.1556],[-82.5777,35.1465],[-82.686,35.1245],[-82.7464,35.0791],[-82.7621,35.0819],[-82.7833,35.0856],[-82.8975,35.056],[-83.0085,35.0269],[-83.1086,35.0007],[-83.1086,35.0007],[-83.3228,34.9959],[-83.4829,34.9909],[-83.5492,34.9888],[-83.62,34.9866],[-83.9364,34.9875],[-83.9366,34.9875],[-84.0053,34.9876],[-84.1294,34.9879],[-84.3219,34.9884],[-84.2866,35.2058]]]}},{"type":"Feature","properties":{"NAME":"South Carolina","STATEFP":"45"},"geometry":{"type":"Polygon","coordinates":[[[-83.3532,34.7286],[-83.3201,34.7596],[-83.3239,34.7897],[-83.2848,34.823],[-83.2526,34.8535],[-83.2012,34.8847],[-83.1406,34.9249],[-83.1244,34.9552],[-83.1086,35.0007],[-83.0085,35.0269],[-82.8975,35.056],[-82.7833,35.0856],[-82.7621,35.0819],[-82.7464,35.0791],[-82.686,35.1245],[-82.5777,35.1465],[-82.5326,35.1556],[-82.4556,35.1774],[-82.4113,35.2025],[-82.3532,35.1987],[-82.2954,35.195],[-82.216,35.1933],[-82.0484,35.1896],[-82.0397,35.1894],[-81.9694,35.1869],[-81.8744,35.1835],[-81.7681,35.1797],[-81.4943,35.1699],[-81.3676,35.1641],[-81.3281,35.1623],[-81.0429,35.1492],[-81.0423,35.1468],[-81.0368,35.1226],[-81.058,35.0732],[-81.0415,35.0447],[-80.935,35.1074],[-80.9062,35.0752],[-80.9035,35.0721],[-80.8406,35.0015],[-80.782,34.9358],[-80.797,34.8239],[-80.5617,34.8175],[-80.5617,34.8175],[-80.3208,34.8136],[-80.0772,34.8097],[-79.9274,34.8079],[-79.9247,34.8078],[-79.6929,34.805],[-79.6753,34.8047],[-79.4618,34.63],[-79.4503,34.6206],[-79.3583,34.5454],[-79.0713,34.2993],[-79.0712,34.2993],[-79.0712,34.2992],[-78.8117,34.081],[-78.6509,33.9451],[-78.6159,33.9155],[-78.5411,33.8511],[-78.6723,33.8176],[-78.7727,33.7685],[-78.8629,33.7057],[-78.9381,33.6398],[-78.9951,33.5727],[-79.0285,33.5334],[-79.0846,33.4837],[-79.1354,33.4039],[-79.1623,33.3272],[-79.1806,33.238],[-79.1724,33.2066],[-79.2155,33.1556],[-79.2745,33.1201],[-79.2916,33.1098],[-79.3299,33.09],[-79.3393,33.0503],[-79.36,33.0067],[-79.4234,33.0151],[-79.4835,33.0013],[-79.5224,33.0354],[-79.5807,33.0064],[-79.6066,32.9722],[-79.5698,32.9267],[-79.6013,32.8982],[-79.6951,32.8504],[-79.7264,32.806],[-79.8182,32.7664],[-79.8684,32.7348],[-79.885,32.6844],[-79.9685,32.6397],[-80.0008,32.6059],[-80.077,32.6033],[-80.1484,32.5785],[-80.1901,32.5468],[-80.2464,32.5311],[-80.2494,32.5294],[-80.3384,32.4787],[-80.4135,32.4712],[-80.4657,32.4953],[-80.4723,32.4833],[-80.4846,32.461],[-80.4575,32.4103],[-80.4343,32.3752],[-80.4552,32.3265],[-80.5394,32.287],[-80.5964,32.2735],[-80.6448,32.2915],[-80.7146,32.3257],[-80.766,32.2926],[-80.727,32.2657],[-80.6692,32.2168],[-80.7215,32.1604],[-80.8125,32.1097],[-80.8587,32.0996],[-80.8674,32.0785],[-80.8855,32.0346],[-80.9432,32.0578],[-81.0067,32.1012],[-81.0383,32.0845],[-81.1133,32.1132],[-81.1194,32.1771],[-81.1476,32.2272],[-81.1535,32.2377],[-81.128,32.2763],[-81.133,32.3348],[-81.1735,32.3849],[-81.1949,32.4115],[-81.1948,32.4651],[-81.2749,32.5442],[-81.2842,32.5471],[-81.3288,32.5612],[-81.3869,32.599],[-81.3971,32.6056],[-81.3938,32.6535],[-81.4127,32.7391],[-81.4131,32.7443],[-81.4206,32.8312],[-81.4641,32.8978],[-81.4996,32.9437],[-81.502,33.0151],[-81.544,33.0444],[-81.6017,33.0847],[-81.616,33.0893],[-81.6584,33.1032],[-81.7551,33.1516],[-81.7625,33.1973],[-81.7635,33.2036],[-81.8465,33.2417],[-81.8465,33.2473],[-81.8461,33.3038],[-81.9327,33.3435],[-81.9201,33.4108],[-81.9263,33.4629],[-81.9909,33.4942],[-82.0163,33.5287],[-82.0282,33.5449],[-82.1062,33.5956],[-82.1147,33.5979],[-82.1425,33.6054],[-82.1619,33.6106],[-82.1997,33.6576],[-82.2159,33.6878],[-82.2391,33.7309],[-82.3245,33.82],[-82.4312,33.8671],[-82.513,33.937],[-82.5568,33.9454],[-82.563,33.9566],[-82.5919,34.009],[-82.595,34.0135],[-82.6428,34.0813],[-82.7154,34.1482],[-82.736,34.2155],[-82.745,34.2449],[-82.7746,34.2884],[-82.7803,34.2967],[-82.8234,34.3589],[-82.842,34.3998],[-82.8738,34.4715],[-82.9258,34.4818],[-82.9914,34.473],[-82.9951,34.4725],[-83.0483,34.4933],[-83.0506,34.4951],[-83.0969,34.5315],[-83.1029,34.5374],[-83.1546,34.5882],[-83.2214,34.6099],[-83.278,34.6449],[-83.3387,34.682],[-83.34,34.6863],[-83.3496,34.717],[-83.3532,34.7286]]]}}]}'

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
const stateBoundaries = {NC_SC_GEOJSON};

// Initialize map centered on NC/SC (shifted south, higher zoom to reduce VA labels)
const map = L.map('map', {{
  zoomControl: true,
  scrollWheelZoom: true,
}}).setView([34.4, -79.8], 7);

L.tileLayer('https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
  attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
  subdomains: 'abcd',
  maxZoom: 19
}}).addTo(map);

// Add NC/SC state boundary overlay
L.geoJSON(stateBoundaries, {{
  style: {{
    color: '#2b4c7e',
    weight: 2.5,
    opacity: 0.7,
    fillColor: '#f0f4f8',
    fillOpacity: 0.08,
    dashArray: null,
  }}
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
        '<strong>Crisis Pregnancy Center</strong><br>' +
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
