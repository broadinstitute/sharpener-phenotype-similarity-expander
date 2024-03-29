#!/usr/bin/env python3

import connexion

from swagger_server import encoder

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'API for an expander based on phenotype similarity'})

def main():
    app.run(port=8081)


if __name__ == '__main__':
    main()
