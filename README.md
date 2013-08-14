## crfsuite

CRFSuite is an implementation of Conditional Random Fields (CRFs) for
labeling sequential data.

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
    - `python setup.py build_ext`
    - `python setup.py install_lib`

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
