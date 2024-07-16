import pandas as pd
import matplotlib.pyplot as plt

# Load data (replace with your actual file path)
df = pd.read_csv("dataset.csv")

# Clean column names (optional)
clean_cols = [x.strip().lower() for x in df.columns]
df.columns = clean_cols

# Handle missing values (optional, replace with your logic)
# Example: fill numeric columns with mean, categorical with mode
df.fillna(df.mean(numeric_only=True), inplace=True)  # Numeric
df.fillna(df.mode(axis=0), inplace=True)  # Categorical

# Gender Distribution
male_count = df[df["gender"] == "M"].shape[0]
female_count = df[df["gender"] == "F"].shape[0]
print("Total Males:", male_count)
print("Total Females:", female_count)

gender_counts = df["gender"].value_counts()
gender_counts.plot(kind="bar", color=["blue", "pink"])
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Symptom Analysis (Replacing Codes)
code_map = {1: "yes", 2: "no"}
df["yellow_fingers"] = df["yellow_fingers"].replace(code_map)

df_filtered = df[df["yellow_fingers"] == "yes"]
df_filtered_numeric = df_filtered.iloc[:, 2:].apply(pd.to_numeric, errors='coerce')
yes_no_counts = df_filtered_numeric.apply(pd.value_counts).fillna(0)

yes_counts = yes_no_counts.iloc[0]
no_counts = yes_no_counts.iloc[1]
x_axis_labels = yes_no_counts.columns.tolist()

plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(x_axis_labels))
plt.bar(index, yes_counts, bar_width, label="Yes", color="lightblue")
plt.bar([i + bar_width for i in index], no_counts, bar_width, label="No", color="lightcoral")
plt.xlabel("Symptoms (YES/NO)")
plt.ylabel("Count")
plt.title("People Having Cancer")
plt.xticks([i + bar_width / 2 for i in index], x_axis_labels, rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.show()

# Lung Cancer Distribution (Pie Chart)
cancer_counts = df['lung_cancer'].value_counts()
plt.pie(cancer_counts, labels=cancer_counts.index, autopct="%1.1f%%")
plt.title('Lung Cancer Distribution')
plt.show()

# Age vs. Smoking Status (Dot Graph)
plt.scatter(df['age'], df['smoking'])
plt.xlabel('Age')
plt.ylabel('Smoking Status')
plt.title('Age vs. Smoking Status')
plt.show()