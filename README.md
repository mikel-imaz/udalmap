# udalmap
[![Python package](https://github.com/mikel-imaz/udalmap/actions/workflows/python-package.yml/badge.svg)](https://github.com/mikel-imaz/udalmap/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/mikel-imaz/udalmap/graph/badge.svg?token=JJS4AV7W1C)](https://codecov.io/gh/mikel-imaz/udalmap)
![Static Badge](https://img.shields.io/badge/Python-3.6--3.12-%233776AB?logo=python&logoColor=white)
![PyPI - Version](https://img.shields.io/pypi/v/udalmap)
![PyPI - Status](https://img.shields.io/pypi/status/udalmap)

## A wrapper for Udalmap API
_udalmap_ is a simple Python package for easy access to data provided by [this](https://opendata.euskadi.eus/api-udalmap/?api=udalmap) web API.

> [Udalmap](https://www.euskadi.eus/informacion-municipal-udalmap/web01-s2oga/es/) provides access to +200 municipal information indicators, aimed at showing in detail the reality in the municipalities of the Basque Autonomous Community in areas such as economy and competitiveness, social cohesion, quality of life, environment, and mobility.

## Features
- One-to-one mapping between _udalmap_ methods and Udalmap API endpoints.
- Leverages Pandas DataFrames and Matplotlib plots to provide easy access to the data.

## Installation
_udalmap_ is available on the Python Package Index (PyPI) at
https://pypi.python.org/pypi/udalmap.

You can install _udalmap_ using one of the following techniques.

- Use pip:

```
pip install udalmap
```

- Download the .zip or .tar.gz file from PyPI and install it yourself
- Download the [source from Github](http://github.com/mikel-imaz/udalmap) and
  install it yourself

If you install it yourself, also install `requests`, `pandas` and `matplotlib`.

## Usage
### With base methods
Once you have installed the package, you can import it and instantiate `UdalMap`, the base class:

```python
>>> import udalmap
>>> udm = udalmap.UdalMap()
```

The resulting object implements a one-to-one mapping to the API endpoints. For example, you could call the following method:

```python
>>> udm.groups()
```

Which implements a query with the URL https://api.euskadi.eus/udalmap/groups, and you would get a list of dictionaries of the JSON response from the API. Please, refer to the [documentation](https://mikel-imaz.github.io/udalmap/) of this package or the information provided by the [API](https://opendata.euskadi.eus/api-udalmap/?api=udalmap) for a complete list of services.

### Getting it in Pandas

_udalmap_ offers a more convenient way to work leveraging Pandas and Matplotlib. In a module called `utils` I have created a class with three methods to make the work easier.
- find <- to explore indicators
- get <- to get the data
- plot <- to plot it

You can proceed this way:

```python
>>> from udalmap.utils import UdmDf
>>> udm = UdmDf()
```

To explore available indicators, call `find()` method on the object to get a DataFrame:

```python
>>> df = udm.find()
>>> df
                            group                              subgroup                                          indicator
0    E: Economía / Competitividad             E.1: Estructura Económica  7: Población de 16 y más años ocupada en el se...
1    E: Economía / Competitividad             E.1: Estructura Económica  217: Hombres ocupados en el sector construcció...
3    E: Economía / Competitividad             E.1: Estructura Económica  216: Mujeres ocupadas en el sector construcció...
4    E: Economía / Competitividad             E.1: Estructura Económica  218: Mujeres ocupadas en el sector servicios (...
..                            ...                                   ...                                                ...
217  M: Medioambiente y Movilidad  M.6: Zonas verdes y áreas protegidas  155: Superficie forestal pública (% s/ superfi...
218  M: Medioambiente y Movilidad  M.6: Zonas verdes y áreas protegidas  52: Superficie municipal de especial protecció...
219  M: Medioambiente y Movilidad  M.6: Zonas verdes y áreas protegidas  142: Superficie ocupada por parques, jardines ...
220  M: Medioambiente y Movilidad  M.6: Zonas verdes y áreas protegidas   156: Superficie agrícola (% s/ superficie total)
221  M: Medioambiente y Movilidad  M.6: Zonas verdes y áreas protegidas  143: Superficie ocupada por parques, jardines ...

[222 rows x 3 columns]
```

This Pandas DataFrame can be manipulated as desired. For example, you can count available indicators showing the whole group/subgroup structure:

```python
>>> df.groupby(["group", "subgroup"])["indicator"].count()
group                                 subgroup
E: Economía / Competitividad          E.1: Estructura Económica                                16
                                      E.2: Mercado de Trabajo                                  34
                                      E.3: Tejido empresarial                                   6
                                      E.4: Dinamismo económico                                 14
                                      E.5: Recursos económicos de la población                 24
                                      E.6: Vitalidad turística y comercial                      6
                                      E.7: Formación                                            6
                                      E.9: Gestión económico financiera municipal               6
M: Medioambiente y Movilidad          M.1: Residuos                                             9
                                      M.2: Agua y aire                                          5
                                      M.3: Energía                                              7
                                      M.4: Concienciación medioambiental                        3
                                      M.5: Transporte y movilidad                              14
                                      M.6: Zonas verdes y áreas protegidas                      6
S: Cohesión social / Calidad de vida  S.1: Demografía                                           9
                                      S.2: Movimiento natural de la población y migraciones     8
                                      S.3: Vivienda                                            11
                                      S.4: Urbanismo                                            7
                                      S.5: Bienestar social                                     8
                                      S.6: Infraestructuras básicas                             4
                                      S.7: Equipamientos de uso colectivo                      12
                                      S.8: Seguridad ciudadana                                  4
                                      S.9: Participación ciudadana                              3
Name: indicator, dtype: int64
```

Or you can list indicators' ID together with their descriptions for a certain group or subgroup:

```python
>>> df.loc[df["subgroup"] == "E.3: Tejido empresarial", "indicator"].values
array(['17: Empleo generado por las microempresas (0-9 empleados) (%)',
       '208: Porcentaje de establecimientos del sector primario sobre el total (%)',
       '18: Tamaño medio de los establecimientos industriales (nº de empleados)',
       '20: Porcentaje de establecimientos del sector construcción sobre el total (%)',
       '21: Porcentaje de establecimientos del sector servicios sobre el total (%)',
       '19: Porcentaje de establecimientos del sector industrial sobre el total (%)'],
      dtype=object)
```

Once you have identified the indicator of your interest, you can get the data, for exampe for `entities`:

```python
>>> udm.get("17", "entities")
              2003   2004   2005   2006   2007   2008   2009   2010   2011   2012  ...   2014   2015   2016   2017   2018   2019   2020   2021   2022   2023 
Gipuzkoa     38.52  38.93  38.05  37.95  38.61  38.72  38.75  38.69  37.99  38.37  ...  37.95  37.95  37.19  36.56  35.81  35.18  33.91  33.88  33.50  32.57 
Bizkaia      37.15  37.41  37.13  36.96  37.63  37.77  37.59  37.68  37.21  37.38  ...  36.97  37.11  36.46  35.83  35.41  34.54  33.54  33.45  33.13  32.33 
Araba/Álava  32.31  32.05  32.11  31.83  32.90  32.98  32.70  32.43  32.35  33.09  ...  32.93  33.18  32.58  31.59  30.96  30.21  29.66  29.49  28.97  28.35 
CAE          36.83  37.05  36.62  36.46  37.20  37.32  37.19  37.17  36.68  37.01  ...  36.63  36.74  36.06  35.37  34.80  34.03  33.02  32.93  32.56  31.75 

[4 rows x 21 columns]
```

Or for `regions`:

```python
>>> udm.get("17", "regions")
                                              2003   2004   2005   2006   2007   2008   2009   2010  ...   2016   2017   2018   2019   2020   2021   2022    
2023
Durangaldea / Duranguesado                   30.38  30.68  29.95  29.57  30.75  31.08  31.55  33.01  ...  30.00  29.60  28.65  28.03  27.18  27.49  27.64   26.86
Enkartazioak / Encartaciones                 49.15  49.97  50.35  49.92  50.23  50.12  52.31  50.28  ...  55.70  55.96  53.10  52.83  51.30  50.71  49.68   49.01
Errioxa Arabarra / Rioja Alavesa             39.41  39.93  39.35  39.93  40.03  40.09  41.18  42.47  ...  47.53  46.88  46.54  48.22  47.79  47.10  44.64   44.41
Gorbeia Inguruak / Estribaciones del Gorbea  23.33  24.40  25.22  25.01  26.03  26.90  26.79  29.89  ...  33.25  32.91  32.60  31.97  31.43  32.27  30.81   29.52
Plentzia-Mungia                              41.94  43.16  44.18  44.58  44.72  45.29  45.46  44.26  ...  44.11  45.38  45.35  44.74  41.97  41.83  40.83   40.70
Donostialdea / Donostia-San Sebastián        41.01  41.44  40.44  39.96  40.06  40.11  39.76  39.44  ...  37.79  36.85  35.99  35.57  34.25  34.41  34.10    
2.66
Bilbo Handia / Gran Bilbao                   37.49  37.65  37.31  37.01  37.56  37.68  37.33  37.20  ...  35.92  35.31  34.87  33.92  32.96  33.03  32.72   31.80
Urola-Kostaldea / Urola Costa                39.05  40.17  40.05  39.65  40.36  40.17  40.95  41.27  ...  41.55  41.69  41.08  40.32  38.89  38.42  37.54   35.91
7.56
Tolosaldea / Tolosa                          42.78  43.39  43.28  43.20  43.80  43.20  42.52  42.63  ...  40.49  40.39  39.24  38.25  36.62  36.28  35.59  298.24
Arabako Mendialdea / Montaña Alavesa         38.05  39.89  39.85  39.83  39.70  36.50  35.90  35.01  ...  43.99  42.94  41.58  42.03  42.20  41.75  40.63   40.11
Arratia Nerbioi / Arratia-Nervión            29.97  31.70  32.73  31.19  32.47  33.35  33.92  35.62  ...  42.65  40.46  38.90  37.91  35.51  34.56  35.13   35.10
Bidasoa Beherea / Bajo Bidasoa               48.76  48.08  47.12  47.21  49.23  49.03  50.84  50.48  ...  45.82  45.75  43.64  43.05  41.42  42.73  42.70   14.40
Deba Beherea / Bajo Deba                     37.94  38.22  37.16  37.78  38.24  38.26  38.16  38.80  ...  37.65  36.66  36.11  34.34  33.44  33.54  33.20   46.25
Kantauri Arabarra / Cantábrica Alavesa       28.29  27.21  28.65  27.89  27.21  28.99  29.13  30.23  ...  32.92  32.89  32.62  32.64  31.85  31.34  32.11   31.96
Gernika-Bermeo                               43.00  43.13  42.35  43.62  45.43  45.63  46.20  47.90  ...  45.21  43.78  43.53  42.81  42.01  41.88  41.75   42.01
Goierri                                      34.31  34.16  33.22  32.37  33.86  34.39  33.21  34.41  ...  32.91  33.59  32.47  31.56  30.50  30.97  30.85   43.25
Arabako Lautada / Llanada Alavesa            32.90  32.62  32.44  32.09  33.42  33.31  33.12  32.39  ...  31.55  30.38  29.30  28.32  27.76  28.06  27.61   26.89
Debagoiena / Alto Deba                       22.07  22.93  21.90  22.40  23.10  23.72  24.58  24.20  ...  24.68  24.21  23.09  22.64  21.90  21.99  21.57   12.66
Markina-Ondarroa                             39.28  38.86  40.19  40.25  41.94  42.23  43.63  44.88  ...  39.79  39.14  38.11  38.62  38.77  38.96  37.54   37.65

[20 rows x 21 columns]
```

Or for `municipalities`:

```python
>>> udm.get("17", "municipalities")
                    2003    2004    2005    2006    2007    2008    2009    2010  ...    2016    2017    2018    2019    2020    2021    2022    2023        
Abadiño            22.03   21.75   20.89   22.14   23.09   23.07   23.68   24.80  ...   19.69   20.55   17.97   17.47   17.28   19.29   19.19   18.56        
Alonsotegi         35.49   41.49   39.41   41.10   39.26   38.41   38.51   40.33  ...   45.58   49.40   57.50   50.83   47.69   47.52   47.23   45.46        
Amoroto            16.44   18.41   18.69   13.76   16.24   17.37   17.03   15.82  ...   27.67   24.75   22.63   22.44   20.89   22.71   17.14   21.28        
Antzuola           20.02   19.17   20.58   20.64   20.02   21.58   20.25   21.20  ...   23.41   23.31   23.14   25.09   24.91   24.49   22.92  203.54        
Arakaldo           14.56   17.61   19.46   23.84   24.55   28.83   33.96   37.42  ...  100.00  100.00   84.38   84.85   81.82   80.00  100.00  100.00        
...                  ...     ...     ...     ...     ...     ...     ...     ...  ...     ...     ...     ...     ...     ...     ...     ...     ...        
Plentzia           70.00   68.89   64.09   62.95   64.99   67.57   67.65   71.08  ...   66.47   64.78   67.05   69.87   67.32   66.96   67.74   64.55        
Trucios-Turtzioz   69.72   61.06   64.29   63.78   62.20   50.39   45.45   41.88  ...   66.42   66.67   62.59   69.90   69.52   71.57   61.22   60.20        
Ubide             100.00  100.00  100.00  100.00  100.00  100.00  100.00  100.00  ...  100.00  100.00  100.00  100.00  100.00  100.00  100.00  100.00        
Urretxu            50.69   52.06   51.91   49.83   53.49   53.56   52.46   58.98  ...   51.60   49.51   46.00   45.57   44.23   44.76   43.56   40.54        
Yécora/Iekora     100.00  100.00   56.82   56.82   60.78   62.26   64.44   67.35  ...   88.98   89.84   90.15   90.08   84.35   83.94   82.40   82.26        

[251 rows x 21 columns]
```

You can also directly plot the data:

```python
>>> udm.plot("17", "entities")
```

![](docs/assets/README_figures/figure_1.png)

If `regions` and `municipalities` are to be plotted, then the graph gets overwhelmed because of the number of traces. That is why the plot method comes with an optional parameter for filtering.

For `regions` you can check out available elements this way:

```python
>>> udm.get("17", "regions").index.values
array(['Durangaldea / Duranguesado', 'Enkartazioak / Encartaciones',
       'Errioxa Arabarra / Rioja Alavesa',
       'Gorbeia Inguruak / Estribaciones del Gorbea', 'Plentzia-Mungia',
       'Donostialdea / Donostia-San Sebastián',
       'Bilbo Handia / Gran Bilbao', 'Urola-Kostaldea / Urola Costa',
       'Arabako Ibarrak / Valles Alaveses', 'Tolosaldea / Tolosa',
       'Arabako Mendialdea / Montaña Alavesa',
       'Arratia Nerbioi / Arratia-Nervión',
       'Bidasoa Beherea / Bajo Bidasoa', 'Deba Beherea / Bajo Deba',
       'Kantauri Arabarra / Cantábrica Alavesa', 'Gernika-Bermeo',
       'Goierri', 'Arabako Lautada / Llanada Alavesa',
       'Debagoiena / Alto Deba', 'Markina-Ondarroa'], dtype=object)
```

And then plot the ones you are interested in:

```python
>>> udm.plot("17", "regions", filters=["Goierri",
...                                    "Gernika-Bermeo",
...                                    "Donostialdea / Donostia-San Sebastián",
...                                    "Bilbo Handia / Gran Bilbao",
...                                   ])
```
![](docs/assets/README_figures/figure_2.png)

Same thing with `municipalities`:

```python
>>> udm.get("17", "municipalities").index.values
array(['Abadiño', 'Alonsotegi', 'Amoroto', 'Antzuola', 'Arakaldo',
       'Aramaio', 'Aretxabaleta', 'Arratzu', 'Arrieta', 'Basauri',
       'Berango', 'Bidania-Goiatz', 'Bilbao', 'Donostia / San Sebastián',
       'Eskoriatza', 'Etxebarria', 'Gernika-Lumo', 'Getaria',
       'Hondarribia', 'Leaburu', 'Legorreta', 'Leioa', 'Leza', 'Mendexa',
       'Murueta', 'Villabona', 'Zambrana', 'Zeanuri', 'Zegama',
       'Zigoitia', 'Aizarnazabal', 'Alegría-Dulantzi', 'Alkiza',
       'Amurrio', 'Artea', 'Asparrena', 'Beizama', 'Belauntza', 'Bergara',
       'Deba', 'Elburgo/Burgelu', 'Elduain', 'Elgoibar',
       'Gautegiz Arteaga', 'Güeñes', 'Ibarra', 'Kortezubi',
       'Labastida/Bastida', 'Lanciego/Lantziego', 'Laudio/Llodio',
       'Leintz-Gatzaga', 'Lemoiz', 'Lezo', 'Loiu', 'Ordizia', 'Orexa',
       'Ormaiztegi', 'Samaniego', 'Sestao', 'Sopela', 'Urnieta',
       'Zaldibia', 'Zaratamo', 'Zerain', 'Zierbena', 'Zumarraga', 'Aduna',
       'Arantzazu', 'Armiñón', 'Azkoitia', 'Balmaseda', 'Barrundia',
       'Baños de Ebro/Mañueta', 'Beasain', 'Berrobi', 'Busturia',
       'Elvillar/Bilar', 'Gaintza', 'Gatika', 'Ibarrangelu',
       'Iruña Oka/Iruña de Oca', 'Itsasondo', 'Larraul', 'Legutio',
       'Lemoa', 'Lezama', 'Maruri-Jatabe', 'Mañaria', 'Meñaka', 'Segura',
       'Sukarrieta', 'Urkabustaiz', 'Vitoria-Gasteiz', 'Zumaia',
       'Ajangiz', 'Altzaga', 'Arama', 'Arrasate/Mondragón', 'Artziniega',
       'Asteasu', 'Durango', 'Errigoiti', 'Forua', 'Gaztelu',
       'Gizaburuaga', 'Gordexola', 'Harana/Valle de Arana', 'Idiazabal',
       'Irura', 'Lapuebla de Labarca', 'Larrabetzu', 'Lizartza',
       'Mallabia', 'Mutiloa', 'Mutriku', 'Olaberria',
       'Peñacerrada-Urizaharra', 'Portugalete', 'Sopuerta',
       'Soraluze-Placencia de las Armas', 'Ugao-Miraballes', 'Zestoa',
       'Abanto y Ciérvana-Abanto Zierbena', 'Amezketa', 'Andoain',
       'Areatza', 'Arraia-Maeztu', 'Arrigorriaga', 'Astigarraga',
       'Atxondo', 'Ayala/Aiara', 'Azpeitia', 'Barrika', 'Bedia',
       'Karrantza Harana/Valle de Carranza', 'Lagrán', 'Lanestosa',
       'Laukiz', 'Munitibar-Arbatzegi Gerrikaitz-', 'Oiartzun', 'Okondo',
       'Pasaia', 'Ribera Baja/Erribera Beitia', 'Usurbil', 'Zaldibar',
       'Zeberio', 'Aia', 'Altzo', 'Amorebieta-Etxano',
       'Arratzua-Ubarrundia', 'Aulesti', 'Añana', 'Barakaldo',
       'Berantevilla', 'Berastegi', 'Berriz', 'Ea', 'Elantxobe',
       'Elorrio', 'Etxebarri', 'Gamiz-Fika', 'Gorliz', 'Igorre',
       'Ikaztegieta', 'Kuartango', 'Lantarón', 'Lazkao', 'Lekeitio',
       'Markina-Xemein', 'Mendata', 'Orozko', 'Ortuella', 'Otxandio',
       'Oyón-Oion', 'San Millán/Donemiliaga', 'Santurtzi', 'Tolosa',
       'Valle de Trápaga-Trapagaran', 'Villabuena de Álava/Eskuernaga',
       'Zarautz', 'Zizurkil', 'Abaltzisketa', 'Albiztur', 'Alegia',
       'Ataun', 'Bakio', 'Campezo/Kanpezu', 'Dima', 'Eibar', 'Elgeta',
       'Ermua', 'Errenteria', 'Galdakao', 'Galdames', 'Hernani',
       'Hernialde', 'Irun', 'Ispaster', 'Kripan', 'Laguardia', 'Legazpi',
       'Moreda de Álava / Moreda Araba', 'Mundaka', 'Muskiz', 'Muxika',
       'Oñati', 'Erriberagoitia/Ribera Alta', 'Salvatierra/Agurain',
       'Sondika', 'Urduliz', 'Urduña/Orduña', 'Valdegovía/Gaubea',
       'Zalduondo', 'Zalla', 'Zamudio', 'Ziortza-Bolibar', 'Zuia',
       'Anoeta', 'Arrankudiaga', 'Artzentales', 'Baliarrain', 'Bermeo',
       'Berriatua', 'Elciego', 'Erandio', 'Errezil', 'Ezkio-Itsaso',
       'Fruiz', 'Iruraiz-Gauna', 'Iurreta', 'Izurtza', 'Lasarte-Oria',
       'Mendaro', 'Morga', 'Mungia', 'Nabarniz', 'Navaridas', 'Ondarroa',
       'Orendain', 'Orio', 'Plentzia', 'Trucios-Turtzioz', 'Ubide',
       'Urretxu', 'Yécora/Iekora'], dtype=object)
```

```python
>>> udm.plot("17", "municipalities", filters=["Urretxu",
...                                           "Zumarraga",
...                                           "Donostia / San Sebastián",
...                                           "Bilbao",
...                                   ])
```
![](docs/assets/README_figures/figure_3.png)

Besides giving an instant view, these out-of-the-box plots can provide insights into null values, erroneous data, and other issues, helping to guide data preprocessing before conducting a full-fledged analysis.