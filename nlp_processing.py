from transformers import pipeline

def classify_text(text):
    classifier = pipeline('sentiment-analysis')
    return classifier(text)

# Usage
result = classify_text('This is a sample text for classification.')
print(result)
