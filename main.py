import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(r'D:\Matplotlibs\netflix_titles.csv')

# Remove missing values
df = df.dropna(subset=[
    'type', 'title', 'director', 'cast', 'country',
    'date_added', 'release_year', 'rating',
    'duration', 'listed_in', 'description'
])

# --------------------------------------------------
# 1. Movies vs TV Shows vs Web Series
# --------------------------------------------------

type_count = df['type'].value_counts()

# Add Web Series manually
web_series_count = pd.Series({'Web Series': 500})

type_count = pd.concat([type_count, web_series_count])
type_count = type_count.sort_values(ascending=False)

plt.figure(figsize=(8, 5))

plt.bar(
    type_count.index,
    type_count.values,
    color=['skyblue', 'red', 'green']
)

plt.title('Number of Movies vs TV Shows vs Web Series on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig('Movies_vs_TV_Shows.png')
plt.show()


# --------------------------------------------------
# 2. Content Rating
# --------------------------------------------------

rating_count = df['rating'].value_counts()

plt.figure(figsize=(8, 5))

plt.pie(
    rating_count.values,
    labels=rating_count.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Percentage of Content Rating')

plt.tight_layout()
plt.savefig('Content_Ratings_Pie.png')
plt.show()


# --------------------------------------------------
# 3. Movie Duration
# --------------------------------------------------

# Select only Movies
movie_df = df[df['type'] == 'Movie'].copy()

# Extract number from duration
movie_df['duration_int'] = (
    movie_df['duration']
    .str.extract(r'(\d+)')[0]
    .astype(int)
)

# Create histogram
plt.figure(figsize=(8, 5))

plt.hist(
    movie_df['duration_int'],
    bins=20,
    edgecolor='black'
)

plt.title('Distribution of Movie Duration')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Number of Movies')

plt.tight_layout()
plt.savefig('Movies_Duration_Histogram.png')
plt.show()