# Excaliban Feedback Query Tool

A simple Python utility to fetch and save customer feedback from the Excaliban Feedback API to a CSV file.

## Features

- Fetches feedback data from the Excaliban Feedback API
- Saves feedback in CSV format for easy viewing
- No external dependencies - uses built-in Python libraries
- Works on macOS (and other platforms)
- Configurable number of results

## Requirements

- Python 3.6 or higher
- Access to the Excaliban Feedback API
- Admin API key for authentication

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Excaliban-Feedback-Query.git
   cd Excaliban-Feedback-Query
   ```

2. Configure your API key in `fetch_feedback.py`:
   ```python
   API_KEY = "your_api_key_here"  # Replace with your actual API key
   ```

## Usage

Run the script to fetch feedback and save it to a CSV file:

```bash
python3 fetch_feedback.py
```

This will:
1. Connect to the Excaliban Feedback API
2. Fetch up to 20 most recent feedback items
3. Save them to `feedback_data.csv` in the current directory
4. Overwrite any existing CSV file with the same name

## Configuration

You can modify the following settings in `fetch_feedback.py`:

- `API_URL`: The endpoint URL for the feedback API
- `API_KEY`: Your admin API key
- `CSV_FILE`: Output filename
- `MAX_RESULTS`: Maximum number of feedback items to fetch

## Viewing Results

On macOS, you can open the CSV file with:

- **Numbers**: Double-click the file or open with Numbers
- **Preview**: Right-click and select "Open With" > "Preview"
- **TextEdit**: Right-click and select "Open With" > "TextEdit"
- **VS Code**: Open in VS Code with CSV extension

## Documentation

See `CLAUDE.md` for more detailed documentation about the project.

## License

This project is private and confidential.