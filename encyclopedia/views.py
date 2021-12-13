from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title): # не впевнений що записав все првильно
    #title = util.get_entry(title) # Варіант 2 не проканав пуста страниця контексту нема
    return render(request, "encyclopedia/index.html", { # мені не падобается те що з html-емом
        "entry": util.get_entry(title),
        "title": title
        #"title": util.get_entry(title) # Видало "All Pages" але тексту нема, працює але не зовсім
        #"entry": title # Варіант 2 не проканав пуста страниця контексту нема
    })