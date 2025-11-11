# Example Usage

This file shows example usage patterns for the book-scan-to-md tool.

## Basic Usage

### 1. Setup
```bash
# Install dependencies
uv venv
source .venv/bin/activate
uv pip install -e .

# Configure API key
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### 2. Single PDF Conversion
```bash
# Place PDF in data/raw/
cp my_book.pdf data/raw/

# Convert (test with 2 pages first)
python scripts/convert_pdf_to_md.py my_book.pdf --max-pages 2

# Check output
cat data/output/my_book.md

# If it looks good, process full book
python scripts/convert_pdf_to_md.py my_book.pdf
```

### 3. Batch Processing
```bash
# Place multiple PDFs in data/raw/
cp book1.pdf book2.pdf book3.pdf data/raw/

# Process all of them
python scripts/batch_convert.py

# Or with page limit for testing
python scripts/batch_convert.py --max-pages 5
```

### 4. Custom Output Location
```bash
# Save to specific location
python scripts/convert_pdf_to_md.py my_book.pdf -o /path/to/output.md
```

## Environment Variables

You can control behavior via .env file:

```env
# Required
GEMINI_API_KEY=your_api_key_here

# Optional
MAX_PAGES=10                    # Process only first 10 pages
GEMINI_MODEL=gemini-2.0-flash-exp  # Model to use
```

## Python API Usage

You can also import and use the functions in your own scripts:

```python
from pathlib import Path
from scripts.convert_pdf_to_md import (
    setup_gemini,
    pdf_to_images,
    process_image_with_gemini,
    process_pdf_to_markdown
)

# Setup
model = setup_gemini()

# Convert PDF to images
pdf_path = Path("data/raw/my_book.pdf")
processed_dir = Path("data/processed/my_book")
image_paths = pdf_to_images(pdf_path, processed_dir)

# Process single image
text = process_image_with_gemini(model, image_paths[0], page_num=1)
print(text)

# Or process entire PDF
output_path = Path("data/output/my_book.md")
process_pdf_to_markdown(pdf_path, output_path, max_pages=None)
```

## Common Workflows

### Workflow 1: Process a new book
```bash
# 1. Add PDF
cp new_book.pdf data/raw/

# 2. Test first few pages
python scripts/convert_pdf_to_md.py new_book.pdf --max-pages 3

# 3. Review output
cat data/output/new_book.md

# 4. If good, process full book
python scripts/convert_pdf_to_md.py new_book.pdf

# 5. Clean up intermediate files to save space
make clean
```

### Workflow 2: Batch process a collection
```bash
# 1. Add all PDFs to data/raw/
cp *.pdf data/raw/

# 2. Test with limited pages
python scripts/batch_convert.py --max-pages 2

# 3. Check a few outputs
ls -lh data/output/

# 4. Process full collection
python scripts/batch_convert.py

# 5. Archive outputs
tar -czf book_collection.tar.gz data/output/*.md
```

### Workflow 3: Iterate on a difficult page
```bash
# If a particular page has issues, you can:
# 1. Extract just that page as separate PDF
# 2. Pre-process the image for better quality
# 3. Run conversion again
# 4. Manually edit the output markdown

# Example:
python scripts/convert_pdf_to_md.py problem_page.pdf --max-pages 1
# Review and edit data/output/problem_page.md as needed
```

## Makefile Commands

```bash
make help        # Show available commands
make setup       # Create virtual environment
make install     # Install dependencies
make clean       # Remove processed images
make clean-all   # Remove all generated files
make format      # Format code with black
make lint        # Run linters
```

## Tips for Best Results

1. **Test first**: Always use `--max-pages 2` initially
2. **Check quality**: If results are poor, check `data/processed/` images
3. **Edit manually**: AI isn't perfect, review and edit the output
4. **Save space**: Use `make clean` to remove intermediate images
5. **Backup originals**: Keep your PDF files safe

## Troubleshooting Examples

### Problem: Page numbers still appearing
```bash
# The prompt should handle this, but if not:
# 1. Check the generated markdown
# 2. Use find/replace to remove remaining page numbers
# 3. Or modify the prompt in convert_pdf_to_md.py
```

### Problem: Poor text extraction
```bash
# Try increasing DPI for better quality:
# Edit scripts/convert_pdf_to_md.py
# Change: images = convert_from_path(pdf_path, dpi=300)
# To:     images = convert_from_path(pdf_path, dpi=600)
```

### Problem: Rate limiting
```bash
# Add delays between API calls:
# Edit scripts/convert_pdf_to_md.py
# Add: import time
# Add: time.sleep(2)  # After each API call
```
