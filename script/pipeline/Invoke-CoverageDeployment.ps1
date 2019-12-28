# Start-Pipeline
. $(Join-Path -Path $PSScriptRoot -ChildPath "common" "Start-Pipeline.ps1" -Resolve)

# Install-Dependencies
& $Paths.InstallDependencies -FilePath $Paths.RequirementsPath

# Executable name
[ValidateNotNullOrEmpty()][String]$ExecutablePath = Join-Path -Path "." -ChildPath "cc-test-reporter"

# Url location
[ValidateNotNullOrEmpty()][String]$CodeClimateUrl = "https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64"

# Download reporter
Invoke-WebRequest -Uri $CodeClimateUrl -OutFile $Executable

# Code Climate prepare; Invoke via bash script as it bugs if run from the PS
bash $Paths.CodeClimateBefore; if (-not $?) { throw }

# Run coverage
coverage run -m pytest; if (-not $?) { throw }

# Generate XML for Code Climate
coverage xml; if (-not $?) { throw }

# Code Climate deploy; Invoke via bash script as it bugs if run from the PS
bash $Paths.CodeClimateAfter; if (-not $?) { throw }

# Stop-Pipeline
$Paths.StopPipeline