# pygments-custom-cpplexer

A custom C++-lexer for Pygments, for my master thesis. Adds some extra keywords like *Atom*, *System* and *vec3*.

## Install

### Using PyPI and pip

    $ (sudo) pip install pygments-mdcpp


### Manual

    $ git clone https://github.com/FSund/pygments-custom-cpplexer.git
    $ cd pygments-custom-cpplexer
    $ (sudo) python setup.py install

## Using the lexer in latex

Just use the **mdcpp** "language". In LaTeX this means something like this

    \begin{minted}{mdcpp}
    vec3 position(0.0, 0.0, 0.0);
    Atom *atom = new Atom(position);
    \end{minted}

See the minted package at https://github.com/gpoore/minted for more information.
