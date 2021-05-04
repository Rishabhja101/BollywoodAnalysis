from imdb import IMDb
from imdb.Person import Person
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
 
ia=IMDb()
per=Person()
 
actors = ['Aamir Khan','Shah Rukh Khan','Amitabh Bachchan','Dilip Kumar',' Kamal Haasan',' Raj Kapoor','Rajesh Khanna',' Uttam Kumar',' Irrfan Khan',' Mohanlal',' Mammootty',
'Dev Anand','Naseeruddin Shah','Amrish Puri',' Soumitra Chatterjee',' Anupam Kher',' Sanjeev Kumar','Ajay Devgn',' Akshay Kumar','Rajinikanth','Anil Kapoor','Dharmendra',
'Hrithik Roshan',' Salman Khan','Madhavan','Abhishek Bachchan','Aashish Chaudhary','Abbas',' Amjad Khan',' Amol Palekar','Akshaye Khanna',' Arshad Warsi','Atul Kulkarni',
' Asrani',' Ayushmann Khurrana',' Annu Kapoor','Ashish Vidyarthi']
actors = np.unique(actors)
c=0

def indAnalysis():
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
    
    for date in list_:
        if str(date) not in dic:
            dic[str(date)] = 0
    
    dic_rev = {}
    for item in sorted(dic.keys()):
        dic_rev[item] = dic[item]


    movies = [int(x) for x in dic_rev.values()]

    su = sum(movies)
    # print(su)
    mean = np.mean(movies)
    std = np.std(movies)
    spike_point = (np.max(movies) / len(movies))*100
    print("Total number of movies produced: "+ str(su) + " , " + "Average number of movies per year : " + str(mean) + " Percent into career when most successful: " + str(spike_point))

indAnalysis()
