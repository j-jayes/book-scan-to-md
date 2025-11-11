# Output Files

This directory (`data/output/`) contains the generated markdown files from your book scans.

## Contents

Each processed PDF will generate a markdown file with the same name:

```
data/output/
├── book1.md
├── book2.md
└── my_scanned_book.md
```

## Markdown Format

The generated files contain:

1. **Title**: Derived from the PDF filename
2. **Content**: All extracted text from the book
3. **Formatting**: 
   - Headings (# ## ###)
   - Bold and italic text
   - Lists and bullet points
   - Tables (when detected)
   - Figure descriptions

## What's Included

✅ All visible text from the PDF  
✅ Preserved document structure  
✅ Clean markdown formatting  

## What's Removed

❌ Page numbers (automatically removed)  
❌ Headers and footers (attempted removal)  
❌ Image quality notes or commentary  

## Post-Processing

After generation, you should:

1. **Review the output**: AI isn't perfect, check for errors
2. **Edit as needed**: Fix any OCR mistakes or formatting issues
3. **Save elsewhere**: Copy to your preferred location if needed

## Example Output

```markdown
# My Book Title

*Generated from book scans using Gemini AI*

---

## Chapter 1: Introduction

This is the beginning of the book...

- Point one
- Point two
- Point three

**Important concept**: Some emphasized text here.

## Chapter 2: Main Content

...
```

## Backup

These files are valuable - consider backing them up or committing them to your repository (they are not ignored by git).

For more information, see the [documentation](../../docs/DOCUMENTATION.md).
