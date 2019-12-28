#!/usr/bin/env pwsh
# Deploy Code Climate pipeline.
# Currently supports only Linux and Windows with WSL deployment.

# Start-Pipeline
. $(Join-Path -Path $PSScriptRoot -ChildPath "common" "Start-Pipeline.ps1" -Resolve)

# Executable name; Url location; Download reporter
[ValidateNotNullOrEmpty()][String]$ExecutablePath = Join-Path -Path "." -ChildPath "cc-test-reporter"
[ValidateNotNullOrEmpty()][String]$CodeClimateUrl = "https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64"
Invoke-WebRequest -Uri $CodeClimateUrl -OutFile $ExecutablePath
if (-not $IsWindows) {
	chmod +x $ExecutablePath
}

# Set WSL vars
$ExecutableBashPath = if ($IsWindows) { $ExecutablePath -replace '\\', '/' } else { $ExecutablePath }
$InstallDependencies = if ($IsWindows) { $Paths.InstallDependencies -replace '\\', '/' } else { $Paths.InstallDependencies }
$RequirementsPath = if ($IsWindows) { $Paths.RequirementsPath -replace '\\', '/' } else { $Paths.RequirementsPath }

# Invokes bash scripts
function Invoke-PipelineCommand {
	param([String[]]$Arguments)

	# Make sure we have what to call
	if ($Arguments.Count -eq 0) {
		throw
	}

	if ($IsWindows) {
		& $Paths.InvokeBashWrapper -Argument ($Arguments -join " ")
	}
	else {
		# $Rest would be assigned to empty string if $Arguments has one element, but the behaviour is not documented, so no validation on $Rest
		[ValidateNotNullOrEmpty()][String]$First, [String[]]$Rest = $Arguments
		& $First $Rest
	}
}

# Install-Dependencies
Invoke-PipelineCommand -Arguments @($InstallDependencies, "-FilePath", $RequirementsPath)

# Code Climate prepare; Invoked using bash script as it bugs if run from the PS
& $Paths.InvokeBashWrapper -Argument "$ExecutableBashPath before-build"

# Run coverage
Invoke-PipelineCommand -Arguments @("coverage", "run", "-m", "pytest")

# Generate XML for Code Climate
Invoke-PipelineCommand -Arguments @("coverage", "xml")

# Code Climate deploy; Invoked using bash script as it bugs if run from the PS
& $Paths.InvokeBashWrapper  -Argument "$ExecutableBashPath after-build --coverage-input-type coverage.py"

# Stop-Pipeline
& $Paths.StopPipeline