# pygments-custom

A custom lexer for [Pygments](http://pygments.org/) for easily adding
extra keyword highlighting by setting environment variables. This
module works with any tool that uses Pygments, and is specifically
designed for the [minted](https://github.com/gpoore/minted) package in
LaTeX.

## Example usage

<ul>

`export PYGMENTS_CUSTOM_TYPE="[ 'vec3', 'Atom', 'System' ]"`<br/>
`pygmentize -l custom `[`example.c`](examples/example.c)<br/>
`pdflatex `[`example.ltx`](examples/example.ltx)<br/>

</ul>

## Example output

[![Custom Keyword example][screenshot]](examples/example.pdf)

See the full [example.pdf](examples/example.pdf).

[screenshot]: README.md.d/2custom.png "Click to see full PDF"

## Capabilities

You can define any identifier (e.g., `vec3`) to be any of the subtypes
of `Keyword` that pygments recognizes. As of 2023, pygments uses:

* `Keyword.Type`  ← This is probably what you want.
* `Keyword.Constant`
* `Keyword.Declaration`
* `Keyword.Namespace`
* `Keyword.Pseudo`
* `Keyword.Removed`
* `Keyword.Reserved`
* `Keyword` (a generic Keyword token)

By default, the CustomLexer inherits Keywords from the C Lexer, but
that is easily changed by setting the PYGMENTS_CUSTOM_BASE_LEXER
environment variables.

### Limitations

* Does not handle regular expressions or Tokens other than Keyword.
* Does not change the Style.

## Customization

New keywords can be highlighted as Type, Constant, Namespace,
Declaration, Pseudo, Removed, Reserved, or plain old Keyword. To
add keywords, set the environment variables `PYGMENTS_CUSTOM_TYPE`,
`PYGMENTS_CUSTOM_CONSTANT`, ..., `PYGMENTS_CUSTOM_KEYWORD`.

Each variable is a Python list (square brackets surrounding a
comma separated list of quoted strings). For example, this
highlights new types (e.g., classes or typedefs):

	export PYGMENTS_CUSTOM_TYPE="[ 'vec3', 'Atom', 'System' ]"


### Choosing the base lexer class to build upon

The default base class for CustomLexer is the C language lexer,
"CLexer" from `pygments.lexer`.

Pygments comes with over 500 lexers (listed below). To inherit from a
different lexer, set the `PYGMENTS_CUSTOM_BASE_LEXER` environment
variable. For example. to extend C++ syntax highlighting, one would do
this:

``` python
export PYGMENTS_CUSTOM_BASE_LEXER=CppLexer
```

## Install

    git clone https://github.com/FSund/pygments-custom-cpplexer.git
    cd pygments-custom
    (sudo) python setup.py install

### Verify

Verify that the package installed correctly by checking if "custom" is
in the list of lexers. You can run:

    pygmentize -L lexers | grep custom

## Using the lexer in latex

Use the **custom** "language". In LaTeX this means something like this

``` latex
\begin{minted}{custom}
vec3 position(0.0, 0.0, 0.0);
Atom *atom = new Atom(position);
\end{minted}
```

You can test it using the [example.ltx](examples/example.ltx) file like so:

	export PYGMENTS_CUSTOM_BASE_LEXER=CppLexer
	export PYGMENTS_CUSTOM_TYPE="[ 'vec3', 'Atom', 'System' ]"
    pdflatex -shell-escape example.ltx

See the minted package at https://github.com/gpoore/minted for more information.

