# Student Performance Analysis

This project analyzes student performance data from the StudentsPerformance.csv dataset.
It calculates overall averages, parent-education-based averages, and stores individual student records for further analysis.

## 📌 Features

Reads and processes CSV data using Python’s built-in csv module

Calculates:
- Average math, reading, and writing scores
- Average score grouped by parent education level
- Stores each student’s record in a structured Python dictionary
- Demonstrates core data-analysis concepts such as:
    - Aggregation
    - Grouping
    - Iterating through datasets
    - Type conversion and error handling

## 📂 Project Structure
```bash
student-performance-practice/
│── StudentsPerformance.csv
│── students.py
│── README.md
```

## ▶️ How to Run the Script

Place students.py and StudentsPerformance.csv in the same folder. Run the Python script:
```bash
python students.py
```

The script will output:
- Column names
- Total number of processed rows
- Average scores for each subject
- Average student performance grouped by parent education level

## 🧠 What the Script Does
1. Reads the CSV File
Uses csv.reader to read all rows and skip the header.
2. Builds a List of Students
Each entry is stored as:
```bash
{
  'gender': ...,
  'race': ...,
  'parent_education': ...,
  'lunch': ...,
  'test_preparation': ...,
  'math_score': ...,
  'reading_score': ...,
  'writing_score': ...
}
```

3. Calculates Averages
Uses sums[] to accumulate totals
Computes averages for each subject
Groups students by parent_education and calculates mean score per group

## 🚀 Future Improvements

Visualizations (Matplotlib/Seaborn)
Using Pandas for faster and cleaner analysis
Exporting grouped averages to a CSV
Building a dashboard (Streamlit)

## 📜 License

This project is free to use for learning and educational purposes.