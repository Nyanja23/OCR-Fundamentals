import pytesseract
from pathlib import Path

IMAGE_PATH = Path("output/images/page_1_thresh.png")
OUTPUT_DIR = Path("output")

PSM_VALUES = [3, 6, 11, 12]
OEM = 1

def character_count(text):
    return sum(1 for c in text if not c.isspace())

def run_psm_experiment():
    results = []

    for psm in PSM_VALUES:
        config = f"--oem {OEM} --psm {psm}"
        text = pytesseract.image_to_string(str(IMAGE_PATH), config=config)

        output_file = OUTPUT_DIR / f"psm_{psm}.txt"
        output_file.write_text(text, encoding="utf-8")

        count = character_count(text)
        results.append((psm, count))

    return results

if __name__ == "__main__":
    results = run_psm_experiment()

    report_lines = [
        "PSM Experiment (Processed Image - Page 1)",
        "----------------------------------------"
    ]

    for psm, count in results:
        report_lines.append(f"PSM {psm}: {count} characters")

    report = "\n".join(report_lines)
    (OUTPUT_DIR / "psm_metrics.txt").write_text(report)

    print(report)
