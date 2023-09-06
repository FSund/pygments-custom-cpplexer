example.pdf: example.ltx example.c
	pdflatex -shell-escape $<

.PHONY: clean
clean:
	rm -rf example.aux example.log _minted-example *~

