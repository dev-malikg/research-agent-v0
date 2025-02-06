"""
Configuration file for the Research Agent project.
Users can modify these settings to customize the behavior of the research agent.
"""

# LLM Model Configuration
LLM_CONFIG = {
    "model": "llama3.2",  # Options: "llama3.2", "mistral", "mixtral", "gemma"
    "api_endpoint": "http://localhost:11434/api/generate",
    "context_length": 7144,
    "temperature": 0.75,
    "top_p": 0.85,
    "top_k": 50,
    "repeat_penalty": 1.1,
}

# Search Configuration
SEARCH_CONFIG = {
    "main_topic_results": 3,     # Number of results to fetch for main topic
    "keyword_results": 1,        # Number of results to fetch per keyword
    "max_keywords": 3,           # Maximum number of keywords to generate
    "search_timeout": 30,        # Timeout in seconds for search requests
}

# Source Quality Thresholds
QUALITY_THRESHOLDS = {
    "relevance_score_min": 0.6,  # Minimum relevance score for sources
    "credibility_score_min": 0.7,  # Minimum credibility score for sources
}

# Web Scraping Configuration
SCRAPER_CONFIG = {
    "timeout": 20,               # Timeout in seconds for scraping requests
    "max_retries": 3,           # Maximum number of retry attempts
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# Report Generation Settings
REPORT_CONFIG = {
    "min_word_count": 7000,     # Minimum word count for the final report
    "max_word_count": 20000,     # Maximum word count for the final report
    "include_citations": True,   # Whether to include citations in the report
    "citation_style": "APA",    # Citation style to use
}

# File Output Settings
OUTPUT_CONFIG = {
    "save_intermediates": True,  # Save intermediate results
    "output_format": "json",    # Output format for saved files
    "output_dir": "research_outputs",  # Directory for saving outputs
}

# Blacklisted Domains (for filtering out unwanted sources)
BLACKLISTED_DOMAINS = {
    'quora.com',
    'brainly.com',
    'coursehero.com',
    'scribd.com',
    'answers.com',
    'ask.com',
    'wiki.answers.com',
    'yahoo.com',
    'buzzfeed.com',
    'dailymail.co.uk',
    'thesun.co.uk',
    'wikihow.com',
    'pinterest.com',
    'tiktok.com',
    'facebook.com',
    'instagram.com',
}

# Debug Settings
DEBUG_CONFIG = {
    "verbose_output": True,     # Print detailed progress information
    "log_errors": True,         # Log errors to file
    "log_file": "research_agent.log",
}

def get_model_params(model_name=None):
    """
    Get model-specific parameters. If no model is specified,
    returns parameters for the default model.
    """
    model_params = {
        "llama3.2": {
            "context_length": 6144,
            "temperature": 0.75,
            "top_p": 0.85,
        },
        "mistral": {
            "context_length": 8192,
            "temperature": 0.7,
            "top_p": 0.9,
        },
        "mixtral": {
            "context_length": 12288,
            "temperature": 0.8,
            "top_p": 0.9,
        },
        "gemma": {
            "context_length": 8192,
            "temperature": 0.7,
            "top_p": 0.85,
        }
    }
    
    if model_name and model_name in model_params:
        return model_params[model_name] 