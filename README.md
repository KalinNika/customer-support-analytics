# 📊 Customer Support Analytics

**End-to-end NLP & forecasting pipeline with Telegram automation**

This project simulates and analyzes customer support requests using machine learning and time series forecasting.

---

## 🚀 Features

- Generate realistic support messages using `Faker`
- Preprocess and vectorize text via `TF-IDF`
- Classify requests using `Naive Bayes`
- Forecast request volume using `Prophet`
- Create PDF reports with `matplotlib` and `FPDF`
- Send reports automatically via Telegram bot every Monday
![image](https://github.com/user-attachments/assets/53c5fbc2-397c-480d-87e2-c18ea477d84c)

---

## 🧠 Tech Stack

- Python 3.12  
- pandas · scikit-learn · matplotlib  
- prophet · faker · fpdf  
- pyTelegramBotAPI · schedule · threading


## 🔍 AI Module Integration

See [`ai_module/`](./ai_module) for GPT-based enhancement of classification and reporting logic.

---

## 🗂️ Project Structure
📦 customer-support-analytics
├── notebooks/
│ ├── preprocessing.ipynb
│ └── forecasting.ipynb
├── scripts/
│ ├── generate_data.py
│ ├── generate_report.py
│ └── send_report_bot.py
├── data/
│ └── client_requests.csv
├── reports/
│ └── weekly_report.pdf
├── requirements.txt
└── README.md
## ✅ How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/customer-support-analytics.git
   cd customer-support-analytics
2. **Create and activate virtual environment**  
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
3. pip install -r requirements.txt
4. jupyter notebook

🤖 Telegram Bot
Use /report command to receive the latest PDF report

Sends the report automatically every Monday at 10:00 AM

## 📄 Example PDF Report

This is a sample of the automatically generated weekly report.
![image](https://github.com/user-attachments/assets/542b8e80-6d15-45a7-9cf5-b65151dc8e0b)


👤 Author
Nika Kalinnikova
Junior Business & System Analyst · Python · SQL · R · Forecasting · Automation


