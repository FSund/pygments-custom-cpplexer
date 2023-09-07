all: example.pdf

# Pattern rule for building the pdf from latex and C source files.
# Note 1: $< represents the latex filename.
# Note 2: The date embedded in the pdf is set to the last modification
#         time of the latex file according to the git commit log or
#         the file timestamp.
%.pdf: %.ltx %.c
	SOURCE_DATE_EPOCH=`(git log -1 --format=%at $< 2>/dev/null; \
			    date +%s -r $<) | head -1` \
		pdflatex -shell-escape $< 

%.pdf: %.tex
	SOURCE_DATE_EPOCH=`(git log -1 --format=%at $< 2>/dev/null; \
                date +%s -r $<) | head -1` \
        pdflatex $< 


.PHONY: clean
clean:
	rm -rf example.aux example.log _minted-example *~

