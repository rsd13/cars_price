def clean_mean(cars, column):
    """
    funcion que limpia una columna del datagrame a través de la media
    :param cars: dataframe a limpiar
    :param column: columba a limpiar
    """

    mean = int(cars[column].mean())
    cars.loc[cars[column].isnull(), column ] = mean

    # asi ocupa menos el dataset
    cars[column] = cars[column].astype(int)

def clean_num(cars):
    """
    funcion que limpia las columnas numeericas
    :return: devuelve el dataset "limpiado" de columnas numericas
    """

    #columnas con nulos enteros (lo se por el estudio hecho previamente en jupyter)
    cols_nulls_int = ["year", "odometer", "weather"]
    for col in cols_nulls_int:
        clean_mean(cars, col)

