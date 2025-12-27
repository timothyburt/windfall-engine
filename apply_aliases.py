import os

def update_file_imports(file_path):
    # Added encoding='utf-8' and errors='ignore' to handle ASCII art/special chars
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"[!] Could not read {file_path}: {e}")
        return

    new_lines = []
    changed = False

    for line in lines:
        if "from windfall.engine.scenes.base import BaseScene" in line:
            new_lines.append("from windfall.engine import BaseScene\n")
            changed = True
        elif "from windfall.engine.scenes.splash import SplashScene" in line:
            new_lines.append("from windfall.engine import SplashScene\n")
            changed = True
        elif "from windfall.engine.scenes.menu import MainMenuScene" in line:
            new_lines.append("from windfall.engine import MainMenuScene\n")
            changed = True
        elif "from windfall.engine.core.core import WindfallCore" in line:
            new_lines.append("from windfall.engine import WindfallCore\n")
            changed = True
        else:
            new_lines.append(line)

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"[✓] Updated imports in: {file_path}")

def run_alias_migration():
    for root, dirs, files in os.walk("."):
        # Don't look in .git or venv folders if they exist
        if '.git' in root or 'venv' in root:
            continue
            
        for file in files:
            if file.endswith(".py") and file != "apply_aliases.py":
                update_file_imports(os.path.join(root, file))

if __name__ == "__main__":
    run_alias_migration()