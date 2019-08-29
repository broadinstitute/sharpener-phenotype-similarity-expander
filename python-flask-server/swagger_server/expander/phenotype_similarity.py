
from swagger_server.models.transformer_info import TransformerInfo
from swagger_server.models.parameter import Parameter
from swagger_server.models.transformer_query import TransformerQuery
from swagger_server.models.gene_info import GeneInfo
from swagger_server.models.attribute import Attribute

import requests
from translator_modules.module1.module1b import PhenotypicallySimilarGenes

def expander_info():
    """
        Return information for this expander
    """
    return TransformerInfo(
        name = 'Functional Similarity with Shared GO Terms',
        function = 'expander',
        parameters = [
            Parameter(
                name='similarity threshold',
                type='double',
                default='0.5'
            )
        ]
    )


def expand(query: TransformerQuery):
    """
        Execute this expander, find all genes correlated to query genes.
    """
    controls = {control.name: control.value for control in query.controls}
    # try:
    threshold = float(controls['similarity threshold'])
    genes = {}

    psg = PhenotypicallySimilarGenes(query.genes, threshold, file=False)
    results = psg.results.to_dict('records')

    query_gene_ids = [gene.gene_id for gene in query.genes]

    for gene in query.genes:
        for result in results:
            gene_id = result['hit_id']
            symbol = result['hit_symbol']
            similarity = result['score']
            shared_terms = list(result['shared_terms'])

            if gene_id != gene.gene_id:
                gene = GeneInfo(gene_id=gene_id,
                                attributes=[
                                    Attribute(
                                        name='phenotype_similarity',
                                        value=str(similarity),
                                        source='Phenotype Similarity'
                                    ),
                                    Attribute(
                                        name='Shared GO Terms',
                                        value=str(shared_terms),
                                        source='Phenotype Similarity'
                                    )
                                ])
                genes[gene_id] = gene
            elif gene_id == gene.gene_id:

                gene.attributes.append(
                    Attribute(
                        name='phenotype_similarity',
                        value=str(similarity),
                        source='Phenotype Similarity'
                    )
                )
                gene.attributes.append(
                    Attribute(
                        name='Shared GO Terms',
                        value=str(shared_terms),
                        source='Phenotype Similarity'
                    )
                )
                genes[gene_id] = gene


    return list(genes.values())

    # except ValueError:
    #     msg = "invalid similarity threshold: '"+controls['similarity threshold']+"'"
    #     return ({ "status": 400, "title": "Bad Request", "detail": msg, "type": "about:blank" }, 400 )


# CORR_URL = 'https://indigo.ncats.io/gene_knockout_correlation/correlations/{}'

