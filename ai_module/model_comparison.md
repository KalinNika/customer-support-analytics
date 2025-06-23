# Model Comparison: GPT-4 vs Claude vs Gemini

## Task: Classify customer request types

### Example Input:
> "I want to return the item I ordered last week. It was damaged."

### Results:

| Model     | Output  | Notes                     |
|-----------|---------|---------------------------|
| GPT-4     | return  | Correct, confident answer |
| Claude    | refund  | Close, but not exact match|
| Gemini    | return  | Correct                   |

GPT-4 and Gemini returned the expected label. Claude used a synonym that might require normalization.
