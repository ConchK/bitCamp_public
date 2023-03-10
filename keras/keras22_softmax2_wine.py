from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split


#1. 데이타
datasets= load_wine()
x= datasets.data
y= datasets.target

print(x.shape, y.shape)     #(178, 13) (178,)
print(y)
print(np. unique(y))    #y에 대한 유니크한 값이 나온다? > [0 1 2]  >y는 0,1,2  > y 값의 종류는 3개  > (178,3) 라는 의미
print(np. unique(y, return_counts=True))    #array([59, 71, 48] : 0이 59개, 1이 71개, 2가 48개

from tensorflow.keras.utils import to_categorical    
y= to_categorical(y)
print(y)
print(y.shape)   #(178, 3)

x_train, x_test, y_train, y_test= train_test_split(
    x, y, shuffle=True,  #False의 문제점은 shuffle이 되지 않음. 
                        #True의 문제점은 특정 class를 제외할 수 없음.-데이터를 수집하다 보면 균형이 안맞는 경우.
                        #회귀는 데이터가 수치라서 상관 없음.
    stratify=y,     # y : yes  / 수치가 한 쪽으로 치우치는 걸 방지. y의 데이터가 분류형일 때만 가능.
    random_state=333,
    test_size=0.2
)
print(y_train)
print(y_test)

#2. 모델구성
model=Sequential()
model.add(Dense(5, activation='relu', input_shape=(13,)))   #or input_dim=4   
model.add(Dense(90,activation='sigmoid'))
model.add(Dense(150,activation='relu'))
model.add(Dense(90,activation='relu'))
model.add(Dense(40,activation='relu'))
model.add(Dense(20,activation='linear'))
model.add(Dense(3,activation='softmax'))  

#3. 컴파일, 훈련         
model.compile(loss='categorical_crossentropy', optimizer='adam',
                metrics=['accuracy'])

from tensorflow.keras.callbacks import EarlyStopping   
earlystopping= EarlyStopping(monitor='val_loss', mode='min', patience=10, restore_best_weights=True, verbose=1)  

model.fit(x_train, y_train, epochs=200, batch_size=5, 
            validation_split=0.2, verbose=1, callbacks=[earlystopping])

#4. 평가, 예측
loss, accuracy= model.evaluate(x_test, y_test)
print('loss : ', loss)
print('accuracy : ', accuracy)

from sklearn.metrics import accuracy_score
import numpy as np
y_predict= model.predict(x_test)
y_predict=np.argmax(y_predict, axis=1)    #가장 큰 위치값을 찾아냄
print("y_pred(예측값) : ",y_predict)

y_test= np.argmax(y_test, axis=1)
print("y_test(원래값) : ",y_test)  

acc= accuracy_score(y_test, y_predict)
print("accuracy_score : ",acc)

'''
loss :  0.2900731861591339
accuracy :  0.9166666865348816
y_pred(예측값) :  [1 0 1 0 1 1 2 0 0 1 1 1 2 0 2 1 2 0 1 0 1 2 0 0 0 0 0 2 2 2 2 2 2 0 2 1]
y_test(원래값) :  [1 0 1 0 1 1 1 0 0 1 1 1 2 0 2 1 2 1 1 0 1 2 0 0 0 0 0 2 2 2 1 2 2 0 2 1]
accuracy_score :  0.9166666666666666
'''