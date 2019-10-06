


def clean_year(cars):
    """
    funcion que limpia de nulos los años
    :param cars:  dataset
    :return: devuelve el dataframe con el año limpiado
    """
    mean = int(cars.year.mean())
    cars.loc[cars['year'].isnull(), 'year'] = mean

    #asi ocupa menos el dataset
    cars["year"] = cars["year"].astype(int)



def clean_num(cars):
    """
    funcion que limpia las columnas numeericas
    :return: devuelve el dataset "limpiado" de columnas numericas
    """

    #columnas con nulos enteros (lo se por el estudio hecho previamente en jupyter)
    cols_nulls_int = ["year", "make", "cylinders", "county_fips", "weather", "state_fips"]

    clean_year(cars)
    print(cars.year.dtypes)
