import pandas as pd 
log = pd.read_csv("log.csv")  
log = log.dropna()  
log.columns = ['user_id', 'time', 'bet', 'win']  
log['time'] = log['time'].apply(lambda x: x[1:])  
log['time'] = pd.to_datetime(log['time'])  
# Пропущенная строка  
log['time'].head()