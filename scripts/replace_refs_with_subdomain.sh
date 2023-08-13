#!/bin/bash

# Get the directory of the script
SCRIPT_DIR=$(dirname "$0")

# Change to the parent directory
cd "$SCRIPT_DIR/.."


# Replace href="/ with href="/2023.nerdear.la/, and the same with src for images
find app/build/ -type f -name "*.html" -exec sed -i 's#href="/#href="/2023.nerdear.la/#g' {} +
find app/build/ -type f -name "*.html" -exec sed -i 's#src="/#src="/2023.nerdear.la/#g' {} +