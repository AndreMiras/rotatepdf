# rotatepdf

[![Tests](https://github.com/AndreMiras/rotatepdf/actions/workflows/tests.yml/badge.svg)](https://github.com/AndreMiras/rotatepdf/actions/workflows/tests.yml)

Rotate pdf pages from command line.

## How to use

Here is an example for rotating page 1 to page 3 by 90 degrees clockwise.

```shell
rotatepdf.py --src src.pdf --dst dst.pdf --rotate-right 1-3
```

It's also possible to rotate in multiple ways in one go.

```shell
rotatepdf.py --src src.pdf --dst dst.pdf --rotate-right 1-3 --rotate-180 4-10
```

## Installing

```shell
pip install -e git://github.com/AndreMiras/rotatepdf.git#egg=rotatepdf
```

## Dev

Run tests:

```shell
make pytest
# or
tox -e py
```

Lint:

```shell
make lint
```

Format:

```shell
make format
```
