"""
PDF Reader Challenge using PyMuPDF
"""

import fitz

def read_pdf(file_path):
    doc = fitz.open(file_path)
    all_text = ""

    for page_num in range(len(doc)):
        page_text = doc[page_num].get_text()
        all_text += page_text

    doc.close()
    return all_text

def main():
    file_path = "sample.pdf"
    
    try:
        content = read_pdf(file_path)
        print("-" * 30)
        print(content)
        print("-" * 30)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return


if __name__ == "__main__":
    main()