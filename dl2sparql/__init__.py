"""OWLAPY

loosely based on OWL API

many help texts copied from OWL API [1]
OWLAPI licence: LGPL and Apache

[1] https://github.com/owlcs/owlapi
"""

from .core import DescriptionLogicConcept, SPARQLQuery
# the import order must be fixed otherwise there are circular import errors
import dl2sparql.model  # noqa: F401
