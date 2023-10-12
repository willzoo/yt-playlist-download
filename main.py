import time

import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


def download(driver_local, string):
    driver_local.get("https://ytmp3.nu/")
    driver_local.find_element(By.XPATH, "//*[@id=\"url\"]").send_keys(string)
    driver_local.find_element(By.XPATH, "/html/body/form/div[2]/input[3]").click()
    while True:
        try:
            driver_local.find_element(By.XPATH, "//*[@id=\"download\"]/a[1]").click()
            return
        except:
            get_source = driver_local.page_source
            if "backend error" in get_source:
                download(driver_local, string)
                return
            pass


if __name__ == '__main__':
    start = 1
    length = 61
    length += 1
    counter = 0
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/playlist?list=PLtP7k2prFAuXBtsqL92d-UNUT0IS5U9ny")
    time.sleep(1)
    list = []
    for i in range(start, length):
        list.append(driver.find_element(By.XPATH,
                                        "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse"
                                        "-results-renderer/div[1]/ytd-section-list-renderer/div["
                                        "2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div["
                                        "3]/ytd-playlist-video-renderer[" + str(
                                            i) + "]/div[2]/div[1]/div/h3/a").get_attribute("href"))
    for i in list:
        slice_index = i.find("&list")
        i = i[:slice_index]
        print(i)
        download(driver, i)
    print("Operation complete")
    time.sleep(10000)
