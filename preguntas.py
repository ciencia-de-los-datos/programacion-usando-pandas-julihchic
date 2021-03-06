"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    import pandas as pd

    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


    
    return len(tbl0)


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    import pandas as pd

    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    tbl0.columns

    
    return len(tbl0.columns)


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    import pandas as pd


    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


    #utilizo value_counts() para contar las veces que esta cada letra
    #utilizo sort_index() para ordenar alfabeticamente, puede ser ascending true o false
    #si quisiera ordenarlos numericamente pongo ascending true o false en los parentesis de value_count()
    sum_c1= tbl0['_c1'].value_counts().sort_index(ascending=True)


    return sum_c1


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    import pandas as pd


    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    #hago groupby para traer los de _c2  
    #pongo la funcion luego de los corchetes de la columna a la que se la quiero hacer
    prom_c2 = tbl0.groupby('_c1')['_c2'].mean()

    return prom_c2


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    import pandas as pd


    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    #hago groupby para traer los de _c2  
    #pongo la funcion luego de los corchetes de la columna a la que se la quiero hacer
    prom_c2 = tbl0.groupby('_c1')['_c2'].max()
    return prom_c2

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    import pandas as pd


    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    #creo una copia de la base
    data=tbl1.copy('_c4')

    #en la copia pongo en mayusculas los elementos de la columna _c4
    data['_c4']= data['_c4'].str.upper()

    data

    #los ordeno con sorted y le quito duplicados con .unique
    return sorted(data['_c4'].unique())


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    import pandas as pd


    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    #hago groupby para traer los de _c2  
    #pongo la funcion sum luego de los corchetes de la columna a la que se la quiero hacer
    prom_c2 = tbl0.groupby('_c1')['_c2'].sum()

    
    return prom_c2


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    import pandas as pd


    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    df=tbl0.copy()

    #al df original le creo la columna con la funcion sum y le pongo axis=1 para que aplique la funcion en las columnas
    df['suma']=df.sum(axis=1)

    
    return df


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    import pandas as pd

    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    #creo una copia de la tabla
    df=tbl0.copy()

    #agrego la nueva columna y pongo el split para seleccionar el elemento que quiero de la columna
    df['year']=df['_c3'].str.split('-',expand=True)[0]

    
    return df


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    import pandas as pd

    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    df1=tbl0.copy()
    df1['_c2']=df1['_c2'].apply(lambda x: str(x))

    def nueva_lista(df):
        nums=list(df['_c2'])
        nums.sort()
        return ':'.join(nums)

    mi_df=df1.groupby('_c1').apply(nueva_lista)

    df2=df1.drop_duplicates(subset='_c1')
    l=list(sorted(df2['_c1']))

    n_l=list(mi_df)

    result=pd.DataFrame(list(zip(l,n_l)), columns=['_c1','_c2'])
    #df['_c2']=sorted(df['_c2'])
    return result.set_index('_c1')


    
   


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    import pandas as pd

    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    #hago copia para crear mi df
    df1=tbl1.copy()
    #le aplico la funcion a la columna que quiero ver
    df1['_c4']=df1['_c4'].apply(lambda x: str(x))

    #creo una funcion para hacer la lista de str ordendada
    #en el return pongo el caracter por el que van a estar separados los str y el .join para unirlos
    def nueva_lista(df):
        letras= list(df['_c4'])
        letras.sort()
        return ','.join(letras)

    #creo mi fd co nel groupby y le agrego la funcion
    mi_df = df1.groupby('_c0').apply(nueva_lista)
    #quito duplicados y los ordeno en el nuevo df2
    df2=df1.drop_duplicates(subset='_c0')
    l=list(sorted(df2['_c0']))
    #creo mi lista resultante del groupby
    nuev_l=list(mi_df)

    result=pd.DataFrame(list(zip(l,nuev_l)), columns= ['_c0','_c4'])
    
    return result


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    import pandas as pd

    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    df1=tbl2.copy()
    df1['_c5b']=df1['_c5b'].astype(str)
    df1['_c5']=df1['_c5a']+':'+df1['_c5b']


    df1['_c5']=df1['_c5'].apply(lambda x: str(x))

    #creo una funcion para hacer la lista de str ordendada
    #en el return pongo el caracter por el que van a estar separados los str y el .join para unirlos
    def nueva_lista(df):
        letras= list(df['_c5'])
        letras.sort()
        return ','.join(letras)

    #creo mi fd co nel groupby y le agrego la funcion
    mi_df = df1.groupby('_c0').apply(nueva_lista)
    #quito duplicados y los ordeno en el nuevo df2
    df2=df1.drop_duplicates(subset='_c0')
    l=list(sorted(df2['_c0']))
    #creo mi lista resultante del groupby
    nuev_l=list(mi_df)

    result=pd.DataFrame(list(zip(l,nuev_l)), columns= ['_c0','_c5'])
    
    return result


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    import pandas as pd

    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

    #uno los df
    df1=pd.merge(tbl0, tbl2, on='_c0')
    df1

    #hago el groupby con la suma que me piden
    df=df1.groupby('_c1')['_c5b'].sum()
    
    return df
