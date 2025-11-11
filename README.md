# Book Scan to Markdown

Convert scanned book pages (PDF format) to markdown using Google's Gemini 2.5 Flash multimodal AI. This tool is designed to handle phone camera scans and produces clean, machine-readable markdown output with automatic page number removal.

## Features

- 📱 Handles low-quality phone camera scans
- 🤖 Uses Gemini 2.5 Flash multimodal AI for OCR and text extraction
- 📄 Automatic page number removal
- ✨ Preserves document structure (headings, lists, formatting)
- 📝 Outputs clean markdown format
- 🔄 Supports batch processing of multiple PDFs
- ⚙️ Configurable via environment variables

## Project Structure

```
book-scan-to-md/
├── data/
│   ├── raw/              # Place your PDF files here
│   ├── processed/        # Intermediate image files (auto-generated)
│   └── output/           # Generated markdown files
├── scripts/
│   ├── convert_pdf_to_md.py  # Main conversion script
│   └── batch_convert.py      # Batch processing script
├── docs/                 # Documentation
├── .env.example          # Environment variable template
├── pyproject.toml        # Python project configuration
└── README.md             # This file
```

## Setup

### Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)
- Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- `poppler-utils` for PDF processing:
  - **Ubuntu/Debian**: `sudo apt-get install poppler-utils`
  - **macOS**: `brew install poppler`
  - **Windows**: Download from [poppler website](https://github.com/oschwartz10612/poppler-windows/releases)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/j-jayes/book-scan-to-md.git
   cd book-scan-to-md
   ```

2. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Create and activate virtual environment**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   uv pip install -e .
   ```

5. **Configure environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your Gemini API key
   ```

## Usage

### Single PDF Conversion

Place your PDF file in the `data/raw/` directory, then run:

```bash
python scripts/convert_pdf_to_md.py your_book.pdf
```

This will generate `data/output/your_book.md`.

**Options**:
- `-o, --output PATH`: Specify custom output path
- `-m, --max-pages N`: Process only the first N pages (useful for testing)

**Examples**:

```bash
# Process entire PDF
python scripts/convert_pdf_to_md.py my_book.pdf

# Process only first 5 pages
python scripts/convert_pdf_to_md.py my_book.pdf --max-pages 5

# Custom output location
python scripts/convert_pdf_to_md.py my_book.pdf -o custom_output.md

# Use absolute path
python scripts/convert_pdf_to_md.py /path/to/your/book.pdf
```

### Batch Processing

To process all PDFs in the `data/raw/` directory:

```bash
python scripts/batch_convert.py
```

**Options**:
- `-m, --max-pages N`: Process only the first N pages of each PDF

### Processing Pipeline

The script follows this pipeline:

1. **PDF to Images**: Converts each page to a high-resolution PNG (300 DPI)
2. **AI Processing**: Each image is sent to Gemini with instructions to:
   - Extract all text
   - Remove page numbers
   - Format as markdown with proper structure
   - Preserve formatting (bold, italic, headings, lists)
3. **Markdown Output**: Combines all pages into a single markdown file

## Configuration

Edit `.env` file to customize behavior:

```env
# Your Gemini API Key (required)
GEMINI_API_KEY=your_api_key_here

# Maximum pages to process (optional, leave empty for all)
MAX_PAGES=

# Gemini model to use (default: gemini-2.0-flash-exp)
GEMINI_MODEL=gemini-2.0-flash-exp
```

## Tips for Best Results

1. **Image Quality**: While the tool handles low-quality scans, better quality images produce better results
2. **Page Orientation**: Ensure pages are right-side up
3. **Test First**: Use `--max-pages 2` to test on a few pages before processing an entire book
4. **Review Output**: Always review the generated markdown for accuracy
5. **API Limits**: Be aware of Gemini API rate limits for large books

## Troubleshooting

### "GEMINI_API_KEY not set"
- Ensure you've copied `.env.example` to `.env`
- Add your API key to the `.env` file
- Don't commit `.env` to version control

### "PDF file not found"
- Check that your PDF is in `data/raw/` directory
- Verify the filename is correct
- Use absolute paths if the file is elsewhere

### Poor OCR Results
- Try increasing DPI in `pdf_to_images()` function (default: 300)
- Ensure source images are clear and properly oriented
- Consider pre-processing images for better contrast

### Import Errors
- Ensure virtual environment is activated
- Run `uv pip install -e .` to install dependencies

## Development

### Install Development Dependencies

```bash
uv pip install -e ".[dev]"
```

### Code Formatting

```bash
black scripts/
ruff scripts/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Uses [Google Gemini](https://deepmind.google/technologies/gemini/) for multimodal AI processing
- Built with [uv](https://github.com/astral-sh/uv) for fast Python package management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.