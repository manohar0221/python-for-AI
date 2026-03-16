# Warning control
import warnings
warnings.filterwarnings('ignore')

from transformers import AutoTokenizer
from helper import show_tokens

# define the sentence to tokenize
sentence = "Hi, i am raj!"
show_tokens(sentence, "bert-base-cased")
# load the pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

encoding = tokenizer(sentence)

token_ids = encoding["input_ids"]
tokens = tokenizer.convert_ids_to_tokens(token_ids)

for token, token_id in zip(tokens, token_ids):
    print(f"{token:10} -> {token_id}")