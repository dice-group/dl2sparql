# Description Logic Concept to SPARQL Query
# Installation

```bash
conda create -n dl2sparql python=3.9 --no-default-packages && conda activate dl2sparql
pip3 install pytest
pip3 install pandas
pip3 install parsimonious
pip3 install rdflib
# To test it
pytest tests
```

```python
from dl2sparql.parser import DLSyntaxParser
from dl2sparql.owl2sparql.converter import Owl2SparqlConverter
ce_str = "∃hasChild.Male"
ce_parsed = DLSyntaxParser(namespace="http://www.benchmark.org/family#").parse_expression(expression_str=ce_str)
sparql_query = Owl2SparqlConverter().as_query(root_variable='?x', 
                                              ce=ce_parsed, count=False,
                                              values=None, named_individuals=True)
```
