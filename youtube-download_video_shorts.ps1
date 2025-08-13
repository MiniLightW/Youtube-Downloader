######################################################################################
# usage : only copy past url required, better use for casuals users
######################################################################################
# script section 
######################################################################################

# load config and env
. "$PSScriptRoot\youtube-download_config_and_env.ps1"

# show configuration
Write-Host "+---------------------------------------------------------------------+"
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