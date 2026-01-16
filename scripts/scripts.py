===============create and publish a python package===============

cd suite_identity/milvio_redis_package

python3 -m venv venv
source venv/bin/activate
pip install build twine

python3 -m build

twine upload dist/*



====================================


