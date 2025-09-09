from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access to GitHub token variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN is not set in the environment variables.")

print(GITHUB_TOKEN)