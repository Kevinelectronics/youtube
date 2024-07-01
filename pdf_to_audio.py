from gtts import gTTS
import PyPDF2

def pdf_to_speech(pdf_path, audio_path, lang='es', num_pages_to_read=10, tld='com'):
    try:
        # Load the PDF
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)

            # Extract text from the specified number of pages
            text = ""
            for page in range(min(num_pages, num_pages_to_read)):
                text += reader.pages[page].extract_text()

        # Convert text to speech
        tts = gTTS(text, lang=lang, tld=tld)
        tts.save(audio_path)
        print(f'Audio guardo en: {audio_path}')
        
    except FileNotFoundError:
        print(f'El archivo {pdf_path} no fue encontrado.')
    except PyPDF2.errors.PdfReadError:
        print(f'Hubo un error leyendo el PDF {pdf_path}.')
    except Exception as e:
        print(f'Un Error ocurrió: {e}')

# Parameters
pdf_path = 'C:/Users/kevin/Downloads/LIBERTAD-INMOBILIARIA_Carlos-Galan_Actualizado-2024.pdf'
audio_path = 'C:/Users/kevin/Downloads/Libertad_Inmobiliaria_Cap1_3.mp3'
lang = 'es'
num_pages_to_read = 10
tld = 'com.mx'  # Example: for Mexican Spanish

# Call the function
pdf_to_speech(pdf_path, audio_path, lang, num_pages_to_read, tld)

