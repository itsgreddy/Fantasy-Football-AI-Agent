from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent
import os

from src.utils.config import OPENAI_API_KEY, SYSTEM_PROMPT, STORAGE_DIR
from src.agent.tools import create_fantasy_tool
from src.utils.chat_utils import ChatHistory
from src.utils.yahoo_fantasy import YahooFantasyManager

class FantasyFootballAgent:
    def __init__(self):
        # Verify API key exists
        if not OPENAI_API_KEY:
            raise ValueError("OpenAI API key not found. Please check your .env file.")
        
        try:
            self.llm = OpenAI(
                model="gpt-4o-mini", 
                temperature=0.7, 
                max_tokens=1500,
                api_key=OPENAI_API_KEY
            )
            self.agent = None
            self.query_engine = None
            self.chat_utils = ChatHistory()
            try:
                self.yahoo_manager = YahooFantasyManager()
            except Exception as e:
                print(f"Warning: Could not initialize Yahoo Fantasy Manager: {e}")
                self.yahoo_manager = None
        except Exception as e:
            raise ValueError(f"Error initializing OpenAI LLM: {str(e)}")

    def initialize_index(self, documents):
        """Initialize or load the vector index"""
        try:
            storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
            index = load_index_from_storage(storage_context)
        except:
            index = VectorStoreIndex.from_documents(
                documents,
                show_progress=True
            )
            index.storage_context.persist(persist_dir=STORAGE_DIR)

        self.query_engine = index.as_query_engine(
            similarity_top_k=5,
            response_mode="tree_summarize"
        )

    def initialize_agent(self):
        """Initialize the ReAct agent"""
        fantasy_tool = create_fantasy_tool(self.query_engine)
        
        self.agent = ReActAgent.from_tools(
            tools=[fantasy_tool],
            llm=self.llm,
            verbose=True,
            system_prompt=SYSTEM_PROMPT,
            max_iterations=10
        )

    def get_response(self, question):
        """Get response from the agent"""
        try:
            # Add Yahoo Fantasy context if available
            context = ""
            if self.yahoo_manager:
                try:
                    roster = self.yahoo_manager.get_roster()
                    waivers = self.yahoo_manager.get_waiver_players()
                    league_info = self.yahoo_manager.get_league_info()
                    
                    context = f"""
                    Current Team Roster: {roster}
                    Available Players: {waivers}
                    League Info: {league_info}
                    
                    Based on this information and the question: {question}
                    """
                except Exception as e:
                    print(f"Warning: Error getting Yahoo Fantasy data: {e}")
            
            # Get response from agent
            response = self.agent.chat(context + question if context else question)
            return self.chat_utils.format_response(str(response))
        except Exception as e:
            return f"Error processing question: {str(e)}" 