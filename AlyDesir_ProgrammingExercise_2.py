# Create list of spam words/phrases
spam_words = [
    "Act now", "100% Free", "Winner", "Winning", "limited time offer",
    "click here", "double your money", "congratulations", "best price",
    "no obligation", "earn money", "get paid", "risk-free",
    "satisfaction guaranteed", "you have been chosen", "weight-loss",
    "last chance", "affordable", "billion", "cash-out",
    "for free", "free access", "money-back guarantee",
    "save money", "bonus", "please read", "instant",
    "call now", "click here", "exclusive deal"
]

# Function for scanning spam words/phrases
def calculate_spam_score(message, spam_list):
    score = 0
    triggered_words = []

    # Ensures that words/phrases are counted whether capitalized or lowercase
    message_lower = message.lower()

    # For loop to count the number occurrences
    for word in spam_list:
        occurrences = message_lower.count(word.lower())
        if occurrences > 0:
            score += occurrences
            triggered_words.append(f"{word} (x{occurrences})")

    # Return for the spam score and list of triggered words
    return score, triggered_words


# Function that rates likelihood of spam
def rate_spam_likelihood(score):
    if score == 0:
        return "Very unlikely to be spam."
    elif 1 <= score <= 3:
        return "Low likelihood of spam."
    elif 4 <= score <= 6:
        return "Moderate likelihood of spam."
    elif 7 <= score <= 10:
        return "High likelihood of spam."
    else:
        return "Very high likelihood of spam."


# Main function to enter email
def main():
    print("=== Spam Detection Application ===")
    message = input("Enter the email message:\n")

    score, triggered = calculate_spam_score(message, spam_words)
    likelihood = rate_spam_likelihood(score)

    # Display the results of the spam scanning
    print("=== Spam Analysis Results ===")
    print(f"Spam Score: {score}")
    print(f"Likelihood: {likelihood}")

    # Display which words/phrases were detected
    if triggered:
        print("Spam words/phrases detected:")
        for word in triggered:
            print("-", word)
    else:
        print("No spam words detected.")


# Run the application
if __name__ == "__main__":
    main()