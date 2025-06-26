# Gemini Code Assistant Integration

This document outlines how to effectively use Gemini for assistance with the **Excaliban Feedback Query** project.

## Project Overview

The **Excaliban Feedback Query** is a Python script designed to fetch customer feedback from the Excaliban Feedback API and save it to a CSV file. This tool simplifies the process of accessing and analyzing feedback data.

### Key Features:

-   **API Integration**: Fetches data from the Excaliban Feedback API.
-   **CSV Export**: Saves feedback into a structured CSV file.
-   **Configurable**: Allows customization of API URL, key, and the number of results.

## How to Use This Tool

To run the script and fetch feedback, use the following command in your terminal:

```bash
python3 fetch_feedback.py
```

Before running, ensure you have configured your API key in `fetch_feedback.py`.

## Tool Integration

Gemini can assist with various tasks related to this project. Below are some examples of how you can use natural language commands to get help.

### 1. Running the Script

To execute the feedback fetching script, you can ask Gemini:

> "Run the fetch feedback script."

This will trigger the `python3 fetch_feedback.py` command and display the output.

### 2. Viewing the Results

After running the script, a `feedback_data.csv` file is generated. To view its contents, you can ask Gemini:

> "Show me the contents of the feedback data CSV."

Gemini will read the CSV file and display its contents.

### 3. Modifying the Configuration

If you need to change the number of results to fetch, you can ask Gemini:

> "Modify the script to fetch 50 results instead of 20."

Gemini will update the `MAX_RESULTS` variable in `fetch_feedback.py`.

### 4. Answering Questions About the Code

If you have questions about how the script works, you can ask Gemini directly:

> "Explain how the `fetch_feedback` function in `fetch_feedback.py` handles API authentication."

Gemini will analyze the code and provide a detailed explanation.

## Safety and Best Practices

-   **API Key**: Never share your API key or commit it to version control. The `API_KEY` in `fetch_feedback.py` is a placeholder and should be replaced with your actual key.
-   **File Paths**: When asking Gemini to read or write files, it's best to use relative paths from the project root (e.g., `fetch_feedback.py` or `feedback_data.csv`).
-   **Clarity**: Be as clear as possible with your requests to ensure Gemini understands your intent.

This integration is designed to streamline your workflow and make it easier to manage the feedback-gathering process. If you have any questions, feel free to ask!
