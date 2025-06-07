from typing import List
import openai
from crewai.tools.base_tool import BaseTool
from .config import configure_openai


class AzureTestReviewTool(BaseTool):
    """Use Azure OpenAI to review python test code."""

    name: str = "azure_test_review"
    description: str = (
        "Analyze the quality of python test code using Azure OpenAI and provide a concise report"
    )

    def _run(self, code: str) -> str:
        deployment = configure_openai()
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert QA engineer. Analyze the provided python test "
                    "code and check if it follows best market practices. Suggest improvements "
                    "when necessary. Return your feedback in a short paragraph followed by a "
                    "rating from 1 to 10."
                ),
            },
            {"role": "user", "content": code},
        ]
        response = openai.ChatCompletion.create(
            engine=deployment,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"].strip()
