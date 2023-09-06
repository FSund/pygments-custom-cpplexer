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

Edit the file [pygments_custom/__init.py__](pygments_custom/__init.py__)
and simply list the keywords in the array you'd like. For example:

``` python
EXTRA[Keyword.Type] = ['FLAG', 'vec3', 'Atom' ]
EXTRA[Keyword.Constant] = [ 'M_PI', 'Tau' ]
```

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

    git clone https://github.com/hackerb9/pygments-custom
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

## Problems

* If after changing the __init__.py and reinstalling the module, it
  doesn't seem to have an effect in latex, try removing the
  `_minted-filename` directory which caches the pygments lexer.

  If you will be editing the lexer often, you may wish to disable the
  cache completely like so:
  
  ```latex
  \usepackage[cache=false]{minted}
  ```
  
* Different Keyword subtypes may not look different depending on the
  inherited lexer and the style chosen. When subclassing from CLexer
  and using the default style, Keyword.Constant, Keyword.Declaration,
  Keyword.Namespace, Keyword.Pseudo, and Keyword.Reserved all look the
  same as a generic Keyword.

