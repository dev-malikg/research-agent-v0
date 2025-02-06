# textsum_agent.py
import requests
import json
from config import LLM_CONFIG

def summarize_article(scraped_text, article_title, main_topic):
    """Summarize article content using LLM"""
    api_endpoint = LLM_CONFIG["api_endpoint"]
    
    prompt = f"""Extract key information from this text about {main_topic}:

    Title: {article_title}
    Text: {scraped_text[:3000]}

    Guidelines:
        - Focus on factual content and data
        - Remove redundant/promotional language
        - Keep cause-effect relationships
        - Include dates and statistics 
        - add depth to every topic summarised - quality information 
        - Maintain context of statements
        - Maintain length of about 300-600 words

    Format as clear paragraphs with logical flow."""

    payload = {
        "model": LLM_CONFIG["model"],
        "prompt": prompt,
        "stream": False,
        "context_length": LLM_CONFIG["context_length"],
        "num_predict": LLM_CONFIG["context_length"],
        "temperature": LLM_CONFIG["temperature"],
        "top_p": LLM_CONFIG["top_p"],
        "top_k": LLM_CONFIG["top_k"],
        "repeat_penalty": LLM_CONFIG["repeat_penalty"]
    }

    try:
        response = requests.post(api_endpoint, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "Error: No response text received.")
    except Exception as e:
        return f"Error: {str(e)}"
