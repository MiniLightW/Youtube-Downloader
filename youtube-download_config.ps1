# custom section : set path
$OutPath = "$env:HOMEDRIVE$env:HOMEPATH\Downloads\Youtube-Downloader"
# end custom section

$ProjectPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
$ScriptPath = Join-Path $ProjectPath "youtube-download.py"
$VenvPath = Join-Path $ProjectPath "venv"
$activate = Join-Path $VenvPath "Scripts\Activate.ps1"