"""Completed mock exercise: switching between Groq models with LangChain patterns."""

import os


class ChatGroq:
    """Mock ChatGroq class used by this exercise."""

    def __init__(self, model, temperature=0, max_retries=2):
        self.model = model
        self.temperature = temperature
        self.max_retries = max_retries
        self.valid_models = [
            "llama-4-8b-instant",
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
        ]
        if model not in self.valid_models:
            raise ValueError(f"Invalid model: {model}")

    def invoke(self, messages):
        if not isinstance(messages, list) or not messages:
            raise ValueError("Messages must be a non-empty list")
        if self.model == "llama-4-8b-instant":
            content = (
                "[Llama 4 Response] Machine learning is a subset of AI that "
                "enables computers to learn patterns from data without explicit programming."
            )
        elif self.model == "llama-3.3-70b-versatile":
            content = (
                "[Llama 3.3 Creative Response] Machine learning is like teaching "
                "a computer to recognize patterns in data, much like humans learn from experience!"
                if self.temperature > 0.2
                else "[Llama 3.3 Response] Machine learning allows computers to learn "
                "and improve from data without being explicitly programmed."
            )
        else:
            content = f"[Mock Response] This is a simulated response from {self.model}"
        return MockAIMessage(content)


class MockAIMessage:
    def __init__(self, content):
        self.content = content


def implement_set_api_key(api_key):
    """Store a key in the process environment (mock exercise only)."""
    os.environ["GROQ_API_KEY"] = api_key


def check_api_key():
    if "GROQ_API_KEY" not in os.environ:
        raise Exception("GROQ_API_KEY environment variable is required")


def implement_llama_4_model():
    return ChatGroq(model="llama-4-8b-instant", temperature=0, max_retries=2)


def implement_llama_3_3_model():
    return ChatGroq(
        model="llama-3.3-70b-versatile", temperature=0.3, max_retries=2
    )


def implement_query_model(model, prompt):
    messages = [("human", prompt)]
    return model.invoke(messages).content


def implement_compare_models(prompt):
    return {
        "llama-4-8b-instant": implement_query_model(implement_llama_4_model(), prompt),
        "llama-3.3-70b-versatile": implement_query_model(
            implement_llama_3_3_model(), prompt
        ),
    }


def main():
    print("Groq Model Switching Exercise (mock integration)")
    implement_set_api_key("mock_api_key_for_testing")
    check_api_key()
    prompt = "Explain the concept of machine learning in one sentence."
    print("Llama 4:", implement_query_model(implement_llama_4_model(), prompt))
    print("Llama 3.3:", implement_query_model(implement_llama_3_3_model(), prompt))
    print("Comparison:")
    for model, response in implement_compare_models(prompt).items():
        print(f"  {model}: {response}")


if __name__ == "__main__":
    main()
