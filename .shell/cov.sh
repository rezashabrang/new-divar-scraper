#!/bin/bash
find . -name 'coverage.txt' -delete
poetry run pytest --cov-report term --cov new_divar_scraper tests/ >>.logs/coverage.txt
