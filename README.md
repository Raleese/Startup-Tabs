# Startup-Tabs

Startup-Tabs is a small Windows desktop app that opens your saved websites when you start your computer and sign in.

## Screenshots

<img width="1032" height="888" alt="image" src="https://github.com/user-attachments/assets/daa21aed-d22e-4434-9d64-d6ba59364207" />

## Features

- Add and remove website URLs from a simple GUI.
- Enable or disable startup with one button.
- Automatically creates a Windows Startup batch file when startup is enabled.
- Opens saved websites as browser tabs at login.

## How it works

App settings are stored in [data/config.json](data/config.json).

When startup is enabled, the app creates `startup_tabs.bat` in your Windows Startup folder:

`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`

That batch file runs:

```bash
python -m app.run_config
```

The startup runner loads the saved websites and opens each one in a new browser tab.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies (if any):

```bash
pip install -r requirements.txt
```

## Run

```bash
python run.py
```

## Project files

- [run.py](run.py): Main GUI entry point.
- [app/gui.py](app/gui.py): Tkinter user interface.
- [app/startup.py](app/startup.py): Registers or removes startup batch file.
- [app/run_config.py](app/run_config.py): Startup runner that opens saved websites.
- [app/launcher.py](app/launcher.py): Browser tab launching logic.
- [app/storage.py](app/storage.py): Config file read/write helpers.
- [data/config.json](data/config.json): Saved startup flag and website list.

## Troubleshooting

- If tabs do not open after login, open the app and toggle startup off and back on.
- If Python path changes, toggling startup rewrites the batch file with the current interpreter.
