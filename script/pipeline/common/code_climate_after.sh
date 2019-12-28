#!/usr/bin/env bash
# To be run from a repository root

# Report coverage
./cc-test-reporter after-build --coverage-input-type coverage.py
