#!/usr/bin/env python
# coding: utf-8

# ## Notebook Tripadvisor
# 
# Se realiza el proceso de web scrapping mediante una serie de peticiones a la Api de TripAdvisor

# Creo una lista para ser consumida por la API de Tripadvisor, posteriormente la consumo en dicha API, guardo los datos en el df y posteriormente guardo todos los resultados en el archivo csv

# In[1]:


# marco


# In[2]:


import os
import pandas as pd


# In[3]:


directorio= os.getcwd() # vemos el directorio donde estamos parados
print(f'actualmente estamos en {directorio}')
print('-'*120)


# In[4]:


desired_directory = '/lakehouse/default/Files/DATA FINAL/TRIP ADVISOR' # directorio en el que deseamos trabajar
os.chdir(desired_directory) # cambiamos al directorio donde deseamos trabajar
print(f'Ahora estamos en {os.getcwd()}')


# In[5]:


archivos= os.listdir(os.getcwd())
print(archivos)


# In[6]:


prueba = pd.read_parquet('abfss://558991ad-6fdf-463a-b58a-238ddabaa398@onelake.dfs.fabric.microsoft.com/37a0382d-f783-4728-a697-48b1dc002937/Files/DATA FINAL/TRIP ADVISOR/Detalle_ubicacion_y_Reviews_Tripadvisor.parquet/part-00006-c0f0ee18-a631-4320-bcb3-1a41abf1dae0-c000.snappy.parquet')


# In[7]:


prueba.head()


# ### Código para ejecutar y consumir las APIs de Ubicaciones y Reviews

# In[1]:


# Importo librerías 
import requests
import pandas as pd
import pickle
from pyspark.sql import SparkSession

# Función para crear una lista de locationID
def crear_lista_locationId(lista_numeros):
    lista_locationId = []
    for numero in lista_numeros:
        numero_int32 = int(numero)
        lista_locationId.append(numero_int32)
    return lista_locationId

