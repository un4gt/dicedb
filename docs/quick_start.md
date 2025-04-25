# Quick Start

## Connect to DiceDB server

Before starting, install DiceDB by [installation | DiceDB](https://dicedb.io/get-started/installation/) .

```python
from dicedb import Dice

dice = Dice('localhost', 7379)
```

!!! note "`try_to_convert` settings"
    Because of DiceDB `res.proto` definition, some int value returned from server is `string` type .
    If you want to convert it to `int` type, set `try_to_convert=True` in `Dice` constructor.
    ```python
    from dicedb import Dice

    dice = Dice('localhost', 7379, try_to_convert=True)
    ```
    This will try to convert str-int to int, return `int` type if success, otherwise return `str` type.
    Maybe this will be fixed in the future, but for now, this is the only way to do it.


## `PING`

just `PING`: 

```python
from dicedb import Dice

dice = Dice('localhost', 7379)
dice.ping()
```

or with `message`:

```python
dice.ping('hello')  # return: 'PONG hello'
```

## `SET` and `GET`

```python
dice.set('k-set', 'v-set')
dice.set('k-set', 'v-set', ex=10)
dice.set('k-set', 'v-set', keep_ttl=True)
dice.get('k-set')
```



After that, check out [commands](./commands.md)  