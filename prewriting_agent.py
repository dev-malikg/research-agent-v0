# prewriting_agent.py
import requests
import json
from config import LLM_CONFIG

def generate_report_structure(user_prompt):
    """Generate report structure using LLM"""
    instruction = (
        f"You are tasked with preparing a meaningful and insightful skeleton for a report on the topic: \"{user_prompt}\".\n"
        "Focus on understanding the deeper context and intent behind the topic, ensuring the structure aligns with what the user might want to explore.\n"
        "The structure should include only section headings and a few bullet points under each heading to outline topics to discuss.\n"
        "Avoid writing detailed content—just provide the basic format and key ideas for each section.\n"
    )
    
    payload = {
        "model": LLM_CONFIG["model"],
        "prompt": instruction,
        "stream": False,
        "context_length": LLM_CONFIG["context_length"],
        "num_predict": LLM_CONFIG["context_length"],
        "temperature": LLM_CONFIG["temperature"],
        "top_p": LLM_CONFIG["top_p"],
        "top_k": LLM_CONFIG["top_k"],
        "repeat_penalty": LLM_CONFIG["repeat_penalty"]
    }
    
    try:
        response = requests.post(LLM_CONFIG["api_endpoint"], json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "Error: No response text received.")
    except Exception as e:
        return f"Error: {str(e)}"

