from .parser import DLSyntaxParser
from .owl2sparql.converter import Owl2SparqlConverter


class DescriptionLogicConcept:
    def __init__(self, dl_str: str, namespace: str):
        assert isinstance(dl_str, str) and isinstance(namespace, str)
        assert len(dl_str) > 0 and len(namespace) > 0
        self.name = DLSyntaxParser(namespace=namespace).parse_expression(expression_str=dl_str)


class SPARQLQuery:
    def __init__(self, root_variable='?x', dl_concept=None, only_named_individuals=True):
        self.str = Owl2SparqlConverter().as_query(root_variable=root_variable,
                                                  ce=dl_concept.name, count=False,
                                                  values=None, named_individuals=only_named_individuals)

    def __str__(self):
        return self.str
