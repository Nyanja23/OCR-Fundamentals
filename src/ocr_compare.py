import pytesseract
from pathlib import Path

RAW_IMAGE = Path('output/images/page_1.png')

PROCESSED_IMAGE = Path('output/images/page_1_thresh.png')


RAW_TEXT_PATH = Path('output/raw_ocr.txt')
PROCESSED_TEXT_PATH = Path('output/processed_ocr.txt')

METRICS_PATH = Path('output/metrics.txt')

TESSERACT_CONFIG = "--oem 1 --psm 6"

def run_ocr(image_path):
    text = pytesseract.image_to_string(str(image_path), config= TESSERACT_CONFIG)

    return text


def character_count(text):

    return sum(1 for c in text  if not c.isspace())


if __name__ == "__main__":
    raw_text = run_ocr(RAW_IMAGE)
    processed_text = run_ocr(PROCESSED_IMAGE)

    RAW_TEXT_PATH.write_text(raw_text, encoding='utf-8')
    PROCESSED_TEXT_PATH.write_text(processed_text, encoding='utf-8')

    raw_count = character_count(raw_text)

    processed_count = character_count(processed_text)

    report = (
        f"Character Count Comparison (Page 1)\n"
        f"----------------------------------\n"
        f"Raw image: {raw_count}\n"
        f"Processed image: {processed_count}\n"
    )

    METRICS_PATH.write_text(report)

    print(report)