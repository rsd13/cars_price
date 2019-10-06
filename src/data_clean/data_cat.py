import re

def transform_cylinders(cars):
    """
    funcion que pasa a int la columna cylinders. Ejemplo= "4 cylyndres" -> 4
    """


    #recupero los que no son nan
    cars_notnull_cylindres = cars[cars["cylinders"].notnull()]

    




def clean_cat(cars):
    cols_cat = ["cylinders"]
    transform_cylinders(cars)

