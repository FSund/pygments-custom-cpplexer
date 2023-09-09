all: example.pdf

# Environment variables to add syntax highlighting. Use Python list syntax.
export PYGMENTS_CUSTOM_TYPE 		:= [ "vec3", "Atom", "System" ]
export PYGMENTS_CUSTOM_CONSTANT 	:= [ 'M_PI', 'Tau' ]
export PYGMENTS_CUSTOM_KEYWORD 		:= [ 'xyzzy', 'plugh' ]
export PYGMENTS_CUSTOM_DECLARATION 	:= [ 'declaration' ]
export PYGMENTS_CUSTOM_NAMESPACE	:= [ 'hello_my_name_is' ]
export PYGMENTS_CUSTOM_PSEUDO 		:= [ 'pseudo' ]
export PYGMENTS_CUSTOM_RESERVED 	:= [ 'reserved' ]
export PYGMENTS_CUSTOM_REMOVED 		:= [ 'removed' ]


# Pattern rule for building the pdf from latex and C source files.
# Note 1: $< represents the latex filename.
# Note 2: The date embedded in the pdf is set to the last modification
#         time of the latex file according to the git commit log or
#         the file timestamp.
%.pdf: %.ltx %.c FORCE
	SOURCE_DATE_EPOCH=`(git log -1 --format=%at $< 2>/dev/null; \
			    date +%s -r $<) | head -1` \
		pdflatex -shell-escape $< 

.PHONY: clean
clean:
	rm -rf *.aux *.log *.out.pyg  _minted-* *~


# Always re-create the pdf when run cause we're not tracking .aux, .bbl, etc.
FORCE:

export:

