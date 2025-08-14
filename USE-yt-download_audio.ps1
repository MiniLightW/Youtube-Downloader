######################################################################################
# usage : only copy past url required, better use for casuals users
######################################################################################
# script section 
######################################################################################

# load config and env
. "$PSScriptRoot\PS_config_and_env.ps1"

# show configuration
Write-Host "+---------------------------------------------------------------------+"
Write-Host "Configuration :"
Write-Host "Output folder is here : $OutPath"
Write-Host "Script path is here   : $ScriptPath"
Write-Host "!!! THIS SCRIPT IS FOR YOUTUBE AUDIO DOWNLOAD ONLY !!!"
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
Write-Host "python $ScriptPath -t "$url" -mp3"
python $ScriptPath -t "$url" -mp3

Write-Host "+---------------------------------------------------------------------+"
Write-Host ""
Write-Host "Output folder is here : $OutPath"
Write-Host ""
Write-Host "+---------------------------------------------------------------------+"
Pause

######################################################################################
# end script section 
######################################################################################