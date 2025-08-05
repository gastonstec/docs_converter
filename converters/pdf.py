import pytesseract
from pdf2image import convert_from_path

def pdf_to_text(pdf_path):
    # Convert PDF to images
    pages = convert_from_path(pdf_path, 600)

    # Extract text from each page
    text_data = ''
    for page in pages:
        text = pytesseract.image_to_string(page, lang='spa')
        text_data += text + '\n'

    return text_data


def save_text_to_file(text_data, output_path):
    with open(output_path, "w") as f:
        f.write(text_data)


def convert_pdf(pdf_path, output_path):
    text_data = pdf_to_text(pdf_path)
    save_text_to_file(text_data, output_path)
    print(f"Text extracted and saved to {output_path}")
