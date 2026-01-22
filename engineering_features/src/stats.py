from typing import List, Dict
import csv
from statistics import *

def stats(path: str) -> Dict[str, float]: 
    with open(path, 'r') as csv_file: 
        csv_content = csv.reader(csv_file)
        dic = {}

        multiplatforms_games = 0
        non_multiplatforms_games = 0

        metascores_list = []
        userscores_list = [] 
        year_list = []
        metascore_count_list = []
        userscore_count_list = []

        next(csv_content) #ignore the header
        for line in csv_content: 
            year_list.append(int(line[0]))
            metascores_list.append(float(line[1]))
            userscores_list.append(float(line[2]))
            metascore_count_list.append(int(line[3]))
            userscore_count_list.append(int(line[5]))


            if int(line[4]) > 1: 
                multiplatforms_games += 1
            else: 
                non_multiplatforms_games += 1
        
        dic["metascore_mean"] = mean(metascores_list)
        dic["userscore_mean"] = mean(userscores_list)
        dic["metascore_median"] = median(metascores_list)
        dic["userscore_median"] = median(userscores_list)
        dic["year_mean"] = mean(year_list)
        dic["year_median"] = median(year_list)
        dic["metascore_count_mean"] = mean(metascore_count_list)
        dic["userscore_count_mean"] = mean(userscore_count_list)
        dic["percentage_of_multiplatform_games"] = (multiplatforms_games/(multiplatforms_games+non_multiplatforms_games))*100

        return dic
         