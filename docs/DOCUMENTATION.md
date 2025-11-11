# Project Documentation

## Overview

This project provides a streamlined workflow for converting physical book scans into machine-readable markdown format. It's specifically designed to handle the common challenges of phone-camera scans, including variable quality, lighting issues, and perspective distortions.

## Architecture

### Components

1. **PDF Processing** (`pdf2image`)
   - Converts PDF pages to high-resolution images
   - Configurable DPI (default: 300)
   - Preserves image quality for AI processing

2. **AI Processing** (Google Gemini)
   - Multimodal AI model processes images
   - Extracts text with context awareness
   - Understands document structure
   - Removes page numbers automatically

3. **Output Generation**
   - Combines all pages into single markdown file
   - Preserves formatting and structure
   - Clean, readable output

### Data Flow

```
PDF File → Images → Gemini AI → Markdown Text → Combined Output
   ↓          ↓          ↓             ↓              ↓
raw/    processed/   API call    text chunks    output/
```

## Gemini Prompt Engineering

The prompt used for Gemini is carefully crafted to:

1. **Extract all text**: Ensures nothing is missed
2. **Remove page numbers**: Specifically targets common page number locations
3. **Preserve structure**: Maintains headings, lists, and formatting
4. **Format as markdown**: Uses proper markdown syntax
5. **Avoid commentary**: Returns only the content, no notes about quality

### Prompt Template

The prompt instructs Gemini to:
- Use `#` for chapter titles
- Use `##` for section headings
- Use `**bold**` and `*italic*` for emphasis
- Format tables as markdown tables
- Note figures as `[Figure: description]`

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GEMINI_API_KEY` | Yes | - | Your Google Gemini API key |
| `GEMINI_MODEL` | No | `gemini-2.0-flash-exp` | Gemini model to use |
| `MAX_PAGES` | No | - | Limit pages processed (for testing) |

## Directory Structure

### data/raw/
Place your original PDF files here. This directory should only contain input files.

### data/processed/
Intermediate PNG files are stored here during processing. Each PDF gets its own subdirectory named after the PDF file (without extension).

**Note**: These files can be large. Consider adding patterns to `.gitignore` if needed.

### data/output/
Final markdown files are saved here. One markdown file per PDF, using the same base name.

## Script Details

### convert_pdf_to_md.py

Main conversion script with the following functions:

- `setup_gemini()`: Configures API and model
- `pdf_to_images()`: Converts PDF to image files
- `process_image_with_gemini()`: Sends image to API and gets markdown
- `process_pdf_to_markdown()`: Orchestrates the full pipeline
- `main()`: CLI interface

### batch_convert.py

Batch processing script that:
- Finds all PDFs in `data/raw/`
- Processes them sequentially
- Reports progress and errors
- Continues on error (doesn't stop for one failed file)

## Best Practices

### For Input Files

1. **Orientation**: Ensure pages are right-side up
2. **Quality**: Higher quality = better results, but tool handles low quality
3. **Format**: PDF format preferred (other formats may need conversion)

### For Processing

1. **Test First**: Use `--max-pages 2` to verify setup
2. **Monitor Output**: Check first few pages before processing entire book
3. **API Costs**: Be aware of API usage, especially for large books
4. **Batch Wisely**: Don't process too many large files at once

### For Output

1. **Review**: Always manually review generated markdown
2. **Edit**: Fix any OCR errors or formatting issues
3. **Backup**: Keep original PDFs as source of truth

## Limitations

1. **Image Quality**: Very poor quality scans may produce incomplete results
2. **Complex Layouts**: Tables and multi-column layouts may need manual review
3. **Special Characters**: Mathematical formulas or special symbols may not convert perfectly
4. **Languages**: Optimized for English text (may work with other languages)

## Future Enhancements

Potential improvements for future versions:

- [ ] Support for direct image input (not just PDF)
- [ ] OCR confidence scoring
- [ ] Automatic image preprocessing (rotation, contrast adjustment)
- [ ] Multi-language support with language detection
- [ ] Resume capability for interrupted processing
- [ ] Progress saving for large documents
- [ ] Web interface for easier use

## Troubleshooting Guide

### Problem: Poor text extraction
**Solution**: 
- Increase DPI in PDF conversion
- Pre-process images for better contrast
- Try a different Gemini model

### Problem: Page numbers still present
**Solution**:
- Review the prompt to ensure it's clear
- May need manual editing for unusual page number formats

### Problem: Formatting lost
**Solution**:
- Check source image quality
- Review Gemini model capabilities
- May need manual markdown formatting

### Problem: API rate limits
**Solution**:
- Add delays between requests
- Process in smaller batches
- Use MAX_PAGES to limit scope

## Support and Resources

- [Gemini API Documentation](https://ai.google.dev/docs)
- [Markdown Guide](https://www.markdownguide.org/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [pdf2image Documentation](https://github.com/Belval/pdf2image)
