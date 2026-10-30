# 🧠 LocalMind-AI

**A Python-based AI agent powered by Ollama, featuring LLM-driven tool calling and chained tool execution.**

LocalMind-AI is a command-line AI assistant that uses a locally running Large Language Model (LLM) through Ollama. Instead of only generating text, the model can request Python functions to perform tasks, receive their results, and continue processing until it produces a final response.

## ✨ Features

- 🧠 **LLM-powered decision-making** — The model decides which available tools are appropriate for a request.
- 🛠️ **Function calling** — Executes Python functions requested by the LLM.
- 🔗 **Chained tool calling** — Supports multiple rounds of tool execution.
- 🕒 **Current time** — Retrieves the current date and time.
- 🌦️ **Weather information** — Retrieves weather information for a specified city.
- 📰 **News search** — Searches for news related to a given topic.
- 📍 **Approximate location detection** — Attempts to identify the user's city using IP geolocation.
- 💻 **Local LLM integration** — Uses Ollama to run the language model locally.

## 🧰 Tech Stack

- **Python** — Application logic and tool execution
- **Ollama** — Local LLM runtime
- **Qwen3.5:4b** — Language model
- **OpenAI Python SDK** — Communication through Ollama's OpenAI-compatible API
- **DDGS** — News search
- **Requests** — HTTP requests
- **Geocoder** — Approximate IP-based location detection

## 📂 Project Structure

```text
LocalMind-AI/
├── ai_agent.py       # Main assistant and agent loop
├── tools.py          # Tool definitions and implementations
├── requirements.txt  # Python dependencies
├── .env.example      # Example environment configuration
├── .gitignore        # Files excluded from Git
└── README.md         # Project documentation
```

## ⚙️ Prerequisites

Before running the project, install:

1. Python
2. [Ollama](https://ollama.com/)
3. Git (optional, for cloning the repository)

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/LocalMind-AI.git
cd LocalMind-AI
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Download the model

Make sure Ollama is running, then execute:

```bash
ollama pull qwen3.5:4b
```

Verify the installed model:

```bash
ollama list
```

### 3. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project directory.

For an Ollama setup using the OpenAI-compatible API, the configuration may look like this:

```env
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=qwen3.5:4b
```

Ensure these variable names match those used by your Python code.

**Note:** The API key value above is a local placeholder for Ollama's compatible API, not a real secret. Never upload actual API keys or credentials.

### 6. Run the assistant

```bash
python ai_agent.py
```

## 🔄 How It Works

LocalMind-AI uses a tool-calling loop:

```text
            User Input
                |
                v
          Python AI Agent
                |
                v
          Ollama LLM
                |
                v
      Model Requests Tool Calls
                |
                v
       Python Executes Tools
                |
                v
       Results Return to LLM
                |
                v
       More Tools Needed?
          /           \
        Yes             No
         |               |
         v               v
    Execute Again    Final Answer
```

The model determines which tools to request. Python executes the functions and returns their results to the model. This process can repeat for multiple rounds before the final answer is generated.

## 🛠️ Available Tools

| Tool | Purpose |
|---|---|
| `get_current_time` | Retrieves the current date and time |
| `get_city_weather` | Retrieves weather information for a city |
| `get_news` | Searches for news about a topic |
| `get_user_city` | Attempts to determine the user's approximate city |

Tool availability depends on the implementations and schemas registered in `tools.py`.

## 🔮 Planned Improvements

- [ ] Persistent conversation memory using SQLite
- [ ] Retrieval of relevant information from older conversations
- [ ] Multi-step task planning
- [ ] More tools for calculations and file operations
- [ ] Improved error handling and execution limits
- [ ] Document question answering using RAG
- [ ] Web-based user interface
- [ ] Automated tests for tool selection and execution

## ⚠️ Limitations

- The Ollama service must be running locally.
- The selected model must support the tool-calling workflow used by the application.
- Weather and news results depend on external services.
- IP-based location detection may be inaccurate.
- Internet access may be required for weather, news, and geolocation features.
- Planned features are not necessarily implemented yet.

## 🤝 Contributing

Suggestions, bug reports, and improvements are welcome. Feel free to fork the repository and experiment with new tools and agent capabilities.

## 📄 License

A license has not yet been selected. Add a license file if you want to specify the terms under which others may use, modify, and distribute this project.