import os

def main():
    exports_dir = os.path.join("arcgis", "exports")
    os.makedirs(exports_dir, exist_ok=True)
    print(f"[arcgis_export] Export directory ready: {exports_dir}")
    # TODO: Add ArcGIS export logic

if __name__ == "__main__":
    main()
