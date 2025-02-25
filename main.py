import pandas as pd


data = {
    "سن": [25, 30, 22, 35, 28],
    "قد (cm)": [175, 180, 168, 182, 190],
    "وزن (kg)": [70, 80, 65, 85, 75]
}

df = pd.DataFrame(data)

# Calculate normalization of data
df["سن نرمال"] = (df["سن"] - df["سن"].min()) / (df["سن"].max() - df["سن"].min())
df["قد نرمال"] = (df["قد (cm)"] - df["قد (cm)"].min()) / (df["قد (cm)"].max() - df["قد (cm)"].min())
df["وزن نرمال"] = (df["وزن (kg)"] - df["وزن (kg)"].min()) / (df["وزن (kg)"].max() - df["وزن (kg)"].min())

# Save the DataFrame to an Excel file
file_path = "data/output.xlsx"
df.to_excel(file_path, index=False)
