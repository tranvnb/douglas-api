## Project structure for Scraper

```
    Scraper/
    ├── src/
    │   └──packagename/
    │       ├── __main__.py
    │       ├── subpackage1/
    │       │   ├── __main__.py
    │       │   ├── subpackage1.py
    │       ├── subpackage2/
    │       │   ├── __main__.py
    │       │   ├── subpackage2.py
    │       └── subpackage3/
    │           ├── __main__.py
    │           ├── subpackage3.py
    ├── tests/
    │   ├── test_subpackage1.py
    │   └── test_subpackage2.py
    ├── .gitignore
    ├── requirements.txt
    ├── Pipfile
    ├── Pipfile.lock
    ├── LICENSE
    └── README.md
```
## Setup Python working environment

Assuming that you already have pip installed on your system, otherwise these below steps won't work
	
1. Install pipenv and create .venv folder
	```
		$ pip install pipenv
		$ pipenv install --python 3
		$ PIPENV_VENV_IN_PROJECT=1 pipenv install 
	```
2. Install all your required libraries from Pipfile.lock or add more libraries

	```
	    $ PIPENV_VENV_IN_PROJECT=1 pipenv install
	    $ PIPENV_VENV_IN_PROJECT=1 pipenv install requests beautifulsoup4
	```
3. If you already have requirements.txt file, then import it 
	```
		$ PIPENV_VENV_IN_PROJECT=1 pipenv install -r path/to/requirements.txt
	```

4. Start working on virtual environment
	```
		pipenv shell
	```
5. Run a script
	```
		$ python src/packagename #eg: python src/programs PBDCIS
	```
## Testing
