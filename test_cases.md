# Chatbot Test Cases

## Purpose

These tests evaluate the traditional rule-based HealthAssist chatbot for intent recognition, response generation, and handling of unknown or malformed input.

## Functional Tests

| Test | User Input | Expected Intent | Result |
|---|---|---|---|
| 1 | Hello | greeting | PASS |
| 2 | What can you do? | capabilities | PASS |
| 3 | How can I stay healthy? | healthy_habits | PASS |
| 4 | What are flu symptoms? | flu_information | PASS |
| 5 | I need a doctor appointment | appointment | PASS |
| 6 | Bye | goodbye | PASS |
| 7 | xyz123 @@@ | unknown | PASS |

**Overall result: 7/7 tests passed.**

## Robustness Tests

The chatbot was additionally tested with:

- Uppercase input: `HELLO!!!`
- Extra spaces: `  What can you do?  `
- Uppercase and punctuation: `HEALTHY HABITS!!!`
- Punctuation variation: `What are flu symptoms???`
- Uppercase appointment request
- Special characters: `@@@###`
- Empty input
- Random unsupported input: `random question 12345`

The chatbot successfully normalized supported variations and returned the fallback response for unsupported or malformed input.
