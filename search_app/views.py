from django.shortcuts import render

import os
#import enchant
from spellchecker import SpellChecker
from django.conf import settings
from django.http import HttpResponse
import json, re, requests
# Create your views here.

def home(request):
    return render(request, "home.html", {"name": "Eddy"})

def search(request):
    spell = SpellChecker()
    #r = enchant.Dict("en_US")
    data = json.load(open(os.path.join(settings.BASE_DIR, 'words_dictionary.json')))
    #data = getJson(res)
    d = []
    d = list(data.keys())
    res = []
    dew = []

    def character_set(w, character):

        while True:
            try:
                t = int(request.POST['num'])
                break
            except ValueError:
                break
        #t = int(input("Enter the Exact lenght of Words you want to be displayed: "))
        for char in w:
            value = 1
            m = possible_words(char)
            for k in m:
                if k not in character:
                    value = 0
                else:
                    if character.count(k) != m[k]:
                        value = 0
            if value == 1:
                try:
                    if len(char)==t:
                        res.append(char)
                        print(res)
                    else:
                        pass
                except UnboundLocalError:
                    res.append(char)
                    print(res)

    def possible_words(character):
        x ={}
        for n in character:
            x[n] = x.get(n, 0) + 1
        return x

    word = request.POST["letter"]
    word = word.casefold()
    words = list(word)
    character_set(d, words) 
    #char = request.Get['num']
    #return render(request, "result.html", {'result': res})
    for i in res:
        if i == spell.correction(i):
            dew.append(i)
        else:
            pass

    return render(request, "result.html", {'result': dew, 'counter': len(dew)})
    
        