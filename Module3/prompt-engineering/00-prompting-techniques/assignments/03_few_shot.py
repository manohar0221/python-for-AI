import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Classify the sentiment of the following sentences as Positive, Negative, or Neutral.

Sentence: I love this product, it works perfectly!
Sentiment: Positive

Sentence: This is the worst experience I have ever had.
Sentiment: Negative

Sentence: The product is okay, nothing special.
Sentiment: Neutral

Sentence: The delivery was fast and the packaging was great.
Sentiment:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)