<div align="center">

# 🔬 M.A.R.S.

### Multi-Agent Research Synthesizer

*AI-powered research automation through collaborative multi-agent orchestration*

---

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-Enabled-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![Mistral AI](https://img.shields.io/badge/Mistral_AI-small--2603-FF7000?style=for-the-badge)](https://mistral.ai)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

</div>

---

## What is M.A.R.S.?

**M.A.R.S.** automates the entire research workflow — from raw query to polished report — by coordinating four specialized AI agents in a structured pipeline. Give it a topic; it searches the web, reads the sources, writes a comprehensive report, and then self-critiques the output. All in one click.

---

## Pipeline Architecture

```
╔══════════════════════════════════════════════════════════════╗
║                     M.A.R.S. Pipeline                        ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   User Input (Text / 🎙️ Voice)                               ║
║          │                                                   ║
║          ▼                                                   ║
║   ┌─────────────────┐                                        ║
║   │  🔍 Search Agent │  ← Tavily API (top 5 results)         ║
║   └────────┬────────┘                                        ║
║            │                                                 ║
║            ▼                                                 ║
║   ┌─────────────────┐                                        ║
║   │  📖 Reader Agent │  ← BeautifulSoup URL scraping         ║
║   └────────┬────────┘                                        ║
║            │                                                 ║
║            ▼                                                 ║
║   ┌─────────────────┐                                        ║
║   │  ✍️  Writer Chain │  ← Mistral AI report generation      ║
║   └────────┬────────┘                                        ║
║            │                                                 ║
║            ▼                                                 ║
║   ┌─────────────────┐                                        ║
║   │  🧠 Critic Chain │  ← Quality scoring & feedback         ║
║   └────────┬────────┘                                        ║
║            │                                                 ║
║            ▼                                                 ║
║   📄 Downloadable Research Report (.md)                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## The Four Agents

| Agent | Role | Tool |
|-------|------|------|
| 🔍 **Search Agent** | Finds top 5 relevant web sources | Tavily Search API |
| 📖 **Reader Agent** | Scrapes and extracts content from URLs | BeautifulSoup4 |
| ✍️ **Writer Chain** | Generates structured, detailed research report | Mistral AI (LLM) |
| 🧠 **Critic Chain** | Reviews, scores (/10), and suggests improvements | Mistral AI (LLM) |

---

## Features

- **Multi-Agent Orchestration** — LangGraph coordinates agents with shared state
- **Voice Input** — Speak your research topic; Whisper transcribes on-device
- **Real-time Pipeline Monitor** — Watch each agent's status live: `WAITING → RUNNING → DONE`
- **Structured Reports** — Introduction, Key Findings (3+), Conclusion, Sources — every time
- **Self-Critique** — Built-in critic scores the report and surfaces improvements
- **Export** — Download the final report as a Markdown file
- **Docker-Ready** — One command to spin up the full stack

---

## Tech Stack

<table>
<tr>
<td><strong>Layer</strong></td>
<td><strong>Technology</strong></td>
</tr>
<tr>
<td>UI Framework</td>
<td>Streamlit 1.45.0 — custom dark theme with orange accents</td>
</tr>
<tr>
<td>Agent Orchestration</td>
<td>LangGraph 1.2.4 + LangChain</td>
</tr>
<tr>
<td>LLM</td>
<td>Mistral AI — <code>mistral-small-2603</code></td>
</tr>
<tr>
<td>Web Search</td>
<td>Tavily API</td>
</tr>
<tr>
<td>Web Scraping</td>
<td>BeautifulSoup4 + Requests</td>
</tr>
<tr>
<td>Speech-to-Text</td>
<td>faster-whisper (base model, CPU, int8)</td>
</tr>
<tr>
<td>Observability</td>
<td>LangSmith 0.8.8</td>
</tr>
<tr>
<td>Runtime</td>
<td>Python 3.14 · Uvicorn · Starlette</td>
</tr>
<tr>
<td>Deployment</td>
<td>Docker + Docker Compose</td>
</tr>
</table>

---

## Getting Started

### Prerequisites

- Python 3.14+
- A [Tavily API key](https://tavily.com) (free tier available)
- A [Mistral AI API key](https://console.mistral.ai)

### 1. Clone & Configure

```bash
git clone <your-repo-url>
cd M.A.R.S

# Copy the environment template
cp .env.example .env
```

Edit `.env` and fill in your keys:

```env
TAVILY_API_KEY=your_tavily_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
```

### 2. Run Locally

```bash
# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

### 3. Run with Docker

```bash
# Build and start
docker-compose up --build

# Open http://localhost:8501
```

> Docker includes all system dependencies (ffmpeg, build tools) required for audio processing. Recommended for production or sharing with teammates.

---

## Usage

### Text Input

1. Type your research topic in the left panel
2. Click **"Run Research"**
3. Watch the pipeline execute step-by-step in the right panel
4. Read the report and critic feedback
5. Download the `.md` file

### Voice Input

1. Click the microphone button
2. Speak your research topic
3. Whisper transcribes on-device (no data sent to external ASR service)
4. Confirm the transcription and run

### Standalone CLI Mode

```bash
python pipeline.py
# Prompts for topic, prints report + critique to terminal
```

---

## Project Structure

```
M.A.R.S/
├── app.py              # Streamlit web interface (UI + pipeline integration)
├── agents.py           # Agent & chain definitions (Search, Reader, Writer, Critic)
├── pipeline.py         # Headless pipeline runner (CLI usage)
├── tools.py            # Tool definitions: search_web(), scrape_url()
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container definition
├── docker-compose.yml  # Multi-service orchestration
└── .env.example        # Environment variable template
```

---

## Configuration Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `TAVILY_API_KEY` | ✅ | Powers the Search Agent's web lookup |
| `MISTRAL_API_KEY` | ✅ | Powers Writer and Critic chains |
| `LANGSMITH_API_KEY` | Optional | Enables LangSmith tracing & observability |

---

## How Each Agent Works

<details>
<summary><strong>🔍 Search Agent</strong></summary>

Uses the Tavily Search API to retrieve up to 5 web results for the given topic. Returns titles, URLs, and content snippets. The agent is equipped with the `search_web` tool via LangChain's `@tool` decorator.

</details>

<details>
<summary><strong>📖 Reader Agent</strong></summary>

Takes URLs from the Search Agent and scrapes their content using `requests` + `BeautifulSoup4`. Strips scripts, styles, navbars, and footers. Returns up to 3,000 characters per page to keep context focused.

</details>

<details>
<summary><strong>✍️ Writer Chain</strong></summary>

A LangChain prompt chain (not a tool-calling agent) that structures scraped content into a professional research report. Sections always include: Introduction, Key Findings (3 minimum), Conclusion, and a Sources list.

</details>

<details>
<summary><strong>🧠 Critic Chain</strong></summary>

Another prompt chain that receives the Writer's output and evaluates it. Produces a score out of 10, highlights strengths, and gives actionable improvement suggestions. Displayed in a styled feedback panel in the UI.

</details>

---

## Docker Details

```yaml
# Exposes port 8501 (Streamlit default)
# Health check: polls /_stcore/health every 30s
# Restart policy: unless-stopped
# Includes: ffmpeg (audio), build-essential, curl
```

Build the image alone:
```bash
docker build -t mars-app .
docker run -p 8501:8501 --env-file .env mars-app
```

---

## Roadmap

- [ ] Support additional LLM providers (OpenAI, Anthropic)
- [ ] Configurable agent count and search depth
- [ ] PDF export for research reports
- [ ] Report history and session persistence
- [ ] Multi-topic batch research mode

---

## License

This project is private. Contact the maintainer for usage rights.

---

<div align="center">

Built with LangGraph · Mistral AI · Streamlit

*M.A.R.S. — because good research shouldn't take all day.*

</div>
