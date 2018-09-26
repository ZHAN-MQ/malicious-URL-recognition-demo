import pandas as pd
import numpy as np
import statsmodels.api as sma

df = pd.read_csv('result.csv')

Dep = pd.DataFrame(df.result)
print(Dep)

Ind = sma.add_constant(df[df.columns.difference(['result'])])
print(Ind)

Indtrain = Ind.iloc[0:1000]
Deptrain = Dep.iloc[0:1000]
Indtest = Ind.tail(10)

print(Indtrain)
print(Deptrain)
print(Indtest)

Ir = sma.Logit(Deptrain, Indtrain)
result = Ir.fit()

predictedValue['predict'] = Ir.fit.predict(Indtest)
compare=pd.DataFrame({'predictedValue':predictedValue,'actualValue':Dep.tail(10)})
print(compare)