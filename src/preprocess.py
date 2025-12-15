import cv2
from pdf2image import convert_from_path
from pathlib import Path
import numpy as np

PDF_PATH = Path('data/pdfs/sample.pdf')

OUTPUT_DIR = Path('output/images')

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def pdf_to_grayscale_images(pdf_path):

    pages = convert_from_path(pdf_path)

    for i, page in enumerate(pages):

        open_cv_image = np.array(page)

        # img = cv2.cvtColor(
        #     cv2.imread(page.filename),
        #     cv2.COLOR_BGR2GRAY
        # )

        gray_img = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2GRAY)

        out_path = OUTPUT_DIR / f" page_{i+1}.png"

        cv2.imwrite(str(out_path), gray_img)

        print(f"Saved grayscale imge: {out_path}")


if __name__ == '__main__':
    pdf_to_grayscale_images(PDF_PATH)