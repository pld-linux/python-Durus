
%define 	module	Durus

Summary:	Durus - a persistent object system for applications written in the Python programming language
Summary(pl.UTF-8):	Durus - system przechowywania obiektów aplikacji napisanych w języku programowania Python
Name:		python-%{module}
Version:	3.9
Release:	2
License:	CNRI
Group:		Libraries/Python
Source0:	http://www.mems-exchange.org/software/files/durus/%{module}-%{version}.tar.gz
# Source0-md5:	a432b65bc9fdc24f80f768022d9a3c04
URL:		http://www.mems-exchange.org/software/durus/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Durus is a system that offers an easy way to use and maintain a
consistent collection of object instances used by one or more
processes. Access and change of a persistent instances is managed
through a cached Connection instance which includes commit() and
abort() methods so that changes are transactional. Durus is best
suited to collections of less than a million instances with relatively
stable state.

%description -l pl.UTF-8
Durus jest system umożliwiającym używanie i zarządzanie w łatwy sposób
kolekcją obiektów używanych przez jeden lub więcej procesów. Dostęp do
obiektów i ich modyfikacje zarządzane są przy pomocy przechowywanych
stale w pamięci obiektów połączeń umożliwiających wykonywanie
transakcyjnych operacji na obiektach. Durus najlepiej sprawdza się
przy bazach, które nie zawierają więcej niż milion obiektów z
relatywnie stabilnym stanem.

%package -n Durus-utils
Summary:	Utility programs for Durus system
Summary(pl.UTF-8):	Programy narzędziowe systemu Durus
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Obsoletes:	Durus-client
Obsoletes:	Durus-server

%description -n Durus-utils
This package contains utility programs for Durus system. It contains
simple Python script with both client and server functionality.

%description -n Durus-utils -l pl.UTF-8
Programy nardzędziowe systemu Durus. Pakiet ten zawiera prosty skrypt
udostępniający funkcjonalność zarówno klienta jaki i serwera systemu
Durus.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build_ext
%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{py_sitedir}}

%{__python} setup.py install \
	--install-lib=%{py_sitedir} \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS.txt CHANGES.txt LICENSE.txt README.txt doc/FAQ.txt
%dir %{py_sitedir}/durus
%{py_sitedir}/durus/*.py[co]
%{py_sitedir}/durus/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/Durus-*.egg-info
%endif

%files -n Durus-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/durus
