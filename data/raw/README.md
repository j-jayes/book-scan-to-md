# Place Your PDF Files Here

This directory (`data/raw/`) is where you should place your book scan PDF files.

## Instructions

1. Copy your PDF files into this directory:
   ```bash
   cp /path/to/your/book.pdf data/raw/
   ```

2. Run the conversion script:
   ```bash
   python scripts/convert_pdf_to_md.py your_book.pdf
   ```

3. Find the output in `data/output/your_book.md`

## Supported Formats

- PDF files (`.pdf`)
- Any PDF containing scanned pages or images

## Tips

- Use descriptive filenames (they'll be used for output files)
- You can process multiple PDFs at once with `batch_convert.py`
- For large books, test with `--max-pages 2` first

## Example

```bash
# Place PDF
cp "My Scanned Book.pdf" data/raw/

# Convert it
python scripts/convert_pdf_to_md.py "My Scanned Book.pdf"

# Check output
cat "data/output/My Scanned Book.md"
```

For more details, see the [Quick Start Guide](../../docs/QUICKSTART.md).
