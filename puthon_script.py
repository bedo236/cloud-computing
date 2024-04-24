import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

def read_document(file_path):
    # Read the content of the document from the specified file path
    with open(file_path, 'r') as file:
        document = file.read()
    return document

def remove_stopwords_from_document(document):
    # Tokenize the document and remove stopwords using NLTK
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(document)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def count_character_occurrences(text):
    # Count the occurrences of each character in the given text
    text = text.replace(" ", "")  # Remove spaces before counting characters
    char_occurrences = Counter(text)
    return char_occurrences

def print_character_occurrences(char_occurrences):
    # Print the occurrences of each character
    for char, occurrence in char_occurrences.items():
        print(f"The character '{char}' appears {occurrence} times.")

file_path = "/app/random_paragraphs.txt"

document = read_document(file_path)

filtered_document = remove_stopwords_from_document(document)

char_occurrences = count_character_occurrences(filtered_document)

print_character_occurrences(char_occurrences)

number_of_characters_original = sum(1 for char in document if char.isalnum())
number_of_characters_filtered = sum(1 for char in filtered_document if char.isalnum())

print(f"Total characters before filtering: {number_of_characters_original:,}")
print(f"Total characters after filtering: {number_of_characters_filtered:,}")