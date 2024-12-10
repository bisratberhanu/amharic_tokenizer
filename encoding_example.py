from tokenizers import Tokenizer

tokenizer = Tokenizer.from_file("amharic_tokenizer.json")
text = "ሰላም ልጆች"

# Encode the text
encoded = tokenizer.encode(text)
print("Encoded:", encoded.ids)

# Decode the encoded ids
decoded = tokenizer.decode(encoded.ids)
print("Decoded:", decoded)