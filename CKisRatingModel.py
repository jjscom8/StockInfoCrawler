import pandas as pd
import requests
import math

class CKisRatingData:
    def __init__(self):
        self.__dBondBBBRate = math.nan

    def SetBondBBB_5Rate(self, dBondBBB_5Rate):
        self.__dBondBBB_5Rate = dBondBBB_5Rate

    def BondBBB_5Rate(self):
        return self.__dBondBBB_5Rate


class CKisRatingModel:

    def __init__(self):
        self.__Data = CKisRatingData()

    def Data(self):
        return self.__Data

    def CrawlBondBBBRate(self):
        url = 'http://kisrating.com/ratingsStatistics/statics_spread.do#'
        response = requests.get(url)
        kisDfList = pd.read_html(response.text)
        kisDf = kisDfList[0]

        # Column Name
        kisDf.set_index(kisDf.columns[0], inplace=True)

        dBondBBB_5Rate = kisDf.loc[self.__sTagBBBMin, self.__sTagYear5]

        self.__Data.SetBondBBB_5Rate(dBondBBB_5Rate)

    # Header
    __sTagBBBMin = 'BBB-'
    __sTagYear5 = '5년'

