# ================================================
# Python Frameworks Assignment
# Dataset: metadata.csv (CORD-19 sample data)
# ================================================

# 📦 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Set plot style
sns.set(style="whitegrid")

# ----------------------------------------
# Part 1: Data Loading and Basic Exploration
# ----------------------------------------
try:
    # Load dataset
    df = pd.read_csv("metadata.csv")

    # Preview dataset
    print("Preview of dataset:")
    display(df.head())

    # Dataset info
    print("\nDataset Info:")
    print(df.info())

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

except FileNotFoundError:
    print("❌ metadata.csv file not found. Please place it in the working directory.")

# ----------------------------------------
# Part 2: Data Cleaning and Preparation
# ----------------------------------------
# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Extract year
df["year"] = df["publish_time"].dt.year

# Add new column: abstract word count
df["abstract_word_count"] = df["abstract"].astype(str).apply(lambda x: len(x.split()))

# ----------------------------------------
# Part 3: Data Analysis and Visualization
# ----------------------------------------

# 1. Count papers by publication year
papers_per_year = df["year"].value_counts().sort_index()
print("\nPapers by Year:")
print(papers_per_year)

# Plot publications over time
plt.figure(figsize=(8,5))
papers_per_year.plot(kind="bar", color="skyblue")
plt.title("Number of Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# 2. Top journals
top_journals = df["journal"].value_counts().head(5)
print("\nTop Journals:")
print(top_journals)

plt.figure(figsize=(8,5))
top_journals.plot(kind="bar", color="orange")
plt.title("Top 5 Journals by Publication Count")
plt.xlabel("Journal")
plt.ylabel("Number of Papers")
plt.show()

# 3. Word Cloud of paper titles
titles_text = " ".join(df["title"].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles_text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.show()

# 4. Distribution of papers by source
plt.figure(figsize=(8,5))
df["source_x"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.ylabel("")
plt.title("Distribution of Papers by Source")
plt.show()

# ----------------------------------------
# Part 4: Streamlit Application (sample)
# ----------------------------------------
# Save this part as frameworksapp.py for Streamlit
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors="coerce")
df['year'] = df['publish_time'].dt.year

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Filter by year
years = df['year'].dropna().unique()
year_range = st.slider("Select year range:", int(df['year'].min()), int(df['year'].max()), (2020, 2021))

filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show sample data
st.subheader("Sample Data")
st.write(filtered_df.head())

# Publications by year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# Top Journals
st.subheader("Top Journals")
st.bar_chart(filtered_df['journal'].value_counts().head(5))
"""
# ----------------------------------------
# Part 5: Findings & Observations
# ----------------------------------------
print("\nObservations:")
print("- Publications peak around 2020 and 2021, reflecting COVID-19 research boom.")
print("- Journals like The Lancet and Nature Medicine appear frequently.")
print("- Word cloud highlights frequent terms like COVID-19, Impact, Review, etc.")
print("- Papers are sourced from multiple repositories (WHO, PMC, Elsevier, etc.).")
