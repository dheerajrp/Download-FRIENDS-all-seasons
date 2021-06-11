"""
The script below, downloads the chrome driver and by using selenium,
it scraps the web page, where there are download mirrors of all the seasons
of F.R.I.E.N.D.S.
"""
import time

from chromedriver_py import binary_path
from humanfriendly import format_timespan
from selenium import webdriver
from selenium.webdriver.common.by import By


def sleep_time(seconds):
    """
    sleep for 5 seconds
    """
    time.sleep(seconds)


def season_download():
    """
    Getting all the episodes in the season and finding the download mirror
    """
    if season in ('0' + str(3), '0' + str(6)):
        for episodes in range(2, 27):
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH,
                                '/html/body/table/tbody/tr[' + str(episodes) + ']/td[1]/a').click()
            sleep_time(seconds=5)

    if season == '0' + str(9):
        for episodes in range(2, 25):
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH,
                                '/html/body/table/tbody/tr[' + str(episodes) + ']/td[1]/a').click()
            sleep_time(seconds=5)

    if season == str(10):
        for episodes in range(2, 20):
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH,
                                '/html/body/table/tbody/tr[' + str(episodes) + ']/td[1]/a').click()
            sleep_time(seconds=5)
    if season in ('0' + str(1), '0' + str(2),
                  '0' + str(4), '0' + str(5),
                  '0' + str(7), '0' + str(8)):
        for episodes in range(2, 26):
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH,
                                '/html/body/table/tbody/tr[' + str(episodes) + ']/td[1]/a').click()
            sleep_time(seconds=5)


if __name__ == '__main__':
    start_time = time.time()
    try:
        season = int(input("Which season you want to download?\n"))
        if 0 < season < 11:
            driver = webdriver.Chrome(executable_path=binary_path)
            season = ['0' + str(season) if len(str(season)) == 1 else season]
            season = season[0]
            driver.get("http://s8.bitdl.ir/Series/friends/S" + str(season) + "/")
            season_download()
            end_time = time.time()
            print("Season", season, "downloaded successfully. "
                                    "Total time taken to download the season", season, 'is',
                  format_timespan(end_time - start_time), "Enjoy with F.R.I.E.N.D.S 😄😄😄")
        else:
            print("Enter a valid season number from 1 to 10")
    except ValueError:
        print("Enter a valid number for the season")
