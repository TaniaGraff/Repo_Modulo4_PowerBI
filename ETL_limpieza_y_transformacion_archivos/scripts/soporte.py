#Importo librerías
import pandas as pd
import numpy as np


import os
import sys
sys.path.append("../")

import warnings
warnings.filterwarnings("ignore")

"""Creo función para abrir los csv y convertir en DF.
"""
def leer_csv(ruta_csv):
    df= pd.read_csv(ruta_csv)
    pd.set_option('display.max_columns', None)
    return df

"""Creo función para ver la info de los csv.
"""
def info_df(df):
    return df.info()

"""Creo función para borrar columnas del DF.
"""
columnas_a_borrar = ['x_etrs89', 'y_etrs89', 'tipus_element', 'cat_especie_id', 'data_plantacio', 'tipus_aigua', 'tipus_reg', 'geom', 'catalogacio']
def borrar_columnas(df):
    return df.drop(columns=columnas_a_borrar, inplace=True)

"""Creo función para ver las columnas del DF.
"""
def ver_columnas(df):
    return df.columns

"""Creo función para igualar mayúsculas y minúsculas
"""
def normalizar_y_renombrar(df):
    columnas_a_normalizar = ['categoria_arbrat', 'nom_barri', 'nom_districte', 'nom_castella', 'nom_catala', 'nom_cientific']
    
    for columna in columnas_a_normalizar:
        # Aplicar str.capitalize() directamente
        df[columna] = df[columna].str.title()
    
    return df

"""Creamos función para ver porcentaje de nulos categóricos.
"""
def nulos_categoricos(df):
    nulos_cat = df[df.columns[df.isnull().any()]].select_dtypes(include="object").columns.tolist()
    return nulos_cat

"""Creo función para ver cómo se distribuyen los valores en esas columnas con nulos categóricos.
"""
def distribucion_categorias_con_nulos(df):
    nulos_cat = nulos_categoricos(df)
    for col in nulos_cat:
        print(f"La distribución de las categorías para la columna {col.upper()}:")
        print(df[col].value_counts() / df.shape[0] * 100) 
        print("........................")

"""Creo función para imputar los nulos categóricos.
"""
def imputacion_nulos_categoricos(df):
    columnas_desconocido = ['espai_verd', 'nom_castella', 'nom_catala', 'categoria_arbrat']
    
    for columna in columnas_desconocido:
        df[columna] = df[columna].fillna('Desconegut')
    
    print("Después del reemplazo usando 'fillna', quedan los siguientes nulos:")
    print(df[columnas_desconocido].isnull().sum())

"""Creo función para ver las cinco primeras filas del DF y comprobar que todo esté correcto antes de guardar.
"""
def primeras_filas(df):
    return df.head()

"""Creo función para guardar el DF
"""
def guardar_df(df, nombre_archivo):
    ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'data', 'output_data', nombre_archivo + '.csv')
    df.to_csv(ruta_archivo, index=False, encoding='utf-8')
    print(f"El DataFrame se ha guardado en {ruta_archivo}")


""""""""""""""""""""""""""""""


"""Creo función para borrar columnas del DF Densitat.
"""
columnas_a_borrar_densidad = ['Any', 'Densitat neta (hab/ha)']
def borrar_columnas_densidad(df):
    return df.drop(columns=columnas_a_borrar_densidad, inplace=True)


"""Creo función para igualar nombres columnas DF Densitat.
"""
def renombrar_columnas_densidad(df):
    columnas_a_renombrar_densidad = {
        'Codi_Districte': 'codi_districte',
        'Nom_Districte': 'nom_districte',
        'Codi_Barri': 'codi_barri',
        'Nom_Barri': 'nom_barri',
        'Població': 'poblacio',
        'Superfície (ha)': 'superficie(ha)',
        'Superfície Residencial (ha)': 'superficie_residencial(ha)',
        'Densitat (hab/ha)': 'densitat(hab/ha)'
    }
    df.rename(columns=columnas_a_renombrar_densidad, inplace=True)


"""Creo función para ver valores únicos columa nom_barri.
"""
def valores_barri(df, columna):
    return df[columna].unique()

"""Creo función para igualar mayúsculas y minúsculas valores columna nom_barris
"""
def normalizar_y_renombrar_densidad(df):
    columnas_a_normalizar_densidad = ['nom_barri']
    
    for columna in columnas_a_normalizar_densidad:
        # Aplicar str.capitalize() directamente
        df[columna] = df[columna].str.title()


""""""""""""""""""""""""""""""

"""Creo función para borrar columnas del DF Renta.
"""
columnas_a_borrar_renta = ['Any', 'Seccio_Censal']
def borrar_columnas_renta(df):
    return df.drop(columns=columnas_a_borrar_renta, inplace=True)

"""Creo función para igualar nombres columnas DF Renta.
"""
def renombrar_columnas_renta(df):
    columnas_a_renombrar_renta = {
        'Codi_Districte': 'codi_districte',
        'Nom_Districte': 'nom_districte',
        'Codi_Barri': 'codi_barri',
        'Nom_Barri': 'nom_barri',
        'Import_Euros': 'import_euros'
    }
    df.rename(columns=columnas_a_renombrar_renta, inplace=True)

