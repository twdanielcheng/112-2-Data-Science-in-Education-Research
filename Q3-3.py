path = "C:/Users/Chao-Hung Cheng/Desktop/Data Science in Education Research/student-behavior.csv"

# 下載檔案
import urllib.request
res = "https://raw.githubusercontent.com/v123582/edu-dataset/main/student-behavior.csv"
urllib.request.urlretrieve(res, path)
import io
import requests

import pandas as pd
df = pd.read_csv(io.StringIO(requests.get(res).content.decode('utf-8')))
num_rows, num_columns = df.shape

# object 為類別欄位、非 object 為數值欄位
print(df.dtypes)

