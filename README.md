# Fantasy Football AI Assistant 🏈

An intelligent AI-powered assistant for fantasy football analysis and team management, combining OpenAI's language models with Yahoo Fantasy Sports integration.

## Features

- **AI-Powered Analysis**: Utilizes OpenAI's language models for intelligent fantasy football insights
- **Yahoo Fantasy Integration**: Direct connection to your Yahoo Fantasy Football league
- **Interactive Web Interface**: Built with Streamlit for a user-friendly experience
- **Data-Driven Insights**: Analyzes combine metrics, injury history, and performance statistics
- **Real-time Team Management**: View and analyze your current roster and available players

## Project Structure

```
Fantasy_Football_AI_Agent
├── src/
│   ├── agent/              # AI agent implementation
│   │   ├── __init__.py
│   │   ├── fantasy_agent.py
│   │   └── tools.py
│   ├── data/              # Data handling and processing
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── data_processor.py
│   │   └── Dataset/       # CSV data files
│   └── utils/             # Utility functions and configurations
│       ├── __init__.py
│       ├── config.py
│       ├── chat_utils.py
│       └── yahoo_fantasy.py
├── storage/               # Persistent storage for vector indices
├── .env                  # Environment variables
├── app.py               # Streamlit web application
├── main.py             # CLI application
└── verify_setup.py    # Setup verification script
```

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/fantasy-football-ai.git
   cd fantasy-football-ai
   ```

2. **Set Up Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   - Create a `.env` file in the root directory
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

4. **Yahoo Fantasy Integration**
   - Create an `oauth.json` file in the root directory with your Yahoo OAuth credentials:
     ```json
     {
         "consumer_key": "your_consumer_key",
         "consumer_secret": "your_consumer_secret",
         "access_token": "your_access_token",
         "refresh_token": "your_refresh_token"
     }
     ```
   - Update the league ID in `src/utils/yahoo_fantasy.py`

5. **Prepare Data**
   Place your CSV files in `src/data/Dataset/`:
   - `combine_data.csv`: NFL Combine performance metrics
   - `injuries.csv`: Player injury history
   - `rush.csv`: Rushing statistics

6. **Verify Setup**
   ```bash
   python verify_setup.py
   ```

7. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## Usage

### Web Interface (Streamlit)
- Access the web interface at `http://localhost:8501`
- Features:
  - Fantasy Football rules in the sidebar
  - Quick access to example questions
  - Real-time chat interface
  - Team roster view
  - Available players list
  - League information

### Command Line Interface
```bash
python main.py
```
- Interactive command-line interface for quick queries
- Type 'quit' to exit

## Configuration

### OpenAI Settings
```python
model = "gpt-4o-mini"
temperature = 0.7
max_tokens = 1500
```

### Yahoo Fantasy Settings
```python
sport_code = "nfl"
league_id = "your_league_id"  # Update in yahoo_fantasy.py
```

## Data Format Requirements

### combine_data.csv
- Player physical metrics
- Combine performance statistics
- Athletic measurements

### injuries.csv
- Injury history
- Recovery timelines
- Current injury status

### rush.csv
- Rushing statistics
- Performance metrics
- Historical data

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify OpenAI API key in `.env`
   - Check API key validity
   - Run `verify_setup.py`

2. **Data Loading Issues**
   - Check CSV file locations
   - Verify file permissions
   - Ensure correct file formats

3. **Yahoo Fantasy Integration**
   - Validate OAuth credentials
   - Check league ID
   - Verify API access permissions

4. **Streamlit Interface**
   - Port conflicts: Change port if 8501 is in use
   - Session state issues: Clear browser cache
   - Display problems: Check browser compatibility

## Support

For support:
1. Check the troubleshooting section
2. Review existing issues
3. Create a new issue with:
   - Detailed description
   - Error messages
   - Steps to reproduce
   - Environment details

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for their language models
- Yahoo Fantasy Sports for their API
- Streamlit for the web interface framework
- Contributors and maintainers

<!-- ## Updates

Check the [CHANGELOG](CHANGELOG.md) for version updates and changes.  -->
