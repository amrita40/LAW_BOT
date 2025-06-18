# LAW BOT – Scalable Copyright Image Retrieval

## Overview

This project demonstrates a **scalable, automatable method for retrieving copyright images** using registration metadata. It is designed for the Law Bot platform, which analyzes intellectual property (IP) data and helps clients assess potential IP-infringement risks.

## Problem Statement

The U.S. Copyright Office provides public metadata (title, author, registration number, etc.) for visual-arts registrations, but **does not supply the actual registered images**. The challenge is to propose and demonstrate a method to efficiently retrieve or locate these images using available data.

## Solution Approach

### Explored Methods

1. **Public Image Search APIs (Bing, Google):**
   - Initially considered for automation and scalability.
   - Currently unavailable due to API restrictions and Bing API retirement.

2. **Web Automation (Selenium):**
   - Explored automating Google Images search and scraping results.
   - Not robust for production due to setup complexity, fragility, and terms of service concerns.

3. **Direct Search Link Generation (Final Solution):**
   - Generates Google Images search URLs for each registration using metadata.
   - Scalable, transparent, and easy to review or adapt to other search engines or APIs.

### Why This Approach?

- **No API keys or browser automation required.**
- **Scalable:** Works for any number of records.
- **Transparent:** Links can be reviewed manually or integrated into future automation.
- **Adaptable:** Can be extended to use APIs or other search engines as they become available.

## How It Works

1. **Reads** a CSV file (`copyright_records.csv`) containing registration metadata.
2. **Generates** a Google Images search URL for each record using the title, claimant, and description.
3. **Outputs** a new CSV (`image_search_links.csv`) with registration numbers, search queries, and direct search links.

## Usage

1. Place your `copyright_records.csv` in the project folder.
2. Run the script:

   ```sh
   python image_search_links.py
   ```

3. Open `image_search_links.csv` and click the links to view image search results for each record.

## Files

- `copyright_records.csv` – Input data with registration metadata.
- `image_search_links.py` – Python script to generate search links.
- `image_search_links.csv` – Output file with search queries and Google Images links.

## Example Output

| Registration Number | Query                                      | Google Images Search URL                                      |
|---------------------|--------------------------------------------|---------------------------------------------------------------|
| VA 2-308-936        | Staying Alive Eduardo Andre Ely 2-D artwork| https://www.google.com/search?tbm=isch&q=Staying+Alive+Eduardo+Andre+Ely+2-D+artwork |

## Future Improvements

- Integrate with public image search APIs if/when available.
- Automate image verification/matching using AI.
- Support additional image sources (e.g., Wikimedia, museum databases).

## License

This project is for demonstration and educational purposes.  
Please ensure compliance with the terms of service of any third-party services used.

---

**Developed for the Law Bot project
