from pygments.lexers.compiled import CLexer
from pygments.token import Name, Keyword

class CustomLexer(CLexer):
    name = 'Custom'
    aliases = ['custom']

    EXTRA = {}
    EXTRA[Keyword.Constant] = [ 'M_PI', 'M_E' ]
    EXTRA[Keyword.Declaration] = [ 'declaration' ]
    EXTRA[Keyword.Namespace] = [ 'hello_my_name_is' ]
    EXTRA[Keyword.Pseudo] = [ 'pseudo' ]
    EXTRA[Keyword.Removed] = [ 'removed' ]
    EXTRA[Keyword.Reserved] = [ 'reserved' ]
    EXTRA[Keyword.Type] = ['FLAG', 'vec3', 'Atom', 'System' ]

    EXTRA[Keyword] = [ 'xyzzy', 'plugh' ]

    
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
        
