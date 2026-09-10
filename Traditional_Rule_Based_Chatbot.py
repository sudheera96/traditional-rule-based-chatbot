# Databricks notebook source
# MAGIC %md
# MAGIC # Traditional Rule-Based Chatbot: HealthAssist
# MAGIC
# MAGIC ## Project Overview
# MAGIC
# MAGIC HealthAssist is a simple traditional rule-based chatbot developed in Python using Databricks Free Edition. The chatbot uses predefined intents, keyword matching, text normalization, and predefined responses rather than a large language model (LLM).
# MAGIC
# MAGIC ## Project Objective
# MAGIC
# MAGIC The objective of this project is to design, implement, and evaluate a simple chatbot using traditional approaches. The chatbot is designed to:
# MAGIC
# MAGIC - Respond to multiple types of user prompts.
# MAGIC - Provide a clear list of its capabilities.
# MAGIC - Handle unknown and malformed user input.
# MAGIC - Demonstrate a basic conversational interaction.
# MAGIC - Provide an architecture that can be extended in the future.
# MAGIC
# MAGIC ## Development Environment
# MAGIC
# MAGIC - Platform: Databricks Free Edition
# MAGIC - Programming Language: Python
# MAGIC - Approach: Traditional rule-based chatbot
# MAGIC - Natural Language Processing Approach: Keyword and pattern matching
# MAGIC - LLM: Not used
# MAGIC
# MAGIC ## Chatbot Development Lifecycle
# MAGIC
# MAGIC The project follows these general stages:
# MAGIC
# MAGIC 1. Requirements Analysis
# MAGIC 2. Conversation and Intent Design
# MAGIC 3. Response Design
# MAGIC 4. Implementation
# MAGIC 5. Testing
# MAGIC 6. Evaluation
# MAGIC 7. Future Extension

# COMMAND ----------

# Traditional Rule-Based Chatbot
# Step 3: Define chatbot responses and keywords

responses = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good afternoon"],
        "response": "Hello! I am HealthAssist, a traditional rule-based chatbot. How can I help you today?"
    },
    
    "capabilities": {
        "keywords": ["what can you do", "capabilities", "help", "what do you do"],
        "response": "I can provide general health information, healthy lifestyle tips, basic information about flu symptoms, and general appointment guidance."
    },
    
    "healthy_habits": {
        "keywords": ["healthy habits", "stay healthy", "healthy lifestyle", "health tips"],
        "response": "Some healthy habits include eating a balanced diet, staying physically active, getting adequate sleep, drinking enough water, and maintaining regular health checkups."
    },
    
    "flu_information": {
        "keywords": ["flu symptoms", "flu", "influenza"],
        "response": "Common flu symptoms can include fever, cough, sore throat, body aches, fatigue, and headache. If symptoms are severe or concerning, consult a qualified healthcare professional."
    },
    
    "appointment": {
        "keywords": ["appointment", "doctor", "schedule", "healthcare provider"],
        "response": "For medical appointments, contact your healthcare provider or use the provider's official scheduling system."
    },
    
    "goodbye": {
        "keywords": ["bye", "goodbye", "exit", "quit"],
        "response": "Goodbye! Thank you for using HealthAssist."
    }
}

print("Chatbot response rules loaded successfully.")
print(f"Number of intents: {len(responses)}")

# COMMAND ----------

import re

def identify_intent(user_input):
    """
    Identify the chatbot intent using traditional
    keyword and pattern matching.
    """
    
    # Normalize the input
    text = user_input.lower().strip()
    
    # Remove unnecessary punctuation
    text = re.sub(r"[^\w\s]", "", text)
    
    # Check each intent
    for intent, data in responses.items():
        for keyword in data["keywords"]:
            if keyword in text:
                return intent
    
    # No matching intent
    return "unknown"


def get_response(user_input):
    """
    Return a predefined response based on the identified intent.
    """
    
    intent = identify_intent(user_input)
    
    if intent in responses:
        return responses[intent]["response"]
    
    return (
        "I'm sorry, I don't understand that request. "
        "Please try asking about my capabilities, healthy habits, "
        "flu information, or appointments."
    )


