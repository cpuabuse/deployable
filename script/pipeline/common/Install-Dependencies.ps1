# To be run from a repository root

param([ValidateNotNullOrEmpty()][string]$FilePath = Join-Path -Path "." -ChildPath "requirements.txt")

pip install -r $File; if (-not $?) { throw }