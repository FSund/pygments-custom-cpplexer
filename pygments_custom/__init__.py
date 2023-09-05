from pygments.lexers.compiled import CLexer
from pygments.token import Name, Keyword

class CustomLexer(CLexer):
    name = 'Custom'
    aliases = ['custom']

    EXTRA_TYPES = ['Atom', 'System', 'vec3']

    EXTRA = {}
    EXTRA[Keyword.Constant] = [ 'Phi', 'Tau' ]
    EXTRA[Keyword.Declaration] = [ 'foo' ]
    EXTRA[Keyword.Namespace] = [ 'bar' ]
    EXTRA[Keyword.Pseudo] = [ 'asdf' ]
    EXTRA[Keyword.Removed] = [ 'fred' ]
    EXTRA[Keyword.Reserved] = [ 'juki' ]
    EXTRA[Keyword.Type] = ['FLAG', 'vec3', 'Atom', 'System' ]

    EXTRA[Keyword] = [ 'quux', 'plugh' ]

    
    def get_tokens_unprocessed(self, text, stack=('root',)):
        for index, token, value in CLexer.get_tokens_unprocessed(self, text, stack):
            if token is Name:
                for key in self.EXTRA:
                    if value in self.EXTRA[key]:
                        token=key

            yield index, token, value


if __name__ == '__main__':
    print( "testing" )
    x = CustomLexer()
    for y in x.get_tokens_unprocessed( "foo bar baz quux fred juki" ):
        print(y)
    for y in x.get_tokens_unprocessed( "vec3 x,y,z; System;" ):
        print(y)
        
