.PHONY: all clean install uninstall

all: hello

clean:
	rm hello
hello: hello_project.cpp
	g++ -o hello_project hello_project.cpp
install:
	sudo install ./hello /usr/local/bin
uninstall:
	sudo rm -rf /usr/local/bin/hello
