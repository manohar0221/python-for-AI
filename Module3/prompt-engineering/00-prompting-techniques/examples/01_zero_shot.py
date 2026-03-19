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
Summarize the following paragraph in 5 simple bullet points for a beginner:

Artificial Intelligence is transforming industries by automating repetitive work,
improving decision-making, and enabling personalized experiences.
Businesses use AI in customer support, fraud detection, marketing, healthcare, and logistics.
However, successful AI adoption requires good data, clear goals, and responsible implementation.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)