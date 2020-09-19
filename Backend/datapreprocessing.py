# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

## Data collection - Scraping stock data

import re
import pandas as pd
import requests
# from bs4 import BeautifulSoup
import pandas_datareader.data as web
from datetime import datetime as dt


# Change the stock ticker to collect different stock data
def preprocessdata(stock_input):
    # stock_id = '096770'
    stock_id = str(stock_input)
    # def get_stocks(stock_id,max_limit):
    #     cate = []
    #     stocks = [] 

    #     count = 1

    #     while count < max_limit:
    #         base_url = 'https://finance.naver.com/item/frgn.nhn?code='+str(stock_id)+'&page='+str(count)
    #         res = requests.get(base_url)
    #         html = BeautifulSoup(res.content,'html.parser')
    #         # Multiple tables of same name and class. Therefore use findAll and select the wanted table.
    #         table_all = html.findAll('table',{'class':'type2'})
    #         table_0 = table_all[1]
    #         cate_0 = table_0.find_all('th')
    #         main_0 = table_0.find_all('span')
    #         # span_0 = main_0.find('span')

    #         # For first iteration (count==1) append the headers to cate.
    #         if count == 1:
    #             for i in range(len(cate_0)):
    #                 if (i == 5 or i== 6):
    #                     continue
    #                 else:
    #                     cate.append(cate_0[i].text)

    #             date = []
    #             close = []
    #             change = []
    #             percentage_change = []
    #             volume = []
    #             org_volume = []
    #             foreign_volume = []
    #             foreign_count = []
    #             foreign_percentage = []

    #         for i in range(len(main_0)):

    #             if(i%9 == 0):
    #                 date.append(main_0[i].text)
    #             if(i%9 == 1):
    #                 close.append(main_0[i].text)
    #             if(i%9 == 2):
    #                 change.append(main_0[i].text)
    #             if(i%9 == 3):
    #                 percentage_change.append(main_0[i].text)
    #             if(i%9 == 4):
    #                 volume.append(main_0[i].text)
    #             if(i%9 == 5):
    #                 org_volume.append(main_0[i].text)
    #             if(i%9 == 6):
    #                 foreign_volume.append(main_0[i].text)
    #             if(i%9 == 7):
    #                 foreign_count.append(main_0[i].text)
    #             if(i%9 == 8):
    #                 foreign_percentage.append(main_0[i].text)
            
    #         df_data = [date, close, change, percentage_change, volume, org_volume, foreign_volume, foreign_count, foreign_percentage]       
    #         # print(cate)

    #         count += 1
    #     df = pd.DataFrame(columns = cate)
    #     df_data = ['Date', 'Close', 'Change', 'Pct_Change', 'Volume', 'Org_Volume', 'Foreign_Volume', 'Foreign_Count', 'Foreign_Pct'] 
    #     df.columns = df_data
    #     # df['날짜'] = date
    #     # df['종가'] = close
    #     # df['전일비'] = change
    #     # df['등락률'] = percentage_change
    #     # df['거래량'] = volume
    #     # df['순매매량'] = org_volume
    #     # df['순매매량'] = foreign_volume
    #     # df['보유주수'] = foreign_count
    #     # df['보유율'] = foreign_percentage
    #     df['Date'] = date
    #     df['Close'] = close
    #     df['Change'] = change
    #     df['Pct_Change'] = percentage_change
    #     df['Volume'] = volume
    #     df['Org_Volume'] = org_volume
    #     df['Foreign_Volume'] = foreign_volume
    #     df['Foreign_Count'] = foreign_count
    #     df['Foreign_Pct'] = foreign_percentage
    
    #     # df['전일비'] = df['전일비'].map(lambda x: x.lstrip('\n\t').rstrip('\n\t'))
    #     df['Change'] = df['Change'].map(lambda x: x.lstrip('\n\t').rstrip('\n\t'))
    #     # df['등락률'] = df['등락률'].map(lambda x: x.lstrip('\n\t').rstrip('\n\t'))
    #     df['Pct_Change'] = df['Pct_Change'].map(lambda x: x.lstrip('\n\t').rstrip('\n\t'))

        
    #     return df 


    ## Data Cleaning

    # This cell runs the scraper funciton above and scrape the data, and may take a (few) minute(s).

    # df = get_stocks(stock_id,71)

    # # Remove special characters in dataframe
    # df['Date'] = pd.to_datetime(df['Date'])
    # df = df.replace('\,','', regex=True)
    # df = df.replace('\+','', regex=True)
    # # df = df.replace('\-','', regex=True)
    # df = df.replace('\%','', regex=True)

    # # Set index as Date
    # df.set_index(df['Date'], inplace= True)
    # df.drop('Date',axis=1,inplace=True)

    # # df.head()

    # # Fill missing values such as weekends/holidays
    # df = df.resample('D').asfreq()
    # df.sort_values(by=['Date'],ascending=False,inplace=True)
    # df.fillna(method='ffill',inplace=True)

    # stock_file = 'stock_'+ str(stock_id) +'.csv'
    # df.to_csv(str(stock_file))


    # Used an API, because the above scraping method took too long.
    df = web.DataReader(stock_id, 'naver', start='2015-01-01', end=dt.now()).reset_index()
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Fill missing values such as weekends/holidays
    df = df.resample('D').asfreq()
    df.fillna(method='ffill',inplace=True)
    # df.head()

    ## Tweak the KR_IR file
    from KR_IR import get_IR
    df_IR = get_IR()

    ## Clean DJI.csv
    from DJI import get_DJI
    df_DJI = get_DJI()


    ## Clean OIL_WTI.csv
    from WTI import get_WTI
    df_WTI = get_WTI()


    ## Clean USD_KRW_XR.csv 
    from XR import get_XR
    df_XR = get_XR()

    # create clone of df
    df_STK = df

    # All cleaned dataframes. But all dataframes have different shapes. Therefore, must unite into a single dataframe and order it by date.
    # df_DJI.shape
    # df_IR.shape
    # df_WTI.shape
    # df_XR.shape
    # df_STK.shape

    # df_STK.tail()
    start_date = '2015-08-10'
    end_date = '2020-08-10'

    df_DJI = df_DJI[(df_DJI.index >= start_date) & (df_DJI.index <= end_date)]
    df_IR = df_IR[(df_IR.index >= start_date) & (df_IR.index <= end_date)]
    df_WTI = df_WTI[(df_WTI.index >= start_date) & (df_WTI.index <= end_date)]
    df_XR = df_XR[(df_XR.index >= start_date) & (df_XR.index <= end_date)]
    df_STK = df_STK[(df_STK.index >= start_date) & (df_STK.index <= end_date)]

    # print('Shape of DJI: ', df_DJI.shape)
    # print('Shape of IR: ', df_IR.shape)
    # print('Shape of WTI: ', df_WTI.shape)
    # print('Shape of XR: ', df_XR.shape)
    # print('Shape of STK: ', df_STK.shape)


    # Concat all dataframes into one

    df_DJI.columns = ['DJI_Close']
    df_XR.columns = ['XR','XR_Pct_Change']
    df = pd.concat([df_STK, df_DJI,df_IR,df_WTI,df_XR], axis=1)

    # df.head()
    # df.tail()


    df.to_csv('processed_data.csv')

    # df = pd.read_csv('processed_data.csv')
    # df = df.sort_values(by='Date')
    # df = df.reset_index(drop = True)
    return

# preprocessdata('005930')