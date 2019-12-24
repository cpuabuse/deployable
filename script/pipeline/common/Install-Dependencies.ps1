# To be run from a repository root

param([ValidateNotNullOrEmpty()][string]$File = "requirements.txt")

pip install -r $File; if (-not $?) { throw }