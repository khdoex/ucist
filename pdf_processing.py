from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

# Usage
text = extract_text_from_pdf('path_to_your_pdf_file.pdf')
print(text)
