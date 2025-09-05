# 🎙️ Assistente Virtual por Voz (Giovanna)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

Um assistente virtual simples em **Python**, ativado por comando de voz (hotword **"giovanna"**), capaz de responder a perguntas, reproduzir áudios, tocar músicas no YouTube, trazer últimas notícias e informar a previsão do tempo.

---

## 🚀 Tecnologias Utilizadas

- [gTTS](https://pypi.org/project/gTTS/) → Conversão de texto para fala  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) → Reconhecimento de voz  
- [Playsound](https://pypi.org/project/playsound/) → Reprodução de áudios locais  
- [Requests](https://pypi.org/project/requests/) → Consumo de APIs e páginas web  
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) → Extração de notícias em RSS  
- [Webbrowser](https://docs.python.org/3/library/webbrowser.html) → Abertura de links no navegador  

---

## ⚙️ Funcionalidades

- 🔊 Ativação por hotword **"giovana"**  
- 📰 Busca das últimas **notícias**  
- 🎵 Reproduz playlists do YouTube  
- 🌦️ Mostra **previsão do tempo** e temperaturas  
- 📢 Respostas em **áudio sintetizado** (voz)  

---

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/assistente-voz.git
   cd assistente-voz

   python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


pip install -r requirements.txt
gTTS
SpeechRecognition
playsound
requests
beautifulsoup4


---

📌 Observações

É necessário configurar sua API Key do OpenWeather no código para a previsão do tempo funcionar.

O projeto ainda está em desenvolvimento e pode ser expandido com novos comandos.

📜 Licença

Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e compartilhar.
