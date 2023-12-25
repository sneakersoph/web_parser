import requests
from bs4 import BeautifulSoup

def search_website(url, search_query):
    # Send a GET request to the website
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find elements with specific attributes or content
        search_results = soup.find_all(text=lambda text: search_query in str(text))

        if search_results:
            return search_results
        else:
            return "No matching information found on the website."
    else:
        return "Failed to retrieve information. Status code:", response.status_code

# Example usage:
url_to_search = 'https://example.com'  # Replace with the URL of the website you want to search
query = 'search query'  # Replace with your specific search query

results = search_website(url_to_search, query)
print(results)
