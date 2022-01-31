import pandas as pd
import requests
import math


class CKisRatingData:

    def __init__(self):
        self.__dBondBBBRate = math.nan

    def SetBondBBB_5Rate(self, dBondBBB_5Rate):
        self.__dBondBBBRate = dBondBBB_5Rate

    def BondBBB_5Rate(self):
        return self.__dBondBBBRate

class CKisRatingModel:

    def __init__(self):
        self.__Data = CKisRatingData()

    def Data(self):
        return self.__Data

    def CrawlBondBBBRate(self):
        try:
            url = 'http://kisrating.com/ratingsStatistics/statics_spread.do#'
            response = requests.get(url)
            kisDfList = pd.read_html(response.text)
            kisDf = kisDfList[0]

            # Column Name
            kisDf.set_index(kisDf.columns[0], inplace=True)

            dBondBBB_5Rate = kisDf.loc[self.__sTagBBBMin, self.__sTagYear5]
            self.__Data.SetBondBBB_5Rate(dBondBBB_5Rate)

            return True

        except ValueError:
            print("         # ValueError : {}".format(self.__stockCode))
            print("           => pd.read_html() 실패 시 발생 가능. Table이 없는 Page")
            return False
        except KeyError:
            print("         # KeyError : {}".format(self.__stockCode))
            print("           => df.loc[] 실패 시 발생 가능 ('해당 row/col Key가 없는 Table)")
            return False
        except IndexError:
            print("         # IndexError : {}".format(self.__stockCode))
            return False


    # Header
    __sTagBBBMin = 'BBB-'
    __sTagYear5 = '5년'

