# metabase_file_import
This is a project of the company [Open Source Politics](https://opensourcepolitics.eu), based on the [python-app template](https://github.com/OpenSourcePolitics/python-app/).

Purpose is to provide a simple way to send data from a local data file to a database already linked in Metabase

## Getting started
Requirements : 
- [**Python 3**](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org) (TL;DR run `curl -sSL https://install.python-poetry.org | python3 -` should work)

1. Clone and setup repository :
```python
git clone https://github.com/OpenSourcePolitics/metabase_file_import.git
cd metabase_file_import
poetry install
cp metabase_file_import/config-example.py metabase_file_import/config.py
```
2. Complete the `config.py` file with database informations
3. `poetry run main`
4. Follow instructions


## Contribute
- [Create an issue](https://github.com/OpenSourcePolitics/metabase_file_import/issues) to report a bug/ask for a new feature
- [Fork this project](https://github.com/OpenSourcePolitics/metabase_file_import/issues) to make your changes and make a PR

## License
This software is licensed under the GNU AGPLv3, which states that **you can use, modify and redistribute this software as long as you publish the modifications under the same license.**
For more information, check [here](https://www.gnu.org/licenses/agpl-3.0.html)