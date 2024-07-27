import pandas as pd
import yfinance as yf

# Función para convertir valores grandes a millones
def to_millions(value):
    if value == 'N/A':
        return value
    return value / 1_000_000 if value else 'N/A'

# Función para obtener los datos fundamentales
def get_fundamentals(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    fundamentals = {
        'Ticker': ticker,
        'Market Cap (M)': to_millions(info.get('marketCap', 'N/A')),
        'Enterprise Value (M)': to_millions(info.get('enterpriseValue', 'N/A')),
        'Trailing P/E': info.get('trailingPE', 'N/A'),
        'Forward P/E': info.get('forwardPE', 'N/A'),
        'PEG Ratio': info.get('pegRatio', 'N/A'),
        'Price to Book': info.get('priceToBook', 'N/A'),
        'Price to Sales': info.get('priceToSalesTrailing12Months', 'N/A'),
        'Dividend Yield': info.get('dividendYield', 'N/A'),
        'Earnings Per Share (EPS)': info.get('trailingEps', 'N/A'),
        'Revenue (M)': to_millions(info.get('totalRevenue', 'N/A')),
        'Gross Profit (M)': to_millions(info.get('grossProfits', 'N/A')),
        'EBITDA (M)': to_millions(info.get('ebitda', 'N/A')),
        'Net Income (M)': to_millions(info.get('netIncomeToCommon', 'N/A')),
        'Debt to Equity': info.get('debtToEquity', 'N/A'),
        'Current Ratio': info.get('currentRatio', 'N/A'),
        'Quick Ratio': info.get('quickRatio', 'N/A'),
        'auditRisk': info.get('auditRisk', 'N/A'),
        'boardRisk': info.get('boardRisk', 'N/A'),
        'compensationRisk': info.get('compensationRisk', 'N/A'),
        'shareHolderRightsRisk': info.get('shareHolderRightsRisk', 'N/A'),
        'overallRisk': info.get('overallRisk', 'N/A'),
        'governanceEpochDate': info.get('governanceEpochDate', 'N/A'),
        'compensationAsOfEpochDate': info.get('compensationAsOfEpochDate', 'N/A'),
        'irWebsite': info.get('irWebsite', 'N/A'),
        'maxAge': info.get('maxAge', 'N/A'),
        'priceHint': info.get('priceHint', 'N/A'),
        'previousClose': info.get('previousClose', 'N/A'),
        'open': info.get('open', 'N/A'),
        'dayLow': info.get('dayLow', 'N/A'),
        'dayHigh': info.get('dayHigh', 'N/A'),
        'regularMarketPreviousClose': info.get('regularMarketPreviousClose', 'N/A'),
        'regularMarketOpen': info.get('regularMarketOpen', 'N/A'),
        'regularMarketDayLow': info.get('regularMarketDayLow', 'N/A'),
        'regularMarketDayHigh': info.get('regularMarketDayHigh', 'N/A'),
        'beta': info.get('beta', 'N/A'),
        'volume': info.get('volume', 'N/A'),
        'regularMarketVolume': info.get('regularMarketVolume', 'N/A'),
        'averageVolume': info.get('averageVolume', 'N/A'),
        'averageVolume10days': info.get('averageVolume10days', 'N/A'),
        'averageDailyVolume10Day': info.get('averageDailyVolume10Day', 'N/A'),
        'bid': info.get('bid', 'N/A'),
        'ask': info.get('ask', 'N/A'),
        'bidSize': info.get('bidSize', 'N/A'),
        'askSize': info.get('askSize', 'N/A'),
        'fiftyTwoWeekLow': info.get('fiftyTwoWeekLow', 'N/A'),
        'fiftyTwoWeekHigh': info.get('fiftyTwoWeekHigh', 'N/A'),
        'fiftyDayAverage': info.get('fiftyDayAverage', 'N/A'),
        'twoHundredDayAverage': info.get('twoHundredDayAverage', 'N/A'),
        'currency': info.get('currency', 'N/A'),
        'profitMargins': info.get('profitMargins', 'N/A'),
        'floatShares': info.get('floatShares', 'N/A'),
        'sharesOutstanding': info.get('sharesOutstanding', 'N/A'),
        'sharesShort': info.get('sharesShort', 'N/A'),
        'sharesShortPriorMonth': info.get('sharesShortPriorMonth', 'N/A'),
        'sharesShortPreviousMonthDate': info.get('sharesShortPreviousMonthDate', 'N/A'),
        'dateShortInterest': info.get('dateShortInterest', 'N/A'),
        'sharesPercentSharesOut': info.get('sharesPercentSharesOut', 'N/A'),
        'heldPercentInsiders': info.get('heldPercentInsiders', 'N/A'),
        'heldPercentInstitutions': info.get('heldPercentInstitutions', 'N/A'),
        'shortRatio': info.get('shortRatio', 'N/A'),
        'shortPercentOfFloat': info.get('shortPercentOfFloat', 'N/A'),
        'impliedSharesOutstanding': info.get('impliedSharesOutstanding', 'N/A'),
        'bookValue': info.get('bookValue', 'N/A'),
        'lastFiscalYearEnd': info.get('lastFiscalYearEnd', 'N/A'),
        'nextFiscalYearEnd': info.get('nextFiscalYearEnd', 'N/A'),
        'mostRecentQuarter': info.get('mostRecentQuarter', 'N/A'),
        'earningsQuarterlyGrowth': info.get('earningsQuarterlyGrowth', 'N/A'),
        'trailingEps': info.get('trailingEps', 'N/A'),
        'forwardEps': info.get('forwardEps', 'N/A'),
        'lastSplitFactor': info.get('lastSplitFactor', 'N/A'),
        'lastSplitDate': info.get('lastSplitDate', 'N/A'),
        'enterpriseToRevenue': info.get('enterpriseToRevenue', 'N/A'),
        'enterpriseToEbitda': info.get('enterpriseToEbitda', 'N/A'),
        '52WeekChange': info.get('52WeekChange', 'N/A'),
        'SandP52WeekChange': info.get('SandP52WeekChange', 'N/A'),
        'exchange': info.get('exchange', 'N/A'),
        'quoteType': info.get('quoteType', 'N/A'),
        'underlyingSymbol': info.get('underlyingSymbol', 'N/A'),
        'shortName': info.get('shortName', 'N/A'),
        'longName': info.get('longName', 'N/A'),
        'firstTradeDateEpochUtc': info.get('firstTradeDateEpochUtc', 'N/A'),
        'timeZoneFullName': info.get('timeZoneFullName', 'N/A'),
        'timeZoneShortName': info.get('timeZoneShortName', 'N/A'),
        'uuid': info.get('uuid', 'N/A'),
        'messageBoardId': info.get('messageBoardId', 'N/A'),
        'gmtOffSetMilliseconds': info.get('gmtOffSetMilliseconds', 'N/A'),
        'currentPrice': info.get('currentPrice', 'N/A'),
        'targetHighPrice': info.get('targetHighPrice', 'N/A'),
        'targetLowPrice': info.get('targetLowPrice', 'N/A'),
        'targetMeanPrice': info.get('targetMeanPrice', 'N/A'),
        'targetMedianPrice': info.get('targetMedianPrice', 'N/A'),
        'recommendationMean': info.get('recommendationMean', 'N/A'),
        'recommendationKey': info.get('recommendationKey', 'N/A'),
        'numberOfAnalystOpinions': info.get('numberOfAnalystOpinions', 'N/A'),
        'totalCash': to_millions(info.get('totalCash', 'N/A')),
        'totalCashPerShare': info.get('totalCashPerShare', 'N/A'),
        'totalDebt': to_millions(info.get('totalDebt', 'N/A')),
        'quickRatio': info.get('quickRatio', 'N/A'),
        'currentRatio': info.get('currentRatio', 'N/A'),
        'totalRevenue': to_millions(info.get('totalRevenue', 'N/A')),
        'debtToEquity': info.get('debtToEquity', 'N/A'),
        'revenuePerShare': info.get('revenuePerShare', 'N/A'),
        'returnOnAssets': info.get('returnOnAssets', 'N/A'),
        'returnOnEquity': info.get('returnOnEquity', 'N/A'),
        'freeCashflow': to_millions(info.get('freeCashflow', 'N/A')),
        'operatingCashflow': to_millions(info.get('operatingCashflow', 'N/A')),
        'earningsGrowth': info.get('earningsGrowth', 'N/A'),
        'revenueGrowth': info.get('revenueGrowth', 'N/A'),
        'grossMargins': info.get('grossMargins', 'N/A'),
        'ebitdaMargins': info.get('ebitdaMargins', 'N/A'),
        'operatingMargins': info.get('operatingMargins', 'N/A'),
        'financialCurrency': info.get('financialCurrency', 'N/A'),
        'trailingPegRatio': info.get('trailingPegRatio', 'N/A')
    }
    return fundamentals

# Obtener la lista de empresas del S&P 500 desde Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
table = pd.read_html(url, header=0)
df = table[0]

# Recopilar datos de todas las empresas del S&P 500
fundamental_data = []
for ticker in df['Symbol']:
    data = get_fundamentals(ticker)
    fundamental_data.append(data)

# Crear un DataFrame con los datos recopilados
fundamental_df = pd.DataFrame(fundamental_data)

# Exportar los datos a un archivo Excel
fundamental_df.to_excel('SP500_Fundamentals1.xlsx', index=False)

print("Datos fundamentales del S&P 500 exportados a 'SP500_Fundamentals.xlsx'")
