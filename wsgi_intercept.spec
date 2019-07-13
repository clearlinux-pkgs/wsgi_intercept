#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wsgi_intercept
Version  : 1.8.0
Release  : 32
URL      : https://files.pythonhosted.org/packages/70/5c/9428532ec1b74a0e0e412495bf52ac2333b49785e83f1d6d1b93690d34a4/wsgi_intercept-1.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/70/5c/9428532ec1b74a0e0e412495bf52ac2333b49785e83f1d6d1b93690d34a4/wsgi_intercept-1.8.0.tar.gz
Summary  : wsgi_intercept installs a WSGI application in place of a real URI for testing.
Group    : Development/Tools
License  : MIT
Requires: wsgi_intercept-license = %{version}-%{release}
Requires: wsgi_intercept-python = %{version}-%{release}
Requires: wsgi_intercept-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3

%description
Introduction
        ============
        
        Testing a WSGI application sometimes involves starting a server at a
        local host and port, then pointing your test code to that address.
        Instead, this library lets you intercept calls to any specific host/port
        combination and redirect them into a `WSGI application`_ importable by
        your test program. Thus, you can avoid spawning multiple processes or
        threads to test your Web app.
        
        Supported Libaries
        ==================
        
        ``wsgi_intercept`` works with a variety of HTTP clients in Python 2.7,
        3.4 and beyond, and in pypy.
        
        * urllib2
        * urllib.request
        * httplib
        * http.client
        * httplib2
        * requests
        * urllib3
        
        How Does It Work?
        =================
        
        ``wsgi_intercept`` works by replacing ``httplib.HTTPConnection`` with a
        subclass, ``wsgi_intercept.WSGI_HTTPConnection``. This class then
        redirects specific server/port combinations into a WSGI application by
        emulating a socket. If no intercept is registered for the host and port
        requested, those requests are passed on to the standard handler.
        
        The easiest way to use an intercept is to import an appropriate subclass
        of ``~wsgi_intercept.interceptor.Interceptor`` and use that as a
        context manager over web requests that use the library associated with

%package license
Summary: license components for the wsgi_intercept package.
Group: Default

%description license
license components for the wsgi_intercept package.


%package python
Summary: python components for the wsgi_intercept package.
Group: Default
Requires: wsgi_intercept-python3 = %{version}-%{release}

%description python
python components for the wsgi_intercept package.


%package python3
Summary: python3 components for the wsgi_intercept package.
Group: Default
Requires: python3-core

%description python3
python3 components for the wsgi_intercept package.


%prep
%setup -q -n wsgi_intercept-1.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541280818
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wsgi_intercept
cp LICENSE %{buildroot}/usr/share/package-licenses/wsgi_intercept/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wsgi_intercept/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
