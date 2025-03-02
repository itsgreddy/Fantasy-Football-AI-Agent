import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration with validation
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")

# Get the project root directory (Fantasy Football AI Agent)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Data Paths
DATA_DIR = os.path.join(ROOT_DIR, "src", "data", "Dataset")  # Updated path
STORAGE_DIR = os.path.join(ROOT_DIR, "storage", "fantasy")

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(STORAGE_DIR, exist_ok=True)

# Fantasy Football Rules
FANTASY_RULES = """
Fantasy Football Rules and Scoring (PPR Format):
1. League Structure:
   - 10-12 teams
   - Snake draft format
   - PPR scoring

2. Roster Positions:
   - 1 QB
   - 2 RB
   - 2 WR
   - 1 TE
   - 1 FLEX (RB/WR/TE)
   - 1 D/ST
   - 1 K
   - 7 Bench spots

3. Scoring System:
   Passing:
   - 1 point per 25 passing yards
   - 4 points per passing TD
   - -2 points per interception

   Rushing:
   - 1 point per 10 rushing yards
   - 6 points per rushing TD

   Receiving:
   - 1 point per reception (PPR)
   - 1 point per 10 receiving yards
   - 6 points per receiving TD
"""

# Agent Configuration
SYSTEM_PROMPT = f"""
You are an expert Fantasy Football AI agent with deep knowledge of player statistics, 
injury histories, and performance metrics. Your analysis should be based on:

1. Recent Performance: Analyze current season and historical statistics
2. Injury Risk: Evaluate injury history and current status
3. Physical Metrics: Consider combine data and athletic measurements
4. Matchup Analysis: Account for opposing team strengths/weaknesses
5. League Rules: Apply the following scoring system:

{FANTASY_RULES}

When making recommendations:
- Provide specific data points to support your analysis
- Consider both floor and ceiling scenarios
- Account for injury risk and recovery patterns
- Explain your reasoning clearly
- Suggest alternatives when relevant
""" 