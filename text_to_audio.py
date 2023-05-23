from gtts import gTTS
import os

text='hello uzb'
language='en'

myobj=gTTS(text=text, lang=language, slow=False)

myobj.save(text+'.mp3')
os.system("welcome.mp3")
print('done')