# cipher_jat2167 

![](https://github.com/julia-tache/cipher_jat2167/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/julia-tache/cipher_jat2167/branch/main/graph/badge.svg)](https://codecov.io/gh/julia-tache/cipher_jat2167) ![Release](https://github.com/julia-tache/cipher_jat2167/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/cipher_jat2167/badge/?version=latest)](https://cipher_jat2167.readthedocs.io/en/latest/?badge=latest)

This cookiecutter creates a boilerplate for a Python cipher project. 

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ cipher_jat2167
```

## Features

 Encodes a string using a Caesar function which shifts each letter n positions in the alphabet based on a numerical input.

## Dependencies

pytest

## Usage

Examples
--------

text = "hello world" 

shift = 2

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

new_text = ''

for c in text:

  index = alphabet.find(c)
  
  if index == -1:
  
    new_text += c
    
  else:
  
    new_index = index + shift if encrypt == True else index - shift
    
    new_index %= len(alphabet)
    
    new_text += alphabet[new_index:new_index+1]
    
return new_text

new_text: "jgnnq yqtnf"

## Documentation

The official documentation is hosted on Read the Docs: https://cipher-tache-julia.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/julia-tache/cipher_jat2167/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
