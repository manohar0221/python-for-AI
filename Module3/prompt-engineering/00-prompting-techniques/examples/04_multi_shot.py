import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Tag each message with one label only:
Billing, Technical Issue, Delivery, Account Access

Message: I was charged twice for the same subscription.
Label: Billing

Message: My order still has not arrived.
Label: Delivery

Message: I cannot reset my password.
Label: Account Access

Message: The application freezes after login.
Label: Technical Issue

Message: I am unable to download the invoice.
Label: Billing

Now tag this:
Message: The website keeps showing an error when I try to sign in.
Label:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)