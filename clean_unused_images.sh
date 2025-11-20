#!/bin/bash

# Find all image files in the images directory
find images -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.gif" -o -iname "*.webp" -o -iname "*.svg" \) > /tmp/all_images.txt

# Create a temporary file to store referenced images
> /tmp/referenced_images.txt

# Search for image references in all markdown files
for mdfile in *.md; do
    if [ -f "$mdfile" ]; then
        # Extract image references from markdown files
        grep -oE '\([^)]*\.(png|jpg|jpeg|gif|webp|svg)\)' "$mdfile" | sed 's/[()]//g' >> /tmp/referenced_images.txt
        grep -oE '!\[.*\]\([^)]*\)' "$mdfile" | sed -E 's/.*$$([^)]*)$$.*/\1/' >> /tmp/referenced_images.txt
        # Handle HTML img tags
        grep -oE '<img[^>]+src="[^"]*"' "$mdfile" | sed -E 's/.*src="([^"]*)".*/\1/' >> /tmp/referenced_images.txt
    fi
done

# Normalize paths (remove leading ./ if present)
sed -i 's/^\.\///' /tmp/referenced_images.txt

# Find unreferenced images
comm -23 <(sort /tmp/all_images.txt) <(sort /tmp/referenced_images.txt) > /tmp/unreferenced_images.txt

# Display the files that would be removed
echo "The following unreferenced images will be removed:"
cat /tmp/unreferenced_images.txt

# Remove the unreferenced files from git
if [ -s /tmp/unreferenced_images.txt ]; then
    while IFS= read -r file; do
        if [ -f "$file" ]; then
            git rm "$file"
            echo "Removed $file from git"
        fi
    done < /tmp/unreferenced_images.txt
else
    echo "No unreferenced images found"
fi

# Clean up temporary files
rm -f /tmp/all_images.txt /tmp/referenced_images.txt /tmp/unreferenced_images.txt