# sharpener-phenotype-similarity-expander

Gene-list expander based on phenotype similarity

Transform query example:

```
{
  "genes": [
    {
      "gene_id": "NCBIGene:100",
      "attributes": [
        {
          "name": "entrez_gene_id",
          "value": "100",
          "source": "query gene"
        },
        {
          "name": "gene_symbol",
          "value": "ADA",
          "source": "query gene"
        }
      ]
    },
    {
      "gene_id": "NCBIGene:2036",
      "attributes": [
        {
          "name": "entrez_gene_id",
          "value": "2036",
          "source": "query gene"
        },
        {
          "name": "gene_symbol",
          "value": "EPB41L1",
          "source": "query gene"
        }
      ]
    }
  ],
  "controls": [
    {
      "name": "similarity threshold",
      "value": "0.25"
    }
  ]
}
```