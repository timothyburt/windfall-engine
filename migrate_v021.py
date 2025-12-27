import os
import shutil
import json

def migrate():
    print("[*] Starting Engine Restructuring (v0.2.1-patch)...")
    
    # 1. Define the base structure
    base_dir = "windfall"
    engine_dir = os.path.join(base_dir, "engine")
    subfolders = ["core", "renderers", "scenes", "events"]
    
    # 2. Create the new engine directories and __init__.py files
    # We create windfall/engine/ and all sub-packages
    for folder in [""] + subfolders:
        path = os.path.join(engine_dir, folder)
        os.makedirs(path, exist_ok=True)
        
        # Create __init__.py to make it an importable package
        init_path = os.path.join(path, "__init__.py")
        with open(init_path, 'a'):
            os.utime(init_path, None)
        print(f"[+] Initialized Package: {path}")

    # 3. Define file movements (Old Path -> New Path)
    # This covers your core, events, and all scenes/renderers
    moves = [
        # Core & Events
        ("windfall/core.py", "windfall/engine/core/core.py"),
        ("windfall/events.py", "windfall/engine/events/events.py"),
        
        # Renderers
        ("windfall/renderers/tui.py", "windfall/engine/renderers/tui.py"),
        
        # Scenes
        ("windfall/scenes/base.py", "windfall/engine/scenes/base.py"),
        ("windfall/scenes/menu.py", "windfall/engine/scenes/menu.py"),
        ("windfall/scenes/splash.py", "windfall/engine/scenes/splash.py"),
    ]

    # 4. Execute Movement
    for src, dest in moves:
        if os.path.exists(src):
            # Ensure the destination directory exists (safety check)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.move(src, dest)
            print(f"[>] Moved: {src} -> {dest}")
        else:
            print(f"[!] Warning: {src} not found, skipping.")

    # 5. Update the Version JSON
    version_path = "updates/version.json"
    if os.path.exists(version_path):
        try:
            with open(version_path, 'r+') as f:
                data = json.load(f)
                data["version"] = "0.2.1"
                data["requires_migration"] = False
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
            print("[*] Updated updates/version.json to v0.2.1")
        except Exception as e:
            print(f"[!] Error updating version.json: {e}")

    print("\n[!] Migration Complete. Remember to update your imports in main.py!")
    print("[!] You can now safely delete the empty windfall/scenes/ and windfall/renderers/ folders.")

if __name__ == "__main__":
    migrate()