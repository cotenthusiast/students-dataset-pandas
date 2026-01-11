import pandas as pd

students = pd.read_csv("StudentsPerformance.csv")

print(students.head())

students['total_score'] = students['math score'] + students['reading score'] + students['writing score']
students['average_score'] = students['total_score'] / 3
students['passed_all'] = (students['math score'] >= 50) & (students['reading score'] >= 50) & (students['writing score'] >= 50)
students['high_achiever'] = students['average_score'] >= 85

def summarize(df, group_col, value_cols, agg):
    return (
        df
        .groupby(group_col)[value_cols]
        .agg(agg)
    )

def summarize_interface(df):
    print("Available columns:")
    print(df.columns.tolist())

    group_col = input("Group by column: ")
    agg = input("Aggregation (mean, median, sum): ")

    value_cols = ["math score", "reading score", "writing score"]

    if group_col not in df.columns:
        raise ValueError("Invalid column")
    
    return summarize(df, group_col, value_cols, agg)