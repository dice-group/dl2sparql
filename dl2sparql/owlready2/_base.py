import logging
import random
from datetime import date, datetime
from enum import Enum, auto
from itertools import chain
from types import MappingProxyType
from typing import Iterable, Set, Final, List

from pandas import Timedelta

from owlapy.owlready2 import axioms
from owlapy import namespaces
from owlapy.ext import OWLReasonerEx
from owlapy.model import OWLObjectPropertyRangeAxiom, OWLOntologyManager, OWLDataProperty, OWLObjectProperty, \
    OWLNamedIndividual, OWLClassExpression, OWLObjectPropertyExpression, OWLOntologyID, OWLAxiom, OWLOntology, \
    OWLOntologyChange, AddImport, OWLThing, DoubleOWLDatatype, OWLObjectPropertyDomainAxiom, OWLLiteral, \
    OWLObjectInverseOf, BooleanOWLDatatype, IntegerOWLDatatype, DateOWLDatatype, DateTimeOWLDatatype, OWLClass, \
    DurationOWLDatatype, StringOWLDatatype, IRI, OWLDataPropertyRangeAxiom, OWLDataPropertyDomainAxiom, OWLClassAxiom, \
    OWLSubClassOfAxiom, OWLEquivalentClassesAxiom, OWLObjectSomeValuesFrom
