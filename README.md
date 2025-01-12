# Book Catalog Scraper

A Python-based web scraping tool that extracts detailed book information from an online catalog. This project demonstrates fundamental web scraping concepts and best practices for data collection.

## Features

- Extracts comprehensive book details including:
  - Book titles
  - Cover image URLs
  - Prices
  - Ratings
  - Availability status
  - Product page URLs
- Handles multi-page navigation
- Implements ethical scraping practices with request delays
- Exports data to CSV format
- Includes robust error handling

## Technical Implementation

- **Language:** Python
- **Libraries:** 
  - BeautifulSoup4 for HTML parsing
  - Requests for HTTP requests
  - CSV for data export
- **Features:**
  - Modular code structure
  - Random delays between requests (1-3 seconds)
  - Proper error handling for HTTP requests
  - Clean data formatting and export

## Key Learnings

- Web scraping fundamentals and best practices
- HTML structure parsing and data extraction
- Handling pagination in web scraping
- Implementing ethical scraping techniques
- Data organization and export
- Error handling in web requests

## Future Improvements

- Add data validation
- Implement concurrent requests for faster processing
- Add more detailed error logging
- Create data visualization of the collected information
- Add support for different export formats

## Setup and Usage

1. Install required libraries:
```bash
pip install beautifulsoup4 requests
```

2. Run the script:
```bash
python scraper.py
```

The script will create an `output.csv` file containing all scraped book information.

## Project Structure

```
book-scraper/
│
├── scraper.py          # Main script
└── output.csv          # Generated data file
```

## License

This project is open source and available under the MIT License.