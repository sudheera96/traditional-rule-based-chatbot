# Traditional Rule-Based Chatbot: HealthAssist

## Project Overview

HealthAssist is a simple traditional rule-based chatbot developed in Python using Databricks Free Edition. The project demonstrates how a chatbot can respond to user inputs using predefined intents, keyword matching, text normalization, and predefined responses without using a Large Language Model (LLM).

## Objective

The objective of this project is to develop and evaluate a simple chatbot using traditional approaches. The chatbot is designed to:

- Respond to multiple user prompts.
- Identify predefined user intents.
- Provide a list of chatbot capabilities.
- Handle unknown and malformed input.
- Support a basic conversational interaction.
- Provide an architecture that can be extended in the future.

## Development Environment

- **Platform:** Databricks Free Edition
- **Programming Language:** Python
- **Approach:** Traditional rule-based chatbot
- **Intent Recognition:** Keyword and pattern matching
- **LLM:** Not used

## Chatbot Capabilities

1. Respond to greetings.
2. Explain chatbot capabilities.
3. Provide general healthy-lifestyle information.
4. Provide general flu information.
5. Provide basic appointment guidance.
6. Handle unknown or malformed input.
7. End the conversation when the user says goodbye.

## Development Lifecycle

The project follows these stages:

1. Requirements Analysis
2. Conversation and Intent Design
3. Response Design
4. Implementation
5. Testing
6. Evaluation
7. Future Extension

## Testing

The chatbot was tested using:

- Normal user questions
- Different capitalization
- Punctuation variations
- Extra spaces
- Unknown input
- Malformed input
- Empty input

The formal test suite successfully passed **7 out of 7 test cases**.

## Project Files

- `Traditional_Rule_Based_Chatbot.ipynb` — Databricks/Python implementation and testing

## Future Enhancement

The chatbot could be extended in the future by incorporating more advanced natural-language processing or an AI-as-a-service solution. The current rule-based design provides a simple foundation for such an extension.

## Disclaimer

HealthAssist provides general informational responses and is not intended to provide medical diagnosis or professional medical advice.
