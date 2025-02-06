# main.py
import json
from prewriting_agent import generate_report_structure
from brainstorming_agent import get_search_keywords
from topic_search import search_web
from scraper import scrape
from textsum_agent import summarize_article
from report_writer_agent import write_report
from datetime import datetime

def research_agent(main_topic):
    """
    Orchestrates an advanced research process using multiple specialized agents
    """
    print(f"\n🔍 Starting comprehensive research on: {main_topic}\n")

    # Step 1: Generate detailed report structure
    print("📑 Generating academic report structure...")
    report_structure = generate_report_structure(main_topic)

    # Step 2: Generate comprehensive search keywords
    print("🔑 Generating targeted search keywords...")
    keywords = get_search_keywords(report_structure)
    
    # Ensure keywords is a list
    if isinstance(keywords, str):
        keywords = [keywords]

    # Step 3: Search for scholarly articles
    print("🌐 Searching for peer-reviewed and academic sources...")
    search_results = []
    
    # First search for main topic with more results
    print(f"\nSearching main topic: {main_topic}...")
    main_topic_results = search_web(main_topic, 3)  # Get 3 results for main topic
    try:
        main_results_dict = json.loads(main_topic_results) if isinstance(main_topic_results, str) else main_topic_results
        search_results.extend(main_results_dict["results"])
    except Exception as e:
        print(f"Error processing main topic results: {e}")

    # Then search for each keyword with fewer results
    print("\nSearching related keywords...")
    for keyword in keywords:
        print(f"Searching: {keyword}")
        results = search_web(keyword, 1)  # Get 1 result per keyword
        try:
            results_dict = json.loads(results) if isinstance(results, str) else results
            search_results.extend(results_dict["results"])
        except Exception as e:
            print(f"Error processing results for {keyword}: {e}")
    
    # Remove duplicate sources
    unique_results = {result["url"]: result for result in search_results}.values()
    search_results = list(unique_results)
    
    print(f"\nFound {len(search_results)} unique academic sources:")
    for result in search_results:
        print(f"- {result['title']}")

    # Step 4: Deep analysis of articles
    print("📚 Performing comprehensive content analysis...")
    article_summaries = []
    for result in search_results:
        try:
            # Scrape article content
            content = scrape(result["url"])
            
            # Enhanced summary with source evaluation
            summary = summarize_article(content, result["title"], main_topic)
            
            article_summaries.append({
                "title": result["title"],
                "url": result["url"],
                "summary": summary,
                "relevance_score": evaluate_source_relevance(content, main_topic),
                "credibility_score": evaluate_source_credibility(result["url"])
            })
            print(f"✓ Analyzed: {result['title']}")
        except Exception as e:
            print(f"Error processing article {result['url']}: {e}")

    # Filter out low-quality sources
    article_summaries = [
        article for article in article_summaries 
        if article["relevance_score"] > 0.6 and article["credibility_score"] > 0.7
    ]

    # Step 5: Generate academic report
    print("\n✍️ Composing scholarly report...")
    final_report = write_report(main_topic, report_structure, article_summaries)
    
    research_output = {
        "topic": main_topic,
        "report_structure": report_structure,
        "search_keywords": keywords,
        "sources": search_results,
        "article_summaries": article_summaries,
        "final_report": final_report,
        "metadata": {
            "total_sources_analyzed": len(search_results),
            "quality_sources_used": len(article_summaries),
            "research_timestamp": datetime.now().isoformat()
        }
    }
    
    return research_output

def evaluate_source_relevance(content, topic):
    """Evaluate how relevant the source is to the research topic"""
    # Add implementation here
    return 0.8  # Placeholder

def evaluate_source_credibility(url):
    """Evaluate the credibility of the source based on domain and content"""
    # Add implementation here
    return 0.9  # Placeholder

if __name__ == "__main__":
    topic = input("Enter your research topic: ")
    results = research_agent(topic)
    
    # Save results to a file
    output_file = f"research_report_{topic.replace(' ', '_')}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n✨ Research complete! Results saved to {output_file}")
    print("\nFinal Report:\n")
    print(results["final_report"])