from unicodedata import name
from django.shortcuts import render

from . import util
import random
import re


#from Tasks.wiki import encyclopedia

entries = util.list_entries()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def wiki(request, title): # не впевнений що записав все правильно
    #title = util.get_entry(title) # Варіант 2 не проканав пуста сторінка контексту нема
    return render(request, "encyclopedia/index.html", { # мені не подобається те що з html
        "entry": util.get_entry(title),
        "title": title
        #"title": util.get_entry(title) # Видало "All Pages" але тексту нема, працює але не зовсім
        #"entry": title # Варіант 2 не проканав пуста сторінка контексту нема
    }) # TODO: Почистити від зайвих комінтарів включно з закоментованим кодом

# SearchList = ["yes"] # Тестове "yes"
#search_f = "Not" # Тестове "Not"
##search = ""
# FIX: Поки що ця функція не працює належним чином, тому відклав її на потім
"""
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("spain", txt, flags=re.IGNORECASE)
print(x)

Читати мануал потребує часу. Вдалося виснити що flags=re.IGNORECASE ігнорує великі та маленькі букви.
Треба обов'язково додати import re
У тілі функції використати re.findall("данні з пошуку", flags=re.IGNORECASE)

Посилання:
https://www.w3schools.com/python/python_regex.asp
https://uk.wikipedia.org/wiki/Регулярний_вираз
https://habr.com/ru/post/349860/
https://habr.com/ru/company/skillbox/blog/552360/
https://msiter.ru/tutorials/javascript/js_regexp
https://docs.microsoft.com/ru-ru/dotnet/standard/base-types/miscellaneous-constructs-in-regular-expressions

Тренажер:
https://regex101.com/r/aGn8QC/2

Нагуглив, у тренажери спрацювало:
(?i)rEgULar 
Найде - Regular

"""
def search(request):
    # FIX: Убрати все зайве з коду
    # FIX: Навести порядок у search.html 
    searchList = []
    search_find = request.GET.get('q')
    for entry_search in entries:
        if  re.findall("(?i)"+search_find, entry_search):
            searchList.append(entry_search)
        
        # FIXME: Додати список пошуку на той випадок коли буде більше одної знахідки
        # FIXME: Знаходить та записує до списка тільки перше знайдене інші ігнорує
    if len(searchList) >= 1 and search_find != '':
        return render(request, "encyclopedia/search.html", {
            "title": 'Пошук дописів у Wiki',
            "searchList": searchList,
            "resume": f' На запит "{search_find}" було знайдено:',
        })

    return render(request, "encyclopedia/search.html", {
        "title": 'Пошук дописів у Wiki',
        "resume": f' У файлах дописів Wiki нічого не знайшлось шоб відповідало запиту "{search_find}"', # resume
    })

    # TODO: Random

def random_md(request):
    # integer_entries = len(entries)
    # integer_random = random.randint(0, integer_entries-1)
    # entry = entries[integer_random]
    return render(request, "encyclopedia/random_md.html", {
        #"entry": get_entry(entry)
        "entry": util.get_entry(entries[random.randint(0, len(entries)-1)]) # Ну так трохи скоротив, але інший, зрозумілий, не видалив - закоментував
    })

# TODO: Create markdown 
# title = ""
# content = ""
# , title, content
def create_md(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # util.save_entry(title, content)
    title=request.POST.get('title')
    # if 'title' in request.POST and 'content' in request.POST:
    #     util.save_entry(title, content)
    # if request.method == 'POST':
    #     title = request.post(name='title')
    #     content = request.post(name='content')
    #     util.save_entry(title, content)
    return render(request, "encyclopedia/create_md.html", {
        # "title_test": 'Тут мій вікі допис',
        "title": "Створити новий допис",
        "title_test": title,
        # "content_test": content

    })

def edit_md(request):
    return render(request, "encyclopedia/edit_md.html", {
        "title_test": 'Тут редагуємо допис',
        # "title": title, #"Редактор дописів"
        # "content": content
    })