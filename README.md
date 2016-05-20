Az alkalmazás egy egyszerű microservice-t valósít meg Flask framework használatával.

## Telepítése 

Klónozás után:
   
```bash
$ git clone git@github.com:kissgyorgy/Log-collector.git
```

egyszerűen telepíthető a 
    
```bash
$ python3.4 setup.py install 
```

paranccsal. Ez telepít egy logcollector nevű parancssori alkalmazást, amivel a következő műveletek hajthatóak végre:

1. SQLite adatbázist létrehozása a projekt főkönyvtárában.

    ```bash
    $ logcollector createdb
    2014-10-24 00:24:40,309 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
    2014-10-24 00:24:40,309 INFO sqlalchemy.engine.base.Engine ()
    2014-10-24 00:24:40,310 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
    2014-10-24 00:24:40,310 INFO sqlalchemy.engine.base.Engine ()
    2014-10-24 00:24:40,311 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("datapoint")
    2014-10-24 00:24:40,311 INFO sqlalchemy.engine.base.Engine ()
    2014-10-24 00:24:40,312 INFO sqlalchemy.engine.base.Engine
    CREATE TABLE datapoint (
        id INTEGER NOT NULL,
        timestamp DATETIME,
        dim1 INTEGER,
        dim2 INTEGER,
        value FLOAT,
        PRIMARY KEY (id)
    )


    2014-10-24 00:24:40,312 INFO sqlalchemy.engine.base.Engine ()
    2014-10-24 00:24:40,314 INFO sqlalchemy.engine.base.Engine COMMIT
    ```

2. Adatbázis adatokkal való feltöltése:

    ```bash
    $ logcollector initdata 10
    Database filled, has 10 datapoints now.
    ```

3. A logcollector microservice elindítása:

    ```bash
    $ logcollector run
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader
    ```

4. A futó logcollector szervernek adatok küldése létrehozásra:
    
    ```bash
    $ logcollector senddata 1400000000 1 1 1500.42
    Created:
    {
      "dim1": 1,
      "dim2": 1,
      "id": 107,
      "timestamp": "1400000000",
      "value": 1500.42
    }
    ```


## API endpointok

### Új adatpont létrehozása

    /new

POST requestben az alábbi paramétereket várja:
- timestamp (UNIX timestamp)
- dim1 (integer)
- dim2 (integer)
- value (float)

Az alábbi endpointok mindegyike legalább két UNIX timestamp paramétert vár GET requestben, illetve a kiválaszott adathalmaz opciónálisan szűrhető `dim1` és `dim2` paraméterek megadásával.

### MEAN aggregáció lekérdezése

    /mean/<first_timestamp>/<last_timestamp>


### MAX aggregáció lekérdezése

    /max/<first_timestamp>/<last_timestamp>


### MIN aggregáció lekérdezése

    /min/<first_timestamp>/<last_timestamp>

### Szórás (STDDEV) lekérdezése

    /stddev/<first_timestamp>/<last_timestamp>


### Mozgó átlag (Moving average, SMA) lekérdezése

    /movavg/<first_timestamp>/<last_timestamp>/<int:points>

Itt van egy kötelező harmadik paraméter, hogy mekkora intervallumokra (mennyi adatpontra) számoljuk az egyes szakaszok átlagait.


Példák:
    
    GET 127.0.0.0:5000/min/1000000000/1000000050?dim1=2
    GET 127.0.0.0:5000/max/1000000000/1000000060?dim1=5&dim2=3
    GET 127.0.0.0:5000/mean/1000000000/1000000050
    GET 127.0.0.0:5000/movavg/1000000000/1000000070/3
