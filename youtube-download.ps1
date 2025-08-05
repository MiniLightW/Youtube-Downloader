# usage : only copy past url required, better use for casuals users

# custom section : set path
$OutPath = "$env:HOMEDRIVE$env:HOMEPATH\Downloads"
$ScriptPath = "D:\DEV\Python\Youtube\Youtube-Downloader\youtube-download.py"
# end custom section

# script section
$url = Read-Host "Entrez l'URL Youtube ou la playlist"
Set-Location $OutPath
python $ScriptPath -t "$url"
Write-Host "Output folder is here : $OutPath"
Pause