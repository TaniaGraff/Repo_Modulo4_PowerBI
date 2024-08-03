import soporte

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

#Llamo a la función para renombrar distrito DF renta.
soporte.renombrar_distrito_renta(df_renta, 'nom_districte')

#Llamo a la función para ver las cinco primeras filas del DF de la renta per capita.
print(soporte.primeras_filas(df_renta))
print('.....................................................\n')

#Llamo a la función para guardar el DF de la renta per capita de BCN como un archivo .csv limpio.
soporte.guardar_df(df_renta, 'renta_per_capita_barcelona')


print('__________________________________________________________________________________________')

print('________  APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME DISTRITOS   __________')

#Llamo a la función de leer el csv de distritos.
df_distritos = soporte.leer_csv('../data/input_data/BarcelonaCiutat_Districtes.csv')
df_distritos
print('Las 5 primeras filas del DataFrame de DISTRITOS son:\n')
print(df_distritos.head())
print('.....................................................')

#Llamo a la función para ver la info del csv de la renta per capita.
print('La INFORMACIÓN del DataFrame de DISTRITOS es:\n')
soporte.info_df(df_distritos)
print('.....................................................')

#Llamo a la función para renombrar las columnas del DF de distritos.
soporte.renombrar_columnas_distritos(df_distritos)

#Llamo a la función para ver las cinco primeras filas del DF de distritos.
print(soporte.primeras_filas(df_distritos))
print('.....................................................\n')

#Llamo a la función para guardar el DF de los distritos como un archivo .csv limpio.
soporte.guardar_df(df_distritos, 'distritos_barcelona')


print('__________________________________________________________________________________________')

print('________  APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME PARQUES Y JARDINES   __________')

#Llamo a la función para leer el archivo csv de parques y jardines.
df_parques_y_jardines_bruto = soporte.leer_csv('../data/input_data/opendatabcn_cultura_parcs-i-jardins.csv')

#Llamo a la funciñon para el DF para organizar el contenido correctamente.
df_parques_y_jardines= soporte.limpiar_dataframe(df_parques_y_jardines_bruto)

#Llamo a la función para ver la info del csv de parques y jardines.
print('La INFORMACIÓN del DataFrame de DISTRITOS es:\n')
soporte.info_df(df_parques_y_jardines)
print('.....................................................')

#Llamo a la función para borrar columnas del DF de parques y jardines.
soporte.borrar_columnas_parques_y_jardines(df_parques_y_jardines)

#Llamo a la función para ver las cinco primeras filas del DF de parques y jardines.
print(soporte.primeras_filas(df_parques_y_jardines))
print('.....................................................\n')

#Llamo a la función para igualar el texto de las columnas del DF de parques y jardines.
soporte.normalizar_y_renombrar_parques_y_jardines(df_parques_y_jardines)

#Llamo a la función para eliminar los duplicados de la columna register id.
soporte.eliminar_duplicados(df_parques_y_jardines, 'register_id')

#Llamo a la función para guardar el DF de parques y jardines como un archivo .csv limpio.
soporte.guardar_df(df_parques_y_jardines, 'parques_y_jardines_barcelona')


print('__________________________________________________________________________________________')

print('________  APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME CÓDIGO CONTAMINANTES   __________')

#Llamo a la función de leer el csv del código de contaminantes.
df_contaminantes = soporte.leer_csv('../data/input_data/qualitat_aire_contaminants.csv')
df_contaminantes
print('Las 5 primeras filas del DataFrame de CONTAMINANTES son:\n')
print(df_contaminantes.head())
print('.....................................................')

#Llamo a la función para ver la info del csv del código de contaminantes.
print('La INFORMACIÓN del DataFrame de CONTAMINANTES es:\n')
soporte.info_df(df_contaminantes)
print('.....................................................')

#Llamo a la función para renombrar columnas.
soporte.renombrar_columnas_contaminantes(df_contaminantes)

#Llamo a la función para guardar el DF de los contaminantes de BCN como un archivo .csv limpio.
soporte.guardar_df(df_contaminantes, 'contaminantes_barcelona')


print('__________________________________________________________________________________________')

print('________  APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME CALIDAD AIRE BCN   __________')

#Llamo a la función de leer el csv de la contaminación.
df_contaminacion = soporte.leer_csv('../data/input_data/2021_qualitat_aire_estacions.csv')
df_contaminacion
print('Las 5 primeras filas del DataFrame de CONTAMINACIÓN son:\n')
print(df_contaminacion.head())
print('.....................................................')

#Llamo a la función para ver la info del csv de la contaminación.
print('La INFORMACIÓN del DataFrame de CONTAMINACIÓN es:\n')
soporte.info_df(df_contaminacion)
print('.....................................................')

#Llamo a la función para igualar nombres columnas contaminación.
soporte.renombrar_columnas_contaminacion(df_contaminacion)

#Llamo a la función para cambiar el nombre a los distritos.
soporte.renombrar_distrito_contaminacion(df_contaminacion, 'nom_districte')

#Llamo a la función para cambiar el código de un distrito.
soporte.actualizar_eixample(df_contaminacion)
print(df_contaminacion[['codi_districte', 'nom_districte']].head(10))

#Llamo a la función para guardar el DF de contaminación como un archivo .csv limpio.
soporte.guardar_df(df_contaminacion, 'contaminacion_barcelona')
