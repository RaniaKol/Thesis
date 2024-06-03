train_texts_grc = 'train_texts_grc.txt'
test_texts_grc = 'test_texts_grc.txt'
valid_texts_grc = 'valid_texts_grc.txt'

train_texts_en = 'train_texts_en.txt'
test_texts_en = 'test_texts_en.txt'
valid_texts_en = 'valid_texts_en.txt'

tok_train_texts_grc = 'tok_train_texts_grc.txt'
tok_test_texts_grc = 'tok_test_texts_grc.txt'
tok_valid_texts_grc = 'tok_valid_texts_grc.txt'

tok_train_texts_en = 'tok_train_texts_en.txt'
tok_test_texts_en = 'tok_test_texts_en.txt'
tok_valid_texts_en = 'tok_valid_texts_en.txt'

# Tokenize Greek texts
with open(train_texts_grc, 'r') as f:
    with open(tok_train_texts_grc, 'w') as f1:
        for line in f:
            tokenized_sentence = " ".join(line.strip().split())
            f1.write(tokenized_sentence + "\n")

with open(test_texts_grc, 'r') as f:
    with open(tok_test_texts_grc, 'w') as f1:
        for line in f:
            tokenized_sentence = " ".join(line.strip().split())
            f1.write(tokenized_sentence + "\n")

with open(valid_texts_grc, 'r') as f:
    with open(tok_valid_texts_grc, 'w') as f1:
        for line in f:
            tokenized_sentence = " ".join(line.strip().split())
            f1.write(tokenized_sentence + "\n")

# Tokenize English texts
with open(train_texts_en, 'r') as f:
    with open(tok_train_texts_en, 'w') as f1:
        for line in f:
            tokenized_sentence = " ".join(line.strip().split())
            f1.write(tokenized_sentence + "\n")

with open(test_texts_en, 'r') as f:
    with open(tok_test_texts_en, 'w') as f1:
        for line in f:
            tokenized_sentence = " ".join(line.strip().split())
            f1.write(tokenized_sentence + "\n")

with open(valid_texts_en, 'r') as f:
    with open(tok_valid_texts_en, 'w') as f1:
        for line in f:
            tokenized_sentence = " ".join(line.strip().split())
            f1.write(tokenized_sentence + "\n")
