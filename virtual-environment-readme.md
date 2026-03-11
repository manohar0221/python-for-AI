# Install Python (if not installed)

Download and install Python from the official site.

Check installation:

python --version

python3 --version


# Open the Terminal in VS Code

Shortcut:  Ctrl +

or

Terminal → New Terminal

# Create a Virtual Environment

Run this inside your project folder:

python -m venv venv

This creates a folder named venv.

# Activate the Virtual Environment

venv\Scripts\activate

source venv/bin/activate


After activation you will see:

(venv) C:\project-folder>

# Select Interpreter in VS Code

1. Press Ctrl + Shift + P

2. Search:

Python: Select Interpreter

3. Choose:

.\venv\Scripts\python.exe


This connects VS Code to your virtual environment.

# To Deactivate the Environment

deactivate

# Create a .gitignore file and add:
venv/

so the environment isn’t pushed to Git.
