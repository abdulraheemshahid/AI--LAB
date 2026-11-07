
import re

samples = [
    "AI, search!",                 # Punctuation
    "I can't log in.",             # Contraction
    "help@example.com",            # Email
    "CS4944 version 2.1",          # Course identifier
    "",                            # Empty string
    "یہ ایک مثال ہے"                # Urdu text
]
for text in samples:
    whitespace_tokens = text.split()
    regex_tokens = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print("\nOriginal Text:", repr(text))
    print("Whitespace Tokens:", whitespace_tokens)
    print("Whitespace Count:", len(whitespace_tokens))
    print("Regex Tokens:", regex_tokens)
    print("Regex Count:", len(regex_tokens))
try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2",
        device="cpu"
    )
    print("\nMODEL TOKENIZER RESULTS")
    for text in samples[:2]:
        tokens = model.tokenizer.tokenize(text)
        print("Original:", text)
        print("Model Tokens:", tokens)
        print("Model Token Count:", len(tokens))
except ImportError:
    print("\nSentence Transformers is not installed.")
    print("Install it using: pip install sentence-transformers")
except Exception as error:
    print("\nModel tokenizer could not run:", error)
