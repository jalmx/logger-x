# Logger X

A logger for my apps

## Install

```bash
pip install loggerx -U
```

## Use

```python
log = LogX(__name__, level=logging.DEBUG)

log.i("information",...)
log.e("e", e.message)
log.w("warning", )
log.i("information", msg)
log.d("Debug", msg)
```

## Test

```
python3 -m venv . #inside repo
source bin/activate
pip install -r requirements.txt

pytest # run tests
```

## Build documentation


```bash
mkdocs build #pendiente
```
