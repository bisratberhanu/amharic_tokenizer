# amharic_tokenizer

This repository contains an Amharic tokenizer. The model is trained using a very simple transformer architecture as suggested by Andrew Karpathy in his [YouTube course](link).

## Files

- `tokenizer.py`: Contains the building of the tokenizer using the file `amharic_txt_tokenizing`.
- `test.py`: A test to check basic tokenizing operations.
- `encoding_example.py`: An example showing the encoder in action.
- `csv_to_txt.py`: A script to change a the  csv file(found here) to txt file. since the txt file returned from this particular csv is very large, I have shortened it to `amharic_text_shortened`. but make sure the folder amharic_dataset is created locally and the csv file is found inside.

- `bigram_model.py`: Where training of the model and a basic example is shown.
- `gpt.py`: A larger part of `bigram_model.py` that contains more classes for better context and output.

## How to Run

1. Run the `tokenizer.py` file to get the JSON file.
2. Run the `bigram_model.py` and see the outputs.

## Issues

The current implementation suffers from high validation loss, most likely due to overfitting. Feel free to improve the `amharic_text_shortened` and see better results.