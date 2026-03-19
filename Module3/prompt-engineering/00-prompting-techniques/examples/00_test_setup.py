import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Summarize the following in one simple sentence:

Prompt engineering helps us write clear instructions for AI models.
"""

response = get_completion(prompt)
print(response)