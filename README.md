# web_downloader
Web Data Downloader

Connect to a website, parse it's contents, and download any displayed data.
The main computational subtask is parsing the contents of a public website.

Some goals for input and output:

Ex 1:
Input: https://www.regentsprep.org/z-score-chart/
Output: a csv file that can be read into a dataframe. The dataframe would contain the table from the website

Ex2: 
Input: http://hyperphysics.phy-astr.gsu.edu/hbase/Astro/blkhol.html
Output: a csv file that contains each section of text, and proper delimiters to denote the chart sections

Outline:
1. Connect to a website
2. Scrape the page (using some suggestions)
3. Clean, format, and save the contents
