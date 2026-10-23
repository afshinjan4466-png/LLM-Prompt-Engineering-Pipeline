"""
LLM Prompt Engineering Pipeline
Main entry point for structured prompt execution and JSON validation.
"""

import json
from pydantic import BaseModel, Field


class PromptOutputSchema(BaseModel):
    summary: str = Field(description="Brief summary of the input text")
    sentiment: str = Field(description="Sentiment analysis: positive, negative, or neutral")
    key_takeaways: list[str] = Field(description="List of key insights extracted")


def run_prompt_pipeline(input_text: str) -> dict:
    """
    Simulates a structured LLM pipeline execution with schema enforcement.
    """
    # Simulated validated output from an LLM
    mock_response = {
        "summary": "The input discusses setting up structured LLM prompt pipelines for high-reliability applications.",
        "sentiment": "positive",
        "key_takeaways": [
            "Structured outputs improve system predictability.",
            "JSON schema enforcement reduces hallucinations.",
            "Prompt chaining enables complex task handling."
        ]
    }
    
    # Validate structure using Pydantic
    validated_data = PromptOutputSchema(**mock_response)
    return validated_data.model_dump()


if __name__ == "__main__":
    print("Executing LLM Prompt Engineering Pipeline...")
    sample_text = "Prompt engineering requires clean structures, retries, and strict output formats."
    result = run_prompt_pipeline(sample_text)
    print(json.dumps(result, indent=4))
