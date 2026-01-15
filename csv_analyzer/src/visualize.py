import matplotlib.pyplot as plt
from typing import Dict, List

def visualize(dic: Dict[str, int], dic_origin: Dict[int, List[str]]): 
    #get only the decade stats
    new_dic = {}
    for stat in dic: 
        if stat[0].isdigit(): 
            new_dic[stat] = dic[stat]

    x = list(new_dic.keys())
    y = list(new_dic.values())

    plt.bar(x, y)
    plt.xlabel("Decade")
    plt.ylabel("Number of languages")
    plt.title("Creation of language per decade")
    plt.savefig("Creation-of-language-per-decade.png", dpi=300)
    plt.show()

    #year's historigram
    year_historigram = []
    for year in dic_origin: 
        l = dic_origin[year]
        n = len(l)

        for i in range(n): 
            year_historigram.append(year)

    plt.hist(year_historigram, rwidth = 0.2)
    plt.xlabel("Years")
    plt.ylabel("Frequency")
    plt.title("Frequency of year")
    plt.savefig("Frequency-of-year.png", dpi=300)
    plt.show()

    #accumulation of languages over time
    total = []
    cumulative_total = 0
    for year in dic_origin: 
        cumulative_total += len(dic_origin[year])
        total.append(cumulative_total)

    x2 = list(dic_origin.keys())
    y2 = total

    plt.plot(x2, y2, marker='o')
    plt.title("Accumulation of languages over time") 
    plt.xlabel("Years")
    plt.ylabel("Number of languages")
    plt.savefig("Accumulation-of-languages-over-time.png", dpi=300)
    plt.show()