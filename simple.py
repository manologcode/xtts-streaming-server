import requests
import os
import base64
import time
import json

SERVER_URL = "http://192.168.1.100:8820"

def create_audio(text, speaker_embeddings, title="default", lang="es"):

    generated_audio = requests.post(
        SERVER_URL + "/tts",
        json={
            "text": text,
            "language": lang,
            "speaker_embedding": speaker_embeddings["speaker_embedding"],
            "gpt_cond_latent": speaker_embeddings["gpt_cond_latent"]
        }
    ).content
    generated_audio_path = os.path.join("demo_outputs", "generated_audios",title + ".wav")
    with open(generated_audio_path, "wb") as fp:
        fp.write(base64.b64decode(generated_audio))
        return fp.name
    
if __name__ == "__main__":
    print("creando audio")

    # studio_speakers = requests.get(SERVER_URL + "/studio_speakers").json()
    # print(studio_speakers.keys())

    speakers=  ['Claribel Dervla', 'Daisy Studious', 'Gracie Wise', 'Tammie Ema', 'Alison Dietlinde', 'Ana Florence', 'Annmarie Nele', 'Asya Anara', 'Brenda Stern', 'Gitta Nikolina', 'Henriette Usha', 'Sofia Hellen', 'Tammy Grit', 'Tanja Adelina', 'Vjollca Johnnie', 'Andrew Chipper', 'Badr Odhiambo', 'Dionisio Schuyler', 'Royston Min', 'Viktor Eka', 'Abrahan Mack', 'Adde Michal', 'Baldur Sanjin', 'Craig Gutsy', 'Damien Black', 'Gilberto Mathias', 'Ilkin Urbano', 'Kazuhiko Atallah', 'Ludvig Milivoj', 'Suad Qasim', 'Torcull Diarmuid', 'Viktor Menelaos', 'Zacharie Aimilios', 'Nova Hogarth', 'Maja Ruoho', 'Uta Obando', 'Lidiya Szekeres', 'Chandra MacFarland', 'Szofi Granger', 'Camilla Holmström', 'Lilya Stainthorpe', 'Zofija Kendrick', 'Narelle Moon', 'Barbora MacLean', 'Alexandra Hisakawa', 'Alma María', 'Rosemary Okafor', 'Ige Behringer', 'Filip Traverse', 'Damjan Chapman', 'Wulf Carlevaro', 'Aaron Dreschner', 'Kumar Dahl', 'Eugenio Mataracı', 'Ferran Simen', 'Xavier Hayasaka', 'Luis Moray', 'Marcos Rudaski']
    with open('studio_speakers.json', 'r') as archivo:
        studio_speakers = json.load(archivo)
    title = "prueba"
    text="Me asomo tímidamente, de vez en cuando, al mundo del emprendimiento, con algunos proyectos propios o colaboraciones en otros."
    # http://192.168.1.100:8820/speakers_studio
    # speaker="Claribel Dervla"
    speaker="Royston Min"

    for speaker in speakers:
        inicio = time.time()
        title = speaker.replace(" ","_")
        print("-----------" +title)
        speaker_embeddings = studio_speakers[speaker]
        create_audio(text, speaker_embeddings, title)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print(f"El tiempo de ejecución fue: {tiempo_ejecucion} segundos")