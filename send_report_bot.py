import telebot
import schedule
import time
import threading
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

API_TOKEN = "7621540595:AAGiUOsqH8X51lUBAocpXVtAXphq6Qj6iFI"
CHAT_ID = "@HayleyRizhik"

bot = telebot.TeleBot(API_TOKEN)

PDF_PATH = "weekly_report.pdf"
CSV_PATH = "client_requests.csv"


def generate_pdf():
    df = pd.read_csv(CSV_PATH)
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
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Weekly Report", ln=True, align="C")
    pdf.image("chart.png", x=10, y=30, w=180)
    pdf.output(PDF_PATH)


def send_report():
    generate_pdf()
    with open(PDF_PATH, "rb") as f:
        bot.send_document(CHAT_ID, f)
    print("✅ Report sent automatically.")


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Hi! Use /report to get the latest report.")


@bot.message_handler(commands=["report"])
def handle_report(message):
    generate_pdf()
    with open(PDF_PATH, "rb") as f:
        bot.send_document(message.chat.id, f)


schedule.every().monday.at("10:00").do(send_report)


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

print("🤖 Bot is running with weekly auto-report. Ctrl+C to stop.")
bot.infinity_polling()
