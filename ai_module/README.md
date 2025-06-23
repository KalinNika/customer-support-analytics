# 🧠 AI Module for Customer Support Analytics

This module demonstrates the integration of large language models (LLMs) into the **Customer Support Analytics** project to enhance text understanding, automate processes, and enrich business insights.

## 💡 What This Module Does

- Performs zero-shot and prompt-based classification of customer requests using LLMs  
- Generates short summaries and interpretable labels  
- Compares outputs of different models (e.g., GPT-4 vs Gemini vs Claude)  
- Explores advanced prompt design and configuration for reliable automation  
- Enhances human-written ML pipelines with LLM-backed augmentation  

## 📂 File Overview

| File | Purpose |
|------|---------|
| **gpt_pipeline.py** | End-to-end classification pipeline using OpenAI API and local config |
| **llm_config.json** | Stores LLM parameters: model, temperature, system prompt |
| **llm_config.py** | Python handler to parse and use `llm_config.json` |
| **model_comparison.md** | Comparison of model outputs (GPT-4, Gemini, Claude) with insights |
| **prompt_classification.txt** | Prompt template for request classification |
| **prompt_forecast.txt** | Prompt to generate demand forecast explanation |
| **prompt_summary.txt** | Prompt to create summaries for weekly reports |
| **llm_sample_output.pdf** | 📎 [Click to view sample classification (PDF)](https://github.com/KalinNika/customer-support-analytics/raw/main/ai_module/llm_sample_output.pdf) |

---

## 🛠️ Pipeline Overview

The pipeline in `gpt_pipeline.py` reads customer request data and:

1. Applies a structured classification prompt (from `prompt_classification.txt`)
2. Sends it to the OpenAI API (configured via `llm_config.json`)
3. Outputs results to a DataFrame and saves them
4. Generates a summary via `prompt_summary.txt`
5. Visualizes the classification logic or forecasts if desired

---

## 🔧 Configuring the LLM

All parameters are defined in `llm_config.json`, such as:

```json
{
  "model": "gpt-4",
  "temperature": 0.2,
  "system_prompt": "You are an assistant classifying support requests for a customer service department..."
}


📊 Model Comparison
The document model_comparison.md provides a qualitative comparison of how different models respond to the same classification and summarization tasks.

It contains:

✅ Strengths and weaknesses per model

🔁 Observed consistency and hallucination rates

🔍 Examples of task misinterpretation and recoveries

🧪 Prompt Engineering
Each prompt was crafted and refined based on:

Real customer data (client_requests.csv)

Business labels used in classic ML model (preprocessing.ipynb)

Need for interpretable, fast, and reliable output

Explore them:

prompt_classification.txt

prompt_forecast.txt

prompt_summary.txt

---

🤖 Use Cases in This Project
This AI module supplements the original project by:

Replacing or augmenting TF-IDF + Naive Bayes with LLM reasoning

Enabling text summarization for reports

Improving explainability for stakeholders

Accelerating idea validation and data exploration

📈 Example Output
Below is a clickable example of model-generated classifications and summaries:

📎 Click to view sample classification (PDF)

🧩 Integration
This module is designed to be complementary to the core pipeline:

Use gpt_pipeline.py to classify or summarize new requests

Use send_report_bot.py to deliver weekly PDF reports

Link results into dashboards or decision logic as needed

