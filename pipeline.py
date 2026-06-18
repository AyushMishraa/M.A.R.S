from  agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# pipeline function
def run_research_pipeline(topic: str) -> dict:
    state = {}
    
    # search agent working
    search_agent = build_search_agent()
    search_agent_response = search_agent.invoke({
        "messages": [("user", f"Find recent and relevant information on the topic: {topic}. Provide URLs and brief summaries.")]
    })
    
    state["search_agent_response"] = search_agent_response['messages'][-1].content
    
    # reader agent working
    reader_agent = build_reader_agent()
    reader_agent_response = reader_agent.invoke({
        "messages": [("user",
                      f"Based on the folloeing search result about '{topic}',"
                      f"pick the most relevant URL and scrap it for deeper content. \n\n"
                      f"Search Results:\n{state['search_agent_response'][:800]}"
                      )]
    })
    
    state["reader_agent_response"] = reader_agent_response['messages'][-1].content
    
    research_combined = (
        f"Search Findings:\n{state['search_agent_response']}\n\n"
        f"Scraped Content:\n{state['reader_agent_response']}" 
    )
    
    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })
    
    state["critique"] = critic_chain.invoke({
        "report": state["report"]
    })
    
    return state

if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    results = run_research_pipeline(topic)
    
    print("=== Research Report ===")
    print(results["report"])
    
    print("\n=== Critique ===")
    print(results["critique"])