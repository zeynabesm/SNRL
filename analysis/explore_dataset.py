from pathlib import Path
import pandas as pd

DATA_DIR = Path("Data")

movies = pd.read_csv(DATA_DIR / "movies.csv")
ratings = pd.read_csv(DATA_DIR / "ratings.csv")
tags = pd.read_csv(DATA_DIR / "tags.csv")
links = pd.read_csv(DATA_DIR / "links.csv")

datasets = {
    "Movies": movies,
    "Ratings": ratings,
    "Tags": tags,
    "Links": links
}

for name, df in datasets.items():
    
    print("=" * 60)
    print(name)
    print("=" * 60)

    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nFirst rows:")
    print(df.head())

    print("\n")

