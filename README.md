## crfsuite

[CRFSuite](http://www.chokkan.org/software/crfsuite/) is an implementation of
[Conditional Random Fields](http://en.wikipedia.org/wiki/Conditional_random_field)
(CRFs) for labeling sequential data.

* [The original CRF paper by Lafferty, McCallum, Pereira](http://www.cis.upenn.edu/~pereira/papers/crf.pdf)
* [CRFSuite SWIG API](http://www.chokkan.org/software/crfsuite/api/crfsuite_hpp_api.html)


## Installation instructions

1. Install dependencies:
    - CentOS / Redhat / Fedora:
        + `yum groupinstall "Development Tools"`
        + `yum install -y python-dev python-setuptools swig`
    - Ubuntu:
        + `apt-get install build-essential`
    - OS X:
        + Get [Xcode](https://itunes.apple.com/us/app/xcode/id497799835) from the Mac App Store.
        + Get [homebrew](http://brew.sh/)
        + `brew install coreutils shtool swig`
    - All: install [libLBFGS](http://www.chokkan.org/software/liblbfgs/)
2. Configure: `./configure`
3. Build: `make`
4. Install: `make install`
5. Install Python links:
    - `cd swig/python`
    - Build the SWIG links, but don't install them to `site-packages` yet:
        + `python setup.py build_ext`
    - Alternatively, build and install in one go (runs `build_ext` if needed):
        + `python setup.py install_lib`


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
