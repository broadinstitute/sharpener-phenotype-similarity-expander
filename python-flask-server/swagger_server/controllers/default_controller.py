import connexion
import six

from swagger_server.models.gene_info import GeneInfo  # noqa: E501
from swagger_server.models.transformer_info import TransformerInfo  # noqa: E501
from swagger_server.models.transformer_query import TransformerQuery  # noqa: E501
from swagger_server import util


from swagger_server.expander.phenotype_similarity import expander_info
from swagger_server.expander.phenotype_similarity import expand

def transform_post(query):  # noqa: E501
    """transform_post

     # noqa: E501

    :param query: transformer query
    :type query: dict | bytes

    :rtype: List[GeneInfo]
    """
    if connexion.request.is_json:
        query = TransformerQuery.from_dict(connexion.request.get_json())  # noqa: E501
    return expand(query)


def transformer_info_get():  # noqa: E501
    """transformer_info_get

     # noqa: E501


    :rtype: TransformerInfo
    """
    return expander_info()
