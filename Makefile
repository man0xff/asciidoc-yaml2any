
VERSION=0.1
NAME=yaml2any
FILES=$(NAME).conf $(NAME).py templates/*.txt asciidocapi.py
PACKAGE=$(NAME)-$(VERSION).zip

all: $(FILES)
	zip -9 $(PACKAGE) $(FILES)

clean:
	rm -rf $(PACKAGE)
	rm -rf *.pyc
