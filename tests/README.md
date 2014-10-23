## Leírás

Főleg funkcionális teszteket, illetve néhány unit tesztet valósítottam meg a `py.test` framework használatával. A lényeges funkcionalitás (pl. API endpointok) 100%-osan lefedettek, a kevésbé hangsúlyos részek, illetve a manuális tesztelést jobban igénylők (GUI, parancssoros alkalmazás) nem.


## Teszt lefedettség

```bash
$ coverage report                                                                                                                         [12:39:29 de]
Name                          Stmts   Miss  Cover
-------------------------------------------------
logcollector/__init__            29      0   100%
logcollector/commands            42     42     0%
logcollector/forms               24     12    50%
logcollector/models              16      0   100%
logcollector/moving_average      12      0   100%
logcollector/views               40      7    82%
tests/conftest                   13      0   100%
tests/test_moving_average        12      0   100%
tests/test_views                 77      0   100%
-------------------------------------------------
TOTAL                           265     61    77%
```

## Tesztek futtatása (telepítés után)

```bash
$ py.test -vv
==================================================================== test session starts =====================================================================
platform darwin -- Python 3.4.2 -- py-1.4.25 -- pytest-2.6.3 -- /Users/walkman/.virtualenvs/logcollector/bin/python3.4
collected 22 items

tests/test_moving_average.py::test_zeroes_only PASSED
tests/test_moving_average.py::test_simple_dataset PASSED
tests/test_moving_average.py::test_simple_dataset2 PASSED
tests/test_moving_average.py::test_complicated_dataset PASSED
tests/test_views.py::test_can_post_new_data PASSED
tests/test_views.py::TestMean::test_mean PASSED
tests/test_views.py::TestMean::test_mean_with_dim1 PASSED
tests/test_views.py::TestMean::test_mean_with_dim2 PASSED
tests/test_views.py::TestMean::test_mean_with_dim1_and_dim2 PASSED
tests/test_views.py::TestMin::test_min PASSED
tests/test_views.py::TestMin::test_min_with_dim1 PASSED
tests/test_views.py::TestMin::test_min_with_dim2 PASSED
tests/test_views.py::TestMin::test_min_with_dim1_and_dim2 PASSED
tests/test_views.py::TestMax::test_max PASSED
tests/test_views.py::TestMax::test_max_with_dim1 PASSED
tests/test_views.py::TestMax::test_max_with_dim2 PASSED
tests/test_views.py::TestMax::test_max_with_dim1_and_dim2 PASSED
tests/test_views.py::TestStandardDeviation::test_standard_deviation PASSED
tests/test_views.py::TestStandardDeviation::test_standard_deviation_with_dim1 PASSED
tests/test_views.py::TestStandardDeviation::test_standard_deviation_with_dim2 PASSED
tests/test_views.py::TestStandardDeviation::test_standard_deviation_with_dim1_and_dim2 PASSED
tests/test_views.py::TestMovingAverage::test_moving_average PASSED

================================================================= 22 passed in 0.44 seconds ==================================================================
```
