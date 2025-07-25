# 🤖 AI Module for Customer Support Analytics

This module enhances the **Customer Support Analytics** project with Large Language Models (LLMs) to classify, summarize, and analyze customer support data using neural networks.

It demonstrates practical AI applications such as:

- 🔠 Zero-shot classification of customer requests
- 🧾 Generation of human-readable summaries for reports
- 🔍 Comparison of LLMs like GPT-4, Claude, and Gemini
- ⚙️ Configurable prompts and temperature settings

---

## 📁 Files Included

| File | Description |
|------|-------------|
| [`gpt_pipeline.py`](gpt_pipeline.py) | Script to run classification/summarization via LLM |
| [`llm_config.json`](llm_config.json) | JSON configuration with model, temperature, and prompt settings |
| [`llm_config.py`](llm_config.py) | Helper to load and parse `llm_config.json` |
| [`model_comparison.md`](model_comparison.md) | Results and analysis of model comparison |
| [`prompt_classification.txt`](prompt_classification.txt) | Prompt for request classification |
| [`prompt_forecast.txt`](prompt_forecast.txt) | Prompt for interpreting future request forecasts |
| [`prompt_summary.txt`](prompt_summary.txt) | Prompt for weekly summary generation |
| [`llm_sample_output.pdf`](https://github.com/KalinNika/customer-support-analytics/raw/main/weekly_report.pdf) | Example of LLM-generated report output |


---

## ⚙️ How It Works

The module loads a saved prompt and sends it to an LLM (e.g., GPT-4) using OpenAI's API. It can:

- Classify customer requests by intent
- Interpret time-series forecasts
- Generate natural language summaries for weekly reports

All outputs can be included in the final report sent via Telegram (`send_report_bot.py`).

---

## 🔧 Configuring the LLM

Model settings are stored in `llm_config.json`:

```json
{
  "model": "gpt-4",
  "temperature": 0.2,
  "system_prompt": "You are an assistant classifying support requests for a customer service department..."
}
```


#### 🔬 Model Comparison
See model_comparison.md for a qualitative analysis of LLM outputs:
| Prompt File              | Purpose                                      |
|--------------------------|----------------------------------------------|
| prompt_classification.txt| Categorize user requests by topic            |
| prompt_forecast.txt      | Translate numeric forecasts into plain language |
| prompt_summary.txt       | Create a summary for a weekly support report |


Each model was tested on real prompts from this project. Differences in tone, structure, and accuracy are discussed.

# ✍️ Prompt Design
Prompts were tailored to the context of real client request data:

Prompt	Purpose
prompt_classification.txt	Categorize user requests by topic
prompt_forecast.txt	Translate numeric forecasts into plain language
prompt_summary.txt	Create a summary for a weekly support report

The design emphasizes clear task instructions and consistent formatting.


# 📎 Sample LLM Output (PDF)

This output shows how the AI complements the traditional ML pipeline by generating readable summaries and insightful classifications.

📄 [Sample LLM Output (PDF)](https://github.com/KalinNika/customer-support-analytics/raw/main/ai_module/summary_report.pdf)


This output shows how the AI complements the traditional ML pipeline by generating readable summaries and insightful classifications.

# 🧩 Integration with Main Project
This module builds on the main pipeline by:

🔁 Enhancing or replacing TF-IDF + Naive Bayes classification

📈 Making time series output human-readable

🤖 Automating insights through prompt engineering

📬 Embedding outputs into final reports via send_report_bot.py

It’s fully modular — easily replaceable or extendable with new models or tasks.
