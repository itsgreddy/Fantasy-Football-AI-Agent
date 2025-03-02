from llama_index.core.tools import QueryEngineTool, ToolMetadata

def create_fantasy_tool(query_engine):
    """Create the fantasy football analysis tool"""
    return QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="fantasy_football_analyzer",
            description="""Analyzes fantasy football data including combine metrics, 
            injury history, and performance statistics. Use this tool to evaluate 
            players and make team decisions."""
        )
    ) 