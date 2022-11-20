.PHONY: pdf clean zip modify

modify:
	py ./src/modify_data.py ./dataset/penguins_lter.csv A.csv B.csv

pdf:
	pdflatex -output-directory doc doc/documentation.tex
	pdflatex -output-directory doc doc/documentation.tex

clean:
	rm -f doc/documentation.aux
	rm -f doc/documentation.log
	rm -f doc/documentation.out
	rm -f doc/documentation.toc
	rm -f xkolec08_xmorav41_xsladk07.zip

zip: pdf clean
	zip -r xkolec08_xmorav41_xsladk07.zip Makefile README.md doc src