# Pego la lista de números aquí
lista_numeros = """
28922
28982
28983
28992
29003
29004
29005
29006
30373
30375
30390
30420
30428
30466
30471
2057395
30477
2057395
30481
30488
30509
30514
30530
30531
28923
60880
30982
30982
60826
60826
26103235
31020
31030
60889
30546
30549
30556
54258
30578
30582
30584
30588
30613
30615
30620
56014
37215
30652
30661
30677
30709
30712
30718
30728
30750
30751
30753
30756
30757
30763
30772
30787
30793
30807
30824
30826
30832
30837
30870
30887
30889
30890
30938
28925
29045
31427
31441
31457
31469
31473
31478
29054
52311
31511
51272
31522
31569
31582
31587
31589
31595
31597
60816
31615
60479
31659
31675
60856
31678
31695
31706
31723
60766
31744
31747
31755
31755
31789
31792
31800
28924
31177
31182
31190
31192
31204
60971
32761
186463
31818
31831
31838
31858
31865
31892
31903
31931
31916
31924
31931
31942
31953
31965
31979
32004
32010
320131
31232
31234
31244
31259
31262
31262
31274
31276
31281
31297
31298
60834
31244
31301
31305
31308
31310
2623686
31323
31325
31337
31350
34352
31352
31356
31365
31373
31377
60950
31274
31399
31405
60773
31407
31411
31418
28926
29073
29078
29087
29092
30090
29094
29099
29106
29111
29112
29120
29125
32037
32041
60902
32044
32055
32066
2018261
32083
32089
32106
32107
32122
32123
32147
32171
32182
32195
32201
32208
32210
32218
32224
32225
32227
34861
49049
46052
32245
47538
32253
60944
32272
55704
32283
31301
32308
32312
32313
32318
32319
32331
32332
32341
32355
32363
32367
32400
32404
32407
32411
32414
32416
32418
32420
32428
32436
1857824
32477
32478
32480
32482
32486
32491
32655
32501
32522
32524
32525
32530
32547
32581
32610
32612
32616
32621
32630
32635
32640
32648
32525
32656
32662
32668
32673
32684
60868
32706
60909
32715
32717
32724
32195
32737
32738
32743
32744
32761
32766
32767
32769
32774
32782
32786
32655
32797
32810
32815
154979
32825
32842
32847
32859
32861
32879
32889
32894
32911
32923
32966
32939
32950
32952
32953
32954
32956
32958
32962
32966
32974
32798
32980
32999
33001
33002
33009
33012
60750
33116
60713
33020
33026
33028
33043
33045
33047
33048
33051
33052
33055
33072
33103
33112
33113
33116
580458
33130
33146
32513
33150
32655
33163
33165
60959
33182
33184
33193
33197
33203
33026
33208
33212
12385474
60769
33224
33230
33231
33250
33252
33259
3658331
33268
58313
33275
33280
33290
33295
33301
33303
33304
28927
29129
29144
1509268
33319
33332
33340
33342
33345
33363
33364
60857
33374
33387
33388
33389
33397
33399
60945
33416
33423
33427
33428
33433
60776
33440
33446
33447
33449
33450
33454
33456
60740
33468
33496
33507
33514
3315
33522
33524
33527
33528
33530
33537
33558
33559
33565
33584
33591
33608
33621
33630
33645
33657
33658
33662
33668
33673
33691
33700
33703
33707
28928
33716
33718
33725
33752
33753
33771
33796
33804
33838
33845
33851
33866
33878
33882
33885
33900
33905
33930
33931
33936
33950
33952
33955
33972
33987
28929
34009
34017
34042
34048
34051
34059
28969
28970
28930
29171
29156
29161
34088
34091
60786
34105
34110
34132
34144
34145
34153
34159
34162
34168
34169
34172
34176
34177
34180
34182
680222
34202
34217
34225
34227
34230
34231
34233
34234
34233
34242
34296
60805
34335
34344
34352
34356
23869903
34360
34366
48023
34373
34378
34382
34388
34408
34409
34411
34422
34423
34433
34438
680222
34443
34448
34438
552079
34439
34449
1479123
34456
34467
34468
34471
34483
34487
34571
34496
34503
34511
34513
34515
34517
34534
34542
34543
34550
34561
34565
34571
34575
34576
34577
34580
34583
3840939
34592
34598
34599
34607
34618
34626
34652
34607
34599
34607
34657
552080
34667
34675
34678
60751
34705
34709
34731
34739
34746
34757
28931
29185
29186
29187
29192
29045
29196
29200
29208
29209
60898
34995
34856
60898
8749994
34913
29212
29213
34760
34776
34792
34793
34802
34809
34812
34815
34817
34820
34821
34830
34843
34856
34859
34861
34864
34867
34868
34870
34882
34885
34892
34895
34904
34906
34907
34911
34913
34916
34922
34937
34950
34951
60770
34957
34963
34986
34987
35004
35011
35028
35031
35034
35037
60874
35046
35051
35053
35056
35057
35068
35069
35071
60920
35085
35091
35102
35110
35115
35130
35148
35152
35185
35194
35195
35220
35222
35232
35235
35236
60814
34964
34964
35266
35267
35277
35281
35283
35292
35293
35309
35310
35311
35313
35320
35322
35330
35331
35335
35338
35340
35348
35356
35377
28932
60982
60982
60872
60872
60616
29220
60626
60626
60608
38020
29343
29352
29355
29356
29360
29377
37682
37696
37719
37735
494966
37742
37743
37746
37749
37750
37762
37765
37771
37773
37778
37791
37797
37801
37816
37837
37822
37831
37835
37853
37861
37887
37890
37891
37897
37913
37914
37960
37961
37963
37973
37978
38011
38014
38016
38020
38021
38027
38030
38040
38055
38079
38135
38143
38147
38182
38204
38210
38217
38228
38245
38247
38257
38258
28933
1124512
35390
35394
35401
35418
35437
35469
35475
38280
38282
38390
38395
38400
38410
38413
38426
38427
38432
38459
38474
38490
38500
38506
38510
38510
37719
37773
38534
38535
35480
35489
35516
35526
35531
35536
35539
35546
35572
35574
35583
35596
35625
28934
29237
29255
29259
29277
29297
35644
35668
35691
35698
35704
35712
35752
3679769
35766
35779
35780
35790
35795
35805
35832
35799
35860
35875
35880
35883
35889
35895
35912
35914
35923
35924
35934
35935
35942
35945
35980
35982
36017
36018
36022
36023
36025
36042
36051
36052
36076
36083
36087
36095
36102
36106
36108
36177
36180
36185
36207
36232
36243
36248
36264
36270
36301
36315
36322
36328
36337
36344
36345
36355
36360
36381
36382
36384
36385
36392
36395
36396
36401
36409
36417
36455
36466
36467
36472
36483
36486
36490
36507
36508
36522
36536
36538
36544
36565
36566
36574
36580
36586
36594
36604
36612
36613
36616
36619
36625
36630
44876
36657
36660
36669
36698
36719
60887
36732
36747
36766
36781
36797
36800
36806
36812
36846
36849
36851
36854
36879
36888
36910
36920
28935
29311
29313
29323
36928
36942
36966
36999
37020
37026
37027
37034
37039
37048
37083
37085
37093
37114
37122
37123
37137
37146
37155
37158
37170
37180
37183
37201
37205
37209
37215
37216
37223
37234
37255
37242
37259
37279
37289
37297
37311
37315
37328
37356
37389
37445
37449
37452
37466
37470
37477
37516
37519
37523
37526
37535
37558
37571
37574
37594
60828
37611
37612
37626
28937
29386
29407
29413
35668
38567
38618
38635
38636
38642
38657
38668
38682
38688
38694
60815
38726
38728
38743
38748
38771
38787
38799
38800
38803
38811
38815
38836
38844
38851
38877
38885
38954
36508
38969
39143
38993
39005
39037
39045
39060
60747
39113
39130
39143
39150
39143
38977
39150
28938
29786
29192
29443
39163
39214
39223
39248
39252
39262
39264
39265
39270
39290
39295
39320
39344
39359
39365
39380
39412
39419
39421
39426
39427
39440
39445
39461
39500
39517
39567
39571
39588
39598
39604
39617
39636
39639
39676
39685
39686
39692
39711
39722
39725
39727
39766
39776
39790
39850
39869
39876
39993
39998
28939
29451
29458
29466
40024
40044
40046
40050
40053
40095
40097
40107
40114
40125
40143
40184
40198
40205
40209
40223
40237
40247
40251
40267
40261
40264
40273
40281
40290
40297
40299
40303
40314
40319
40326
40335
40337
60864
40351
40360
40378
49379
40390
40391
40407
40422
40261
40424
40435
40447
40454
40459
40482
40487
40488
40499
28942
29511
29523
60745
41480
41586
41592
41596
41639
41666
41731
60710
41805
41818
60968
41854
28941
29487
60811
41000
41026
41035
41038
41039
41041
41059
41075
41078
41098
41121
41125
41129
60903
41520
28941
29487
60811
41000
41026
41035
41038
41039
41041
41059
41075
41078
41098
41121
41125
41129
60903
41157
41166
41181
41184
41187
41208
41222
41224
41904
41922
41940
"""

