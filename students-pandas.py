import pandas as pd

students = pd.read_csv("StudentsPerformance.csv")

print(students.head())

students['total_score'] = students['math score'] + students['reading score'] + students['writing score']
students['average_score'] = students['total_score'] / 3
students['passed_all'] = (students['math score'] >= 50) & (students['reading score'] >= 50) & (students['writing score'] >= 50)
students['high_achiever'] = students['average_score'] >= 85

# Section 4: Summarization with Pandas

def summarize_engine(df, group_col, value_cols, agg):
    return (
        df
        .groupby(group_col)[value_cols]
        .agg(agg)
    )

def summarize_validator(df, group_col, value_cols, agg):
    if group_col not in df.columns:
        raise ValueError("Invalid group column")
    for col in value_cols:
        if col not in df.columns:
            raise ValueError(f"Value column '{col}' not found in dataframe")
    if agg not in ['mean', 'median', 'sum']:
        raise ValueError("Invalid aggregation function")

def summarize_input(df):
    print("Available columns:")
    print(df.columns.tolist())
    group_col = input("Group by column: ").strip()
    agg = input("Aggregation (mean, median, sum): ").strip()
    value_cols_input = input("Enter numeric columns separated by commas (default all): ").strip()
    if value_cols_input:
        value_cols = [col.strip() for col in value_cols_input.split(",")]
    else:
        value_cols = ["math score", "reading score", "writing score"]
    return group_col, value_cols, agg  

def summarize_interface(df):
    group_col, value_cols, agg = summarize_input(df)
    summarize_validator(df, group_col, value_cols, agg)
    result = summarize_engine(df, group_col, value_cols, agg)
    
    print(f"\nSummary grouped by '{group_col}' ({agg}):\n")
    print(result.to_string())
    return result


# Section 5: Conditional Comparison with Pandas

def comparison_engine(df, category_col, numeric_cols, conditionA, conditionB, agg):
    aggregated = df.groupby(category_col)[numeric_cols].agg(agg)

    group_A = aggregated.loc[conditionA]
    group_B = aggregated.loc[conditionB]

    absolute_difference = group_A - group_B
    relative_difference = (group_A - group_B) / group_B * 100

    return group_A, group_B, absolute_difference, relative_difference

def comparison_input(df):
    print("Available columns:")
    print(df.columns.tolist())
    category_col = input("Category column: ").strip()
    conditionA = input("Condition A: ").strip()
    conditionB = input("Condition B: ").strip()
    numeric_cols = ["math score", "reading score", "writing score"]
    agg = input("Aggregation (mean, median, sum): ")
    return category_col, numeric_cols, conditionA, conditionB, agg

def comparison_validator(df, category_col, conditionA, conditionB, numeric_cols, agg):
    if category_col not in df.columns:
        raise ValueError("Invalid category column")
    if conditionA not in df[category_col].values:
        raise ValueError("Condition A not found in category column")
    if conditionB not in df[category_col].values:
        raise ValueError("Condition B not found in category column")
    if agg not in ['mean', 'median', 'sum']:
        raise ValueError("Invalid aggregation function")
    for col in numeric_cols:
        if col not in df.columns:
            raise ValueError(f"Numeric column '{col}' not found in dataframe")

    
def comparison_interface(df):
    category_col, numeric_cols, conditionA, conditionB, agg = comparison_input(df)
    comparison_validator(df, category_col, conditionA, conditionB, numeric_cols, agg)
    results = comparison_engine(df, category_col, numeric_cols, conditionA, conditionB, agg)
    group_A, group_B, abs_diff, rel_diff = results
    for col in numeric_cols:
        print(f"{col}: {group_A[col]} | {group_B[col]} | {abs_diff[col]} | {rel_diff[col]:.1f}%")
