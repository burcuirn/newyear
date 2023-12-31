#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:42:01 2023

@author: burcu
"""

#milli piyango tahmini
import pandas as pd
from sklearn.ensemble import RandomForestRegressor




#veri import

veri = pd.read_excel('/Users/burcu/Downloads/Milli Piyango Sonuçları.xlsx')

train_data = veri.head(23)
test_data =veri.tail(1)

#1. NUMARA TAHMİNİ
#bağımsız ve bağımlı değişkenler

x_train = train_data[['Yıl']]
y_train = train_data['1. numara']

x_test = test_data[['Yıl']]
y_test = test_data['1. numara']

model_rf = RandomForestRegressor(n_estimators=700, bootstrap=(True), max_depth=(25), min_samples_leaf=1, min_samples_split=2)  # You can adjust hyperparameters
model_rf.fit(x_train, y_train)

y_pred_rf = model_rf.predict(x_test)
y_pred_rf_int = y_pred_rf.round().astype(int)
print(y_pred_rf)
print(y_pred_rf_int)

# 1. tahmini bağımsız değişkenlere ata
x_test['1. tahmin'] = y_pred_rf_int
tahmin_num=pd.DataFrame()
tahmin_num ['1. tahmin numarası'] = y_pred_rf_int


#2. NUMARA TAHMİNİ
x_train = train_data[['Yıl']]
y_train = train_data['2. numara']

x_test = test_data[['Yıl']]
y_test = test_data['2. numara']

model_rf = RandomForestRegressor(n_estimators=100, bootstrap=(True), max_depth=(25), min_samples_leaf=1, min_samples_split=2)  # You can adjust hyperparameters
model_rf.fit(x_train, y_train)

y_pred_rf = model_rf.predict(x_test)
y_pred_rf_int = y_pred_rf.round().astype(int)
print(y_pred_rf)
print(y_pred_rf_int)

# 2. tahmini bağımsız değişkenlere ata
x_test['2. tahmin'] = y_pred_rf_int
tahmin_num ['2. tahmin numarası'] = y_pred_rf_int


#3. NUMARA TAHMİNİ
x_train = train_data[['Yıl']]
y_train = train_data['3. numara']

x_test = test_data[['Yıl']]
y_test = test_data['3. numara']

model_rf = RandomForestRegressor(n_estimators=100, bootstrap=(True), max_depth=(25), min_samples_leaf=1, min_samples_split=2)  # You can adjust hyperparameters
model_rf.fit(x_train, y_train)

y_pred_rf = model_rf.predict(x_test)
y_pred_rf_int = y_pred_rf.round().astype(int)
print(y_pred_rf)
print(y_pred_rf_int)

# 3. tahmini bağımsız değişkenlere ata
x_test['3. tahmin'] = y_pred_rf_int
tahmin_num ['3. tahmin numarası'] = y_pred_rf_int

#4. NUMARA TAHMİNİ
x_train = train_data[['Yıl']]
y_train = train_data['4. numara']

x_test = test_data[['Yıl']]
y_test = test_data['4. numara']

model_rf = RandomForestRegressor(n_estimators=100, bootstrap=(True), max_depth=(25), min_samples_leaf=1, min_samples_split=2)  # You can adjust hyperparameters
model_rf.fit(x_train, y_train)

y_pred_rf = model_rf.predict(x_test)
y_pred_rf_int = y_pred_rf.round().astype(int)
print(y_pred_rf)
print(y_pred_rf_int)

# 4. tahmini bağımsız değişkenlere ata
x_test['4. tahmin'] = y_pred_rf_int
tahmin_num ['4. tahmin numarası'] = y_pred_rf_int

#5. NUMARA TAHMİNİ
x_train = train_data[['Yıl']]
y_train = train_data['5. numara']

x_test = test_data[['Yıl']]
y_test = test_data['5. numara']

model_rf = RandomForestRegressor(n_estimators=100, bootstrap=(True), max_depth=(25), min_samples_leaf=1, min_samples_split=2)  # You can adjust hyperparameters
model_rf.fit(x_train, y_train)

y_pred_rf = model_rf.predict(x_test)
y_pred_rf_int = y_pred_rf.round().astype(int)
print(y_pred_rf)
print(y_pred_rf_int)

# 5. tahmini bağımsız değişkenlere ata
x_test['5. tahmin'] = y_pred_rf_int
tahmin_num ['5. tahmin numarası'] = y_pred_rf_int

#6. NUMARA TAHMİNİ
x_train = train_data[['Yıl']]
y_train = train_data['6. numara']

x_test = test_data[['Yıl']]
y_test = test_data['6. numara']

model_rf = RandomForestRegressor(n_estimators=100, bootstrap=(True), max_depth=(25), min_samples_leaf=1, min_samples_split=2)  # You can adjust hyperparameters
model_rf.fit(x_train, y_train)

y_pred_rf = model_rf.predict(x_test)
y_pred_rf_int = y_pred_rf.round().astype(int)
print(y_pred_rf)
print(y_pred_rf_int)

# 6. tahmini bağımsız değişkenlere ata
x_test['6. tahmin'] = y_pred_rf_int
tahmin_num ['6. tahmin numarası'] = y_pred_rf_int

#7. NUMARA TAHMİNİ
x_train = train_data[['Yıl']]
y_train = train_data['7. numara']

x_test = test_data[['Yıl']]
y_test = test_data['7. numara']

model_rf = RandomForestRegressor(n_estimators=100, bootstrap=(True), max_depth=(25), min_samples_leaf=1, min_samples_split=2)  # You can adjust hyperparameters
model_rf.fit(x_train, y_train)

y_pred_rf = model_rf.predict(x_test)
y_pred_rf_int = y_pred_rf.round().astype(int)
print(y_pred_rf)
print(y_pred_rf_int)

# 7. tahmini bağımsız değişkenlere ata
x_test['7. tahmin'] = y_pred_rf_int
tahmin_num ['7. tahmin numarası'] = y_pred_rf_int



