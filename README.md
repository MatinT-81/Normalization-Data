# Simple Data Normalization Project

This is a simple Python project that normalizes a small dataset and saves the results in an Excel file.

## Project Structure

```
├── main.py            # Main script to create and normalize data
├── output.xlsx        # Generated Excel file with normalized data
├── requirements.txt   # List of required dependencies
└── Untitled.ipynb     # Jupyter Notebook (optional, for experimentation)
```

## Requirements

This project requires Python and the following libraries:

### Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. To create and activate a virtual environment named `.venv`, run the following commands:

On Windows:

```
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

To install dependencies, run:

```
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```
python main.py
```

This will create an Excel file `output.xlsx` containing the original and normalized data.

## Data Normalization

The script performs min-max normalization on three columns: `سن` (Age), `قد (cm)` (Height), and `وزن (kg)` (Weight). The normalized values are calculated using:

```
normalized_value = (value - min) / (max - min)
```

## Output

The script generates an Excel file (`output.xlsx`) containing both the original and normalized values.
