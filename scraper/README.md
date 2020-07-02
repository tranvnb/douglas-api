## Project structure for Scraper
Content reference from **[How to set up a python project and development environment](https://www.samueldowling.com/2020/06/08/how-to-set-up-a-python-project-and-development-environment/)**.

```
    Scraper/
    ├── src/
    │   └──packagename/
    │       ├── __init__.py
    │       ├── subpackage1/
    │       │   ├── __init__.py
    │       │   ├── subpackage1.py
    │       ├── subpackage2/
    │       │   ├── __init__.py
    │       │   ├── subpackage2.py
    │       └── subpackage3/
    │           ├── __init__.py
    │           ├── subpackage3.py
    ├── tests/
    │   ├── test_subpackage1.py
    │   └── test_subpackage2.py
    ├── docs/
    │    └── Makefile
    ├── .gitignore
    ├── Makefile
    ├── Dockerfile
    ├── requirements.txt
    ├── dev-requirements.in
    ├── dev-requirements.txt
    ├── setup.py
    ├── LICENSE
    └── README.md
```
## Setup Python virtual environment
This environment is isolated from the other Python projects and uses an independent libs, modules, ect

```
    $ cd Scraper
    $ pip install virtualenv
    $ virtualenv venv
    $ which python # to find which version you are using
    ...
    # switch interpretor if you want
    $ virtualenv --python=/usr/bin/python3.6 venv 
    ...
    $ source venv/bin/activate
```

## View and edit dependencies libraries for development
```
    $ cat dev-requirements.in
    pip-tools
    pytest
```

To add more required dependencies, open and add library name to setup.py
```
	....
	install_requires=[
        'requests',
		'beautifulsoup4',
		'your_required_libs==version'*
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ]
    .....
```

Run update dependencies 
```
	make update-deps
```
## Run app
Base on setting in your **setup.py**
```
	....
	#setup
	entry_points={
        'console_scripts': [
            'courses = courses:main',#call to function main in __init__.py in folder courses
        ]
    },
```
Call 
```
	$ courses
```
## Testing
