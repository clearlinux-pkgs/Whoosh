#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Whoosh
Version  : 2.7.4
Release  : 24
URL      : http://pypi.debian.net/Whoosh/Whoosh-2.7.4.tar.gz
Source0  : http://pypi.debian.net/Whoosh/Whoosh-2.7.4.tar.gz
Summary  : Fast, pure-Python full text indexing, search, and spell checking library.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: Whoosh-python3
Requires: Whoosh-license
Requires: Whoosh-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pytest
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : setuptools_scm

%description
============
        
        Whoosh is a fast, featureful full-text indexing and searching library
        implemented in pure Python. Programmers can use it to easily add search
        functionality to their applications and websites. Every part of how Whoosh
        works can be extended or replaced to meet your needs exactly.

%package legacypython
Summary: legacypython components for the Whoosh package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the Whoosh package.


%package license
Summary: license components for the Whoosh package.
Group: Default

%description license
license components for the Whoosh package.


%package python
Summary: python components for the Whoosh package.
Group: Default
Requires: Whoosh-python3
Provides: whoosh-python

%description python
python components for the Whoosh package.


%package python3
Summary: python3 components for the Whoosh package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Whoosh package.


%prep
%setup -q -n Whoosh-2.7.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530379216
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1530379216
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/Whoosh
cp LICENSE.txt %{buildroot}/usr/share/doc/Whoosh/LICENSE.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/Whoosh/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
