#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Whoosh
Version  : 2.7.4
Release  : 29
URL      : http://pypi.debian.net/Whoosh/Whoosh-2.7.4.tar.gz
Source0  : http://pypi.debian.net/Whoosh/Whoosh-2.7.4.tar.gz
Summary  : Fast, pure-Python full text indexing, search, and spell checking library.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: Whoosh-license = %{version}-%{release}
Requires: Whoosh-python = %{version}-%{release}
Requires: Whoosh-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pytest
BuildRequires : setuptools_scm

%description
About Whoosh
============
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.

%package license
Summary: license components for the Whoosh package.
Group: Default

%description license
license components for the Whoosh package.


%package python
Summary: python components for the Whoosh package.
Group: Default
Requires: Whoosh-python3 = %{version}-%{release}
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
export SOURCE_DATE_EPOCH=1554303737
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Whoosh
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/Whoosh/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Whoosh/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
