from transformers import pipeline

# Create a sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Sample conversation
conversation = [
    ("User", "Hello! How are you today?"),
    ("Chatbot", "Hi there! I'm doing great, thank you."),
    ("User", "That's good to hear! I have a question about programming."),
    ("Chatbot", "Of course, feel free to ask your question."),
]

# Copy the conversation for sentiment analysis
copied_conversation = [msg for _, msg in conversation]

# Open a text file for writing
with open("sentiment_scores.txt", "w") as file:
    file.write("User Message\tSentiment Score\n")
    
    # Perform sentiment analysis on each message and write to the file
    for i, message in enumerate(copied_conversation):
        sentiment = sentiment_analyzer(message)[0]
        sentiment_score = sentiment['score']
        
        file.write(f"{message}\t{sentiment_score:.3f}\n")

print("Sentiment scores written to sentiment_scores.txt")
