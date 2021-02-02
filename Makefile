.PHONY: book
book: 
	-rm -rf book/_build/
	jupyter-book build --all book
	-ghp-import -n -p -f book/_build/html