#!/bin/bash

# Test that all environment variables are properly used by pygments

export PYGMENTS_CUSTOM_BASE_LEXER=CppLexer

export PYGMENTS_CUSTOM_TYPE="[ 'vec3', 'Atom', 'System' ]"
export PYGMENTS_CUSTOM_CONSTANT="[ 'M_PI', 'Tau'  ]"
export PYGMENTS_CUSTOM_KEYWORD="[ 'xyzzy', 'plugh'  ]"
export PYGMENTS_CUSTOM_DECLARATION="[ 'def', 'fn' ]"
export PYGMENTS_CUSTOM_NAMESPACE="[ 'using', 'hello_my_name_is' ]"
export PYGMENTS_CUSTOM_PSEUDO="[ 'let' ]"
export PYGMENTS_CUSTOM_RESERVED="[ 'POKE' ]"
export PYGMENTS_CUSTOM_REMOVED="[ 'removed' ]"


input="new vec3 M_PI xyzzy def using let POKE removed"

expected="    def testNeedsName(lexer):
        fragment = 'new vec3 M_PI xyzzy def using let POKE removed\n'
        tokens = [
            (Token.Keyword, 'new'),
            (Token.Text.Whitespace, ' '),
            (Token.Keyword.Type, 'vec3'),
            (Token.Text.Whitespace, ' '),
            (Token.Keyword.Constant, 'M_PI'),
            (Token.Text.Whitespace, ' '),
            (Token.Keyword, 'xyzzy'),
            (Token.Text.Whitespace, ' '),
            (Token.Keyword.Declaration, 'def'),
            (Token.Text.Whitespace, ' '),
            (Token.Keyword, 'using'),
            (Token.Text.Whitespace, ' '),
            (Token.Keyword.Pseudo, 'let'),
            (Token.Text.Whitespace, ' '),
            (Token.Keyword.Reserved, 'POKE'),
            (Token.Text.Whitespace, ' '),
            (Token.Keyword.Removed, 'removed'),
            (Token.Text.Whitespace, '\n'),
        ]
        assert list(lexer.get_tokens(fragment)) == tokens"

output=$(pygmentize -l custom -f testcase <<<"${input}")

if diff <(echo "$output") <(echo "$expected"); then
    echo "All environment variables work as expected."
    exit 0
else
    echo "ERROR: Output did not match what was expected."
    exit 1
fi

