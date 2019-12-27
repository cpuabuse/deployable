# File is to be dot-sourced

$ErrorActionPreference = "Stop"

if ($null -eq (Get-Variable -Name "StartPipeline" -Scope "Script" -ErrorAction "Ignore")) {
	# Guard
	New-Variable -Name "StartPipeline" -Scope "Script"

	Push-Location -Path $(Join-Path -Path $PSScriptRoot -ChildPath ".." ".." "..")

	[ValidateNotNull()][hashtable]$script:Paths += @{
		DeployCoverage      = Join-Path -Path "script" -ChildPath "pipeline" "common" "Deploy-Coverage.ps1";
		InstallDependencies = Join-Path -Path "script" -ChildPath "pipeline" "common" "Install-Dependencies.ps1";
		StopPipeline        = Join-Path -Path "script" -ChildPath "pipeline" "common" "Stop-Pipeline.ps1";
		RequirementsPath    = Join-Path -Path "requirements" -ChildPath "dev.txt"
	}
}