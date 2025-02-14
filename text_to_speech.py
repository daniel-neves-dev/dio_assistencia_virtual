from gtts import gTTS
import os

text_to_say = "How are you doing?."
language = "en"
gtts_object = gTTS(text = text_to_say,
                  lang = language,
                  slow = False)

gtts_object.save("english.mp4")
os.system("english.mp4")

portuguese_text = "Meu cérebro esta derretendo"
portuguese_language = "pt-br"
portuguese_gtts_object = gTTS(text = portuguese_text,
                          lang = portuguese_language,
                          slow = True)

portuguese_gtts_object.save("portuguese.wav")
os.system("portuguese.wav")
