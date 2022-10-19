.PHONY: all clean install uninstall

all: hello

clean:
	rm hello_project
hello: hello_project.cpp
	g++ -o hello_project hello_project.cpp
install:
	sudo install ./hello_project /usr/local/bin
uninstall:
	sudo rm -rf /usr/local/bin/hello_project
