# web_downloader
Web Data Downloader

Connect to a website, parse it's contents, and download any displayed data.
The main computational subtask is parsing the contents of a public website.

Some goals for input and output:

Ex 1:
Input: 'https://data-fairfaxcountygis.opendata.arcgis.com/search'

Output: The names of all the datasets contained in this website


Outline:
1. Connect to a website
2. Scrape the page (using some suggestions)
