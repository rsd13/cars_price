import pandas as pd
import os
from data_num import clean_num
from data_cat import clean_cat


PATH_FILE =  os.path.dirname(os.path.abspath(__file__))

def drop_columns(cars):
    """
    función que borrar las columnas que pienso que no son
    importantes
    """

    columns_drop = ["county_fips", "county_name", "state_fips", "state_code", "size", "city"]
    cars= cars.drop(columns=columns_drop, axis=1, inplace=True)

def get_datase(name = "cars_train.csv"):
    """
    Devuelve un dataset del directorio ./../datasets.

    :param name: nombre del fichero .cvs que se quiere abrir
    :return: devuelve el dataset en formato DataFrame
    """
    if isinstance(name, str):
        path_file_dataset = PATH_FILE + "/../datasets/" + name
        return pd.read_csv(path_file_dataset)
    else:
        raise ValueError("La variable 'name' debe ser de tipo string.")

def clean_datos():
    """limpia los datos para su posterior entrenamiento
    """

    # obtengo el directorio del fichero
    cars = get_datase()
    drop_columns(cars)
    clean_num(cars)
    clean_cat(cars)

    cars.to_csv(PATH_FILE + "/../datasets/medium_clean.csv")






