from yahoo_oauth import OAuth2
from yahoo_fantasy_api import league, game, team
import os
from src.utils.config import ROOT_DIR

class YahooFantasyManager:
    def __init__(self):
        oauth_path = os.path.join(ROOT_DIR, 'oauth.json')
        self.oauth = OAuth2(None, None, from_file=oauth_path)
        self.sport_code = "nfl"
        self.league_id = "449.l.923581"  # You might want to make this configurable
        
        # Initialize game and league
        self.game = game.Game(self.oauth, self.sport_code)
        self.league = league.League(self.oauth, self.league_id)
        self.team_key = self.league.team_key()
        self.team = team.Team(self.oauth, self.team_key)

    def get_waiver_players(self):
        """Get available players from waivers"""
        waiver = self.league.waivers()
        waiver_players = []
        
        for player in waiver:
            player_details = {
                "name": player["name"],
                "position": player["eligible_positions"]
            }
            waiver_players.append(player_details)
        
        return waiver_players

    def get_roster(self):
        """Get current team roster"""
        roster = self.team.roster(self.league.current_week())
        roster_players = []
        
        for player in roster:
            player_details = {
                "name": player["name"],
                "position": player["eligible_positions"]
            }
            roster_players.append(player_details)
        
        return roster_players

    def get_league_info(self):
        """Get basic league information"""
        return {
            "current_week": self.league.current_week(),
            "settings": self.league.settings(),
            "standings": self.league.standings()
        } 