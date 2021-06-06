"""
The script below, downloads the chrome driver and by using selenium, it scraps the web page, where there are download mirrors of all the seasons
of F.R.I.E.N.D.S.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from humanfriendly import format_timespan
from chromedriver_py import binary_path


def find_element_and_download(episodes, driver):
    """

    :param episodes: episodes in each season
    :param driver: chromedriver version 91.0.4472.19
    :return: Downloads all the episodes of the season to the default downloads folder on your computer
    """
    driver.find_element(By.XPATH, '/html/body/table/tbody/tr[' + str(episodes) + ']/td[1]/a').click()


def season_download():
    """
    Getting all the episodes in the season and finding the download mirror
    """
    if season == 3 and season == 6:
        for episodes in range(2, 27):
            find_element_and_download(episodes=episodes, driver=driver)

    elif season == 9:
        for episodes in range(2, 25):
            find_element_and_download(episodes=episodes, driver=driver)

    elif season == 10:
        for episodes in range(2, 20):
            find_element_and_download(episodes=episodes, driver=driver)
    else:
        for episodes in range(2, 26):
            find_element_and_download(episodes=episodes, driver=driver)


if __name__ == '__main__':
    start_time = time.time()
    try:
        season = int(input("Which season you want to download?\n"))
        if 0 < season < 11:
            driver = webdriver.Chrome(executable_path=binary_path)#'/home/delixus/chromedriver')
            season = ['0' + str(season) if len(str(season)) == 1 else season]
            driver.get("http://s8.bitdl.ir/Series/friends/S" + str(season[0]) + "/")
            season_download()
            end_time = time.time()
            print("Season", season, "downloaded successfully. Total time taken to download the season", season, 'is',
                  format_timespan(end_time - start_time), "Enjoy with F.R.I.E.N.D.S 😄😄😄")
        else:
            print("Enter a valid season number from 1 to 10")
    except ValueError:
        print("Enter a valid number for the season")
