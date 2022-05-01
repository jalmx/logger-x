!#/bin/bash

source ./bin/activate
pip install build setuptools wheel twine

python -m build --sdist --wheel --outdir dist/ #build
