## crfsuite

[CRFSuite](http://www.chokkan.org/software/crfsuite/) is an implementation of
[Conditional Random Fields](http://en.wikipedia.org/wiki/Conditional_random_field)
(CRFs) for labeling sequential data.

* [The original CRF paper by Lafferty, McCallum, Pereira](http://www.cis.upenn.edu/~pereira/papers/crf.pdf)
* [CRFSuite SWIG API](http://www.chokkan.org/software/crfsuite/api/crfsuite_hpp_api.html)


## Installation instructions

### Get the requisite development environment

* CentOS / Redhat / Fedora:

        yum groupinstall "Development Tools"
        yum install -y python-dev python-setuptools swig

* Ubuntu:

        apt-get install build-essential

* OS X:
  + Get [Xcode](https://itunes.apple.com/us/app/xcode/id497799835) from the Mac App Store.
  + Get [homebrew](http://brew.sh/) and install the packages we'll need:

            brew install coreutils shtool swig

### Get [libLBFGS](http://www.chokkan.org/software/liblbfgs/)

    git clone https://github.com/chbrown/liblbfgs
    cd liblbfgs
    ./configure
    make
    sudo make install

### Install from source:

    git clone https://github.com/chbrown/crfsuite
    cd crfsuite
    ./configure
    make
    sudo make install

This will produce the following files (depending on your system's build defaults):

    /usr/local/bin/crfsuite
    /usr/local/include/crfsuite.h
    /usr/local/include/crfsuite.hpp
    /usr/local/include/crfsuite_api.hpp
    /usr/local/lib/libcrfsuite.a
    /usr/local/lib/libcrfsuite.la
    /usr/local/lib/libcrfsuite-0.12.dylib
    /usr/local/lib/libcrfsuite.dylib -> libcrfsuite-0.12.dylib
    /usr/local/share/doc/crfsuite/*

### Install Python links:

    cd swig/python

Build the SWIG links, but don't install them to `site-packages` yet:

    python setup.py build_ext

You might need to tell Python where to look for the library, once it's all linked up, with the `-R` flag.

    python setup.py build_ext -R /usr/local/lib

Install into the local Python's `site-packages`:

    python setup.py install_lib

Or maybe:

    sudo python setup.py install_lib


## Development

Uninstall:

    make uninstall

Clean up after a build:

    make clean

Remove _all_ temporary files after a build:

    make distclean


## License

This program is distributed under the modified BSD license.

Copyright (c) 2007-2010, Naoaki Okazaki

Refer to [COPYING](COPYING) for the precise descriptions of all licenses
involved.


### Special thanks goes to...

* Olivier Grisel
* Andreas Holzbach
* Baoli Li
* Yoshimasa Tsuruoka
* Hiroshi Manabe
* Riza Theresa B. Batista-Navarro

And of course, the original author:

* Naoaki Okazaki
