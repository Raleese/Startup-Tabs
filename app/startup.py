import os
import sys
from pathlib import Path

STARTUP_FOLDER = Path(os.environ["APPDATA"]) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
BAT_FILE = STARTUP_FOLDER / "startup_tabs.bat"

def enable_startup():
    project_root = Path(__file__).resolve().parent.parent
    runner_path = project_root / "app" / "startup_config.py"
    python_exe = sys.executable

    content = (
        "@echo off\n"
        f'cd /d "{project_root}"\n'
        f'"{python_exe}" -m app.startup_config\n'
    )

    with open(BAT_FILE, "w") as f:
        f.write(content)

def disable_startup():
    if BAT_FILE.exists():
        BAT_FILE.unlink()

def is_startup_registered():
    return BAT_FILE.exists()