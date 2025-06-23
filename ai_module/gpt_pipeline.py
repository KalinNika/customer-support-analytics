import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("client_requests.csv")
df_count = df.groupby("date").size().reset_index(name="y")

plt.plot(df_count["date"], df_count["y"], marker="o")
plt.title("Requests by Date")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
