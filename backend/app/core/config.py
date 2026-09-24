import os

from dotenv import load_dotenv


load_dotenv()


DEFAULT_OPENAI_MODEL = "gpt-6-luna"


def get_openai_model() -> str:
    """
    Return the configured OpenAI model.

    The environment variable allows deployment environments to
    change models without modifying source code.
    """

    return os.getenv(
        "OPENAI_MODEL",
        DEFAULT_OPENAI_MODEL,
    )