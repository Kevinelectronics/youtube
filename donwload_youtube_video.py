from pytube import YouTube
import pandas as pd
import os

def descargar_audio_youtube(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    destino = "mis_videos"
    out_file = video.download(output_path=destino)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.wav'
    os.rename(out_file, new_file)
    
    # Datos del video
    detalles_video = {
        "Nombre del Canal": yt.author,
        "Fecha de Publicación": yt.publish_date,
        "Vistas": yt.views,
        "Likes": yt.rating,
        # "Comentarios": yt.comments,  # Comentado debido a la estructura de datos compleja
        "Metadatos": str(yt.metadata)  # Convertido a cadena para simplificar
    }

    return new_file, detalles_video

def guardar_datos_excel(detalles, archivo_salida):
    df = pd.DataFrame([detalles])
    df.to_excel(archivo_salida, index=False)

# URL del video de YouTube
url = "https://youtu.be/tP7tJUEiwIc?si=q1KhtGKYZlsgHPUM"

# Descargar audio y obtener detalles del video
audio_file, detalles_video = descargar_audio_youtube(url)

# Guardar los detalles del video en un archivo Excel
nombre_archivo_excel = "detalles_video_youtube.xlsx"
guardar_datos_excel(detalles_video, nombre_archivo_excel)

# Opcional: Eliminar el archivo de audio descargado
os.remove(audio_file)
