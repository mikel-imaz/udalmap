# udalmap
A wrapper for Udalmap API

[![Project Status: In Development](https://img.shields.io/badge/status-in--development-orange)](#)

## Description
The goal of the project is to develop a simple Python library for easy access to this API.

The Udalmap API offers access to over 200 municipal indicators, providing insights into the realities of municipalities within the Basque Autonomous Community (Spain). It covers key areas such as the economy and competitiveness, social cohesion, quality of life, the environment, and mobility.
https://www.euskadi.eus/informacion-municipal-udalmap/web01-s2oga/es/

## ⚠️ Project Status: In Development
This project is currently **under active development**.

## Installation
_udalmap_ will be available on the Python Package Index (PyPI) once it's ready.  
In the meantime, you can download the source code from this repo and install it yourself.

## Usage
Once you have installed the package, you can proceed this way to start exploring the data:
```python
# Import
from udalmap.utils import UdmDf

# Instantiate
udm = UdmDf()

# Use
udm.find()
```
As an example, I leave a Jupyter notebook to show how to start exploring data using the methods of this class.