# Welcome to dicedb

Dicedb - A simple DiceDB client for Python.

⚠️ This is not an official sdk for python and still in development.

[dicedb](https://pypi.org/project/dicedb/) requires a running [Dice](https://github.com/DiceDB/dice), and Python 3.8+ .


## Supported Commands

|    command    | description  |
|:-------------:|:------------:|
|    `decr`     |   `DECRBY`   |
|   `decrby`    |   `DECRBY`   |
|   `delete`    |    `DEL`     |
|    `echo`     |    `ECHO`    |
|   `exists`    |   `EXISTS`   |
|   `expire`    |   `EXPIRE`   |
|  `expire_at`  |  `EXPIREAT`  |
| `expire_time` | `EXPIRETIME` |
|   `flushdb`   |  `FLUSHDB`   |
|     `get`     |    `GET`     |
|   `get_del`   |  `GET_DEL`   |
|   `get_ex`    |   `GET_EX`   |
|    `hget`     |    `HGET`    |
|  `hget_all`   |  `HGETALL`   |
|    `hset`     |    `HSET`    |
|   `incr_by`   |   `INCRBY`   |
|    `incr`     |   `INCRBY`   |
|    `ping`     |    `PING`    |
|     `ttl`     |    `TTL`     |
|   `typeof`    |    `TYPE`    |
|     `set`     |    `SET`     |


## Roadmap

- [ ] More documentation/tests/examples
- [ ] Support for all commands
- [ ] Support `WATCH` mode
- [ ] Connection pool
- [ ] Support for async
- [ ] Fully typed