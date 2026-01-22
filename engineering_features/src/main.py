from loader import loader
from features import features
from stats import stats
from stats_df import stats_df
from visualize import visualize

list_of_game = loader("/Users/steve/Documents/pre-ML/engineering_features/data/raw/metacritic_games.csv")

df = features(list_of_game, "/Users/steve/Documents/pre-ML/engineering_features/output/metacritic_games_processed.csv")

some_stats = stats("/Users/steve/Documents/pre-ML/engineering_features/output/metacritic_games_processed.csv")

df_some_stats = stats_df(df)

visualize(df_some_stats)


