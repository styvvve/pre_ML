from typing import Dict, List
import csv

#we get the programming language and the year
def load_csv(path: str) -> Dict[int, List[str]]: 
    with open(path, 'r') as csv_file: 
        csv_content = csv.reader(csv_file)
        dic = {}
        for line in csv_content: 
            if line[0] == "Language": 
                continue
            elif int(line[2]) not in dic:
                dic[int(line[2])] = []
                dic[int(line[2])].append(line[0])
            else: 
                dic[int(line[2])].append(line[0])
    
    return dic


