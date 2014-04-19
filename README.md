seer
====

A simple and intuitive interface for managing and maintaining cloud-based infrastructure.

Objective
---------

The objective of 'seer' is to quickly and efficiently allocate, convert, and maintain cloud servers spanning different providers and networks. Ideally, this would be a one-stop-shop, for cloud automation and maintenance.

Setup
-----

Install dependencies:

```
$ pip install -r requirements.txt
```

Create your `credentials` file, which should look something like:

```
[aws]
access_key = XXXXXXXXXXX
secret_key = XXXXXXXXXXXXXXXXXXXXXXXXX
```

And then start the CLI, by executing `cli.py`:

```
$ ./cli.py
```
