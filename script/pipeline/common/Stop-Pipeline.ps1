# File is to be dot-sourced

if ($null -ne (Get-Variable -Name "StartPipeline" -Scope "Script" -ErrorAction "Ignore")) {
	# Remove Paths var
	Remove-Variable -Name "Paths" -Scope "Script"
	
	# Return location
	Pop-Location

	# Guard
	Remove-Variable -Name "StartPipeline" -Scope "Script"
}