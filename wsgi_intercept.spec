#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wsgi_intercept
Version  : 1.5.0
Release  : 25
URL      : http://pypi.debian.net/wsgi_intercept/wsgi_intercept-1.5.0.tar.gz
Source0  : http://pypi.debian.net/wsgi_intercept/wsgi_intercept-1.5.0.tar.gz
Summary  : wsgi_intercept installs a WSGI application in place of a real URI for testing.
Group    : Development/Tools
License  : MIT
Requires: wsgi_intercept-python
Requires: Sphinx
Requires: httplib2
Requires: pytest
Requires: requests
Requires: six
Requires: urllib3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Installs a WSGI application in place of a real host for testing.
Introduction
============

%package python
Summary: python components for the wsgi_intercept package.
Group: Default

%description python
python components for the wsgi_intercept package.


%prep
%setup -q -n wsgi_intercept-1.5.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489156186
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489156186
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
