#!/usr/bin/env bash
# To be run from a repository root

curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter
chmod +x ./cc-test-reporter
./cc-test-reporter before-build
coverage run -m pytest
coverage xml
./cc-test-reporter after-build --coverage-input-type coverage.py
