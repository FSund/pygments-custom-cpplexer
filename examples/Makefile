all: example.pdf

# The Pygments Custom language module uses Environment Variables to
# add keywords for syntax highlighting. All are optional.
# Note that this maps strings to subtypes of Token.Keyword.

export PYGMENTS_CUSTOM_BASE_LEXER=CppLexer

export PYGMENTS_CUSTOM_TYPE        := [ "vec3", "Atom", "System" ]
export PYGMENTS_CUSTOM_CONSTANT    := [  ]
export PYGMENTS_CUSTOM_KEYWORD     := [  ]
export PYGMENTS_CUSTOM_DECLARATION := [  ]
export PYGMENTS_CUSTOM_NAMESPACE   := [  ]
export PYGMENTS_CUSTOM_PSEUDO      := [  ]
export PYGMENTS_CUSTOM_RESERVED    := [  ]
export PYGMENTS_CUSTOM_REMOVED     := [  ]


# Pattern rule for building the pdf from latex and C source files.
# Note 1: $< represents the latex filename.
# Note 2: The date embedded in the pdf is set to the last modification
#         time of the latex file according to the git commit log or
#         the file timestamp.
%.pdf: %.ltx %.cpp FORCE
	SOURCE_DATE_EPOCH=`(git log -1 --format=%at $< 2>/dev/null; \
			    date +%s -r $<) | head -1` \
		pdflatex -shell-escape $< 

# Always re-create the pdf at each `make`.
FORCE:

.PHONY: clean
clean:
	rm -rf *.aux *.log *.out.pyg  _minted-* *~
