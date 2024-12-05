import os
from paddleocr import PaddleOCR
import re

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

# Paths
input_folder = 'E:/python_projects/NumberDetection/image_folder'

# Process each image
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
        image_path = os.path.join(input_folder, filename)
        print(f"Processing file: {filename}")

        try:
            # Perform OCR
            result = ocr.ocr(image_path, cls=True)

            # If OCR returns no result, handle it
            if result is None or len(result) == 0:
                print(f"No text detected in {filename}.")
                continue

            # Collect text from all detected lines and filter for numeric characters only
            extracted_text = ''.join([line[1][0].replace(' ', '') for line in result[0]])

            # Filter out non-numeric characters using regular expressions
            numeric_text = ''.join(re.findall(r'\d+', extracted_text))

            # Print the cleaned numeric result
            print(f"Extracted Numeric Text from {filename}: {numeric_text}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")
    else:
        print(f"Skipping unsupported file: {filename}")

print("\nProcessing completed.")
