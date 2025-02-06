# report_writer_agent.py
import requests
import json
from config import LLM_CONFIG, REPORT_CONFIG

def write_report(main_topic, report_structure, article_summaries):
    """
    Generates a comprehensive research report with enhanced depth and analysis
    """
    api_endpoint = LLM_CONFIG["api_endpoint"]
    
    prompt = f"""You are an expert research analyst writing a comprehensive, really long ({REPORT_CONFIG['min_word_count']}-{REPORT_CONFIG['max_word_count']} words minimum), in-depth report about "{main_topic}". 
    Your goal is to produce profound insights and thorough analysis that demonstrates deep understanding of the subject matter.

    Here are your source materials:

    REPORT OUTLINE:
    {report_structure}

    RESEARCH FINDINGS:
    {json.dumps(article_summaries, indent=2)}

    IMPORTANT INSTRUCTIONS:
    1. Use the actual content from the research summaries but allowed to add deep insightfull information
    2. Integrate specific facts, statistics, and findings from the summaries
    3. Use proper citations by referencing the article titles
    4. Follow the report structure but focus on presenting real findings

    DEPTH INDICATORS:
    - Explain mechanisms and processes in detail
    - Provide multiple levels of analysis
    - Include both theoretical frameworks and practical applications
    - Discuss implications for different stakeholders
    - Address complexities and nuances
    - Consider historical context and future trajectories

    FORMAT:
    Structure your report with clear sections, but prioritize depth over rigid formatting.
    Use headings that reflect the natural flow of your analysis.
    Include a comprehensive reference section.

    Remember: Your goal is to produce a report that demonstrates mastery of the subject matter and provides valuable insights beyond the surface level."""

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
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {str(e)}" 