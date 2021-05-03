from imdb import IMDb
from imdb.Person import Person
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
 
ia=IMDb()
per=Person()
 
#This function makes a csv and also outputs some information about filmography history without gender or language
def dynasty():
    print("Enter an actor's name")
    person = ia.search_person(input())
    filmography=ia.get_person(person[0].personID, info=['filmography'])
    filmography_list=filmography['filmography']
    dic = {}
    list_ = []
    if 'actor' not in filmography_list:
        data = filmography_list['actress']
    else:
        data = filmography_list['actor']
    for item in data:
        if item.items()[1][1] == 'movie' and type(item.items()[2][1]) == int:
            if str(item.items()[2][1]) not in dic:
                dic[str(item.items()[2][1])] = 1
            else:
                dic[str(item.items()[2][1])] += 1
            list_.append(item.items()[2][1])
    for date in range(min(list_), max(list_)):
        if str(date) not in dic:
            dic[str(date)] = 0
    dic_reversed = {}
    for item in sorted(dic.keys()):
        dic_reversed[item] = dic[item]
    # print(dic_reversed)
    plt.bar(dic_reversed.keys(), dic_reversed.values(), 1, color='g')
    plt.xlabel("Year")
    plt.ylabel("Movies Produced")
    plt.title("Number of movies produced per year")
    plt.xticks(rotation = 90)
    plt.show()
while True: 
    dynasty()
