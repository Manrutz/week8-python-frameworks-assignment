# week8-python-frameworks-assignment
# 📘 CORD-19 Data Explorer

A beginner-friendly data analysis and visualization project built with Python, Pandas, Matplotlib/Seaborn, and Streamlit.
This project explores the CORD-19 metadata dataset (COVID-19 research papers) to uncover trends such as publication years, top journals, and common keywords in paper titles.

📂 Project Structure
Frameworks_Assignment/
│── notebook.ipynb        # Jupyter Notebook with full analysis
│── app.py                # Streamlit app for interactive exploration
│── metadata.csv          # Dataset (download separately, not included here)
│── README.md             # Project documentation

🚀 Features

Data Cleaning: Handle missing values, convert dates, and create new features (e.g., abstract word count).

Exploratory Analysis:

Count publications by year

Identify top journals

Extract frequent words from titles

Analyze paper distribution by source

Visualizations: Bar charts, trends over time, and keyword analysis

Streamlit App: Simple interactive dashboard to explore research papers

📊 Sample Insights

Research publications peaked between 2020–2021.

Certain journals dominated early COVID-19 research output.

Common title keywords include “covid”, “coronavirus”, and “pandemic”.

🛠️ Tools & Libraries

Python 3.7+

Pandas
 (data manipulation)

Matplotlib
 & Seaborn
 (visualization)

Streamlit
 (interactive web app)

📥 Dataset

This project uses the metadata.csv file from the CORD-19 Dataset on Kaggle
.

⚠️ Note: The full dataset is large. For testing, you may use a smaller sample of metadata.csv.

▶️ How to Run
1. Clone this repository
git clone https://github.com/your-username/Frameworks_Assignment.git
cd Frameworks_Assignment

2. Install dependencies
pip install pandas matplotlib seaborn streamlit

3. Run the Jupyter Notebook
jupyter notebook notebook.ipynb

4. Launch the Streamlit App
streamlit run app.py

✍️ Reflection

During this project, I learned:

How to clean and preprocess real-world research data.

The basics of data visualization in Python.

How to build an interactive dashboard with Streamlit.

The importance of incremental debugging and exploratory analysis.

📌 Future Improvements

Add a word cloud visualization of paper titles.

Provide filters by journal or keywords in the Streamlit app.

Expand analysis to include author networks.

👨‍💻 Author

[Remmy Kipruto Tumo]
