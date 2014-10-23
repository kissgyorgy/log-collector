## Szerkezet
A kód több python modulba van szervezve:

```bash
$ tree logcollector -I __pycache__
logcollector
├── README.md
├── __init__.py         # view decorátorok
├── commands.py         # logcollector parancsai, click framework használatával
├── forms.py            # HTML form és validátorok
├── models.py           # adatmodell definíciója (web frameworktől független)
├── moving_average.py   # mozgóátlag számító függvény
├── templates
│   ├── _form_helper.html
│   └── new_data_form.html
└── views.py            # API endpointok
```

Mivel az öt aggregátor függvényben nagyon sok a közös elem (mindegyik ugyanazon paraméterek alapján hajt végre adatbázis lekérdezéseket majd számítést végez a halmazon), ezért funckionális programozással (dekorátorok használatával) nagyon egyszerű view kódokat kaphatunk, pl.:

```python
@app.route('/max/<first_timestamp>/<last_timestamp>')
@convert_timestamps
@get_dataset_by_dates
def max_view(dataset):
    return jsonify(max=max(dataset))
```

## Dekorátorok:

- convert_timestamps: két kapott timestampet konvertál Python datetime formátumba. Erre azért volt szükség, mert az SQLite nem ismer külön UNIX timestamp adattípust
- get_dataset_by_dates: az előző dekorátor által átalakított datetime típusú paraméterek alapján az adatbázisból lekérdezést indít.

Ez után már csak annyi a dolgunk a view függvényben hogy a kapott adathalmazon valamilyen műveletet végezzünk és json formában visszaadjuk az eredményt.
A rendszer további aggregációk hozzáadásával nagyon könnyen bővíthető.
