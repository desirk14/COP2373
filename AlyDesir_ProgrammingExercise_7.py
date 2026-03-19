import re

# Function that extracts the sentences from the user's input
def extract_sentences(s):
    # Create a pattern that allows A-Z or digits at start and stops matching when ., ?, or ! occurs
    pat = r'([A-Z0-9][^.?!]*[.?!])'

    sentences = re.findall(pat, s, flags=re.DOTALL)

    # Remove spaces from each sentence and return the list
    return [s.strip() for s in sentences]

# Function that prints each sentence in the paragraph and the total number of sentences
def display_sentences(sentences):
    # Iterate through the sentences and count them
    for i, sentence in enumerate(sentences, start=1):
        print(f'{i}. {sentence}')

    print(f'\nTotal Number of Sentences: {len(sentences)}')
    return sentences

def main():
    # Ask the user to enter a paragraph
    paragraph = input('Enter a paragraph: ')

    sentences = extract_sentences(paragraph)

    # Display the sentences and the number of sentences
    display_sentences(sentences)

# Call the function
if __name__ == "__main__":
    main()