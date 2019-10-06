import re
from data_num import clean_mean

def get_most_frequent(cars, col):
    mode = cars[col].mode()
    cars.loc[cars[col].isnull(), col] = mode[0]


def get_cylinders(col):
    try:
        return int(re.findall("[\d]", col)[0])

    except:
        return None

def transform_cylinders(cars):
    """
    funcion que pasa a int la columna cylinders. Ejemplo= "4 cylyndres" -> 4
    """
    #pongo los electricos a cero
    cars.loc[cars[cars["fuel"] == "electric"].index, 'cylinders'] = 0
    #transformo lo que estan en string a num
    cars["cylinders"] = cars.cylinders.apply(get_cylinders)
    #obtengo la media y la pongo a los que faltan
    clean_mean(cars, "cylinders")


def clean_cat(cars):
    cols_cat = ["cylinders"]
    transform_cylinders(cars)

    cols_freq = ["title_status", "transmission", "fuel"]
    for freq in cols_freq:
        get_most_frequent(cars, freq)

    #lo transformo en unknown porque el modelo y el fabricante no me los puedo inventar
    #ya que hay miles de cada uno
    cols_unknown = ["manufacturer", "make"]

    for col in cols_unknown:
        cars.loc[cars[col].isnull(), col] = 'unknown'
    print(cars.isnull().sum())
