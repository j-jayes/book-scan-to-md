#!/usr/bin/env python3
"""
Batch process multiple PDF files in the data/raw directory.
"""

import sys
from pathlib import Path

from convert_pdf_to_md import process_pdf_to_markdown, setup_gemini


def main():
    """Process all PDF files in data/raw directory."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Batch process all PDFs in data/raw directory"
    )
    parser.add_argument(
        "-m", "--max-pages",
        type=int,
        help="Maximum number of pages to process per PDF"
    )
    
    args = parser.parse_args()
    
    # Find all PDFs in data/raw
    raw_dir = Path("data/raw")
    pdf_files = list(raw_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in data/raw directory")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) to process:")
    for pdf in pdf_files:
        print(f"  - {pdf.name}")
    print()
    
    # Setup Gemini once for all files
    try:
        model = setup_gemini()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    # Process each PDF
    for pdf_path in pdf_files:
        output_path = Path("data/output") / f"{pdf_path.stem}.md"
        
        print(f"\n{'='*60}")
        print(f"Processing: {pdf_path.name}")
        print(f"{'='*60}\n")
        
        try:
            process_pdf_to_markdown(pdf_path, output_path, args.max_pages)
        except Exception as e:
            print(f"Error processing {pdf_path.name}: {e}")
            continue
    
    print(f"\n\n{'='*60}")
    print("Batch processing complete!")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
