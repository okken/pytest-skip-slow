# pytest-skip-slow

A pytest plugin to skip `@pytest.mark.slow` tests by default. 
Include the slow tests with `--slow`.

## Installation

```
$ pip install pytest-skip-slow
```

## Usage

Example `test_slow.py`:

```python
import pytest

def test_normal():
    pass

@pytest.mark.slow
def test_slow():
    pass
```

Normal pytest sessions skip slow tests:

```shell
(venv) $ pytest -v test_slow.py
========================= test session starts ==========================
collected 2 items                                                      

test_slow.py::test_normal PASSED                                 [ 50%]
test_slow.py::test_slow SKIPPED (need --slow option to run)      [100%]

===================== 1 passed, 1 skipped in 0.00s =====================
```

Include the slow tests with `--slow`.


```shell
(venv) $ pytest -v --slow test_slow.py
========================= test session starts ==========================
collected 2 items                                                      

test_slow.py::test_normal PASSED                                 [ 50%]
test_slow.py::test_slow PASSED                                   [100%]

========================== 2 passed in 0.00s ===========================
```
