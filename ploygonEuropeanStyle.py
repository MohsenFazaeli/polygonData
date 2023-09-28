import requests
from polygonAPIkey import polygonAPIkey as API_KEY

# Replace 'YOUR_API_KEY' with your actual Polygon API key
# API_KEY = 'YOUR_API_KEY'

# Define the endpoint for retrieving options data
POLYGON_OPTIONS_URL = 'https://api.polygon.io/v2/aggs/grouped/locale/us/market/STOCKS/%s?apiKey=%s'
POLYGON_OPTIONS_URL = 'https://api.polygon.io/v2/snapshot/options/EVRI/O:EVRI240119C00002500?%s?apiKey=%s'

# Define the symbol for the European style contract you want to extract
contract_symbol = 'AAPL'  # Replace with the symbol you're interested in

# Make the API request to retrieve European style options data


def get_european_options_data(contract_symbol):
    try:
        response = requests.get(POLYGON_OPTIONS_URL %
                                (contract_symbol, API_KEY))
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Main function to extract European style contracts


def extract_european_contracts():
    european_options_data = get_european_options_data(contract_symbol)

    if european_options_data:
        # Process the data as needed
        # You can extract relevant information from 'european_options_data' here

        # Example: Print the data
        print(european_options_data)


# Run the extraction function


if __name__ == "__main__":
    extract_european_contracts()
