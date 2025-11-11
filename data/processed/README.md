# Processed Files

This directory (`data/processed/`) contains intermediate image files generated during PDF processing.

## Structure

When you convert a PDF, the script will:

1. Create a subdirectory named after your PDF file (without extension)
2. Extract each page as a PNG image (300 DPI by default)
3. Save images with names like `page_0001.png`, `page_0002.png`, etc.

## Example

```
data/processed/
└── my_book/
    ├── page_0001.png
    ├── page_0002.png
    ├── page_0003.png
    └── ...
```

## Storage Considerations

These image files can be quite large (several MB per page at 300 DPI).

**To save disk space:**
```bash
# Remove processed images for all books
make clean

# Or manually
rm -rf data/processed/*
```

## Purpose

These intermediate files allow you to:
- Inspect image quality if OCR results are poor
- Re-run processing without re-converting the PDF
- Manually edit images if needed before processing

**Note:** These files are automatically ignored by git (not committed to the repository).
