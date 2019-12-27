# To be run from a repository root

# Executable name
[ValidateNotNullOrEmpty()][String]$ExecutablePath = Join-Path -Path "." -ChildPath "cc-test-reporter" -Resolve;

# Url location
[ValidateNotNullOrEmpty()][String]$CodeClimateUrl = "https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64"

# Download reporter
Invoke-WebRequest -Uri $CodeClimateUrl -OutFile $Executable

# Deploy
& $ExecutablePath "before-build"

# Run test
coverage run -m pytest

& $ExecutablePath "after-build" --input-type "coverage.py" --exit-code $?