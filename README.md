## Installation
* Install [https://github.com/ipython-contrib/jupyter_contrib_nbextensions#installation](jupyter_contrib_nbextensions) and its prerequisites (pip or conda).
* Enable the extensions: `jupyter contrib nbextension install --user`
* Install this project's extra requirements: `pip install --requirement requirements.txt`

## Running
* In the directory where your notebook is saved (and where this README file exists), run:
  ```bash
  jupyter notebook
  ```
* Go to «Edit», «nbextension config» and enable Python Markdown. Instructions discussed [here](http://www.codehamster.com/author/connygy/).

## Troubleshooting
* Is Jupyter reporting that there are duplicate installations? [Link](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator/issues/25)