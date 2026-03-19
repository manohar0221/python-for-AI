import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Convert the sentence into a more professional business tone.

Example:
Input: send me the file fast
Output: Could you please share the file at your earliest convenience?

Now do the same for:
Input: I need this work today only
Output:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)