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
# check if script path exists
if (-not (Test-Path $ScriptPath)) {
    Write-Host "The script path does not exist. Please check the path."
    Pause
    Exit
}

# show configuration
Write-Host "Configuration :"
Write-Host "Output folder is here : $OutPath"
Write-Host "Script path is here   : $ScriptPath"
Write-Host "!!! THIS SCRIPT IS FOR YOUTUBE SHORTS DOWNLOAD ONLY !!!"

Write-Host "+---------------------------------------------------------------------+"
$url = Read-Host "Write the Youtube URL or playlist"
if ($url -eq "") {
    Write-Host "No URL provided. Please run the script again and provide a valid URL."
    Pause
    Exit
}

# change directory
Write-Host "Set-Location $OutPath"
Set-Location $OutPath

# execute download
Write-Host "python $ScriptPath -t "$url" -s"
python $ScriptPath -t "$url" -s

Write-Host "+---------------------------------------------------------------------+"
Write-Host ""
Write-Host "Output folder is here : $OutPath"
Write-Host ""
Write-Host "+---------------------------------------------------------------------+"
Pause

######################################################################################
# end script section 
######################################################################################