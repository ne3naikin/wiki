from django.shortcuts import render

from . import util
import random

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
# TODO: Поки що ця функція не працює належним чином, тому відклав її на потім
def search(request):
    #if request.method == 'GET':
    # search_f = request.GET
    search_f = request.GET.get('q')
    #entries = util.list_entries()
    # if util.get_entry(search_f):
    #     return render(request, "encyclopedia/search.html", {
    #     "search": search_f,
    #     "title": ' Заходить у якщо, якщо це бачимо'
    #     })

    if search_f in entries:
        
        # searchfinal = search_f
        return render(request, "encyclopedia/search.html", {
            "search": search_f,
            "title": ' Заходить у якщо, якщо це бачимо',
            # "search_f": search_f,                
        })
    else:
        return render(request, "encyclopedia/search.html", {
            "text_fail": 'Нічого не знайшлось',
            # "title": request.GET,
            # "search_f": search_f,                
    })
    return render(request, "encyclopedia/search.html", {
        "info": ' info-test',
        "info_entries": entries, 
        "info_search": search_f,
        "info_title": request.GET,
        "info_q": search_f,
        "info_search_f": search_f in entries
        #"entries": util.list_entries()
        })
    # SearchList.append(search)
    # return render(request, "encyclopedia/search.html", {
    #     "entries": entries, 
    #     "test1": 'test1',
    #     "search": search_f,
    #     "title": request.GET,
    #     "q": search_f
    #     #"entries": util.list_entries()
    # })

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

def create_md(request):
    return render(request, "encyclopedia/create_md.html", {
        "title1": 'Тут мій вікі допис'
    })