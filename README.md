# swrlcli
CLI tool for working with SWRL rules

## Usage

Install swrlcli by running the following from the root directory 

```
python3 -m pip install -e .
```

To reason over an ontology with a rule and output the result in the same folder as the input ontology, run

```
swrlcli path/to/rules.txt path/to/ontology.owl
```

To write the inferred facts to a separate file run
```
swrlcli path/to/rules.txt path/to/separate.owl
```

## Developing

To run the unit tests, run the following from `swrlcli/swrlcli`,

```commandline
python3 -m pytest
```