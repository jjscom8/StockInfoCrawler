import pandas as pd
import requests
from io import BytesIO

class CKrxData:
    def __init__(self):
        self.__CompDf = pd.DataFrame()

    def SetCompDf(self, compDf):
        self.__CompDf = compDf

    def CompDf(self):
        return self.__CompDf

class CKrxModel:
    def __init__(self):
        self.__Data = CKrxData()

    def Data(self):
        return self.__Data

    def ColCompName(self):
        return self.__sTagName

    def CrawlCompanies(self, compNames = []):
        try:
            # Excel(.xls)을 다운로드하지만 vim으로 열어보면 실제로는
            # HTML 형식으로 구성된 것을 확인할 수 있다.
            url = 'https://kind.krx.co.kr/corpgeneral/corpList.do'
            data = {
                'method': 'download',
                'orderMode': '1',  # 정렬할 컬럼
                'orderStat': 'D',  # 내림차순
                'searchType': '13',  # 검색유형(상장법인)
                'fiscalYearEnd': 'all',  # 결산월(전체)
                'location': 'all',  # 지역(전체)
            }
            # Return DF 정의
            ret_df = pd.DataFrame()

            # 데이터 가저오기
            response = requests.post(url, data=data)
            bytes = BytesIO(response.content)
            krxDfList = pd.read_html(bytes, header=0)
            krxDf = krxDfList[0].copy()

            # 종목코드 자리수 채우기
            krxDf[self.__sTagCode] \
                = krxDf[self.__sTagCode].astype(str).str.zfill(6)

            # get/set
            compDf = krxDf.loc[:,[self.__sTagName, self.__sTagCode,  self.__sTagIndustry]]

            # 파라미터 종목 필터링
            if compNames:
                compDf = compDf[compDf[self.__sTagName].isin(compNames)]

            compDf.set_index(self.__sTagCode, inplace=True)
            self.__Data.SetCompDf(compDf)

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

    def ExportExcel(self, outPath):
        self.__Data.CompDf().to_excel(outPath)

    # Header
    __sTagName = '회사명'
    __sTagCode = '종목코드'
    __sTagIndustry = '업종'


