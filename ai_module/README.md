# 🧠 AI Module: GPT-Powered Classification Extension

This module enhances the main **Customer Support Analytics** pipeline by integrating large language models (LLMs) to compare traditional and neural approaches for request classification.

---

## ⚙️ Purpose

🔍 To evaluate the accuracy and interpretability of GPT-based classification  
📊 To prototype prompt-based automation for support ticket categorization  
🤖 To prepare for further GPT integration into support pipelines

---

## 📁 Module Structure

| File | Description |
|------|-------------|
| `gpt_prompt_examples.txt` | Prompt samples used for manual LLM testing |
| `gpt_config.txt` | Settings (model, temperature, system prompt, etc.) |
| `gpt_results_comparison.txt` | Output comparison: TF-IDF vs. GPT-4 vs. Gemini |
| `gpt_pipeline.py` | Code that loads a GPT model and performs classification |
| `llm_sample_output.pdf` | Sample of real GPT output (classification results) |

---

## 💬 Prompt Sample

> **System prompt**:  
> _"You are an expert customer support classifier. Based on the text, classify it into one of the following: payment, delivery, return, bug, question, support."_

> **User prompt example**:  
> _"The product was damaged during delivery and I want to return it."_

> **Expected output**:  
> _"return"_

---

## 🧪 Model Settings

```txt
Model: GPT-4
Temperature: 0.3
System Prompt: Classify messages into one of six topics based on meaning.
Max Tokens: 100
Top-p: 1.0


🆚 Comparison: ML vs. LLM
Model	Accuracy	Pros	Cons
Naive Bayes (TF-IDF)	~88%	Fast, interpretable	Fails on ambiguous phrasing
GPT-4	~94%	Context-aware, flexible	Slower, costlier
Gemini	~92%	Stable, multilingual	Slightly verbose

📎 See gpt_results_comparison.txt for details.

📎 Sample Output


(If preview fails, open the file manually from the repo.)

🔮 Future Directions
✅ GPT auto-classification integration into main pipeline

🪄 Smart reply suggestions for agents

📬 AI triage based on urgency and sentiment

🙌 Author
Nika Kalinnikova

