from typing import Dict, List
import csv

#load the file and return a list of dict. A dict = one game
def loader(path: str) -> List[Dict]: 
    with open(path, 'r') as csv_file: 
        csv_content = csv.reader(csv_file) #return an iterator
        list_of_game = []
        next(csv_content) #ignore the header
        critical_clues = [2, 6, 7, 8, 10, 11]
        for line in csv_content: 
            dic = {}
            invalid_line = False
            #we only extract metascore, userscore, metascore_count, userscore_count, release-date and platforms
            for i in critical_clues: 
                if line[i] == "" or line[i] == "N/A" or line[i] == "tbd": 
                    invalid_line = True
                    break
            
            if invalid_line: 
                continue

            #else we take values
            release_date = line[2].split(sep='-')
            nb_platforms = line[6].split(sep=',')
            dic["release_year"] = int(release_date[0]) 
            dic["metascore"] = float(line[7])
            dic["userscore"] = float(line[10])
            dic["metascore_count"] = int(line[8])
            dic["platforms"] = len(nb_platforms)
            dic["userscore_count"] = int(line[11])

            list_of_game.append(dic)
    return list_of_game
            
                