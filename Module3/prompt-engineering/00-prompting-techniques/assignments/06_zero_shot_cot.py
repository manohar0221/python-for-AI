import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Solve the following problem step by step.

A person earns ₹500 per day and works for 26 days in a month. They spend ₹8,000 on rent and ₹5,000 on other expenses.

First, calculate the total monthly income.
Then, calculate the total expenses.
Finally, determine how much money is saved at the end of the month.

Think step by step and show your reasoning before giving the final answer.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)