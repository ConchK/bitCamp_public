import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#1. 데이터
x=np.array([[1,2,3,4,5,6,7,8,9,10],
            [1,1,1,1,2,1.3,1.4,1.5,1.6,1.4],
            [9,8,7,6,5,4,3,2,1,0]])
y=np.array([2,4,6,8,10,12,14,16,18,20])

print(x.shape)  #(3, 10)
print(y.shape)  #(10,) 10개의 스칼라를 가진 베터

x=x.T
print(x.shape)  #(10, 3)

model=Sequential()
model.add(Dense(5,input_dim=3))
model.add(Dense(10))
model.add(Dense(20))
model.add(Dense(30))
model.add(Dense(15))
model.add(Dense(10))
model.add(Dense(1))


model.compile(loss='mae', optimizer='adam')
model.fit(x,y,epochs=200, batch_size=5)

loss=model.evaluate(x,y)
print('loss= ',loss)

result=model.predict([[10,1.4,0]])
print('10,1.4,0의 예측값: ',result)


'''
결과: 
loss=  0.08754456043243408
10,1.4,0의 예측값:  [[20.038979]]
'''