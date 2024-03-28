import pandas as pd
from textblob import TextBlob

# Function to analyze sentiment of a single comment
def analyze_sentiment(comment):
    # Perform sentiment analysis using TextBlob
    blob = TextBlob(comment)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Function to analyze sentiment of multiple comments
def analyze_multiple_sentiments(comments):
    sentiments = []
    for comment in comments:
        sentiment = analyze_sentiment(comment)
        sentiments.append(sentiment)
    return sentiments

# Example comments (replace with your dataset)
comments = [
    "I love this product! It's amazing.",
    "The service was terrible, never going back.",
    "Neutral comment here.",
    "The quality is good, but the price is too high.",
    "Excellent customer support!"
]

# Analyze sentiments of the comments
sentiments = analyze_multiple_sentiments(comments)

# Create a DataFrame to display results
results = pd.DataFrame({'Comment': comments, 'Sentiment': sentiments})
print(results)
