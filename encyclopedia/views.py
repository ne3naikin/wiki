# from unicodedata import name
from django.shortcuts import render
from django import forms

from . import util
import random
import re

from django import forms # Створюємо форму для створення файлу та його редагування у форматі *.md
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.urls import reverse

class NameMdFaleForm(forms.Form):
    title = forms.CharField(label='Введіть назву файлу', max_length=250, help_text='(не більше 250 сімволів)') # назва файлу - повинна бути
    content = forms.CharField(label='Створити новий допис', widget=forms.Textarea) # текст допису, або новий, або для редагування



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
    searchList = []
    search_find = request.GET.get('q')
    for entry_search in entries:
        if  re.findall("(?i)"+search_find, entry_search):
            searchList.append(entry_search)
        # Додав список пошуку на той випадок коли буде більше одної знахідки
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

    # TODO: Random a post - Випадковий допис

def random_md(request):
    # integer_entries = len(entries)
    # integer_random = random.randint(0, integer_entries-1)
    # entry = entries[integer_random]
    return render(request, "encyclopedia/random_md.html", {
        #"entry": get_entry(entry)
        "entry": util.get_entry(entries[random.randint(0, len(entries)-1)]) # Ну так трохи скоротив, але інший, зрозумілий, не видалив - закоментував
    })

# TODO: Create a post markdown - Створити допис markdown
def create_md(request):
# Три тижня потратив що це знайти та спробвати
# замінити у файлі create_md.html такі строки коду:
# <form action="{% url 'edit_md' %}", method="POST"> на 
# <form action="", method="POST"> и все запрацювало. 
# А то робив вигляд що не бачить методу 'POST'
# Знайшов на форумі тут - https://courses.prometheus.org.ua/courses/course-v1:Prometheus+CS50+2021_T1/discussion/forum/2de62297d52cdefe74320fff37fc6c28578a3caa/threads/616b1372bbdbe40db756851b
    if request.method == 'POST':
        CreateForm = NameMdFaleForm(request.POST)  
        # Перевіряємо якщо вірно і це POST записуємо дані у функції util.save_entry(title, content) утілити util.py 
        if CreateForm.is_valid():
            title = CreateForm.cleaned_data['title']        # назва файлу
            content = CreateForm.cleaned_data['content']    # текст вмісту файлу
            util.save_entry(title, content)                 # зберегаємо все це 
            # Переходимо до сторінки редагування
            return render(request,"encyclopedia/edit_md.html", {
                "label_from_title": 'Назва файлу:',
                "form_title": title,
                "form": CreateForm,
                "heading": 'Редагувати допис',
                "text_heading": "Вітаю ви щойно створили новій допис та можете його відреагувати."
            })
        # Якщо щось не так повертаємо данні сторінки для виправлення 
        else:
            return render(request, "encyclopedia/create_md.html", {
                "form": CreateForm,
                "title": "Створити новий допис"
            })
    # Пуста форма
    return render(request, "encyclopedia/create_md.html", {
                "form": NameMdFaleForm(),
                "title": "Створити новий допис",
            })

def edit_md(request):
    return render(request, "encyclopedia/edit_md.html", {
        "label_from_title": 'Назва файлу:',
        # "form_title": title,
        # "form": NameMdFaleForm(),
        "heading": 'Редагувати допис',
        # "test_title": test_title,
        # "test_content": test_content,
        "title": "Редагувати допис"
        # "content": content
    })