import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

# Count the number of males and females
male_count = df[df["GENDER"] == "M"].shape[0]
female_count = df[df["GENDER"] == "F"].shape[0]

# Print the counts
print("Total Males:", male_count)
print("Total Females:", female_count)

# Alternatively, use value counts for all categories
gender_counts = df["GENDER"].value_counts()
print("\nGender Distribution:")
print(gender_counts)

if len(gender_counts) == 2:  # Check if only two categories (male, female)
    gender_counts.plot(kind="bar", color=["blue", "pink"])
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()


# Clean the column names (optional, replace if names are already clean)
clean_cols = [x.strip().lower() for x in df.columns]
df.columns = clean_cols

# Filter rows with "YES" in lung_cancer column
lung_cancer_df = df[df['lung_cancer'] == "YES"]

# Count the number of males and females with lung cancer
males_with_cancer = lung_cancer_df[lung_cancer_df['gender'] == "M"].shape[0]
females_with_cancer = lung_cancer_df[lung_cancer_df['gender'] == "F"].shape[0]

# Prepare data for pie chart
labels = ["Males", "Females"]
sizes = [males_with_cancer, females_with_cancer]

# Create the pie chart
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=["lightblue", "lightcoral"])
plt.title("Gender Distribution of Lung Cancer Cases")
plt.axis("equal")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Create a dictionary for translating codes to yes/no
code_map = {1: "Yes", 2: "No"}

# Sample data (replace with your CSV data)
data = pd.read_csv('dataset.csv')

# Create DataFrame, converting codes to yes/no using the code_map
df = pd.DataFrame(data, columns=["GENDER", "AGE", "SMOKING", "YELLOW_FINGERS", "ANXIETY", "PEER_PRESSURE", "CHRONIC_DISEASE", "FATIGUE", "ALLERGY", "WHEEZING", "ALCOHOL_CONSUMING", "COUGHING", "SHORTNESS_OF_ breath", "SWALLOWING_DIFFICULTY", "CHEST_PAIN", "LUNG_CANCER"])
df["YELLOW_FINGERS"] = df["YELLOW_FINGERS"].replace(code_map)

# Filter for people with yellow fingers
df_filtered = df[df["YELLOW_FINGERS"] == "Yes"]

# Fix: Convert relevant columns to numeric before value_counts
df_filtered_numeric = df_filtered.iloc[:, 2:].apply(pd.to_numeric, errors='coerce')  # Convert to numeric, handle errors (coerce to NaN)
yes_no_counts = df_filtered_numeric.apply(pd.value_counts).fillna(0)

# Extract data for the bar graph (assuming you want counts for all yes/no options)
yes_counts = yes_no_counts.iloc[0]  # Get the first row (counts for "Yes")
no_counts = yes_no_counts.iloc[1]  # Get the second row (counts for "No")
x_axis_labels = yes_no_counts.columns.tolist()  # Get column names as x-axis labels

# Create the bar graph
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
bar_width = 0.35  # Adjust bar width as needed
index = range(len(x_axis_labels))
plt.bar(index, yes_counts, bar_width, label="Yes", color="lightblue")
plt.bar([i + bar_width for i in index], no_counts, bar_width, label="No", color="lightcoral")
plt.xlabel("Symptoms (YES/NO)")
plt.ylabel("Count")
plt.title("People Having Cancer")
plt.xticks([i + bar_width / 2 for i in index], x_axis_labels, rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.legend()
plt.tight_layout()
plt.show()
