# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "phenotype-similarity-expander"
VERSION = "1.3.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="HPO phenotype similarity",
    author_email="",
    url="",
    keywords=["Swagger", "HPO phenotype similarity"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Gene-list expander based on phenotype similarity using shared  terms from Human Phenotype Ontology (https://hpo.jax.org/app/).
    """
)

