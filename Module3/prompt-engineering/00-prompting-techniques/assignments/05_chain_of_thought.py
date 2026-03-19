import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Solve the following problem step by step.

A shop sells pens at ₹10 each and notebooks at ₹50 each.
Rahul buys 3 pens and 2 notebooks.

First, calculate the total cost of pens.
Then, calculate the total cost of notebooks.
Finally, add both to get the total amount.

Think step by step and show your reasoning before giving the final answer.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)