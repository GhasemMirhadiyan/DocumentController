import pandas as pd
import RegexChecking
import GetFile


def convert(taglist):
    #For Convert To Excel File
    TagToExcel = taglist
    excel = pd.DataFrame()
    excel['Tags'] = TagToExcel
    excel.to_excel('result.xlsx', index=False)