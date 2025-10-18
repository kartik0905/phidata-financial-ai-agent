# FinSight AI AgenticAI Project

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Phidata](https://img.shields.io/badge/phidata-2.7.10-orange)](https://pypi.org/project/phidata/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-yellow)](https://openai.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-lightblue)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## Overview

**AgenticAI Phi Data** is a multi-agent AI framework leveraging the [Phidata](https://github.com/Phidata/phidata) library.  
It supports both **console-based** and **web playground** interaction for agents such as:

- Financial AI Agent (via `YFinanceTools`)
- Web Search Agent (via `DuckDuckGo`)

Features include:

- Streamed AI responses
- Markdown tables for structured data
- Multiple agent coordination
- Live web search and financial data insights

---

## Demo

- **Console:** Run `financial_agent.py` for direct agent responses in the terminal.
- **Playground (Web UI):** Run `playground.py` to interact with agents via a FastAPI-powered UI.

<img width="1440" height="900" alt="Image" src="https://github.com/user-attachments/assets/839d7434-659d-4a3a-82a7-828986faecd1" />

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd AgenticAI-Phi-data
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Console Agent

```bash
python financial_agent.py
```

### Web Playground

```bash
uvicorn playground:app --reload
```

Then open your browser at `https://phidata.app/playground?endpoint=localhost%xxxxxx`.

---

## Features

- **Financial Agent:** Fetches real-time stock data and insights using `YFinanceTools`.
- **Web Search Agent:** Provides live search capabilities using `DuckDuckGo`.
- **Multi-Agent Coordination:** Agents can work together and share context.
- **Markdown Responses:** Structured tables and formatted outputs.
- **Streaming Responses:** View AI outputs in real-time.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

- GitHub: [kartik0905](https://github.com/kartik0905)
- Email: kartikamitgarg2005@gmail.com
