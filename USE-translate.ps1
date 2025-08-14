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
Write-Host "THIS SCRIPT IS FOR YOUTUBE SUBTITLE DOWNLOAD AND TRANSLATE ONLY"
Write-Host "+---------------------------------------------------------------------+"
$url = Read-Host "Write the full path of the file to translate"
if ($url -eq "") {
    Write-Host "No URL provided. Please run the script again and provide a valid URL."
    Pause
    Exit
}

# change directory
Write-Host "Set-Location $OutPath"
Set-Location $OutPath

# execute download
Write-Host "py $ScriptTradPath -t "$url" -l "fr"" 
py $ScriptTradPath -t "$url" -l "fr"

# check
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error : $LASTEXITCODE"
    Pause
    Exit
}

Write-Host "+---------------------------------------------------------------------+"
Write-Host ""
Write-Host "Output folder is here : $OutPath"
Write-Host ""
Write-Host "+---------------------------------------------------------------------+"
Pause

######################################################################################
# end script section 
######################################################################################