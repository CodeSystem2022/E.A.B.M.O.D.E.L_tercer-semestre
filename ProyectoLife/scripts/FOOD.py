import pandas as pd
import numpy as np
import logging
from DDBB import connect_DDBB

def FillAndReplace(tabla) -> pd.DataFrame:
    '''
    Esta función cambia valores NaN y "..."
    por 0
    '''
    columnas =['id', 'alimento', 'energía (Kcal)', 'proteinas', 'grasa total', 'carbohidratos']
    try:
        tabla = tabla.iloc[7:,[0,1,5,7,8,9]]
        tabla.columns = columnas

        #elimino filas NaN en base a la columna id
        tabla.dropna(subset='id', inplace=True)
        #cambio valores "..." y NaN por 0
        tabla.replace(to_replace='...', value= np.nan, inplace=True)
        tabla.fillna(value=0, inplace=True)
        logging.info(f'Tabla normalizada')

    except Exception as e:
        logging.error(e)
    return tabla

def TransformAndLoad()-> pd.DataFrame: 
    '''
    Esta función normaliza las tablas de alimentos
    y finalmente las carga a la DDBB.
    '''
    
    #Lectura de las tablas
    try:
        engine = connect_DDBB()
        path = 'scripts\Dataset'
        carnes = pd.read_excel(path +'\Carnes.xls')
        cereales = pd.read_excel(path + '\Cereales.xls')
        frutas = pd.read_excel(path + '\Frutas.xls')
        grasas = pd.read_excel(path + '\Grasas.xls')
        huevos = pd.read_excel(path + '\Huevo.xls')
        leche = pd.read_excel(path + '\Leche.xls')
        pescados = pd.read_excel(path + '\Pescados.xls')
        azucarados = pd.read_excel(path + '\ProdAz.xls')
        vegetales = pd.read_excel(path + '\Vegetales.xls')
        logging.info('se realizó la lectura de los archivos xls')

    except Exception as e:
        logging.error(e)

    

    #Normalizado de la columna carne
    try:
        #Normalizo las columnas del df grasas
        grasas = grasas.iloc[7:,[0,1,5,7]]
        grasas = grasas.assign(proteinas=0, carbohidratos=0)
        columnas = ['id', 'alimento', 'energía (Kcal)', 'proteinas', 'grasa total', 'carbohidratos']
        grasas.columns = columnas
        DataSet = [carnes, cereales, frutas, huevos, leche, pescados, azucarados, vegetales]

        for i in range(len(DataSet)):
            DataSet[i] = FillAndReplace(DataSet[i])
        
        #Genero una sola tabla maestra
        DataSet.append(grasas)
        DataSet = pd.concat(DataSet, ignore_index=True)
        
        #asigno Dtype correspondiente a cada columna
        DataSet[['id', 'energía (Kcal)']] = DataSet[['id', 'energía (Kcal)']].astype(int)
        DataSet[['proteinas', 'grasa total', 'carbohidratos']] = DataSet[['proteinas', 'grasa total', 'carbohidratos']].astype(float).round(1)

        #ordeno en forma ascendente al DataSet en base a la columna id
        DataSet.sort_values(by='id', ascending=True, inplace=True)
        logging.info('Tabla normalizada de Dtype y ordenada de forma ascendente en base a columna "id"')

    except Exception as e:
        logging.error(e)

    #carga de la tabla "DataSet" a la DDBB
    try:
        DataSet.to_sql('alimentos', con=engine, if_exists='replace', index=False)
        logging.info('Tabla alimentos cargada a la DDBB')
    except Exception as e:
         logging.error(e)
    


if __name__== '__main__':
    TransformAndLoad()
