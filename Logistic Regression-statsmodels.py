import pandas as pd
import numpy as np
import statsmodels.api as sma
import csv

df = pd.read_csv('url-train.csv')
tf = pd.read_csv('url-test.csv')

Deptrain = pd.DataFrame(df.result)
Indtrain = sma.add_constant(df[df.columns.difference(['result'])])

Indtest = sma.add_constant(tf[tf.columns.difference(['result'])])

Ir = sma.Logit(Deptrain, Indtrain)

predictedValue = Ir.fit().predict(Indtest)
predictedValue = list(predictedValue)

with open('url-test.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    column = list([row['result'] for row in reader])
    l = len(predictedValue)
    sum = 0
    i = 0
    while i < l:
        if predictedValue[i] < 0.5:
            predictedValue[i] = 0
        else:
            predictedValue[i] = 1
        if predictedValue[i] == int(column[i]):
            sum += 1
        i += 1
    print(sum/i)