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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# +
# 데이터 불러오기 > hr-info.csv
# hr 변수에 저장

hr =  pd.read_csv('./data/hr-info.csv',encoding = 'EUC-KR')
# -

#인덱스를 1부터 시작하도록 설정
# 1 ~ len(hr) + 1
hr.index = range(1,len(hr) + 1)

hr.index.name = 'No'


hr

# +
# SERVICE_YEAR : 근속 연수
# 최대 근속 연수 구하기 : max()

print(hr.loc[:,'SERVICE_YEAR'].max())


# 최소 근속 연수 구하기 : min()
print(hr.loc[:,'SERVICE_YEAR'].min())

# +
# 직원의 EID, ENAME ,EDU_LEVEL, SALARY 컬럼의 정보를 추츌해서 'data'라는 변수에 저장

data = hr.loc[:,['EID' , 'ENAME','EDU_LEVEL','SALARY']]

# -

# 데이터 확인 
data.shape
data.ndim

# +
# 직원들의 굥육 수준의 데이터를 확인
# data['EDU_LEVEL'].value_counts()

data.value_counts('EDU_LEVEL')
# -

data[data.loc[:,'EDU_LEVEL'] == '박사 학위']['SALARY']

# +
baksa =  data[data['EDU_LEVEL'] == '박사 학위']

print('박사 :',baksa['SALARY'].mean())
# -

# 교육 수준이 박사학위에 해당하는 직원들의 평균 급여를 구하기
data[data.loc[:,'EDU_LEVEL'] == '박사 학위']['SALARY'].sum() / len(data[data.loc[:,'EDU_LEVEL'] == '박사 학위'])

# +
edu_unique = data['EDU_LEVEL'].unique()

# 교육 수준별 평균 급여를 구하기

for item in edu_unique:
    print(f'{item} :', data[data['EDU_LEVEL'] == item]['SALARY'].mean())
        
# 반복문을 통해서 구해보자
# -

# ### Group by()
# - 데이터를 그룹화하여 집계를 내는 것
# - 분할 / 반영 / 결합
# - 빅데이터를 처리하기 위해 사용하는 방법

# +
# 교육 수준별 급여의 평균을 group by
# 분할
hr['EDU_LEVEL'].unique()
# 반영
# 1) 교육 수준이 고등학교 졸업인 직원의 평균 급여
hi_sal_mean = data[data['EDU_LEVEL'] == '고등학교 졸업']['SALARY'].mean()

baksa_sal_mean = data[data['EDU_LEVEL'] == '박사 학위']['SALARY'].mean()
# 결합

pd.DataFrame({'교육수준' : ['고등학교 졸업','박사 학위'], '평균' : [hi_sal_mean, baksa_sal_mean]})

# +
# group by() 활용


hr.groupby(by = 'EDU_LEVEL')['SALARY'].mean()

# +
# agg() 여러 함수들을 한번에 적용 하는 것
# -> 다야한 통계적 요약을 할 수 있는 group by() 사용하는 함수이다.

# 교육수준과 성별에 따른 평균, 최대,최소,중앙값에 대한 급여를 확인하기
hr.head(3)

hr.groupby(by = ['EDU_LEVEL', 'GENDER'])['SALARY'].mean()
hr.groupby(by = ['EDU_LEVEL', 'GENDER'])['SALARY'].max()

hr.groupby(by = ['EDU_LEVEL', 'GENDER'])['SALARY'].median()


hr.groupby(by = ['EDU_LEVEL', 'GENDER'])['SALARY'].agg(['mean','max','min','median'])
