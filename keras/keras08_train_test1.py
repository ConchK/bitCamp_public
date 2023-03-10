import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#1.데이터  -train set / test set 분리 
# x=np.array([1,2,3,4,5,6,7,8,9,10])  #(10, )
# y=np.array(range(10))               #(10, )
x_train=np.array([1,2,3,4,5,6,7])   #(7, )
x_test=np.array([8,9,10])   #(3, )  train과 test 행이 달라도 열이 같으면 괜찮음.
y_train=np.array(range(7))   #x,y를 train과 test로 분리할 때 %는 동일하게
y_test=np.array(range(7,10))


#2. 모델구성 
model=Sequential()
model.add(Dense(8, input_dim=1))
model.add(Dense(13))
model.add(Dense(20))
model.add(Dense(30))
model.add(Dense(40))
model.add(Dense(20))
model.add(Dense(10))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mae', optimizer='adam')
model.fit(x_train,y_train, epochs=100, batch_size=1)

#4.평가, 예측
loss=model.evaluate(x_test,y_test)
print('loss :', loss)
result=model.predict([11])
print('[11의 결과 :', result)

'''
결과 :
loss : 0.015483061783015728
[11의 결과 : [[10.021771]]
'''