# API Reference

## Engine Modules

### engine.core
Main 4D engine orchestration.

### engine.ingestion
Loads vector, raster, and time-series data.

### engine.processing
Spatial/temporal operations:
- clipping
- reprojection
- time filtering
- aggregation

### engine.rendering
Outputs AR-ready formats:
- GeoJSON
- tiles
- time-stamped snapshots

## Scripts

### arcgis_export.py
Exports ArcGIS layers into engine-friendly formats.

### update_layers.py
Refreshes datasets from external sources.

### build_zip.py
Packages the project into a ZIP.
