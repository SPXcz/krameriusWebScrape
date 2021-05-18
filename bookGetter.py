from selenium import webdriver
from functools import reduce
import threading
from time import sleep

def getUuid(listNum, mzk):

    print("Thread {} started".format(listNum))
    uuids = []
    unique = True
    with webdriver.Firefox() as browser:
        if(mzk):
            browser.get("http://www.digitalniknihovna.cz/mzk/search?collections=vc:b1adb6f0-01db-45fd-bc4a-d36fa3eab050&page={}".format(listNum))
        else:
            browser.get("https://ds-coil.uibk.ac.at/search?page={}".format(listNum))
        sleep(4)
        elements = browser.find_elements_by_xpath('/html/body/app-root/main/app-search/div/app-search-results/app-document-card[*]/a')

        for element in elements:
            uuids.append(element.get_attribute("href").split("view/")[1]+"\n")

    with open("uibk.txt", "a") as fw:
        fw.writelines(uuids)
    print("Thread {}: FINISHED".format(listNum))


def main():
    threadsMZK = []
    for i in range(0,7):
        threadsMZK.append(threading.Thread(target=getUuid, args=[i+1, False]))
        threadsMZK[i].start()
        sleep(5)
main()