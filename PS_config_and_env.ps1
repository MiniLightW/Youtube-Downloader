# Youtube-Downloader - Configuration Script
# This script sets up the environment for the Youtube-Downloader project

Write-Host "+---------------------------------------------------------------------+"
Write-Host "Loading config..."

# custom section : set path
$OutPath = "$env:HOMEDRIVE$env:HOMEPATH\Downloads\Youtube-Downloader"
# end custom section

$ProjectPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
$ScriptPath     = Join-Path $ProjectPath "youtube-download.py"
$ScriptSubPath  = Join-Path $ProjectPath "youtube-download-sub.py"
$ScriptTradPath = Join-Path $ProjectPath "text_translator.py"
$VenvPath = Join-Path $ProjectPath "venv"
$activate = Join-Path $VenvPath "Scripts\Activate.ps1"

Write-Host "Loading config : OK"

# Youtube-Downloader - Check Environment
Write-Host "+---------------------------------------------------------------------+"
Write-Host "Check Environment prerequisites..."

# check if python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python to use this script."
    Pause
    Exit
}
# check if script path exists
if (-not (Test-Path $ScriptPath)) {
    Write-Host "The script path does not exist. Please check the path."
    Pause
    Exit
}
# check if script path exists
if (-not (Test-Path $ScriptSubPath)) {
    Write-Host "The script path does not exist. Please check the path."
    Pause
    Exit
}
# check if script path exists
if (-not (Test-Path $ScriptTradPath)) {
    Write-Host "The script path does not exist. Please check the path."
    Pause
    Exit
}
# Check if output path exists, if not create it
if (-not (Test-Path $OutPath)) {
    New-Item -ItemType Directory -Path $OutPath | Out-Null
    if (-not (Test-Path $OutPath)) {
        Write-Host "Failed to create output directory. Please check your permissions."
        Pause
        Exit
    }
}
Write-Host "Check Environment prerequisites : OK"

# Activate the virtual environment
Write-Host "+---------------------------------------------------------------------+"
Write-Host "Activating virtual environment..."
& $activate

$pythonPath = Get-Command python | Select-Object -ExpandProperty Source
if ($pythonPath -like "*venv*python.exe") {
    Write-Host "Activating virtual environment : OK"
} else {
    Write-Host "Executable Python used : $pythonPath"
    Write-Host "Activating virtual environment : FAIL"
    Pause
    exit
}
