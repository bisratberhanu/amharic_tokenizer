from tokenizers import Tokenizer

tokenizer = Tokenizer.from_file("amharic_tokenizer.json")
encoding = tokenizer.encode("ሰላም ለዓለም!")
print(encoding.tokens)  # Output: tokenized Amharic text
