path = "C:/Users/Chao-Hung Cheng/Desktop/Data Science in Education Research/student-behavior.csv"

# 下載檔案
import urllib.request
res = "https://raw.githubusercontent.com/v123582/edu-dataset/main/student-behavior.csv"
urllib.request.urlretrieve(res, path)

# 開檔讀檔
import csv
with open(path) as csvfile:
    rows = list(csv.reader(csvfile))

# 利用 Pandas 將資料讀成 DataFrame
import pandas as pd
df = pd.DataFrame(rows[1:], columns = rows[0])
# print(df['Height(CM)'])
# print(type(df['Height(CM)']))

# 印出資料數量、欄位數量
print(f"資料筆數 {df.shape[0]}")
print(f"欄位數量 {df.shape[1]}")
