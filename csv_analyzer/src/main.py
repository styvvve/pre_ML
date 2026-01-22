from loader import load_csv
from clean import clean
from stats import stats 
from visualize import visualize

dic = load_csv("/Users/steve/Documents/pre-ML/csv_analyzer/data/raw/top_programming_languages.csv")

new_dic = clean(dic)

the_stats = stats(new_dic)

visualize(the_stats, new_dic)
