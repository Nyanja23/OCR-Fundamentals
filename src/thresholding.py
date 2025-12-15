import cv2
import numpy as np

from pdf2image import convert_from_path

from pathlib import Path

PDF_PATH = Path("data/pdfs/sample.pdf")
OUTPUT_DIR = Path("output/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def pre_process_page(pil_image):
    # from  PIL to NUMPY
    img = np.array(pil_image)

    # from RGB to GrayScale 

    if len(img.shape) == 3:
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        gray_img = img

     # Ensure uint8
    new_gray_img = gray_img.astype("uint8")


    #Adapting thresholding

    thresh = cv2.adaptiveThreshold(
        new_gray_img,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return thresh

def pdf_to_processed_images(pdf_path):
    pages = convert_from_path(pdf_path, dpi=300) #Higher DPI = much better OCR results

    for i, page in enumerate(pages):
        processed = pre_process_page(page)

        out_path = OUTPUT_DIR/ f"page_{i+1}_thresh.png"
        cv2.imwrite(str(out_path), processed)

        print(f"Saved processed image: {out_path}")


if __name__ == "__main__":
    pdf_to_processed_images(PDF_PATH)