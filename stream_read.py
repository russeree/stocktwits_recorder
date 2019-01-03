##
# @auth: Reese Russell
# @desc: This is the primary StockTwits Recoding Module
import os
import sys
import time
from multiprocessing import Pool
# Selenium Requirements
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
##
class StockTwitsStreamRecorder:
    # @desc: This class contains everything neccesary to record data from the stock twits website to a file to be processesed
    ##
    # @desc: Initializes the Class Object, this object will have enough info to run multiple stream recorders
    def __init__(self):
        self.stockTwitsURLForm = "https://www.stocktwits.com/symbol/{}"
        self.stockTwitsStreamButton = 'StreamPlayButton__icon'
        self.stockTwitsMessageId = 'MessageList__item'
        self.stockTwitsSentimentIncicatorPartialId = 'MessageStreamView__sentiment'
        print("Stocktwits Stream Recorder Activated")
    ##
    # @desc: When the Class is destroyed give the user a freindly reminder that it has closed successfuly
    def __del__(self):
        print("Stocktwits Stream Recorder Deactivated")
    ##
    # @desc: This is the stream recording loop: WARN: MANY MAGIC NUMBERS
    # @param:[symbol] string for the symbol that will be grabbed from the stocktwits website
    def twitStreamRecorder(self,symbol):
        print("Stocktwits Stream of ${} has began recording.".format(symbol))
        driver = webdriver.Chrome('./chromedriver')
        try: #Visit the StockTwits Ticker Symbol
            driver.get(self.stockTwitsURLForm.format(str(symbol)))
        except Exception as E:
            print("${} Failed to connect with Exception:".format(symbol))
            print('\t{}'.format(str(E)))
            return "${} Recoder URL Failure".format(symbol)
        try: #Try to click the 'Real Time' Play Button
            driver.find_elements_by_xpath('//*[contains(@class, "' + self.stockTwitsStreamButton + '")]')[0].click() #Presses the Play Button To Begin Streaming Data
        except Exception as E:
            print("${} Failed to begin streaming user 'Twits' with Exception:".format(symbol))
            print('\t{}'.format(str(E)))
            return "${} Recoder Sream Failure".format(symbol)
        while True: #The Continuious Monitoring Loop
            try:
                _onScreenTwits = driver.find_elements_by_xpath('//*[contains(@class, "' + self.stockTwitsMessageId +'")]') #This is the equivilant of pointing to each message that comes though the stream
                for twit in _onScreenTwits:
                    try:
                        _x = twit.find_element_by_xpath('.//*[contains(@class, "' + self.stockTwitsSentimentIncicatorPartialId +'")]').text
                        if str(_x) == '':
                            _x = 'None'
                    except NoSuchElementException:
                        _x = 'None'
                    finally:
                        print(_x)
                print("----UPDATE----")
                time.sleep(5)
            except Exception as E:
                print("${} Failed to read 'twit' with Exception:".format(symbol))
                print('\t{}'.format(str(E)))
                return "${} Recoder Sream Failure".format(symbol)
        driver.close()
        return "${} Recoder Success".format(symbol)

#Example Process Pool of Recorders
if __name__ == '__main__':
    x = StockTwitsStreamRecorder()
    with Pool(5) as p:
        print(p.map(x.twitStreamRecorder,['SPY']))
    sys.exit(0)
