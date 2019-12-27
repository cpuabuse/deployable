# Start-Pipeline
. $(Join-Path -Path $PSScriptRoot -ChildPath "common" "Start-Pipeline.ps1" -Resolve)

# Install-Dependencies
& $Paths.InstallDependencies -FilePath $Paths.RequirementsPath

# Coverage
& $Paths.DeployCoverage

# Stop-Pipeline
$Paths.StopPipeline