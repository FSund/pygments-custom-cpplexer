# pygments-custom

A custom lexer for [Pygments](http://pygments.org/) for extra keyword
highlighting when using the [minted](https://github.com/gpoore/minted)
package in LaTeX. This was inspired by [FSund's Molecular
Dynamics]{https://github.com/FSund/pygments-custom-cpplexer.git}.

You can define any identifier (e.g., `vec3`) to be any of the subtypes
of `Keyword` that pygments recognizes (or, in fact, any token at all).
As of 2023, pygments uses:

* `Keyword.Type`  ← This is probably what you want.
* `Keyword.Constant`
* `Keyword.Declaration`
* `Keyword.Namespace`
* `Keyword.Pseudo`
* `Keyword.Removed`
* `Keyword.Reserved`
* `Keyword` (a generic Keyword token)

By default, it inherits from the C Lexer, but that is easily changed.

## Customization

Edit the file [pygments_custom/__init.py__](pygments_custom/__init.py__).

### Changing the super class

The default super class is "C" as seen in the first line of `__init.py__`:

``` python
from pygments.lexers.compiled import CLexer as mysuper
```

To inherit from the C++ lexer, for example, one would change it to say:
``` python
from pygments.lexers.compiled import CppLexer as mysuper
```

## Install

    git clone 
    cd pygments-custom
    (sudo) python setup.py install

### Verify

Verify that the package installed correctly by checking if "custom" is
in the list of lexers. You can run:

    pygmentize -L lexers | grep custom

## Using the lexer in latex

Just use the **custom** "language". In LaTeX this means something like this

``` latex
\begin{minted}{custom}
vec3 position(0.0, 0.0, 0.0);
Atom *atom = new Atom(position);
\end{minted}

```

You can test it using the [example.ltx](example.ltx) file like so:

    pdflatex -shell-escape example.ltx

See the minted package at https://github.com/gpoore/minted for more information.
