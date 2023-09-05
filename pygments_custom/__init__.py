from pygments.lexers.compiled import CppLexer
from pygments.token import Name, Keyword

class CustomLexer(CppLexer):
    name = 'Custom'
    aliases = ['custom']

    EXTRA_TYPES = ['Atom', 'System', 'vec3']

    def get_tokens_unprocessed(self, text, stack=('root',)):
        for index, token, value in CppLexer.get_tokens_unprocessed(self, text, stack):
            if token is Name:
                if value in self.EXTRA_TYPES:
                    token=Keyword.Type
            yield index, token, value
