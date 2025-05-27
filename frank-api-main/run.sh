#!/usr/bin/env bash

set -uvx
poetry run python --version
poetry run pwd
poetry run python frank_api_main.py
exit_status=$?
echo "app.py exited with status: [$exit_status]"
date
exit $exit_status
