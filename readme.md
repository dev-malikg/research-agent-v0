# Research Agent 🔬

A sophisticated research automation system that leverages multiple specialized AI agents to conduct comprehensive academic research on any given topic. This system streamlines the research process from initial topic exploration to final report generation.

## 🌟 Key Features

- **Intelligent Report Structure Generation**: Creates detailed, topic-specific report outlines
- **Smart Keyword Research**: Develops targeted search strategies using AI
- **Academic Source Analysis**: Evaluates and filters scholarly sources
- **Quality Control**: Implements rigorous source evaluation (relevance score > 0.6, credibility score > 0.7)
- **Automated Report Writing**: Generates in-depth reports (7,000-20,000 words)
- **Flexible Configuration**: Extensive customization options

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Local LLM server running on localhost:11434
- Internet connection for web searches
- Sufficient storage for research outputs

### Installation

```bash
# Clone the repository
git clone https://github.com/dev-malikg/research-agent-v0.git

# Navigate to project directory
cd research-agent

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from main import research_agent

# Simple usage
topic = "Artificial Intelligence in Healthcare"
results = research_agent(topic)

# Results are automatically saved to: research_report_Artificial_Intelligence_in_Healthcare.json
```

## 🛠️ Configuration

### LLM Model Options (`config.py`)
```python
LLM_CONFIG = {
    "model": "llama3.2",  # Options: llama3.2, mistral, mixtral, gemma
    "temperature": 0.75,
    "context_length": 7144,
    # ... other parameters
}
```

### Search Settings
```python
SEARCH_CONFIG = {
    "main_topic_results": 3,    # Results for main topic
    "keyword_results": 1,       # Results per keyword
    "max_keywords": 3,          # Maximum keywords
}
```

## 📁 Project Structure

```
research-agent/
├── main.py                 # Main orchestration logic
├── config.py              # Configuration settings
├── prewriting_agent.py    # Report structure generation
├── brainstorming_agent.py # Keyword generation
├── topic_search.py        # Web search functionality
├── scraper.py            # Content scraping
├── textsum_agent.py      # Article summarization
├── report_writer_agent.py # Report generation
└── research_outputs/     # Generated research outputs
```

## 📊 Output Format

The system generates a structured JSON output:

```json
{
    "topic": "Research Topic",
    "report_structure": {
        "sections": [],
        "subsections": []
    },
    "search_keywords": ["keyword1", "keyword2"],
    "sources": [
        {
            "title": "Source Title",
            "url": "source_url",
            "relevance_score": 0.85
        }
    ],
    "final_report": "Comprehensive research report...",
    "metadata": {
        "total_sources_analyzed": 10,
        "quality_sources_used": 7,
        "research_timestamp": "2024-03-14T12:00:00"
    }
}
```

## ⚠️ Limitations

- Requires active LLM server connection
- Search API dependencies
- Processing time scales with research scope
- Web scraping subject to site restrictions

## 🔒 Security Notes

- API keys should be stored in `.env` file
- Local configuration files are git-ignored
- Respect robots.txt when scraping
- Monitor rate limits for external APIs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with various LLM models
- Uses academic search APIs
- Implements ethical web scraping
- Community contributions welcome

## 📮 Support

For support, please:
1. Check existing GitHub issues
2. Review documentation
3. Create a new issue with detailed description

---
**Note**: This project is under active development. Features and APIs may change.
