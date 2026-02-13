import os
import shutil

def main():
    root = "4d-ar-blackpool-system-v4"
    zip_name = f"{root}.zip"
    if not os.path.isdir(root):
        print(f"[build_zip] Folder '{root}' not found.")
        return
    shutil.make_archive(root, "zip", root_dir=root)
    print(f"[build_zip] Created {zip_name}")

if __name__ == "__main__":
    main()
