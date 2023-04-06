from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

def get_recommendation_tours(sum_for_tours_from, sum_for_tours, city_preference_tours_from, city_preference_tours_to, date_picker):
    cityRus = {"Krasnoyarsk": 37, "Moscow": 2, "Khabarovsk": 80, "Vladivostok": 19, "Blagoveshensk": 15, "Irkutsk": 28}
    cityOutside = {"Thailand": 87, "Turkish": 92, "Egypt": 29, "UAE": 68, "Venezuela": 21, "Cuba": 48, "Vietnam": 22}
    from_country = str(cityRus[city_preference_tours_from])
    to_country = str(cityOutside[city_preference_tours_to])
    date_from = (lambda x: '.'.join(x[::-1]))(date_picker.split("-"))
    price = str(sum_for_tours)
    if sum_for_tours_from == 0 or sum_for_tours_from is None:
        sum_for_tours_from = 15000
    URL = f"https://tinkoff.travelata.ru/search#?fromCity={from_country}&toCountry={to_country}" \
          f"&dateFrom={date_from}" \
          f"&dateTo={date_from}&nightFrom=8&nightTo=15" \
          f"&adults=2&hotelClass=all&meal=all&priceFrom={str(sum_for_tours_from)}&priceTo={price}&sid=1px7n2x8d5&sort=priceUp&f_noScore=true"
    print(URL)
    # Initialize Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)

    # Create an empty list to store tour recommendations
    recommendations = []

    try:
        # Open the URL in the browser
        driver.get(URL)

        # Wait for the page to load and find all the "Book" buttons
        wait = WebDriverWait(driver, 30)
        wait.until(EC.invisibility_of_element_located((By.ID, "searchProgressBar")))
        time.sleep(10)
        elementes = driver.find_element(By.CLASS_NAME, "no-tours-banner")
        stylef = elementes.get_property("style")
        if len(stylef) == 0:
            # driver.quit()
            raise Exception
        elif "display" in stylef:
            tours = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "serpHotelCard__btn")))
            y = 1
            for tour in tours:
                tour.click()
                if y >= 3:
                    break
                y += 1
            lenWindow= len(driver.window_handles)
            # Click on each "Book" button and extract the tour price
            for i in range(0, int(lenWindow)-1):
                driver.switch_to.window(driver.window_handles[-1])
                inner_list = []
                # Wait for the new page to load and switch to the new window
                wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "brawn-progress-bar__container")))
                # Find and click on the desired element on the new page
                price_block = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'hotelTour__price-block__btn')))
                price_block.click()
                time.sleep(5)
                # Find the tour price on the page and add it to the recommendations list
                name_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ticket__title')))
                name_text = name_element.text.strip()
                location_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ticket__position')))
                location_text = location_element.text.strip()
                price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tourInfo__price')))
                price_text = price_element.text.strip()
                date_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-tourDuration')))
                date_text = date_element.text.strip()
                inner_list.append(name_text)
                inner_list.append(location_text)
                inner_list.append(price_text)
                inner_list.append(date_text)
                recommendations.append(inner_list)
                # Close the new window and switch back to the original window
                driver.close()
            return recommendations
    except Exception as e:
        # print(f"Error: {e}")
        return "error"

    finally:
        # Quitting the driver and returning up to 10 tour recommendations
        driver.quit()




