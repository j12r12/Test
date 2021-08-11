import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("JR.csv", dayfirst=True)

df.drop(["Transaction Type", "Sort Code", "Account Number"], axis=1, inplace=True)

df["Datetime"] = pd.to_datetime(df["Transaction Date"]) # Need to change the format here as something is wrong

df.set_index("Datetime", inplace=True)

df_months = df.resample("M").sum()

print(df_months)
print("HELLO")

df_months["Balance"].plot.bar()
plt.title("Testing")

plt.show()



