# To be run from a repository root

# Executable name
[ValidateNotNullOrEmpty()][String]$Executable = "cc-test-reporter"

# Url location
[ValidateNotNullOrEmpty()][String]$CodeClimateUrl = "https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64"

# Download reporter
Invoke-WebRequest -Uri $CodeClimateUrl -OutFile $Executable

# Deploy
& $Executable "before-build"

# Run test
coverage run -m pytest

& $Executable "after-build" --input-type "coverage.py" --exit-code $?