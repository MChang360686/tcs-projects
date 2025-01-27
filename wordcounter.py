from collections import Counter
import string

STOPWORDS = {'and', 'the', 'is', 'in', 'to', 'of', 'a', 'it'}

def clean_text(text):
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def tokenize(text):
    #print(text.split())
    return text.split()

def remove_stopwords(words):
    #print([word for word in words if word not in STOPWORDS])
    return [word for word in words if word not in STOPWORDS]

def count_words(words):
    return Counter(words)

def sort_by_frequency(word_counts):
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

def word_count_pipeline(input_text, top_n=10):
    cleaned_text = clean_text(input_text)
    words = tokenize(cleaned_text)
    filtered_words = remove_stopwords(words)
    word_counts = count_words(filtered_words)
    sorted_word_counts = sort_by_frequency(word_counts)

    print(f"Top {top_n} words:")
    for word, count in sorted_word_counts[:top_n]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    user_input = input("Enter a string of text: ")
    word_count_pipeline(user_input, top_n=5)