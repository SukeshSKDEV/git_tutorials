import os

from dotenv import load_dotenv

load_dotenv()

mode = os.getenv("GITHUB_MODE", "development")

print(f"GITHUB mode: {mode}")
