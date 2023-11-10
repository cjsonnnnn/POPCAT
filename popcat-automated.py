from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def gt(startTime, endTime, curTotal):
    elp = endTime - startTime
    curTotal += elp
    print(f"elapsed time: {elp}\ntotal: {curTotal}")
    return curTotal


def run(numClicks: int, numIteration: int):
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager("115.0.5790.102").install())
    )
    driver.get("https://popcat.click/")
    driver.maximize_window()
    wd = WebDriverWait(driver, 10)

    element = wd.until(EC.element_to_be_clickable((By.XPATH, "//body/div[1]")))
    k = 100 / numIteration
    l = ((100 // k) - 1) if ((100 / k).is_integer()) else (100 // k)
    devider = int(numClicks * (k / 100))
    total_elapsed_time = 0
    j = 0
    start_time = time.time()
    for i in range(1, numClicks + 1):
        element.click()
        if (i == numClicks) and (j >= l):
            end_time = time.time()
            print(f"\nat 100%: {i} clicks finished")
            total_elapsed_time = gt(start_time, end_time, total_elapsed_time)
            start_time = time.time()

        if (i % devider == 0) and (j < l):
            end_time = time.time()
            print(f"\nat {round((i/numClicks)*100, 2)}%: {i} clicks finished")
            total_elapsed_time = gt(start_time, end_time, total_elapsed_time)
            start_time = time.time()
            j += 1


if __name__ == "__main__":
    numClicks = int(input("Enter number of clicks: "))
    numIteration = int(input("Enter number of output iteration: "))
    run(numClicks, numIteration)
