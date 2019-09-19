
from swagger_server.models.transformer_info import TransformerInfo
from swagger_server.models.parameter import Parameter
from swagger_server.models.transformer_query import TransformerQuery
from swagger_server.models.gene_info import GeneInfo
from swagger_server.models.gene_info_identifiers import GeneInfoIdentifiers
from swagger_server.models.attribute import Attribute

import json
import requests
from translator_modules.gene.gene.phenotype_similarity import PhenotypicallySimilarGenes

NAME = 'Phenotype similarity'
THRESHOLD = 'similarity threshold'

def expander_info():
    """
        Return information for this expander
    """
    global NAME, THRESHOLD
    with open("transformer_info.json",'r') as f:
        info = TransformerInfo.from_dict(json.loads(f.read()))
        NAME = info.name
        THRESHOLD = info.parameters[0].name
        return info


def expand(query: TransformerQuery):
    """
        Execute this expander, find all genes correlated to query genes.
    """
    controls = {control.name: control.value for control in query.controls}

    threshold = float(controls[THRESHOLD])
    gene_list = []
    genes = {}
    for gene in query.genes:
        gene_list.append(gene)
        genes[gene.gene_id] = gene

    psg = PhenotypicallySimilarGenes(query.genes, threshold)
    results = psg.results.to_dict('records') if len(psg.results)>0 else []

    for result in results:
        gene_id = result['hit_id']
        hgnc = gene_id if gene_id.startswith('HGNC:') else None
        symbol = result['input_symbol']
        similarity = result['score']
        shared_terms = list(result['shared_terms'])
        shared_term_names = list(result['shared_term_names'])

        if gene_id not in genes:
            gene = GeneInfo(
                gene_id=gene_id,
                identifiers=GeneInfoIdentifiers(hgnc=hgnc),
                attributes=[]
            )
            gene_list.append(gene)
            genes[gene_id] = gene

        gene = genes[gene_id]
        gene.attributes.append(
            Attribute(
                name='phenotype_similarity to '+symbol,
                value=str(similarity),
                source=NAME
            )
        )
        gene.attributes.append(
            Attribute(
                name='Shared HPO term ids with '+symbol,
                value=str(shared_terms),
                source=NAME
            )
        )
        gene.attributes.append(
            Attribute(
                name='Shared HPO terms with '+symbol,
                value=str(shared_term_names),
                source=NAME
            )
        )

    return gene_list


