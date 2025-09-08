#!/usr/bin/env python3
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

import sys

def install() -> None:
    print("install")
def url(url : str) -> None:
    print("url: ", url)
def test() -> None:
    print("test")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(EXIT_FAILURE)
    
    if sys.argv[1] == "install":
        install()
    elif sys.argv[1] == "test":
        test()
    else:
        url(sys.argv[1])
    