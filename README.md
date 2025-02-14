<h1>Assistência virtual</h1>

<h2>Desafio 7</h2>

<h3>Objetivo:</h3>
<p>Este projeto foi desenvolvido como parte do Bootcamp BairesDev - Machine Learning Practitioner, oferecido pela Digital Innovation One (DIO). 
 "Este desafio tem como objetivo simular comandos de voz, como abrir uma página da internet e gerar áudio a partir de um texto.</p>
  
-------------------------------------------------------------------------------------------------------------

## 👨‍💻 Tecnologias Usadas:
- Python 3 v3.12
- SpeechRecognition
- PyAudio

-----------------------------------------------------------
## ⚙ Instalação e Setup:

Clonar o projeto:

```bash
  git clone https://github.com/daniel-neves-dev/dio_assistencia_virtual.git
```

Abrir a pasta do projeto:

```bash
  cd dio_assistencia_virtual
```

No terminal digite:

```bash
  pip install SpeechRecognition
  pip install PyAudio
  pip install gTTS
```
Se você usar conda ou miniconda:

```bash
  conda install -c conda-forge libstdcxx-ng  
```

No terminal digite:
- Para speech to text
```bash
  python3 speec_to_text.py
```

- Para text to speech
```bash
  python3 test_to_speech.py
```
-----------------------------------------------------------
## 💻 text_to_speech:
<p>Ao executar o programa serão criados dois arquivos na raiz do programa:</p>
<p>english.mp4 e portuguese.wav</p>
<p>Clique para executar o áudio.</p>

## 💻 speech_to_text:
<p>Execute o programa e então utilizando um microfone diga: "Open Yotube"</p>
<p>uma página do yotube deve abrir no navegador</p>
<p>Execute o programa novamente e agora diga: "Open Google"</p>
<p>uma página do google deve abrir no navegador</p>
