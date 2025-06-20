from faker import Faker
import random
import pandas as pd

fake = Faker()
topics = ["payment", "delivery", "return", "bug", "question", "support"]
channels = ["email", "website", "telegram"]

data = []

for _ in range(2000):
    topic = random.choice(topics)
    channel = random.choice(channels)

    days_ago = random.randint(0, 180)
    date = pd.Timestamp.today().normalize() - pd.Timedelta(days=days_ago)

    entry = {
        "date": date.date().isoformat(),
        "channel": channel,
        "text": f"{fake.sentence()} {topic}",
        "label": topic,
    }
    data.append(entry)

df = pd.DataFrame(data)
df.to_csv("client_requests.csv", index=False)
print("✅ New dataset saved as client_requests.csv")
