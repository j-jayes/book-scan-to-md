#!/usr/bin/env python3
"""
Convert book scans (PDF) to markdown using Gemini 2.5 Flash multimodal AI.
This script processes PDF pages as images and uses Gemini to extract text while
removing page numbers and formatting the content as markdown.
"""

import os
import sys
from pathlib import Path
from typing import Optional

import google.generativeai as genai
from dotenv import load_dotenv
from pdf2image import convert_from_path
from PIL import Image
from tqdm import tqdm


# Load environment variables
load_dotenv()


def setup_gemini() -> genai.GenerativeModel:
    """
    Set up and configure the Gemini API.
    
    Returns:
        Configured GenerativeModel instance
        
    Raises:
        ValueError: If GEMINI_API_KEY is not set
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        raise ValueError(
            "GEMINI_API_KEY not set. Please copy .env.example to .env and add your API key."
        )
    
    genai.configure(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-exp")
    return genai.GenerativeModel(model_name)


def pdf_to_images(pdf_path: Path, output_dir: Path) -> list[Path]:
    """
    Convert PDF pages to images.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save the images
        
    Returns:
        List of paths to the generated images
    """
    print(f"Converting PDF to images: {pdf_path}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Convert PDF to images
    images = convert_from_path(pdf_path, dpi=300)
    
    image_paths = []
    for i, image in enumerate(tqdm(images, desc="Saving images")):
        image_path = output_dir / f"page_{i+1:04d}.png"
        image.save(image_path, "PNG")
        image_paths.append(image_path)
    
    print(f"Converted {len(image_paths)} pages to images")
    return image_paths


def process_image_with_gemini(
    model: genai.GenerativeModel,
    image_path: Path,
    page_num: int
) -> str:
    """
    Process a single image with Gemini to extract text as markdown.
    
    Args:
        model: Configured Gemini model
        image_path: Path to the image file
        page_num: Page number for reference
        
    Returns:
        Extracted text in markdown format
    """
    prompt = """Extract all text from this book page image and convert it to markdown format.

Instructions:
1. Extract ALL visible text from the page
2. Remove any page numbers (typically at top or bottom of page)
3. Preserve the structure and formatting using markdown:
   - Use # for chapter titles
   - Use ## for section headings
   - Use ### for subsections
   - Use **bold** for emphasized text
   - Use *italic* for italicized text
   - Use bullet points (-) for lists
   - Preserve paragraph breaks
4. Do NOT add any commentary or notes about the image quality
5. Do NOT include page numbers in the output
6. If there are tables, format them as markdown tables
7. If there are images or figures, note them as: [Figure: brief description]

Output only the markdown text, nothing else."""

    try:
        # Load and process the image
        image = Image.open(image_path)
        
        # Generate content
        response = model.generate_content([prompt, image])
        
        return response.text
    except Exception as e:
        print(f"Error processing page {page_num}: {e}")
        return f"\n\n[Error processing page {page_num}: {e}]\n\n"


def process_pdf_to_markdown(
    pdf_path: Path,
    output_path: Path,
    max_pages: Optional[int] = None
) -> None:
    """
    Process entire PDF and convert to markdown.
    
    Args:
        pdf_path: Path to the input PDF file
        output_path: Path to the output markdown file
        max_pages: Maximum number of pages to process (None for all)
    """
    # Setup
    model = setup_gemini()
    
    # Create processed images directory
    processed_dir = Path("data/processed") / pdf_path.stem
    
    # Convert PDF to images
    image_paths = pdf_to_images(pdf_path, processed_dir)
    
    # Limit pages if specified
    if max_pages:
        image_paths = image_paths[:max_pages]
        print(f"Processing first {max_pages} pages only")
    
    # Process each image
    markdown_content = []
    markdown_content.append(f"# {pdf_path.stem}\n\n")
    markdown_content.append("*Generated from book scans using Gemini AI*\n\n")
    markdown_content.append("---\n\n")
    
    for i, image_path in enumerate(tqdm(image_paths, desc="Processing pages"), start=1):
        text = process_image_with_gemini(model, image_path, i)
        markdown_content.append(text)
        markdown_content.append("\n\n")
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(markdown_content))
    print(f"\nMarkdown file saved to: {output_path}")


def main():
    """Main entry point for the script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Convert book scans (PDF) to markdown using Gemini AI"
    )
    parser.add_argument(
        "pdf_path",
        type=Path,
        help="Path to the PDF file (relative to data/raw/ or absolute path)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output markdown file path (default: data/output/<pdf_name>.md)"
    )
    parser.add_argument(
        "-m", "--max-pages",
        type=int,
        help="Maximum number of pages to process"
    )
    
    args = parser.parse_args()
    
    # Resolve PDF path
    if not args.pdf_path.is_absolute():
        pdf_path = Path("data/raw") / args.pdf_path
    else:
        pdf_path = args.pdf_path
    
    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)
    
    # Resolve output path
    if args.output:
        output_path = args.output
    else:
        output_path = Path("data/output") / f"{pdf_path.stem}.md"
    
    # Get max_pages from args or environment
    max_pages = args.max_pages
    if max_pages is None:
        max_pages_env = os.getenv("MAX_PAGES")
        if max_pages_env:
            max_pages = int(max_pages_env)
    
    # Process the PDF
    try:
        process_pdf_to_markdown(pdf_path, output_path, max_pages)
        print("\n✓ Processing complete!")
    except ValueError as e:
        print(f"\nError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
