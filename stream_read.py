from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool

class StockTwitsStreamRecorder:
    def __init__(self):
        print("Stocktwits Stream Recorder Activated")
    def __del__(self):
        print("Stocktwits Stream Recorder Deactivated")
    def visitSite(self,symbol):
        print("Stocktwits Stream of ${} has began recording.".format(symbol))
        driver = webdriver.Chrome('./chromedriver')
        driver.get("https://www.stocktwits.com/symbol/{}".format(str(symbol)))

if __name__ == '__main__':
    x = StockTwitsStreamRecorder()
    with Pool(5) as p:
        print(p.map(x.visitSite,['SPY','QQQ','AMZN']))
