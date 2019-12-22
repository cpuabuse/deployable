# File is to be dot-sourced

$ErrorActionPreference = "Stop"

if ($null -eq (Get-Variable -Name "StartPipeline" -Scope "Script" -ErrorAction "Ignore")) {
	# Guard
	New-Variable -Name "StartPipeline" -Scope "Script"

	Push-Location -Path $(Join-Path -Path $PSScriptRoot -ChildPath ".." ".." -Resolve)

	[ValidateNotNull()][hashtable]$script:Paths += @{
		DeployCoverage      = Join-Path -Path "./" -ChildPath "script" "common" "Deploy-Coverage.ps1" -Resolve;
		InstallDependencies = Join-Path -Path "./" -ChildPath "script" "common" "Install-Dependencies.ps1" -Resolve;
		StopPipeline        = Join-Path -Path "./" -ChildPath "script" "common" "Stop-Pipeline.ps1" -Resolve;
		RequirementsPath    = Join-Path -Path "./" -ChildPath "requirements" "dev.txt" -Resolve
	}
}