from docx import Document

def docx_to_text(docx_path):
    doc = Document(docx_path)
    return ' '.join([paragraph.text for paragraph in doc.paragraphs])

# Usage
text = docx_to_text('path_to_your_docx_file.docx')
print(text)
