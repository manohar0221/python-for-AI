import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Classify the intent of the following emails as Complaint, Request, or Inquiry.

Email: I received a damaged product and need a replacement.
Intent: Complaint

Email: Can you please update me on the status of my order?
Intent: Inquiry

Email: I would like to change my delivery address.
Intent: Request

Email: The service was very disappointing and slow.
Intent: Complaint

Email: Could you provide more details about your pricing plans?
Intent: Inquiry

Email: I need help resetting my password.
Intent:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)