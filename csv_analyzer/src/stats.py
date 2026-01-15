from typing import Dict, List
from statistics import *

def stats(dic: Dict[int, List[str]]) -> Dict[str, int]: 
    stats = {}
    min_year = min(dic.keys())
    max_year = max(dic.keys())

    stats["max year"] = max_year
    stats["min year"] = min_year
    #the year with the most languages creation
    productive_year = 0
    best_count = 0
    for year in dic.keys():
        if len(dic[year]) > best_count: 
            best_count = len(dic[year])
            productive_year = year
    
    stats["most productive year"] = productive_year
    mean_year = mean(dic.keys())

    stats["mean year"] = mean_year
    median_year = median(dic.keys())

    stats["median year"] = median_year


    #get the number of languages per decade
    stats["1940-1949"] = 0
    stats["1950-1959"] = 0
    stats["1960-1969"] = 0
    stats["1970-1979"] = 0
    stats["1980-1989"] = 0
    stats["1990-1999"] = 0
    stats["2000+"] = 0
    for year in dic: 
        if year < 1950 and year >= 1940: 
            stats["1940-1949"] += len(dic[year])
        elif year < 1960 and year >= 1950: 
            stats["1950-1959"] += len(dic[year])
        elif year < 1970 and year >= 1960: 
            stats["1960-1969"] += len(dic[year])
        elif year < 1980 and year >= 1970: 
            stats["1970-1979"] += len(dic[year])
        elif year < 1990 and year >= 1980: 
            stats["1980-1989"] += len(dic[year])
        elif year < 2000 and year >= 1990: 
            stats["1990-1999"] += len(dic[year])
        elif year >= 2000: 
            stats["2000+"] += len(dic[year])
        else: 
            #error
            print("Error")


    return stats
