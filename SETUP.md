# Cosmic Portfolio Setup Guide

## THE IMMEDIATE FIX - DO THIS FIRST ⚠️

The error you're seeing is caused by a **Flet VS Code extension trying to auto-install packages**.

### Step 1: Disable the Flet Extension
1. Open VS Code
2. Press `Ctrl+Shift+X` (Extensions)
3. Search for: `flet`
4. Click on any "Flet" extension you find
5. Click the **gear icon** → **Disable (Workspace)** or **Uninstall**
6. Close and reopen VS Code

### Step 2: Tell VS Code to Use the Virtual Environment
1. Press `Ctrl+Shift+P` (Command Palette)
2. Type: `Python: Select Interpreter`
3. Choose: `.\.venv\Scripts\python.exe` (or the full path)
4. Press Enter

### Step 3: Run Your App
Use ONE of these methods:

#### Method A: Double-Click Launcher (Easiest)
Simply double-click: **`start-app.bat`**

#### Method B: VS Code Terminal
1. Press ``Ctrl+` `` to open Terminal
2. Run: `.\.venv\Scripts\python.exe main.py`

#### Method C: PowerShell
1. Open PowerShell in the project folder
2. Run: `.\run.ps1`

---

## If the Error Persists

### Check for Hidden Flet Extensions
1. `Ctrl+Shift+X` (Extensions)
2. Look for extensions with these names:
   - `Flet`
   - `Flet Tools`
   - Any Python/Flet related extensions
3. Disable all of them for this workspace

### Force VS Code to Forget
1. Delete the `.vscode` folder and restart VS Code
2. Then press `Ctrl+Shift+P` → `Python: Select Interpreter` → Choose `.\.venv\Scripts\python.exe`

### Still Not Working?
Run your app **without** VS Code:
```cmd
cd c:\Users\225109611\Desktop\attachments
start-app.bat
```

---

## Problem Explanation

When VS Code launches, it or an extension tries to run:
```
uv pip install flet-desktop==0.85.3
```

But this fails because:
1. The command doesn't specify which Python environment to use
2. The system Python (managed by `uv`) is locked down
3. It doesn't find the `.venv` directory in the right way

**The virtual environment IS correctly set up** - we just need to prevent VS Code from trying to auto-install anything.

## Solution Summary
- ✅ Virtual environment: `.venv/` (exists and working)
- ✅ Packages: `flet` & `flet-desktop` (already installed)
- ❌ VS Code Extension: Trying to auto-install (DISABLE THIS)
- ✅ Launchers: `start-app.bat` (always works)

---

## Files in This Project
- `main.py` - Your Flet application
- `.venv/` - Virtual environment with dependencies (working!)
- `.vscode/` - VS Code configuration
- `requirements.txt` - Package list
- `pyproject.toml` - Project metadata
- `start-app.bat` - Recommended launcher (works without VS Code)
- `run.ps1` - PowerShell launcher
- `run.bat` - Simple launcher
- `.env` - Environment variables

---

**Bottom line**: Double-click `start-app.bat` to run your app immediately without any VS Code issues.

