from tokenizers import Tokenizer, models, trainers, pre_tokenizers

# Initialize a tokenizer with a BPE model
tokenizer = Tokenizer(models.BPE())

# Pre-tokenization rules (e.g., split on spaces)
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

# Define the trainer
trainer = trainers.BpeTrainer(special_tokens=["<pad>", "<unk>", "<bos>", "<eos>"])

# Load your Amharic dataset
files = ["amharic_text_tokenizing.txt"]

# Train the tokenizer
tokenizer.train(files, trainer)

# Save the tokenizer
tokenizer.save("amharic_tokenizer.json")
