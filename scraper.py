from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url = 'https://data-fairfaxcountygis.opendata.arcgis.com/search'

## Create an instance of Chrome WebDriver.
driver = webdriver.Chrome()

# Go to the web page
driver.get(url)

# Wait for page to load completely.
# There is a button "More Results" at the end of the page, except the last one. 
# When the button presents, the page should load completely.
# Click "More Results" will load next 20 records. So use the WebDriver to click "More Results" until there is
# no more results.
# The expected_conditions module contains a set of predefined conditions to use with WebDriverWait.

while True:
    try:
        # Get the "More Results" button, click the button.
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn more-results link-color-primary']"))).click()
        #print("Clicked on More Results")
    except TimeoutException:
        #print("No more results")
        break

# Get all the elements contain the name of the results.
result_names = driver.find_elements(By.XPATH, "//a[@class='ember-view result-name']")
for name in result_names:
    print(name.text)

# Close the browser window.
driver.quit()

