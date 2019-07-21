# Jupyter Business Demo
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/owen9825/jupyter_demo/blob/master/Kamarian_trade.ipynb)

Here we demonstrate a workflow of how business processes could evolve by 2021, in a way that'll create a staging ground for even greater paradigm shifts after that.

The workflow here is that an "insightful" business analyst will be writing [this report](https://colab.research.google.com/drive/1XX-ejLYYKyq9W-Yo3xqN_PS9a01DV96U) in [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb), while being supported by software engineers ("code monkeys") who will be writing useful code here in this repository.

It shall be shown how business reports can quickly be re-generated, with any assumptions tested against the current state of the world, for the easy spotting of new opportunities and risks.

![A ship in the ocean](https://images.unsplash.com/photo-1527685816164-fa0d282cd89a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1548&q=80 "A ship sailing for trade.")

Note that by convention, programming is conducted in US English, even if the resultant report is in some other language (in this case, British English).

## Purpose
This project demonstrates the quickest and easiest way to introduce programming into the workflow of an executive or any sort of "non-technical" person.

It can be seen that even if business executives implement placeholder functions returning constants, it lays the groundwork for later contributors to turn the thinking into something that's repeatable over a timescale of decades rather than months.

Jupyter notebooks use the [easiest programming language to learn](https://www.quora.com/Is-Python-easy-to-learn), giving access to the state of the art in terms of [natural-language processing](https://www.nltk.org/), [computer vision](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_setup/py_intro/py_intro.html), [web scraping](https://scrapy.org/) and even [monetary transactions](http://blog.ethereum-alarm-clock.com/blog/2016/2/22/introduction-to-the-python-ethereum-ecosystem), enabling you to run a business well into the future, even beyond the extent of your own life.

Note that this is intended as a tutorial, hence there are gaps for excited readers to implement!

## Setup for Business Analysts
* Have a look at the associated [Colab file](https://colab.research.google.com/github/owen9825/jupyter_demo/blob/master/Kamarian_trade.ipynb) and save a copy − this is where you'll be working.
* Go through some of [Google's tutorial](https://colab.research.google.com/notebooks/welcome.ipynb).
* Note that although most of the functionality is meant to come from the code in GitHub, it will be possible for you to create your own functions too, within the Colab document.

If you'd like to export the Colab file for presenting in a more typical way to fellow business executives, the current method is to download the notebook file, then use [nbconvert](https://nbconvert.readthedocs.io/en/latest/usage.html) at the command line in order to generate a file in HTML.
```bash
jupyter nbconvert --to HTML Kamarian_trade.ipynb
```

If you'd like to export to PDF (requires [TeX](https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex)) [the steps are](https://stackoverflow.com/questions/29156653/ipython-jupyter-problems-saving-notebook-as-pdf):
* Download the notebook (`.ipynb`) file.
* Use [nbconvert]() to convert it to LaTeX format.
* Use [xelatex]() to convert the LaTeX format to PDF. If we tried to skip the LaTeX step, the [paths to imagery would be messed up](https://github.com/jupyter/nbconvert/issues/552).

Example usage:


## Setup for Engineers

### IDE Support
* In considering [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment):
  * The [jupyter-notebook](https://atom.io/packages/jupyter-notebook) package for [Atom](https://ide.atom.io/) says that it lacks autocompletion, which is a core reason for using an IDE.
  * PyCharm [only offers support in its Professional edition](https://www.jetbrains.com/help/pycharm/running-jupyter-notebook-cells.html), whereas this code is aimed at newcomers.
  * Editing is possible in Google's [Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb), with the possibility of local or cloud computation.
  * Running a Jupyter notebook locally and accessing it through a browser, both [Chrome](https://www.google.com/intl/en/chrome/) and [Brave](https://brave.com) require users to press `Tab`. Chrome omits showing the actual suggestions.  

### Installation
* Install Python and [Jupyter](https://jupyter.readthedocs.io/en/latest/install.html#installing-jupyter-using-anaconda-and-conda).
* `pip install --requirement requirements.txt`
* If using a [virtual environment](https://virtualenv.pypa.io/en/latest/), you'll need to [create a local Python kernel too](https://medium.com/@eleroy/jupyter-notebook-in-a-virtual-environment-virtualenv-8f3c3448247).
* Set up an account with [Wolfram Alpha](http://wolframalpha.com) and get an API key [here](http://developer.wolframalpha.com/portal/myapps/). 
* You might wish to install [jupyter_contrib_nbextensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions#installation).
* You might like to enable a filter for notebooks in Git repositories, stripping their output so that only the source code is kept in version control.
    * At your command line, run `echo PATH` and choose one of the folders as a place to put your script.    
    * Visit [here](https://gist.github.com/pbugnion/ea2797393033b54674af) and scroll down to find the new script for Jupyter v4. Also note that you should take the suggestion of adding the argument `ensure_ascii=False`. Download the script into your chosen folder.
    * Follow the rest of that script's installation instructions.

### Running
* In the directory where your notebook is saved (and where this `README` file exists), run:
  ```bash
  jupyter notebook
  ```
* Going to «Edit» and «nbextension config», you might wish to enable Python Markdown. Instructions discussed [here](http://www.codehamster.com/author/connygy/).

### Implementation notes
* Notice the awkward importing mechanism imposed by the path mismatch in Google Colab. Explanation is available [here](https://zerowithdot.com/colab-workspace/).

## Troubleshooting
* Feel free to reach out with questions in a public forum, such as [the _Issues_ tab](https://github.com/owen9825/jupyter_demo/issues).

## Future Improvements:
* How do engineers get notified that the business executives want a new function?
* Is there an easier way to export a published version? Ideally it would stay as HTML rather than being printed on trees, so as to keep the accessibility afforded by web browsers, and to maintain the benefits of hyperlinks.
* Include a demonstration of how [Scrapy](https://scrapy.org/) could be included here.
* Include the lunar cycles in the [calculation for shipping distance](/shipping/helpers.py).
* Unit tests for shipping distance.
* Include some financial data for pig futures markets.
* Include some data directly from Google Drive.

## See Also:
For further discussion regarding the reasoning behind integrating Jupyter notebooks into business operations, you may be interested in:
* [Spreadsheets Are Sabotaging Your Business](https://www.applicoinc.com/blog/spreadsheets-sabotaging-business/)
* [Basilisk-Centered Design](https://www.linkedin.com/pulse/basilisk-centered-design-owen-miller/)
