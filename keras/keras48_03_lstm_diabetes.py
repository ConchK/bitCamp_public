from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input, Dropout, LSTM
import numpy as np
from sklearn.datasets import load_diabetes

#1. 데이터
datasets=load_diabetes()
x=datasets.data
y=datasets.target
'''
print(x)
print(x.shape)  #(442, 10)
print(y)
print(y.shape)  #(442,)

print(datasets.feature_names)
#['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
print(datasets.DESCR)
'''
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x,y,
        train_size=0.7, shuffle=True, random_state=123
        )   

from sklearn.preprocessing import MinMaxScaler, StandardScaler
scaler= MinMaxScaler()
# scaler= StandardScaler()

scaler.fit(x_train)
x_train= scaler.transform(x_train)
# x_train= scaler.fit_transform(x_train)    #x범위 만큼의 가중치 생성

x_test= scaler.transform(x_test)

print(x_train.shape, x_test.shape)      #(309, 10) (133, 10)

x_train= x_train.reshape(309,5,2)
x_test= x_test.reshape(133,5,2)


#2. 모델구성

model= Sequential()
model.add(LSTM(units = 40, input_shape= (5,2), activation= 'relu'))
model.add(Dropout(0.5))
model.add(Dense(80, activation= 'relu'))  
model.add(Dense(40,activation= 'relu'))
model.add(Dense(1, activation= 'linear'))
model.summary()


#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

from tensorflow.keras.callbacks import EarlyStopping
earlystopping= EarlyStopping(monitor='val_loss', mode=min, patience=10, restore_best_weights=True, verbose=1)

hist=model.fit(x_train, y_train, epochs=100, batch_size=1,
         validation_split=0.2, callbacks= [earlystopping], verbose=2)

#4. 평가, 예측

loss=model.evaluate(x_test,y_test)  #x_test,y_test 값으로 평가
print('loss :', loss)
y_predict=model.predict(x_test)  #x_test값으로 y_predict 예측
# print('x_test :', x_test)
# print('y_predict :', y_predict)

from sklearn.metrics import mean_squared_error, r2_score
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print('RMSE: ', RMSE(y_test, y_predict))
r2=r2_score(y_test, y_predict)
print('R2: ', r2)

'''
loss : [27759.556640625, 147.6917266845703]
RMSE:  166.61199353881292
R2:  -3.6680532287903844
cnn
loss : [27759.556640625, 147.6917266845703]
RMSE:  166.61199353881292
R2:  -3.6680532287903844
lstm
loss : [4879.6806640625, 58.04718780517578]
RMSE:  69.85470996007172
R2:  0.17943183206897728

'''

