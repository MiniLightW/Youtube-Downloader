######################################################################################
# usage : only copy past url required, better use for casuals users
######################################################################################

# custom section : set path
$OutPath = "$env:HOMEDRIVE$env:HOMEPATH\Downloads"
$ScriptPath = "D:\DEV\Python\Youtube\Youtube-Downloader\youtube-download.py"
# end custom section

######################################################################################
# script section 
######################################################################################

# check if python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python to use this script."
    Pause
    Exit
}

# show configuration
Write-Host "Configuration :"
Write-Host "Output folder is here : $OutPath"
Write-Host "Script path is here   : $ScriptPath"

$url = Read-Host "Entrez l'URL Youtube ou la playlist"

# change directory
Write-Host "Set-Location $OutPath"
Set-Location $OutPath

# execute download
Write-Host "python $ScriptPath -t "$url""
python $ScriptPath -t "$url"

Write-Host "Output folder is here : $OutPath"
Pause