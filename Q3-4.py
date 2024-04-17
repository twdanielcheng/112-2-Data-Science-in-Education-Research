import urllib.request
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import io

path = "C:/Users/Chao-Hung Cheng/Desktop/Data Science in Education Research/student-behavior.csv"

# 下載檔案
res = "https://raw.githubusercontent.com/v123582/edu-dataset/main/student-behavior.csv"
urllib.request.urlretrieve(res, path)

# 讀取資料
df = pd.read_csv(io.StringIO(requests.get(res).content.decode('utf-8')))
df_encoded = df.apply(lambda x: x.factorize()[0])

correlation_matrix = df_encoded.corr()

plt.figure(figsize=(20, 16))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Matrix")
plt.savefig("image.jpg")
plt.show()
