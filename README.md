## Installation
* I found that Jupyter doesn't play nicely with virtualenv, so I discourage you from trying it either. Alternatively, please propose how I can get Jupyter to contain itself in virtualenv :)
* Install [https://github.com/ipython-contrib/jupyter_contrib_nbextensions#installation](jupyter_contrib_nbextensions) and its prerequisites (pip or conda).
* Enable the extensions: `jupyter contrib nbextension install --user`
* Enable a filter for notebooks in Git repositories, stripping their output so that only the source code is kept in version control.
    * At your command line, run `echo PATH` and choose one of the folders as a place to put your script.    
    * Visit [here](https://gist.github.com/pbugnion/ea2797393033b54674af) and scroll down to find the new script for Jupyter v4. Also note that you should take the suggestion of adding the argument `ensure_ascii=False`. Download the script into your chosen folder.
    * Follow the rest of that script's installation instractions.
* Install this project's extra requirements: `pip install --requirement requirements.txt`

## Running
* In the directory where your notebook is saved (and where this README file exists), run:
  ```bash
  jupyter notebook
  ```
* Go to «Edit», «nbextension config» and enable Python Markdown. Instructions discussed [here](http://www.codehamster.com/author/connygy/).

## Troubleshooting
* Is Jupyter reporting that there are duplicate installations? [Link](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator/issues/25)
* I had problems with the filtering of cell output in Git. I had to follow [this guide](https://stackoverflow.com/questions/18734739/using-ipython-notebooks-under-version-control).