"""
Module 01 — Prompting Guidelines
Example: Zero-shot prompting
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Rewrite the below sentense.

Sentense: "I play cricket well."
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)
