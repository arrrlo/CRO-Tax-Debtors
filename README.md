<h1>Cro Tax Deptors</h1>



<p>Parse and search data from Croatian Tax Deptors website.</p>

<h2>Installation</h2>


```
pip install cro-tax-deptors
```

<h2>CLI</h2>

```
Usage: crotaxdeptors [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  find
  parse
```

<p>Parse data from website:</p>

```
Usage: crotaxdeptors parse [OPTIONS]

Options:
  -p, --print_in_terminal  Print in terminal
  --help                   Show this message and exit.
```

<p>Search through scraped data:</p>

```
Usage: crotaxdeptors find [OPTIONS]

Options:
  -n, --name TEXT  Name of the deptor
  --help           Show this message and exit.
```

<p>Delete all data:</p>

```
Usage: crotaxdeptors delete [OPTIONS]

Options:
  --help           Show this message and exit.
```
