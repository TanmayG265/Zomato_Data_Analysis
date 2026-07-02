import pandas as pd
import numpy as np

def handlerate(value):
    if (value == "NEW" or value == "-"):
        return np.nan
    else:
        value = str(value).split('/')
        value = value[0]
        return float(value)

df = pd.read_csv("zomato.csv")

df.drop('url', axis=1, inplace=True)
df.drop('address', axis=1, inplace=True)
df.drop('reviews_list', axis=1, inplace=True)
df.drop('phone', axis=1, inplace=True)

df.drop_duplicates(inplace=True)

df.drop('dish_liked', axis=1, inplace=True)

df.drop(columns=['listed_in(city)', 'menu_item'], axis=1, inplace=True)

df.rename(columns={
    'name': 'restaurant_name',
    'rate': 'rating',
    'approx_cost(for two people)': 'cost_per_person'
}, inplace=True)

df.drop('rest_type', axis=1, inplace=True)

df.rename(columns={
    'listed_in(type)': 'restaurant_type'
}, inplace=True)

df.dropna(subset=['cuisines', 'cost_per_person'], inplace=True)

df['rating'] = df['rating'].apply(handlerate)
df['rating'] = df['rating'].fillna(df['rating'].mean())

df['cost_per_person'] = (
    df['cost_per_person']
      .str.replace(',', '')
      .astype(int)
)

df['cost_per_person'] = df['cost_per_person'] / 2


df["online_order"] = df["online_order"].astype("string")
df["book_table"] = df["book_table"].astype("string")
df["location"] = df["location"].astype("string")
df["cuisines"] = df["cuisines"].astype("string")
df["restaurant_type"] = df["restaurant_type"].astype("string")

df.to_csv("zomato_cleaned.csv", index=False)