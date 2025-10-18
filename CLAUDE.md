# CLAUDE.md - Excaliban Feedback Query Tool

## Project Overview
The Excaliban Feedback Query Tool is a simple Python utility to fetch feedback data from the Excaliban Feedback API and save it to a CSV file for easy viewing and analysis. This tool is designed for macOS users who need to keep track of customer feedback.

## Project Structure
```
Excaliban-Feedback-Query/
├── fetch_feedback.py           # Main Python script to fetch feedback
├── feedback_data.csv           # Output CSV file (generated, ignored by git)
├── .env                        # Environment variables (ignored by git)
├── .env.example                # Template for environment variables
├── requirements.txt            # Python dependencies
├── CLAUDE.md                   # This documentation file
├── README.md                   # Project README
└── .gitignore                  # Git ignore file
```

## Key Commands

### Running the Query Tool
```bash
# Run the script to fetch feedback
python3 fetch_feedback.py
```

### API Connection
The tool connects to the Excaliban Feedback API using:
- `GET /feedback` endpoint to list all feedback (with pagination)
- Authentication via the `X-API-Key` header
- SSL verification is disabled for development purposes

## Configuration

### Environment Variables
Configuration is managed through a `.env` file in the project root. Create this file from the template:

```bash
cp .env.example .env
```

Required environment variables:
- `API_URL`: The base URL of the Excaliban Feedback API
- `FEEDBACK_API_KEY`: Your API key for accessing admin endpoints

### Script Settings
Additional settings in `fetch_feedback.py`:
- `CSV_FILE`: Name of the output CSV file (default: `feedback_data.csv`)
- `MAX_RESULTS`: Maximum number of feedback items to fetch (default: 20)

## CSV Output Format
The tool generates a CSV file with the following columns:
- ID: Unique identifier for the feedback
- Message: The feedback text content
- App Version: Version of the app the feedback was submitted from
- Browser: Browser information
- Created At: Timestamp when feedback was submitted
- Status: Current status (new/reviewed/addressed/closed)

## Authentication
Admin endpoints require an API key, which should be configured in your `.env` file:
```
FEEDBACK_API_KEY=your_api_key_here
```

**Security Note:** Never commit your `.env` file to version control. The `.gitignore` file is configured to exclude it.

## Dependencies
- `python-dotenv`: For loading environment variables from `.env` file

Install dependencies with:
```bash
pip3 install -r requirements.txt
```

## Tips
- The CSV file is overwritten each time you run the script
- For viewing CSV files on macOS, you can use:
  - Numbers (built-in spreadsheet app)
  - Preview (built-in viewer)
  - TextEdit (built-in text editor)
  - VS Code (with appropriate extensions)
- The tool works with Python 3.6+
- Rotate your API key regularly for security