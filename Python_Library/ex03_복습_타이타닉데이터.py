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

# 파이썬 라이브러리
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# +
# 데이터 불러오기 > population.csv


population = pd.read_csv("./data/population.csv",index_col = "도시")



# -

population

# +
# 원하는 데이터 추출하기
# loc(Location) : 인덱스를 기준으로 행을 추출, '컬럼 이름으로 접근'
# loc[행, 열] -> ㄱ끝 열을 포함하지 않는다. ex) df명.loc[부산 : 인천]
# iloc(Integer Location) : 행 번호를 기준으로 데이터를 추출, '행 번호로 접근'
# iloc[행,열] -> 끝 열을 포함하는
population.loc['부산' : '인천']



# +
# 인천에 2015년도 인구수 행을 추출 > 2925815.0
# loc를 사용

population.loc['인천','2015']
# -

# 부산에서 인천까지의 2020년~2010년까지의 인구 수를 추출
population.iloc[1:3,1:4]

population.iloc[0:3,2:4]

population.loc['부산':'인천','2010']

# ### 그외 함수를 사용하기
#     - count() : 데이터 개수를 세는 함수
#     - values_counts() : 값이 숫자, 문자열, 카테고리 값인 경우에 각각의 값이 나온 횟수를 세는 함수
#     - sort_index() : 인덱스 값을 기준으로 정렬
#     - sort_values() : 데이터 값을 기준으로 정렬
#     - fillna() :  결측치(NaN) 에 원하는 값 지정

# +
# count()
# axis : 축방향
# axis = 0 :  행 축: 위에서 아래로 축 행을 기준으로 작업
# axis = 1 : 열 축: 왼쪽에서 오른쪽로 축 컬럼을 기준으로 작업

population.count(axis = 0)

# +
# 2020년도 특정 컬럼의 카룬트를 세워보자

population['2020'].value_counts()
# -

population.sort_values(by = '2010', ascending = False)
population.sort_values(by = ['지역','2020'], ascending = False)

# +
# 데이터 프레임 형태로 확인하고 싶은면 []안에 []를 쓴다.
population[['2015']]


population.fillna(value = 0)

# +
#testtest
