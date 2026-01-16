===============create and publish a python package===============

cd milvio_package

# Use existing venv or create new one
# python3 -m venv .venv
# source .venv/bin/activate
pip install build twine

# Build
rm -rf dist build *.egg-info
python3 -m build

# Publish to PyPI
# You will be prompted for your username (__token__) and password (your PyPI API token)
twine upload dist/*



