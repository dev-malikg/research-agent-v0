# brainstorming_agent.py
import requests
import json
from config import LLM_CONFIG, SEARCH_CONFIG

def get_search_keywords(pre_written_report):
    """Generate search keywords using LLM"""
    prompt = f"""Based on the following structured pre-written report, generate exactly {SEARCH_CONFIG['max_keywords']} unique and contextual keywords or lines (covers the topic from every direction) suitable for web searches:
    {pre_written_report}
    The response should be strictly in JSON format as shown below:
    {{
        "search_keywords": [
            "keyword or line 1",
            "keyword or line 2",
            "keyword or line 3"
        ]
    }}
    Ensure the response is valid JSON."""

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
        response = requests.post(LLM_CONFIG["api_endpoint"], json=payload)
        response.raise_for_status()
        response_text = response.json().get('response', '')
        
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        if start != -1 and end != 0:
            json_str = response_text[start:end]
            parsed_json = json.loads(json_str)
            
            if "search_keywords" in parsed_json:
                return parsed_json["search_keywords"][:SEARCH_CONFIG['max_keywords']]
    except Exception as e:
        print(f"Error fetching keywords: {e}")

    return ["Error: Unable to generate search keywords."]

# if __name__ == "__main__":
#     # user_prompt = input("Enter your research topic: ")
#     keywords = get_search_keywords()
#     print(json.dumps({"search_keywords": keywords}, indent=2))
