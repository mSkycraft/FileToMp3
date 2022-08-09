from art import tprint
from defs import controller

def main():
    tprint("FILE>>TO>>AUDIO",'bulbhead')
    pdf = input('Введите путь к файлу: ')
    lang = input('Введите язык озвучивания ru/en: ')
    print(controller(pdf,lang))

if __name__ == '__main__':
    main()
