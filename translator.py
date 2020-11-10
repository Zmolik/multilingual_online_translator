import requests
import sys
from bs4 import BeautifulSoup

args = sys.argv  # translate from = args[1], translate to = args[2], word = args[3]
error = False
languages = {'1': 'Arabic', '2': 'German', '3': 'English', '4': 'Spanish', '5': 'French', '6': 'Hebrew', '7': 'Japanese', '8': 'Dutch', '9': 'Polish', '10': 'Portuguese', '11': 'Romanian', '12': 'Russian', '13': 'Turkish'}
languages_list = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']


def translate(lang_from, lang_to, word):
    global error
    url = f'https://context.reverso.net/translation/{lang_from.lower()}-{lang_to.lower()}/{word.lower()}'

    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    except requests.exceptions.ConnectionError:
        print('Something wrong with your internet connection')
        error = True
        return False
    if r.status_code == 404:
        print(f'Sorry, unable to find {word}')
        error = True
        return False

    soup = BeautifulSoup(r.content, 'html.parser')

    words = soup.find('div', id="translations-content")
    words_final = words.text.split()
    sentences = soup.find('section', {'id': 'examples-content'})
    both = sentences.find_all('div', {'class': 'example'})
    from_helper = sentences.find_all('div', {'class': 'src ltr'})
    from_l = from_helper[0].text.strip()
    print("")
    print(f'{lang_to.capitalize()} translation:')
    print(words_final[0])

    print(f'\n{lang_to.capitalize()} example:')
    print(from_l)
    to_l = both[0].text.strip().replace('\n', '').replace(from_l, '').strip()
    print(to_l, '\n')

    with open(f'{word}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{lang_to} Translation:\n')
        file.write(f'{words_final[0]}\n')
        file.write(f'\n{lang_to} Example:\n')
        file.write(f'{from_l}\n')
        file.write(f'{to_l}\n\n\n')


if len(args) != 4:
    print("The script should be called with 3 arguments, 1.translate from, 2.translate to, 3.word to translate")
    print("e.g. python translator.py english german hello")
else:
    if args[1].capitalize() not in languages_list:
        print(f"Sorry, the program doesn't support {args[1]}")
    elif args[2].capitalize() not in languages_list and args[2] != 'all':
        print(f"Sorry, the program doesn't support {args[2]}")
    elif args[2] == 'all':
        for n in languages:
            if args[1].capitalize() == languages[n]:
                pass
            else:
                if error is True:
                    break
                else:
                    translate(args[1], languages[n], args[3])
    else:
        translate(args[1], args[2], args[3])






