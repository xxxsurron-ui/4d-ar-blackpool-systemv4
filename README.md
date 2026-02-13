# 4D AR Blackpool System

A 4D (3D + time) geospatial and augmented‑reality system built using ArcGIS, Python, and AR frameworks.  
This project integrates ArcGIS Pro workflows, spatial datasets, temporal layers, and AR rendering pipelines to create a digital‑twin environment for Blackpool.

---

## 🧭 ArcGIS Integration

This system is designed to work with:

- ArcGIS Pro (.aprx projects)
- ArcGIS Online feature/scene services
- Time‑enabled layers (tide, weather, traffic, environmental change)
- 3D scene layers (SLPK, multipatch, voxel)
- Geoprocessing tools (ModelBuilder + Python toolboxes)

ArcGIS handles **data creation, editing, analysis, and publishing**, while this repository manages **code, automation, AR integration, and deployment**.

---

## 📁 Project Structure

---

## ▶️ Quick Start

1. Open the ArcGIS Pro project in `arcgis/aprx/`.
2. Run geoprocessing tools or ModelBuilder workflows.
3. Export processed layers using:
   ```bash
   python scripts/arcgis_export.py

python engine/main.py
Code

---

## ▶️ Quick Start

1. Open the ArcGIS Pro project in `arcgis/aprx/`.
2. Run geoprocessing tools or ModelBuilder workflows.
3. Export processed layers using:
   ```bash
   python scripts/arcgis_export.py
Launch the 4D engine:

bash
python engine/main.py
Start AR interface:

bash
npm install
npm run 
