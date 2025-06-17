# import all necessary libraries/modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from itertools import chain

#1 Rename the file downloaded. I got a csv file when I clicked on the link, not a zipped file
old_filename = 'netflix_data.csv'
new_filename = 'Netflix_shows_movies.csv'

try:
    os.rename(old_filename, new_filename)
    print(f"File renamed to: {new_filename}")
except FileNotFoundError:
    print(f"The file '{old_filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Load and preview dataset
#Check the first few rows using the head() function
#Confirm column names and data types using df.info().
#Identify missing values using df.isnull().sum() 

df = pd.read_csv('Netflix_shows_movies.csv')
df.head()
df.info()
print("-"*40)
df.isnull().sum()

#2 Data cleaning
# extract numeric values for duration column and fill empty cells with the value 'Unknown'
df['duration_num'] = df['duration'].str.extract('(\\d+)').astype(float)
df['duration_type'] = df['duration'].str.extract('([a-zA-Z]+)')
# Fill empty spaces with the word 'Unknow'
df['country'].fillna('Unknown', inplace=True)
df['title'].fillna('Unknown', inplace=True)
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)

#3 Exploratory Data Analysis (EDA)

# Descriptive statistics
df.describe(include='all')
# Distribution of Movies vs TV Shows
df['type'].value_counts().plot(kind='bar', title='Movies vs TV Shows')
#Top countries by count
df['country'].value_counts().head(10).plot(kind='barh')
# Releases over time
df['release_year'].value_counts().sort_index().plot(kind='line', title='Content Released per Year')
# Cast and director analysis
df['director'].value_counts().head(10)
from collections import Counter

cast_list = df['cast'].dropna().str.split(', ')
all_cast = [actor for sublist in cast_list for actor in sublist]
pd.Series(Counter(all_cast)).sort_values(ascending=False).head(10)

#4 Create visualisations using matplotlib
# A. Most watched genres
# Split the 'listed_in' column by commas and flatten the list
genres = df['listed_in'].dropna().str.split(', ')
all_genres = list(chain.from_iterable(genres))
genre_counts = pd.Series(Counter(all_genres)).sort_values(ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x=genre_counts.head(10).values, y=genre_counts.head(10).index, palette='viridis')
plt.title('Top 10 Most Common (Approx. Watched) Genres on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.tight_layout()
plt.show()
# B. Rating distribution
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(10,6))
sns.barplot(x=rating_counts.values, y=rating_counts.index, palette='Set2')
plt.title('Distribution of Ratings on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Rating')
plt.tight_layout()
plt.show()

