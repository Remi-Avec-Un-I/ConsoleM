#!/bin/bash

# Build the documentation
cd docs
make html

# Create a temporary directory
cd ..
TEMP_DIR=$(mktemp -d)

# Copy the built documentation
cp -r docs/_build/html/* $TEMP_DIR/

# Create .nojekyll file
touch $TEMP_DIR/.nojekyll

# Create index.html
cat > $TEMP_DIR/index.html << EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>ConsoleM Documentation</title>
    <meta http-equiv="refresh" content="0; url=index.html">
</head>
<body>
    <p>Redirecting to ConsoleM documentation...</p>
</body>
</html>
EOF

# Switch to gh-pages branch
git checkout gh-pages

# Remove all files except .git
git rm -rf *

# Copy the new documentation
cp -r $TEMP_DIR/* .

# Add and commit the changes
git add .
git commit -m "Update documentation"

# Push to GitHub
git push origin gh-pages

# Clean up
rm -rf $TEMP_DIR

# Switch back to the original branch
git checkout - 