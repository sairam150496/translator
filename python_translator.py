import os
from googletrans import Translator
import json


for each_file in os.listdir('input'):
    f_name, f_type = each_file.split('.')
    if f_name != 'en' and f_type == 'json':
        pronunciations = dict()
        ln_conversions = dict()
        file = open('input/' + each_file, 'r')
        f_data = json.load(file)
        file.close()
        translator = Translator()
        translated_text = ''
        try:
            translated_text = translator.translate(list(f_data), src="en", dest=f_name)
        except Exception as e:
            print(e)
            exit()
        [(ln_conversions.update({x.origin: x.text}), pronunciations.update({x.text: x.pronunciation}))
         for x in translated_text]
        with open('output/'+f_name+'.'+f_type, 'w') as f:
            f.write(json.dumps(ln_conversions, indent=4, ensure_ascii=False))
        with open('pronunciations/'+f_name+'.'+f_type, 'w') as f:
            f.write(json.dumps(ln_conversions, indent=4, ensure_ascii=False))


