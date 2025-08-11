######################################################################################
# install script with PowerShell for Youtube-Downloader
######################################################################################

# Paths
$ProjectPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
$VenvPath = Join-Path $ProjectPath "venv"
$Requirements = Join-Path $ProjectPath "requirements.txt"

# Check Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python."
    Pause
    Exit
}

# install de ffmpeg
if (Get-Command ffmpeg -ErrorAction SilentlyContinue) {
    Write-Host "ffmpeg not installed."
} else {
    Write-Host "ffmpeg not installed or not in the PATH."
}

# install de ffmpeg
if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    Write-Host "ffmpeg not installed or not in the PATH."
    Write-Host "Attempting to install ffmpeg with winget..."
    winget install -e --id Gyan.FFmpeg
    # reloading the path
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
    # After installation, check again
    if (Get-Command ffmpeg -ErrorAction SilentlyContinue) {
        Write-Host "ffmpeg has been installed successfully."
    } else {
        Write-Host "ffmpeg installation failed. Please install it manually."
        Pause
        Exit
    }
}

# Create virtual environment if needed
if (-not (Test-Path $VenvPath)) {
    Write-Host "Creating virtual environment..."
    python -m venv $VenvPath
}

# Activate the virtual environment
$activate = Join-Path $VenvPath "Scripts\Activate.ps1"
Write-Host "Activating virtual environment..."
& $activate

# Upgrade pip
Write-Host "Upgrading pip... if required"
python -m pip install --upgrade pip

# Install dependencies
if (Test-Path $Requirements) {
    Write-Host "Installing dependencies..."
    pip install -r $Requirements
} else {
    Write-Host "requirements.txt not found, no dependencies installed."
}

Write-Host "---------------------------------------------------------------"
Write-Host "All required packages are installed."
Write-Host "Now please use the .py script or the other PowerShell scripts."

Pause
######################################################################################