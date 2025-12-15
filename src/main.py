from pdf2image import convert_from_path
import pytesseract
from pathlib import Path

# Take a scanned PDF → turn each page into an image → run OCR → save the text

PDF_PATH = Path('data/pdfs/sample.pdf')
OUTPUT_PATH = Path('output/result.txt')

def ocr_pdf(pdf_path):
    pages = convert_from_path(pdf_path) #Reads the PDF, Converts each page into a PIL Image, Returns a list of images, eg: pages = [page1_image, page2_image, page3_image]
    extracted_text = ""

    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        extracted_text += f"\n--- Page {i + 1} ---\n{text}"

    return extracted_text

def save_text(text, output_path):
    output_path.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    text = ocr_pdf(PDF_PATH)
    save_text(text, OUTPUT_PATH)
    print("OCR complete. Text saved to output/result.txt")