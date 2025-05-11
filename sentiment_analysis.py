from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text using VADER sentiment analysis.

    Parameters:
    text (str): The text to analyze.

    Returns:
    float: A sentiment score between -1 (negative) and 1 (positive).
    """
    # Initialize the VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Get the sentiment scores
    sentiment_score = analyzer.polarity_scores(text)
    
    # Return the compound score, which is a normalized score between -1 and 1
    return sentiment_score['compound']

# Example usage (optional)
if __name__ == "__main__":
    sample_text = "I love this product! It's amazing."
    score = analyze_sentiment(sample_text)
    print(f"Sentiment score for the text: {score}")