from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures
import time


def gt(startTime, endTime, curTotal):
    elp = endTime - startTime
    curTotal += elp
    print(f"elapsed time: {elp}\ntotal: {curTotal}")
    return curTotal


def main(pId, numClick: int, numIteration: int=1000):
    print(f"Process {pId} started with numClicks={numClick} and numIteration: {numIteration}")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get("https://popcat.click/")
    driver.maximize_window()
    wd = WebDriverWait(driver, 10)

    element = wd.until(EC.element_to_be_clickable((By.XPATH, "//body/div[1]")))
    k = 100 / numIteration
    l = ((100 // k) - 1) if ((100 / k).is_integer()) else (100 // k)
    devider = int(numClick * (k / 100))
    total_elapsed_time = 0
    j = 0
    start_time = time.time()
    for i in range(1, numClick + 1):
        element.click()
        if (i == numClick) and (j >= l):
            end_time = time.time()
            print(f"\nat 100%: {i} clicks finished")
            total_elapsed_time = gt(start_time, end_time, total_elapsed_time)
            start_time = time.time()

        if (i % devider == 0) and (j < l):
            end_time = time.time()
            print(f"\nat {round((i/numClick)*100, 2)}%: {i} clicks finished")
            total_elapsed_time = gt(start_time, end_time, total_elapsed_time)
            start_time = time.time()
            j += 1
    print(f"Process {pId} completed")

if __name__ == "__main__":
    numWorkers = int(input("Number of workers: "))
    numClicks = numClicks if len(numClicks := str(input("Number of click each worker (e.g. 30 20 100): ")).split(" ")) == numWorkers else 0
    if numClicks:
        numClicks = [int(num) for num in numClicks]
    else:
        raise ValueError
    numIteration = 1000
    numIteration = numIteration if (i:=input(f"Enter number of output iteration for all the workers [{numIteration}]: ")) == '' else int(i)

    with concurrent.futures.ProcessPoolExecutor(max_workers=numWorkers) as pool:
        pIds = list(range(numWorkers))
        pool.map(main, *[pIds, numClicks, [numIteration]*numWorkers])
