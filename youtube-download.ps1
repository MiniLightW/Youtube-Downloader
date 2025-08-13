######################################################################################
# usage : only copy past url required, better use for casuals users
######################################################################################
# script section 
######################################################################################

# load config
. "$PSScriptRoot\youtube-download_config_and_env.ps1"

# show configuration
Write-Host "+---------------------------------------------------------------------+"
Write-Host "Configuration :"
Write-Host "Output folder is here : $OutPath"
Write-Host "Script path is here   : $ScriptPath"
Write-Host "THIS SCRIPT IS FOR YOUTUBE ONLY"
Write-Host "+---------------------------------------------------------------------+"
$url = Read-Host "Entrez l'URL Youtube ou la playlist"
if ($url -eq "") {
    Write-Host "No URL provided. Please run the script again and provide a valid URL."
    Pause
    Exit
}

$media = ""
$quality = ""
while ($media -eq "") {
    # choose output media format
    $choice = Read-Host "Download video (v), short video (s) or Audio (a) only (write v, s or a)"
    if ($choice -eq 'v') {
        $media = $choice
        # ask if you want to choose quality
        $choice = "If you want other quality than BestQuality write (b) instead press ENTER"
        if ($choice -eq "b") {
            while ($quality -eq "") {
                # choose specific quality
                $choice = Read-Host "Choose the required Quality (1080p, 720p, ...) if you know it or write '?' if you don't know yet"
                if ($choice -eq '?') {
                    $quality = $choice
                } elseif ($choice -ne '') {
                    $quality = $choice
                }
            }
        }
    } elseif ($choice -eq 's') {
        $media = $choice
    } elseif ($choice -eq 'a') {
        $media = $choice
    }
}

# change directory
Write-Host "Set-Location $OutPath"
Set-Location $OutPath

# execute download
if ($media -eq "v") {
    if ($quality -eq "") {
        Write-Host "python $ScriptPath -t "$url" -v"
        python $ScriptPath -t "$url" -v
    } else {
        Write-Host "python $ScriptPath -t "$url" -v -q "$quality""
        python $ScriptPath -t "$url" -v -q "$quality"
    }
} elseif ($media -eq "s")  {
    Write-Host "python $ScriptPath -t "$url" -v -s"
    python $ScriptPath -t "$url" -v -s
} elseif ($media -eq "a")  {
    Write-Host "python $ScriptPath -t "$url" -mp3"
    python $ScriptPath -t "$url" -mp3
} else {
    Write-Host "Invalid media type selected. Please run the script again."
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