print("Intent-matching system is ready.")

# COMMAND ----------

# Step 5: Test the chatbot with different types of input

test_inputs = [
    "Hello",
    "What can you do?",
    "How can I stay healthy?",
    "What are flu symptoms?",
    "I need a doctor appointment",
    "Bye",
    "xyz123 @@@"
]

for user_input in test_inputs:
    print(f"User: {user_input}")
    print(f"HealthAssist: {get_response(user_input)}")
    print("-" * 70)

# COMMAND ----------

# Step 6: Interactive chatbot

print("HealthAssist: Hello! I am HealthAssist.")
print("HealthAssist: Type 'bye' to end the conversation.")
print()

while True:
    user_input = input("You: ")
    
    response = get_response(user_input)
    print("HealthAssist:", response)
    
    if identify_intent(user_input) == "goodbye":
        break

# COMMAND ----------

# Step 7: Formal chatbot test cases

test_cases = [
    ("Hello", "greeting"),
    ("What can you do?", "capabilities"),
    ("How can I stay healthy?", "healthy_habits"),
    ("What are flu symptoms?", "flu_information"),
    ("I need a doctor appointment", "appointment"),
    ("Bye", "goodbye"),
    ("xyz123 @@@", "unknown")
]

print("CHATBOT TEST RESULTS")
print("=" * 70)

passed = 0

for user_input, expected_intent in test_cases:
    actual_intent = identify_intent(user_input)
    
    if actual_intent == expected_intent:
        status = "PASS"
        passed += 1
    else:
        status = "FAIL"
    
    print(f"Input: {user_input}")
    print(f"Expected: {expected_intent}")
    print(f"Actual:   {actual_intent}")
    print(f"Status:   {status}")
    print("-" * 70)

print(f"Tests passed: {passed}/{len(test_cases)}")

# COMMAND ----------

# Step 8: Robustness testing
# Test capitalization, punctuation, extra spaces, and malformed input

robustness_tests = [
    "HELLO!!!",
    "  What can you do?  ",
    "HEALTHY HABITS!!!",
    "What are flu symptoms???",
    "I NEED A DOCTOR APPOINTMENT",
    "@@@###",
    "",
    "random question 12345"
]

print("ROBUSTNESS TEST RESULTS")
print("=" * 70)

for user_input in robustness_tests:
    intent = identify_intent(user_input)
    response = get_response(user_input)

    print(f"Input: {repr(user_input)}")
    print(f"Detected intent: {intent}")
    print(f"Response: {response}")
    print("-" * 70)

# COMMAND ----------

# Step 9: Display chatbot capabilities

def show_capabilities():
    print("HealthAssist Capabilities")
    print("=" * 40)
    print("1. Respond to greetings")
    print("2. Explain what the chatbot can do")
    print("3. Provide general healthy-lifestyle tips")
    print("4. Provide general flu information")
    print("5. Provide basic appointment guidance")
    print("6. Handle unknown or malformed input")
    print("7. End the conversation when the user says goodbye")


show_capabilities()

# COMMAND ----------

# Step 10: Project information

project_info = """
TRADITIONAL RULE-BASED CHATBOT
HealthAssist

Project Description:
HealthAssist is a simple traditional chatbot developed in Python
using rule-based keyword matching. It does not use an LLM.

Development Environment:
Databricks Free Edition

Chatbot Approach:
- Predefined intents
- Keyword matching
- Text normalization
- Predefined responses
- Fallback handling for unknown input

Supported Functions:
1. Greetings
2. Capability information
3. Healthy-lifestyle information
4. General flu information
5. Appointment guidance
6. Unknown/malformed input handling
7. Conversation termination

Testing:
The chatbot was tested using normal questions, variations in
capitalization and punctuation, extra spaces, and malformed input.

Future Extension:
The traditional rule-based architecture could later be extended
with an AI service to provide more advanced natural-language
understanding and response generation.
"""

print(project_info)