# DL2SPARQL: Description Logic Concept to SPARQL Query

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
from dl2sparql import DescriptionLogicConcept, SPARQLQuery
ce_str = "∃hasChild.Male"
concept = DescriptionLogicConcept(dl_str="∃hasChild.Male", namespace="http://www.benchmark.org/family#")
query = SPARQLQuery(dl_concept=concept)
"""
SELECT
 DISTINCT ?x WHERE { 
?x a <http://www.w3.org/2002/07/owl#NamedIndividual> . 
?x <http://www.benchmark.org/family#hasChild> ?s_1 . 
?s_1 a <http://www.benchmark.org/family#Male> . 
 }
"""
```
For any questions or wishes, please contact:  ```caglar.demir@upb.de``` or ```caglardemir8@gmail.com```