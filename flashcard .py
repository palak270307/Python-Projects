import streamlit as st
import pdfplumber
import pytesseract
from PIL import Image
import io
import random

st.title("📚 PDF To Flashcard Converter ")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
def extract_text_from_pdf(pdf_file):
    text =" "
    with pdfplumber.open(pdf_file)as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() + "\n"
            if page_text:
                text += page_text + "\n"
                return text 
def extract_images_from_pdf(pdf_file):
    images = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            for img in page.images:
                x0,top,x1,bottom = img["x0"], img["top"], img["x1"], img["bottom"]
                im = page.crop((x0, top, x1, bottom)) .to_image(resolution=300)
                img_bytes = im.BytesIO()
                im.save(img_bytes, format="PNG")
                images.append(Image.open(io.Bytes.IO(img_bytes.getvalue())))
                return images

def generate_flashcards(text, images):
    flashcards = []
    sentences = text.split(".")  
    for sentence in sentences:
        if len(sentence.split()) > 5:
            flashcards.append({"question": sentence.strip(), "answer": "Define the above concept."})

            for img in images:
                ocr_text = pytesseract.image_to_string(img)   # Extract text from image using OCR
                if ocr_text.strip():
                    flashcards.append({"question": ocr_text.strip(), "answer": "Expalin the above image." })
                    random.shuffle(flashcards)
                    return flashcards
                
                if uploaded_file is not None:
                    st.success("File uploaded successfully!")
                    text = extract_text_from_pdf(uploaded_file)
                    images = extract_images_from_pdf(uploaded_file)

                    flashcards = generate_flashcards(text, images)
                    st.subheader("Generate Flashcards")
                    for i,card in enumerate(flashcards[:10]):
                        st.write(f"**Q{i+1}:** {card['question']}")
                        with st.expander("Show Answer"):
                            st.write(f"**A{i+1}:** {card['answer']}")



    
