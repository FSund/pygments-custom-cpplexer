from pygments.lexers.compiled import CLexer
from pygments.token import Name, Keyword

class CustomLexer(CLexer):
    name = 'Custom'
    aliases = ['custom']

    EXTRA_TYPES = ['Atom', 'System', 'vec3']

    def get_tokens_unprocessed(self, text, stack=('root',)):
        for index, token, value in CLexer.get_tokens_unprocessed(self, text, stack):
            if token is Name:
                if value in self.EXTRA_TYPES:
                    token=Keyword.Type
            yield index, token, value
