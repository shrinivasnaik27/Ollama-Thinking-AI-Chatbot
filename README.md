# Ollama AI Chatbot 🤖

A simple Python-based AI chatbot powered by **Ollama** and the **Qwen 3.5 (0.8B)** language model. It allows users to interact with a locally running AI model and customize its response generation settings.

## Features

- **Local AI Chatbot:** Runs using Ollama on your computer.
- **Thinking Mode:** Enable or disable thinking using `True` or `False`, depending on model support.
- **Temperature Control:** Adjust temperature from `0` to `2` to control response randomness.
- **Interactive Chat:** Ask multiple questions without restarting the program.
- **Error Handling:** Displays helpful messages when errors occur.
- **Custom Instructions:** Configures the AI to provide clear and simple responses.

## Technologies Used

- Python
- Ollama
- Qwen 3.5 (0.8B)
- Ollama Python library

## Prerequisites

Make sure you have installed:

- Python
- Ollama
- The Qwen 3.5 (0.8B) model

## Installation and Setup

### 1. Install Ollama

Download Ollama from the official website:

https://ollama.com/download

### 2. Download the AI model

Open PowerShell or your terminal and run:

```bash
ollama pull qwen3.5:0.8b
```

### 3. Clone this repository

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate into the project folder:

```bash
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholder values with your actual GitHub repository URL and folder name.

### 4. Create a virtual environment (optional)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install the Python dependency

```bash
python -m pip install ollama
```

### 6. Run the chatbot

Save the Python program as `prompt.py` and execute:

```bash
python prompt.py
```

## How to Use

1. Enter a question when prompted.
2. Choose `true` or `false` to enable or disable thinking mode.
3. Enter a temperature between `0` and `2`.
4. Read the AI response in the terminal.
5. Ask another question or type `exit` to quit.

## Temperature Settings

| Temperature | General behavior |
|---|---|
| `0` | More predictable responses |
| `0.8` | Moderate variation |
| `1` | More varied responses |
| `2` | High randomness; responses may be less consistent |

Actual behavior depends on the model and its configuration.

## Project Structure

```text
ollama-ai-chatbot/
├── prompt.py
└── README.md
```

## Troubleshooting

**Ollama connection error:** Make sure Ollama is running on your computer.

**Model not found:** Run `ollama pull qwen3.5:0.8b`.

**Python module error:** Run `python -m pip install ollama` in the same Python environment used to run the program.

**Empty response with thinking enabled:** Check model support, the generated thinking output, and the token generation limit.

## Future Improvements

- Add a graphical user interface.
- Store conversation history.
- Support multiple Ollama models.
- Add response streaming.
- Save conversations to a file.

## License

This project is available for educational and personal learning purposes. Add a license file if you intend to distribute it under a specific open-source license.
