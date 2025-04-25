# Installation


## From Pypi

[dicedb](https://pypi.org/project/dicedb/) can be installed using pip , [uv](https://github.com/astral-sh/uv), 
[poetry](https://python-poetry.org/) or [pdm](https://pdm-project.org/) .

=== "pip"

    ```
    $ pip install dicedb
    ```

=== "uv"

    ```
    $ uv add dicedb
    ```

=== "poetry"

    ```
    $ poetry add dicedb
    ```

=== "PDM"

    ```
    $ pdm add dicedb
    ```


## From Source

<!-- termynal -->
```
$ git clone https://github.com/un4gt/dicedb.git
Cloning into 'dicedb'...
remote: Enumerating objects: 36, done.
remote: Counting objects: 100% (36/36), done.
remote: Compressing objects: 100% (27/27), done.
remote: Total 36 (delta 2), reused 24 (delta 2), pack-reused 0 (from 0)
Receiving objects: 100% (36/36), 24.54 KiB | 318.00 KiB/s, done.
Resolving deltas: 100% (2/2), done.
$ uv sync
Using CPython 3.8.20
Creating virtual environment at: .venv
Resolved 11 packages in 1.08s
      Built dicedb @ file:///E:/some_shit/dicedb
Prepared 1 package in 9.94s
░░░░░░░░░░░░░░░░░░░░ [0/10] Installing wheels...                                                                        
Installed 10 packages in 1.74s
 + colorama==0.4.6
 + dicedb==0.1.1 (from file:///E:/some_shit/dicedb)
 + exceptiongroup==1.2.2
 + iniconfig==2.1.0
 + packaging==24.2
 + pluggy==1.5.0
 + protobuf==5.29.4
 + pytest==8.3.5
 + ruff==0.11.4
 + tomli==2.2.1
$ uv buid
Building source distribution...
Building wheel from source distribution...
Successfully built dist\dicedb-0.1.1.tar.gz
Successfully built dist\dicedb-0.1.1-py3-none-any.whl
```