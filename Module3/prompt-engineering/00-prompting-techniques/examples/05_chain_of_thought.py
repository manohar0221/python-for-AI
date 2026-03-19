import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
A small business sells 120 products per month at ₹500 each.
Its monthly marketing spend is ₹12,000 and operational costs are ₹25,000.

Think through the problem step by step and calculate:
1. Total revenue
2. Total cost
3. Profit
4. One suggestion to improve profitability
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)