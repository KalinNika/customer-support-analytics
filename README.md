# 📊 Customer Support Analytics

**End-to-end NLP & forecasting pipeline with Telegram automation**

This project analyzes customer support requests using classical machine learning tools, enhanced with GPT-based AI models (see [`ai_module/`](./ai_module)).

---

## 🚀 Features

- 📬 Generate realistic support messages using `Faker`
- 🧹 Clean and vectorize text data with `TF-IDF`
- 📊 Classify request topics using `Naive Bayes`
- 📈 Forecast daily request volume with `Prophet`
- 📄 Create weekly PDF reports with `matplotlib` and `FPDF`
- 🤖 Automate report delivery via Telegram bot (scheduled every Monday)
- 🧠 Enhance analytics with LLMs (GPT) for:
  - Topic classification via prompt engineering
  - Time series summarization
  - Natural language insights and reporting

![image](https://github.com/user-attachments/assets/53c5fbc2-397c-480d-87e2-c18ea477d84c)

---

## 📁 Project Structure

- `generate_data.py` — generates synthetic dataset
- `preprocessing.ipynb` — cleans text and trains classifier
- `forecasting.ipynb` — creates request forecast
- `generate_report.py` — builds the weekly PDF report
- `send_report_bot.py` — Telegram bot logic
- `ai_module/` — GPT/LLM integration module 🔥

## 🔍 AI Integration (`ai_module/`)

The `ai_module` folder contains GPT-based enhancements to the traditional pipeline:

- 🔤 Prompt-based classification, forecasting, and summarization
- ⚙️ Custom LLM configurations via `llm_config.json`
- 📊 Comparison of different LLMs (e.g., GPT-4, Claude, Gemini)
- 📄 AI-generated output sample ([Weekly Report](https://github.com/KalinNika/customer-support-analytics/blob/main/weekly_report.pdf))

Explore full details in [`ai_module/README.md`](https://github.com/KalinNika/customer-support-analytics/blob/main/ai_module/README.md)

---

## 🧠 Tech Stack

- **Languages & Environment**: Python 3.12, Jupyter Notebook
- **Data Processing & ML**: pandas, scikit-learn, Prophet
- **Visualization & Reporting**: matplotlib, FPDF
- **Synthetic Data Generation**: Faker
- **Automation & Scheduling**: schedule, threading
- **Telegram Integration**: pyTelegramBotAPI
- **AI & LLM Integration**: OpenAI API (GPT)


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


