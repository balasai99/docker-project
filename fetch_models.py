import requests
import json

def fetch_top_models():
    url = "https://huggingface.co/api/models?sort=downloads"
    response = requests.get(url)
    models = response.json()

    top_10_models = models[:10]
    report = "Top 10 Downloaded Models on Hugging Face:\n"
    for i, model in enumerate(top_10_models, 1):
        report += f"{i}. {model['modelId']} - Downloads: {model['downloads']}\n"

    with open("/reports/top_10_models.txt", "w") as file:
        file.write(report)

if __name__ == "__main__":
    fetch_top_models()
