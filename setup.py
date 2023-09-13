from setuptools import setup, find_packages
with open('README.md', 'r') as fh:
    long_description = fh.read()
setup(
    name="dl2sparql",
    description="Description Logic Concept to SPARQL query",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "pandas",
        "parsimonious",
        "rdflib"],
    author='Caglar Demir',
    author_email='caglardemir8@gmail.com',
    url='https://github.com/dice-group/DL2SPARQL',
    classifiers=[
        "Programming Language :: Python :: 3.9.18",
        "License :: OSI Approved :: MIT License"],
    python_requires='>=3.9.18',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
