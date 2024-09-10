import pdfplumber
import re

def extract_info_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    # Funciones para extracción
    def extract_email(text):
        match = re.search(r'[\w\.-]+@[\w\.-]+', text)
        return match.group(0) if match else "No encontrado"

    def extract_phone(text):
        match = re.search(r'(\+\d{1,3}\s?\d{1,3}[\s-]?\d{3}[\s-]?\d{3,4}[\s-]?\d{3,4})', text)
        return match.group(0) if match else "No encontrado"

    def extract_name(text):
        match = re.search(r'(KEVIN MENESES GONZÁLEZ)', text, re.IGNORECASE)
        return match.group(0).strip() if match else "No encontrado"

    def extract_skills(text):
        match = re.search(r'SKILLS\s*(.*?)\s*(LANGUAGE|EDUCATION)', text, re.S | re.IGNORECASE)
        return match.group(1).strip() if match else "No encontrado"

    def extract_experience(text):
        match = re.search(r'WORK EXPERIENCE\s*(.*?)\s*(SKILLS|EDUCATION)', text, re.S | re.IGNORECASE)
        return match.group(1).strip() if match else "No encontrado"

    def extract_education(text):
        match = re.search(r'ACADEMIC\s*(.*?)\s*(SKILLS|LANGUAGE)', text, re.S | re.IGNORECASE)
        return match.group(1).strip() if match else "No encontrado"

    def extract_languages(text):
        match = re.search(r'LANGUAGE\s*(.*?)\s*(SKILLS|EDUCATION)', text, re.S | re.IGNORECASE)
        return match.group(1).strip() if match else "No encontrado"

    # Extraemos los diferentes campos
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)
    experience = extract_experience(text)
    education = extract_education(text)
    languages = extract_languages(text)

    # Imprimir los resultados
    print("Nombre:", name)
    print("Correo:", email)
    print("Teléfono:", phone)
    print("Habilidades:", skills)
    print("Experiencia Profesional:", experience)
    print("Formación:", education)
    print("Idiomas:", languages)

# Ruta al archivo PDF
pdf_path = r'C:\Users\kevin\OneDrive\Desktop\youtube_scripts\CV_KEVIN_MENESES_DATA_ANALYST (2).pdf'
extract_info_from_pdf(pdf_path)
