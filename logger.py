import imp
from data_greate import name, surname, number_mobile, description
import pandas as pd 
import numpy as np 
def print_data():
    data = pd.read_csv("phone1.csv")
    data.index += 1
    print(data)
# поиск контакта 

def search_data():
    df = pd.read_csv('phone1.csv')
    print(df)
    a = input('Введите имя для поиска в справочнике: ')
    print(df.loc[df['Name'] == a])
    df.to_csv('phone1.csv', index=False)


# удаление
def delete_data():
    df = pd.read_csv('phone1.csv')
    print(df)
    а = int(input("Впишите порядковый номер абонента из справочника, кого хотите удалить: "))
    df.drop(labels = [а],axis = 0, inplace=True)
    df.to_csv('phone1.csv', index=False)
    print(df)

# добавление нового контакта
def input_data():
    df = pd.DataFrame(
    {"Name": ['vova', 'evgeniy', "kaduk"], 
    "Surname": ['smirnov', 'astronomov', 'marmeladov'], 
    "Number mobile": [13132, 324324, 234324, ], 
    "Description": ['good', 'cool', 'god']})
    df.to_csv('phone1.csv', index=False)
    df = pd.read_csv('phone1.csv')
    df_1 = {}
    pair = {'Name': name(), 'Surname':surname(), 'Number mobile':number_mobile(), 'Description': description()}
    df_1.update(pair)
    df = df.append(df_1, ignore_index=True) 
    print(df)
    df.to_csv('phone1.csv', index=False)

