# swrlcli
CLI tool for working with SWRL rules

## Usage

Install the utility with 

```
python3 -m pip install -e .
```

Run the CLI as 

```
swrlcli --rules path/to/rules.txt --onto path/to/ontology.owl
```

## Developing

To run the unit tests, run the following from `swrlcli/swrlcli`,

```commandline
python3 -m pytest
```