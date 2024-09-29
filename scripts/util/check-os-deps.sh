#!/bin/bash

declare -a programs=("python3" "npm" "pyenv" "shfmt" "shellcheck" "mkvirtualenv")

## now loop through the above array
for program in "${programs[@]}"; do
    if ! command -v "${program}" > /dev/null 2>&1; then
        echo "${program} should be there."
        exit 1
    fi
done
