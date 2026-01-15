#we ll just sort the dic by year
from typing import Dict, List, Tuple

def clean(dic: Dict[str, List[str]]) -> Dict[str, List[str]]: 
    #sort by year first
    #convert dict to a list of tuples
    res = list(dic.items())
    res = sorted(res)
    new_dic = {}
    for i in res: 
        new_dic[i[0]] = i[1]
    return new_dic