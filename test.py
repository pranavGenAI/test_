import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import io
import streamlit as st

# Path to your PDF file
pdf_path = 'XYZ Consulting_withimage.pdf'

# Function to extract text from images
def ocr_image(image):
    text = pytesseract.image_to_string(image)
    return text

# Initialize text storage variable
text_ = ""

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Loop through each page
for page_num in range(len(pdf_document)):
    # Get the page
    page = pdf_document.load_page(page_num)
    
    # Extract text directly from the page
    text_ += page.get_text()
    
    # Extract images from the page
    images = page.get_images(full=True)
    
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        # Open the image with PIL
        image = Image.open(io.BytesIO(image_bytes))
        
        # Perform OCR on the image
        text_ += ocr_image(image)

# Close the PDF document
pdf_document.close()

# Print or use the extracted text stored in text_
print(text_)

st.write(text_)