"""Creo función para cambiar el nombre de uno de los distritos.
"""
def renombrar_distrito_renta(df, columna):
    df[columna] = df[columna].replace({
        'Sarrià-St. Gervasi': 'Sarrià-Sant Gervasi'
    })
    return df


"""Creo función para igualar mayúsculas y minúsculas valores columna nom_barris
"""
def normalizar_y_renombrar_renta(df):
    columnas_a_normalizar_renta = ['nom_barri']
    
    for columna in columnas_a_normalizar_renta:
        # Aplicar str.capitalize() directamente
        df[columna] = df[columna].str.title()



""""""""""""""""""""""""""""""

"""Creo función para igualar nombres columnas DF Distritos.
"""
def renombrar_columnas_distritos(df):
    columnas_a_renombrar_renta = {
        'Codi_Districte': 'codi_districte'
    }
    df.rename(columns=columnas_a_renombrar_renta, inplace=True)


""""""""""""""""""""""""""""""

"""Creo funciones para abrir y leer el csv de PARQUES Y JARDINES, teniendo en cuenta la codificación que tiene.
"""
import chardet

def detectar_codificacion(ruta_archivo):
    with open(ruta_archivo, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def leer_csv(ruta_archivo):
    encoding = detectar_codificacion(ruta_archivo)
    df = pd.read_csv(ruta_archivo, encoding=encoding, sep=',', on_bad_lines='skip')
    
    return df

"""Creo función para limpiar el DF de las columnas y filas nulas que ha podido generar tras la apertura.
"""
def limpiar_dataframe(df):
    df = df.dropna(axis=1, how='all') 
    df = df.dropna(axis=0, how='all')
    return df


"""Creo función para borrar columnas del DF Parques y Jardines.
"""
columnas_a_borrar_parques_y_jardines = ['institution_id', 'institution_name', 'modified', 'addresses_start_street_number', 'addresses_end_street_number', 'addresses_main_address',
                           'values_id', 'values_attribute_id', 'values_category', 'values_attribute_name', 'values_value', 'values_outstanding',
                            'values_description']
def borrar_columnas_parques_y_jardines(df):
    return df.drop(columns=columnas_a_borrar_parques_y_jardines, inplace=True)

"""Creo función para igualar mayúsculas y minúsculas valores en diferentes columnas.
"""
def normalizar_y_renombrar_parques_y_jardines(df):
    columnas_a_normalizar_parques_y_jardines = ['addresses_road_name', 'addresses_neighborhood_name', 'addresses_district_name', 'addresses_town']
    
    for columna in columnas_a_normalizar_parques_y_jardines:
        # Aplicar str.capitalize() directamente
        df[columna] = df[columna].str.title()

"""Creo función para eliminar duplicados del ID de parques y jardines
"""
def eliminar_duplicados(df, columna):
    df.drop_duplicates(subset=columna, inplace=True)
    

""""""""""""""""""""""""""""""
"""Creo función para igualar nombres columnas contaminantes.
"""
def renombrar_columnas_contaminantes(df):
    columnas_a_renombrar_contaminantes = {
        'Codi_Contaminant': 'codi_contaminant', 'Desc_Contaminant':'desc_contaminant', 'Unitats':'unitats'
    }
    df.rename(columns=columnas_a_renombrar_contaminantes, inplace=True)


""""""""""""""""""""""""""""""
"""Creo función para igualar nombres columnas contaminación.
"""
def renombrar_columnas_contaminacion(df):
    columnas_a_renombrar_contaminacion = {
        'Estacio': 'estacio', 'Codi_districte':'codi_districte', 'Nom_districte':'nom_districte', 'Codi_barri':'codi_barri', 'Nom_barri':'nom_barri', 'Clas_1':'clas_1', 'Clas_2':'clas_2', 
        'Codi_Contaminant':'codi_contaminant', 'Longitud':'longitud', 'Latitud':'latitud',}
    df.rename(columns=columnas_a_renombrar_contaminacion, inplace=True)

"""Creo función para cambiar el nombre de varios distritos.
"""
def renombrar_distrito_contaminacion(df, columna):
    df[columna] = df[columna].replace({
        'Gracia': 'Gràcia', 'Sant Marti':'Sant Martí', 'Sants-Montjuic':'Sants-Montjuïc', 'Horta-Guinardo':'Horta-Guinardó'})
    return df

"""Creo función para cambiar el código de varios distritos.
"""

def actualizar_eixample(df):
    # Asegurarse de que la columna codi_districte sea del tipo correcto
    df['codi_districte'] = pd.to_numeric(df['codi_districte'], errors='coerce').astype('Int64')

    # Cambiar el valor de codi_districte y nom_districte para 'Eixample'
    df.loc[df['nom_districte'] == 'Eixample', 'codi_districte'] = 2
    
    return df
