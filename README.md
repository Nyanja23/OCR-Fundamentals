## Objective
Convert scanned PDF documents into searchable text using Tesseract OCR.

## Technologies
- Python
- Tesseract OCR
- pdf2image
- pytesseract

## Project Structure
- data/pdfs: input scanned PDFs
- output: extracted text
- src: source code

## How to Run
1. Activate virtual environment
2. Install dependencies
3. Run main.py

### OCR Quality Evaluation

We evaluated OCR quality using character count as a quantitative metric.
For a single page:

- Raw image OCR: 2,798 characters
- Thresholded image OCR: 9,651 characters

This represents a ~245% increase in detected characters, demonstrating
that adaptive thresholding significantly improves OCR performance.
