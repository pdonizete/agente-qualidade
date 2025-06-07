import os
import openai


def configure_openai() -> str:
    """Configure OpenAI SDK to use Azure endpoints.

    Returns the deployment name (engine) to be used when creating
    chat completions.
    Environment variables expected:
        AZURE_OPENAI_KEY - API key.
        AZURE_OPENAI_ENDPOINT - Base URL of the Azure OpenAI resource.
        AZURE_OPENAI_DEPLOYMENT - Deployment/engine name.
        AZURE_OPENAI_API_VERSION - API version (optional).
    """
    openai.api_type = "azure"
    openai.api_key = os.getenv("AZURE_OPENAI_KEY")
    openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
    openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    if not all([openai.api_key, openai.api_base, deployment]):
        raise EnvironmentError(
            "Missing Azure OpenAI configuration. Please set AZURE_OPENAI_KEY, "
            "AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_DEPLOYMENT environment variables."
        )
    return deployment
