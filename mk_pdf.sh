markdowns=$(find . -type f -name "*.md" ! -name "README.md")

for path in $markdowns; do
  if [ -s "$path" ]; then
    save_path=doc/pdfs
    filename="${path##*/}"   # Extract filename from path
    filename="${filename%.md}" # Remove .md extension
    pandoc "$path" -o "$save_path/$filename.pdf" --from markdown --template eisvogel --listings
  fi 
done
