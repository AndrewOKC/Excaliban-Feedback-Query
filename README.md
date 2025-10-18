# Excaliban Feedback Query Tool

A simple Python utility to fetch and save customer feedback from the Excaliban Feedback API to a CSV file.

## Requirements

-   Python 3.6 or higher
-   Access to the Excaliban Feedback API
-   Admin API key for authentication

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/Excaliban-Feedback-Query.git
    cd Excaliban-Feedback-Query
    ```

2. Install dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

3. Create a `.env` file in the project root:

    ```bash
    cp .env.example .env
    ```

4. Edit the `.env` file and add your API credentials:
    ```
    API_URL=https://api.excaliban.com/feedback
    FEEDBACK_API_KEY=your_api_key_here
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

Configuration is managed through environment variables in the `.env` file:

-   `API_URL`: The endpoint URL for the feedback API
-   `FEEDBACK_API_KEY`: Your admin API key

Additional settings can be modified in `fetch_feedback.py`:

-   `CSV_FILE`: Output filename (default: `feedback_data.csv`)
-   `MAX_RESULTS`: Maximum number of feedback items to fetch (default: 20)

## Viewing Results

On macOS, you can open the CSV file with:

-   **Numbers**: Double-click the file or open with Numbers
-   **Preview**: Right-click and select "Open With" > "Preview"
-   **TextEdit**: Right-click and select "Open With" > "TextEdit"
-   **VS Code**: Open in VS Code with CSV extension

## Documentation

See `CLAUDE.md` for more detailed documentation about the project.

## Security

**Important Security Notes:**

-   Never commit your `.env` file to version control
-   Keep your API key confidential
-   Rotate your API key regularly
-   The `.gitignore` file is configured to exclude `.env` files

## License

MIT License - Feel free to use and modify as needed.
