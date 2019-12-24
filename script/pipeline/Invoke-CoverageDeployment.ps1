# Start-Pipeline
. $(Join-Path -Path $PSScriptRoot -ChildPath "common" "Start-Pipeline.ps1" -Resolve)

# Install-Dependencies
& $Paths.InstallDependencies -File $Paths.RequirementsPath

# Coverage
& $Paths.DeployCoverage; if (-not $?) { throw }

# Stop-Pipeline
$Paths.StopPipeline