# Crear la lista de locationId
localId = crear_lista_locationId(lista_numeros.split())

# Guardar esa lista en formato pkl
with open("localId.pkl", "wb") as f:
    pickle.dump(localId, f)

# Crear una sesión de Spark
spark = SparkSession.builder.getOrCreate()

# Ruta para guardar el archivo con el nombre actualizado
ruta_guardado = "abfss://558991ad-6fdf-463a-b58a-238ddabaa398@onelake.dfs.fabric.microsoft.com/37a0382d-f783-4728-a697-48b1dc002937/Files/DATA FINAL/TRIP ADVISOR/Detalle_ubicacion_y_Reviews_Tripadvisor.parquet"

# Cargar el DataFrame existente desde el archivo Parquet si está disponible
try:
    df_spark = spark.read.parquet(ruta_guardado)
    df_pandas = df_spark.toPandas()
    print("Se cargaron los datos existentes desde el archivo Parquet.")
except FileNotFoundError:
    print("No se encontró el archivo Parquet existente. Se creará uno nuevo.")
    df_pandas = pd.DataFrame()

# Crear un DataFrame vacío para almacenar los datos de ambas API
APIs_Tripadvisor = pd.DataFrame()

# Iterar sobre cada locationId para consumir la API de TripAdvisor para detalles de ubicación y reseñas
for locationId in localId:
    # Consumir API para detalles de ubicación
    url_detalle = f"https://api.content.tripadvisor.com/api/v1/location/{locationId}/details?key=6977644DAE794280BDD6E5522698BBBE&language=en&currency=USD"
    headers_detalle = {"accept": "application/json"}
    response_detalle = requests.get(url_detalle, headers=headers_detalle)
    data_detalle = response_detalle.json()

    # Consumir API para reseñas
    url_resenas = f"https://api.content.tripadvisor.com/api/v1/location/{locationId}/reviews?key=6977644DAE794280BDD6E5522698BBBE&language=en"
    headers_resenas = {"accept": "application/json"}
    response_resenas = requests.get(url_resenas, headers=headers_resenas)
    data_resenas = response_resenas.json()

    # Verificar si hay datos de reseñas
    if 'data' in data_resenas:
        reviews_data = data_resenas['data']

        # Crear una lista de diccionarios para almacenar los datos de cada reseña
        rows = []
        for review in reviews_data:
            row = {
                "ID": review['id'],
                "Location ID": review['location_id'],
                "Published Date": review['published_date'],
                "Rating": review['rating'],
                "Helpful Votes": review['helpful_votes'],
                "Text": review['text'],
                "Title": review['title'],
                "Trip Type": review.get('trip_type', None),
                "Travel Date": review.get('travel_date', None),
                "Username": review['user'].get('username', None) if 'user' in review else None,
            }
            rows.append(row)

        # Convertir la lista de diccionarios en un DataFrame de pandas para las reseñas
        df_resenas = pd.DataFrame(rows)

        # Agregar los detalles de ubicación al DataFrame de reseñas
        if 'address_obj' in data_detalle:
            df_resenas['State'] = data_detalle['address_obj'].get('state', None)
            df_resenas['Country'] = data_detalle['address_obj']['country']
        else:
            df_resenas['State'] = None
            df_resenas['Country'] = None
        df_resenas['Name'] = data_detalle.get('name')
        df_resenas['Latitude'] = data_detalle.get('latitude')
        df_resenas['Longitude'] = data_detalle.get('longitude')
        df_resenas['Timezone'] = data_detalle.get('timezone')
        df_resenas['Web URL'] = data_detalle.get('web_url')

        # Concatenar el DataFrame de reseñas con el DataFrame principal
        APIs_Tripadvisor = pd.concat([APIs_Tripadvisor, df_resenas], ignore_index=True)
    else:
        print("No se encontraron datos de reseñas para el locationId:", locationId)

# Mostrar las primeras 5 filas del DataFrame
print("DataFrame de APIs Tripadvisor (primeras 5 filas):")
print(APIs_Tripadvisor.head())



# In[ ]:


# Ruta para guardar el archivo CSV
ruta_csv = "abfss://558991ad-6fdf-463a-b58a-238ddabaa398@onelake.dfs.fabric.microsoft.com/37a0382d-f783-4728-a697-48b1dc002937/Files/DATA FINAL/TRIP ADVISOR/APIs_Tripadvisor.csv"

# Guardar el DataFrame como un archivo CSV
APIs_Tripadvisor.to_csv(ruta_csv, index=False)

# Confirmación
print("DataFrame guardado como archivo CSV en la siguiente ruta:")
print(ruta_csv)

