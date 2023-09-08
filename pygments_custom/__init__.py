# pygments_custom
# This module uses environment variables to customize which
# keywords to highlight and which Pygments Lexer to inherit from.

from pygments.token import Name, Keyword
from pygments.lexers import *
from os import getenv
from sys import stderr
import json

# Previously we used "from pygments.lexers import CLexer as mysuper".
# Now, which lexer to inherit from is variable.
base = getenv( "PYGMENTS_CUSTOM_BASE_LEXER" )
if not base:
    base="CLexer"

try: 
    mysuper = locals()[ base ]  	# Do we have a class named that?
except KeyError:
    mysuper = CLexer
    print( f'\n*** CustomLexer Error: Unknown Lexer: "{base}". ',
           f'Defaulting to CLexer.', file=stderr )
    import pygments.lexers
    print( f'\n*** CustomLexer Error: Please set PYGMENTS_CUSTOM_BASE_LEXER '
           f'to one of {pygments.lexers.__all__}', file=stderr )


class CustomLexer(mysuper):
    """CustomLexer for pygments which extends an existing lexer with
    new keywords. The existing lexer defaults to CLexer but can be
    changed by the environment variable PYGMENTS_CUSTOM_BASE_LEXER.
    For example, one could inherit the C++ Lexer's keywords like so:

    	PYGMENTS_CUSTOM_BASE_LEXER="CppLexer"

    New keywords can be highlighted as Type, Constant, Namespace,
    Declaration, Pseudo, Removed, Reserved, or plain old Keyword. To
    add keywords, set the environment variables PYGMENTS_CUSTOM_TYPE,
    PYGMENTS_CUSTOM_CONSTANT, ..., PYGMENTS_CUSTOM_KEYWORD.

    Each variable is a Python list (square brackets surrounding a
    comma separated list of quoted strings). For example, this adds
    new types (class, typedef) for highlighting:

    	PYGMENTS_CUSTOM_TYPE="[ 'vec3', 'Atom', 'System' ]"

    """

    name = 'Custom'
    aliases = ['custom']
    kwtable = [ ('PYGMENTS_CUSTOM_TYPE',        Keyword.Type),
                ('PYGMENTS_CUSTOM_CONSTANT',    Keyword.Constant),
                ('PYGMENTS_CUSTOM_NAMESPACE',   Keyword.Namespace),
                ('PYGMENTS_CUSTOM_DECLARATION', Keyword.Declaration),
                ('PYGMENTS_CUSTOM_PSEUDO',      Keyword.Pseudo),
                ('PYGMENTS_CUSTOM_REMOVED',     Keyword.Removed),
                ('PYGMENTS_CUSTOM_RESERVED',    Keyword.Reserved),
                ('PYGMENTS_CUSTOM_KEYWORD',     Keyword),               ]
    EXTRA = {}

    for v, k in kwtable:
        s = getenv( v )
        print(v, s)
        if s:
            EXTRA[k] = json.loads(s.replace("'", '"').replace("[]", '{}', EXTRA[k]))
    
    def get_tokens_unprocessed(self, text, stack=('root',)):
        for index, token, value in mysuper.get_tokens_unprocessed(self, text, stack):
            if token is Name:
                for key in self.EXTRA:
                    if self.EXTRA[key] and value in self.EXTRA[key]:
                        token=key
                        break

            yield index, token, value


if __name__ == '__main__':
    print( "testing" )
    x = CustomLexer()
    for y in x.get_tokens_unprocessed( "M_PI", "hello_my_name is", "removed" ):
        print(y)
    for y in x.get_tokens_unprocessed( "vec3 x,y,z; System;", "reserved", Type):
        print(y)
        
