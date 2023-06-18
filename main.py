from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import pickle
import csv

# initialize the service and driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
pages = []
pages.append("https://cardinalservice.stanford.edu/opportunities?su_opp_dimension%5B486%5D=486&sort_by=changed&sort_order=DESC&page=0")
pages.append("https://cardinalservice.stanford.edu/opportunities?su_opp_dimension%5B486%5D=486&sort_by=changed&sort_order=DESC&page=1")
pages.append("https://cardinalservice.stanford.edu/opportunities?su_opp_dimension%5B486%5D=486&sort_by=changed&sort_order=DESC&page=2")
pages.append("https://cardinalservice.stanford.edu/opportunities?su_opp_dimension%5B486%5D=486&sort_by=changed&sort_order=DESC&page=3")
pages.append("https://cardinalservice.stanford.edu/opportunities?su_opp_dimension%5B486%5D=486&sort_by=changed&sort_order=DESC&page=4")
opportunities_dict = {}

for page in pages:
    driver.get(page)

    # wait for the page to load
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".views-row")))

    # scrape the remaining HTML
    opportunity_links = driver.find_elements(By.CSS_SELECTOR, ".views-row .su-opportunity a")

    # loop through the links and get the email for each opportunity
    for i in range(len(opportunity_links)):
        # re-find the links on each iteration to avoid StaleElementReferenceException
        opportunity_links = driver.find_elements(By.CSS_SELECTOR, ".views-row .su-opportunity a")
        href = opportunity_links[i].get_attribute("href")
        opportunity_links[i].click()
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".su-opp-contact-email")))
            email = driver.find_element(By.CSS_SELECTOR, ".su-opp-contact-email").text
        except TimeoutException:
            print("Timeout exception occurred for:", href)
            email = ""
        hsplit = href.split("/")
        opportunities_dict[hsplit[4]] = email
        driver.back()

# close the driver and service
driver.quit()
service.stop()

# print the dictionary of opportunities and email addresses
sorted_dict = dict(sorted(opportunities_dict.items()))
# print(sorted_dict)
with open('sorted_dict.pkl','wb') as f:
    pickle.dump(sorted_dict, f)





