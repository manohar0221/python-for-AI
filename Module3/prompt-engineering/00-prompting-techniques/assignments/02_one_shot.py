import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Rewrite the below sentense.

Example:
Input: send me the file fast 
Output: Could you please share the file at your earliest convenience?

Now do the same for:
Input: Rewrite the below sentense.

Sentense: "I play very well cricket."
output: 
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)