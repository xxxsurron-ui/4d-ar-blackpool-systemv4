# Architecture

The 4D AR Blackpool System is composed of:

## ArcGIS Layer
Used for authoring, analysis, and publishing spatial + temporal datasets.

## Engine Layer (`engine/`)
- `core/` — main 4D engine logic
- `ingestion/` — data loaders
- `processing/` — spatial + temporal transforms
- `rendering/` — AR-ready outputs

## AR Layer (`ar/`)
- WebXR or Unity-based frontends

## Automation (`scripts/`)
- Export, update, and packaging utilities

Data flow:
ArcGIS → scripts/arcgis_export.py → engine → AR client
