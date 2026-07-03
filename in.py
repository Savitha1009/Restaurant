import numpy as np
import pandas as pd
import folium
import matplotlib.pyplot as plt
import sys
import io

# Set UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

Data=pd.read_csv("C:\\Users\\Savitha\\Downloads\\Dataset .csv")
Data.head()
Data.tail()
Data.info()
df=pd.DataFrame(Data)
missing_values=df.isnull().sum()
print(' \ncolumns with missing values\n')
print(missing_values[missing_values>0])
df["Cuisines"] = df["Cuisines"].fillna(df["Cuisines"].mode()[0])
rating_count=df["Aggregate rating"].value_counts().sort_index()
print("\nCount of each rating\n")
print("\nRating counts\n")
print(df.describe())
print("\nMean\n")
print(df.mean(numeric_only=True))
print("\nMedian\n")
print(df.median(numeric_only=True))
print("\nStandard Deviation\n")
print(df.std(numeric_only=True))
print("\nMinimum\n")
print(df.min(numeric_only=True))
print("\nMaximum\n")
print(df.max(numeric_only=True))
print(df["Country Code"].value_counts())
print(df["Cuisines"].value_counts())
print(df["City"].value_counts())
top_cuisines=df["Cuisines"].value_counts().head(10)
print("\nTop 10 Cuisines\n")
print(top_cuisines)
top_cities=df["City"].value_counts().head(10)
print("\nTop 10 Cities\n")
print(top_cities)
restaurant_map = folium.Map(
    location=[df["Latitude"].mean(), df["Longitude"].mean()],
    zoom_start=5
)

# Add restaurant markers
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=3,
        popup=f"{row['Restaurant Name']}<br>Rating: {row['Aggregate rating']}",
        color="blue",
        fill=True,
        fill_color="red"
    ).add_to(restaurant_map)

# Save map
restaurant_map.save("restaurant_map.html")

print("Map saved as restaurant_map.html")

city_counts = df["City"].value_counts().head(10)

plt.figure(figsize=(10,5))
city_counts.plot(kind="bar", color="skyblue")

plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)

plt.savefig("top_cities_chart.png")
plt.close()
print("Chart saved as top_cities_chart.png")
correlation = df[["Latitude", "Longitude", "Aggregate rating"]].corr()

print(correlation)
plt.figure(figsize=(8,5))

plt.scatter(df["Latitude"], df["Aggregate rating"], alpha=0.5)

plt.title("Latitude vs Aggregate Rating")
plt.xlabel("Latitude")
plt.ylabel("Aggregate Rating")

plt.savefig("latitude_vs_rating.png")
plt.close()
print("Chart saved as latitude_vs_rating.png")
plt.figure(figsize=(8,5))

plt.scatter(df["Longitude"], df["Aggregate rating"], alpha=0.5)

plt.title("Longitude vs Aggregate Rating")
plt.xlabel("Longitude")
plt.ylabel("Aggregate Rating")

plt.savefig("longitude_vs_rating.png")
plt.close()
print("Chart saved as longitude_vs_rating.png")
city_rating = (df.groupby("City")["Aggregate rating"]
                 .mean()
                 .sort_values(ascending=False)
                 .head(10))

print(city_rating)
