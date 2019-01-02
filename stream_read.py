from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool

##
# @desc: This class contains everything neccesary to record data from the stock twits website to a file to be processesed

class StockTwitsStreamRecorder:
    ##
    # @desc: Initializes the Class Object, this object will have enough info to run multiple stream recorders
    def __init__(self):
        print("Stocktwits Stream Recorder Activated")
    ##
    # @desc: When the Class is destroyed give the user a freindly reminder that it has closed successfuly
    def __del__(self):
        print("Stocktwits Stream Recorder Deactivated")
    ##
    # @desc: This is the stream recording loop: WARN: MANY MAGIC NUMBERS
    # @param:[symbol] string for the symbol that will be grabbed from the stocktwits website
    def visitSite(self,symbol):
        print("Stocktwits Stream of ${} has began recording.".format(symbol))
        driver = webdriver.Chrome('./chromedriver')
        driver.get("https://www.stocktwits.com/symbol/{}".format(str(symbol)))

#Example Process Pool of Recorders
if __name__ == '__main__':
    x = StockTwitsStreamRecorder()
    with Pool(5) as p:
        print(p.map(x.visitSite,['SPY','QQQ','AMZN']))
