from imdb import IMDb
from imdb.Person import Person
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import time
ia=IMDb()
per=Person()
 
names = ['Deepika Padukone', 'Priyanka Chopra', 'Alia Bhatt', 'Aishwarya Rai Bachchan','Anushka Sharma', 'Kareena Kapoor','Kangana Ranaut','Katrina Kaif','Shraddha Kapoor',
'Karisma Kapoor','Kajol','Madhuri Dixit','Kriti Sanon','Vidya Balan','Sonam K Ahuja','Sridevi','Rani Mukerji','Parineeti Chopra','Jacqueline Fernandez','Disha Patani','Rekha',
'Kiara Advani','Taapsee Pannu','Sharmila Tagore','Ileana DCruz','Bipasha Basu','Babita Shivdasani','Preity Zinta', 'Hema Malini','Yami Gautam','Sonakshi Sinha','Sunny Leone','Tabu',
'Smita Patil','Madhubala','Juhi Chawla','Nargis']
names=np.unique(names)

c=0
average_movies=np.zeros(100)
years=[]
spike_point=[]
for name in names:
    name = name.strip()
    person = ia.search_person(name)
    try:
        filmography=ia.get_person(person[0].personID, info=['filmography'])
    except:
        print(name+" Not Found")
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
    lis=list(dic_reversed.values())
    s=sum(lis)
    mean=np.mean(lis)
    std=np.std(lis)
    max_ind=np.argmax(lis)
    years.append(len(lis))
#    plt.plot(lis)
    lis_copy=lis.copy()
    while(len(lis_copy)<100):
        lis_copy.append(0)
    average_movies+=np.array(lis_copy)
#    print(name +" " +str(s) +" "+ str(mean)+" "+str(std))
    spike_point.append(max_ind/len(lis))
#plt.legend(names)
#plt.show()

average_movies=np.array(average_movies)
average_movies=average_movies/len(names)
average_movies=list(average_movies)
while average_movies[-1] == 0:
    average_movies.pop(-1)

plt.plot(average_movies)
plt.xlabel("Number of years as an actress in the Industry")
plt.ylabel("Average number of movies produced")
plt.title("Average number of movies produced per year for actresses")
plt.show()
#print(years)
#print(np.mean(years))
#print(spike_point)
#print(np.mean(spike_point))
#print(np.std(spike_point))
