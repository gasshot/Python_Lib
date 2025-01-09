# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # 미니프로젝트 샘플자료
# 1. 필요한 라이브러리 목록
# <ol>
#     <li>데이터베이스: cx_Oracle</li>
#     <li>서버: flask</li>
#     <li>분석: numpy, pandas, matplotlib, seaborn</li>
# </ol>
#

# !pip install flask

# +
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from flask import * 

# +
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page')
def page():
    no = request.args.get('name', type=str)
    print(no)
    return render_template('page'+no+'.html')

@app.route('/result')
def result():
    return render_template('index.html')

app.run(host='127.0.0.1', port=5000)
# -

# # 워드클라우드 이미지 저장

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

with open('대한민국헌법.txt', 'r', encoding='utf-8') as f:
    text = f.read()

text

wc = WordCloud(background_color='white', font_path='C:/Windows/Fonts/malgunbd.ttf').generate(text)

plt.figure(figsize=(12,8))
plt.imshow(wc)
plt.axis('off')
plt.savefig('./static/wordcloud.jpg')

# # 그래프 이미지 저장 

# +
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)                # nrows=2, ncols=1, index=1
plt.plot(x1, y1, 'o-')
plt.title('1st Graph')
plt.xlabel('hor_label_name')
plt.ylabel('ver_label_name')

plt.subplot(2, 1, 2)                # nrows=2, ncols=1, index=2
plt.plot(x2, y2, '.-')
plt.title('2nd Graph')
plt.xlabel('hor_label_name')
plt.ylabel('ver_label_name')

plt.tight_layout()
# plt.show()
plt.savefig('./static/graph.jpg')
