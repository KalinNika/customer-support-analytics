import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

df = pd.read_csv("client_requests.csv")
df_count = df.groupby("date").size().reset_index(name="y")

plt.figure(figsize=(10, 5))
plt.plot(df_count["date"], df_count["y"], marker="o", linestyle="-", color="blue")
plt.title("Number of Requests by Day")
plt.xlabel("Date")
plt.ylabel("Requests")
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
plt.tight_layout()
plt.savefig("chart.png", dpi=300)
plt.close()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)  # используем встроенный шрифт без кириллицы
pdf.cell(200, 10, txt="Weekly Report", ln=True, align="C")
pdf.image("chart.png", x=10, y=30, w=180)
pdf.output("weekly_report.pdf")

print("✅ Report saved as weekly_report.pdf")
