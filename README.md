# pypack

https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-archives
----------------------------------------------------------------


pyenv virtualenv venv
source activate venv

python -m pip install --upgrade pip
python -m pip install --upgrade setuptools

python -m pip install --upgrade build
python -m pip install --upgrade twine

python -m build
python -m twine upload --repository testpypi dist/*

===================================================
pip install -i https://test.pypi.org/simple/ newlib-vlakondra

