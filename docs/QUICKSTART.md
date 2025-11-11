# Quick Start Guide

Get up and running in 5 minutes!

## 1. Install Prerequisites

### macOS
```bash
brew install poppler
```

### Ubuntu/Debian
```bash
sudo apt-get install poppler-utils
```

### Windows
Download poppler from: https://github.com/oschwartz10612/poppler-windows/releases

## 2. Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 3. Setup Project

```bash
# Clone the repository
git clone https://github.com/j-jayes/book-scan-to-md.git
cd book-scan-to-md

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e .
```

## 4. Configure API Key

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your Gemini API key
# Get your key from: https://makersuite.google.com/app/apikey
nano .env  # or use your preferred editor
```

Your `.env` should look like:
```env
GEMINI_API_KEY=your_actual_api_key_here
GEMINI_MODEL=gemini-2.0-flash-exp
```

## 5. Process Your First Book

```bash
# Place your PDF in data/raw/
cp /path/to/your/book.pdf data/raw/

# Convert it (test with first 2 pages)
python scripts/convert_pdf_to_md.py book.pdf --max-pages 2

# Check the output
cat data/output/book.md
```

## 6. Process Full Book

If the test looks good:

```bash
# Process entire book
python scripts/convert_pdf_to_md.py book.pdf

# Or process all PDFs at once
python scripts/batch_convert.py
```

## Common Commands

```bash
# Process single PDF with custom output
python scripts/convert_pdf_to_md.py mybook.pdf -o custom_name.md

# Batch process with page limit
python scripts/batch_convert.py --max-pages 10

# Clean processed images to save space
make clean
```

## Tips

1. **Always test first**: Use `--max-pages 2` to verify setup
2. **Check image quality**: Look at `data/processed/` images if results are poor
3. **Review output**: AI isn't perfect, always review the markdown
4. **Save costs**: Use MAX_PAGES in .env for testing

## Troubleshooting

- **"GEMINI_API_KEY not set"**: Check your `.env` file
- **"PDF file not found"**: Ensure PDF is in `data/raw/`
- **"poppler not installed"**: Install poppler (see step 1)
- **Import errors**: Run `uv pip install -e .` again

## Next Steps

- Read the [full README](README.md) for detailed documentation
- Check [DOCUMENTATION.md](docs/DOCUMENTATION.md) for architecture details
- Customize the prompt in `scripts/convert_pdf_to_md.py` if needed

Happy scanning! 📚✨
