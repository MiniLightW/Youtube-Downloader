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

Write-Host "+---------------------------------------------------------------------+"
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

Write-Host "+---------------------------------------------------------------------+"
$url = Read-Host "Entrez l'URL Youtube ou la playlist"

$choice = Read-Host "Do you want to force original audio? (y/n)"
if ($choice -eq 'y') {
    $audioForceItag = $true
} else {
    $audioForceItag = $false
    $choice = Read-Host "Do you want to choose a specific audio itag? (y/n)"
    if ($choice -eq 'y') {
        $audioTag = Read-Host "Enter the audio itag (a number like 18..)"
        Write-Host "Using audio itag: $audioTag"
    } else {
        $audioTag = $null
        Write-Host "No audio itag specified, using default settings."
    }
}

# change directory
Write-Host "Set-Location $OutPath"
Set-Location $OutPath

# execute download
if ($audioForceItag) {
    Write-Host "python $ScriptPath -t "$url" -af"
    python $ScriptPath -t "$url" -af
} elseif ($audioTag) {
    Write-Host "python $ScriptPath -t "$url" -at "$audioTag""
    python $ScriptPath -t "$url" -at "$audioTag"
} else {
    Write-Host "python $ScriptPath -t "$url""
    python $ScriptPath -t "$url"
}

Write-Host "+---------------------------------------------------------------------+"
Write-Host "Output folder is here : $OutPath"
Write-Host "+---------------------------------------------------------------------+"
Pause

######################################################################################
# end script section 
######################################################################################