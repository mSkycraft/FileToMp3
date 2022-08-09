from sys import path_hooks
from gtts import gTTS
import pdfplumber
from pathlib import Path

def text_to_audio(text,name,lg):
    text = ''.join(text)
    text = text.replace("\n",'')
    afile = gTTS(text,lang=lg,slow=False)
    afile.save(f'{name}.mp3')

def pdf_to_audio(path,lg):
    try:
        pdf = pdfplumber.PDF(open(path,'rb'))
        text = [ptext.exctract_text() for ptext in pdf.pages]

        text_to_audio(text,Path(path).name,lg)

        return f': Обработка завершена успешно'
    
    except:
        return f': Обработка файла завершилась с ошибкой'

def txt_to_audio(path,lg):
    try:
        print(f': Файл {Path(path).name}')
        print(': Начата обработка файла...')
        ftxt = open(path,'r')
        text = ftxt.readlines()
        text_to_audio(text,Path(path).name,lg)

        return f': Обработка завершена успешно'
    
    except:
        return f': Обработка файла завершилась с ошибкой'

def controller(path,lg='en'):
    
    print(f': Файл {Path(path).name}')
    print(': Начата обработка файла...')

    if  Path(path).is_file():
        match Path(path).suffix:
            case '.pdf': return pdf_to_audio(path,lg)
            case '.txt': return txt_to_audio(path,lg)
        return f': Не верное расширение файла'
    else:
        return f': Файл не найден. Не верно указан путь к файлу'
