from pytube import YouTube
import speech_recognition as sr
import os
import openai 

def transcribe_audio(extension="temp_audio", output_file="salida.txt", model="whisper-1") -> list:
    print("Converting audio to text...")
    # Configurar la API key de OpenAI
    openai.api_key = os.getenv('OPENAI_API_KEY')
    with open('data.env', 'r') as file:
        for line in file:
            if 'OPENAI_API_KEY' in line:
                key, value = line.strip().split('=', 1)
                os.environ[key] = value



# La ruta específica donde se encuentran los archivos de audio
        audio_folder_path = r'C:\Users\kevin\OneDrive\Desktop\Atani\temp_audio'

# La extensión de los archivos de audio que deseas buscar
        audio_extension = '.mp4'  # Cambia esto a la extensión de archivo correcta

# Lista los archivos en la carpeta especificada que terminan con la extensión deseada
    audio_files = [os.path.join(audio_folder_path, file) for file in os.listdir(audio_folder_path) if file.endswith(audio_extension)]
    print(f"Archivos de audio encontrados: {audio_files}")

    # Obtener todos los archivos de audio con la extensión dada en la carpeta actual
    
    transcripts = []
    for audio_file in audio_files:
        with open(audio_file, "rb") as audio:
            response = openai.Audio.transcribe(model, audio)
            transcripts.append(response["text"])

    if output_file is not None:
        # Save all transcripts to a .txt file
        with open(output_file, "w") as file:
            for transcript in transcripts:
                file.write(transcript + "\n")

    return transcripts

# Ejemplo de uso:
# transcriptions = transcribe_audio(output_file='transcripts.txt')




# URL del video de YouTube
url = "https://youtu.be/tP7tJUEiwIc"

# Descargar y transcribir
#audio_file = descargar_audio_youtube(url)
t1=transcribe_audio(extension=".waw", output_file='datos2.txt', model="whisper-1")

# Guardar la transcripción en un archivo de texto


# Opcional: Eliminar el archivo de audio descargado
#os.remove(audio_file)
