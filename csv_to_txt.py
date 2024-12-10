import pandas as pd

# Load the CSV file
csv_file = "./amharic_dataset/Amharic News Dataset.csv"  # Replace with your CSV file name
df = pd.read_csv(csv_file)

# Specify the columns containing the text you want to extract (e.g., 'headline', 'article')
text_columns = ['headline', 'article']  # Replace with your text columns
text_data = df[text_columns].fillna('')  # Replace NaN with empty strings

# Combine the text from the selected columns into one line per row
text_data_combined = text_data.apply(lambda x: ' '.join(x).strip(), axis=1)

# Save the combined text to a .txt file
output_file = "amharic_text.txt"  # Desired output file name
with open(output_file, "w", encoding="utf-8") as f:
    for line in text_data_combined:
        f.write(line + "\n")

print(f"Text data has been successfully saved to {output_file}")
