######################################################################################
# usage : only copy past url required, better use for casuals users
######################################################################################
# script section 
######################################################################################

# load config
. "$PSScriptRoot\youtube-download_config.ps1"

# start script
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
# Check if output path exists, if not create it
if (-not (Test-Path $OutPath)) {
    New-Item -ItemType Directory -Path $OutPath | Out-Null
    if (-not (Test-Path $OutPath)) {
        Write-Host "Failed to create output directory. Please check your permissions."
        Pause
        Exit
    }
}

# Activate the virtual environment
Write-Host "Activating virtual environment..."
$activate

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
# Check if output path exists, if not create it
if (-not (Test-Path $OutPath)) {
    New-Item -ItemType Directory -Path $OutPath | Out-Null
    if (-not (Test-Path $OutPath)) {
        Write-Host "Failed to create output directory. Please check your permissions."
        Pause
        Exit
    }
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