# Run Flet app with activated virtual environment
$venvPath = "$PSScriptRoot\.venv"
$pythonExe = "$venvPath\Scripts\python.exe"
$mainPy = "$PSScriptRoot\main.py"

# Verify venv exists
if (-not (Test-Path $pythonExe)) {
    Write-Host "ERROR: Virtual environment not found at $venvPath" -ForegroundColor Red
    exit 1
}

Write-Host "Using Python: $pythonExe" -ForegroundColor Green
Write-Host "Running: $mainPy" -ForegroundColor Green

# Run the app
& $pythonExe $mainPy
