import soporte

print('_____________     FASE 1. EXPLORACIÓN INICIAL Y LIMPIEZA DE DATOS     __________________')

print('________  APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME ARBOLADO PARQUES DE BCN   __________')

#Llamo a la función de leer el csv de los parques.
df_parques = soporte.leer_csv('../data/input_data/2021_4T_OD_Arbrat_Parcs_BCN.csv')
df_parques
print('Las 5 primeras filas del DataFrame del ARBOLADO DE LOS PARQUES DE BCN son:\n')
print(df_parques.head())
print('.....................................................')

#Llamo a la función para ver la info del csv de los parques.
print('La INFORMACIÓN del DataFrame del ARBOLADO DE LOS PARQUES DE BCN es:\n')
soporte.info_df(df_parques)
print('.....................................................')

#LLamo a la función para borrar columnas.
soporte.borrar_columnas(df_parques)

#Llamo a la función para eliminar las columnas que sé que no voy a utilizar.
print('Las COLUMNAS del DataFrame del ARBOLADO DE LOS PARQUES DE BCN son:\n')
print(soporte.ver_columnas(df_parques))
print('.....................................................')

#Llamo a la función para normalizar los valores de todas las columnas.
soporte.normalizar_y_renombrar(df_parques)

print('____________________________      GESTIÓN NULOS      _______________________________')

#Llamo a la función para ver porcentaje nulos categóricos
print('Las columnas con NULOS CATEGÓRICOS son:\n')
soporte.nulos_categoricos(df_parques)
print('.....................................................')

#Llamo a la función para ver cómo se distribuyen los valores en esas columnas con nulos categóricos.
soporte.distribucion_categorias_con_nulos(df_parques)

#Llamo a la función para imputar a la categoría desconocido los nulos categóricos.
soporte.imputacion_nulos_categoricos(df_parques)

#Llamo a la función para ver las cinco primeras filas del DF.
print(soporte.primeras_filas(df_parques))
print('.....................................................\n')

#Llamo a la función para guardar el DF como un archivo .csv limpio.
soporte.guardar_df(df_parques, 'parques_barcelona')

print('__________________________________________________________________________________________')

print('________  APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME DENSIDAD DE POBLACIÓN BCN   __________')

#Llamo a la función de leer el csv de la densidad de población.
df_densidad_poblacion = soporte.leer_csv('../data/input_data/2021_densitat.csv')
df_densidad_poblacion
print('Las 5 primeras filas del DataFrame de la DENSIDAD DE POBLACIÓN DE BCN son:\n')
print(df_densidad_poblacion.head())
print('.....................................................')

#Llamo a la función para ver la info del csv de la densidad de población.
print('La INFORMACIÓN del DataFrame de la DENSIDAD DE POBLACIÓN DE BCN es:\n')
soporte.info_df(df_densidad_poblacion)
print('.....................................................')

#Llamo a la función para borrar las columnas del DF de la densidad de población.
soporte.borrar_columnas_densidad(df_densidad_poblacion)

#Llamo a la función para renombrar las columnas del DF de la densidad de población.
soporte.renombrar_columnas_densidad(df_densidad_poblacion)

#Llamo a la función para ver las columnas del DF de la densidad de población.
print(soporte.ver_columnas(df_densidad_poblacion))
print('.....................................................')

#Llamo a la función para normalizar los valores de la columna nom_barri del DF de la densidad de población.
soporte.normalizar_y_renombrar_densidad(df_densidad_poblacion)

#Llamo a la función para ver los valores únicos de la columna nom_barri del DF de la densidad de población.
print("Los Valores únicos en 'nom_barri' del DF DENSIDAD son:\n")
print(soporte.valores_barri(df_densidad_poblacion, 'nom_barri'))
print('.....................................................')

#Llamo a la función para ver las cinco primeras filas del DF.
print(soporte.primeras_filas(df_densidad_poblacion))
print('.....................................................\n')

#Llamo a la función para guardar el DF de la densidad de población como un archivo .csv limpio.
soporte.guardar_df(df_densidad_poblacion, 'densidad_poblacion_barcelona')

print('__________________________________________________________________________________________')

print('________  APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME RENTA PER CAPITA BCN   __________')

#Llamo a la función de leer el csv de la renta per capita.
df_renta = soporte.leer_csv('../data/input_data/Renta_Per_Capita_Barris_Barcelona.csv')
df_renta
print('Las 5 primeras filas del DataFrame de la RENTA PER CAPITA DE BCN son:\n')
print(df_renta.head())
print('.....................................................')

#Llamo a la función para ver la info del csv de la renta per capita.
print('La INFORMACIÓN del DataFrame de la RENTA PER CAPITA DE BCN es:\n')
soporte.info_df(df_renta)
print('.....................................................')

#Llamo a la función para borrar las columnas del DF de la renta per capita.
soporte.borrar_columnas_renta(df_renta)

#Llamo a la función para renombrar las columnas del DF de la renta per capita.
soporte.renombrar_columnas_renta(df_renta)

#Llamo a la función para ver las columnas del DF de la renta per capita.
print(soporte.ver_columnas(df_renta))
print('.....................................................')

#Llamo a la función para normalizar los valores de la columna nom_barri del DF de la renta per capita.
soporte.normalizar_y_renombrar_renta(df_renta)

#Llamo a la función para ver las cinco primeras filas del DF de la renta per capita.
print(soporte.primeras_filas(df_renta))
print('.....................................................\n')

#Llamo a la función para guardar el DF de la renta per capita de BCN como un archivo .csv limpio.
soporte.guardar_df(df_renta, 'renta_per_capita_barcelona')