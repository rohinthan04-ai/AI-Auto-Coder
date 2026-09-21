import os
import base64

from dotenv import load_dotenv
from google import genai


load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)


def solve_screen(image_path):

    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    prompt = """
Look at this screenshot.

Find the programming question shown on the screen.

Determine:
1. What the question is asking.
2. Which programming language is required.
3. What code should be entered into the coding editor.

Return ONLY the final source code.

Do not use Markdown code fences.
Do not explain anything.
Do not include any text before or after the code.
"""

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=[
            {
                "type": "text",
                "text": prompt,
            },
            {
                "type": "image",
                "data": image_data,
                "mime_type": "image/png",
            },
        ],
    )

    return interaction.output_text