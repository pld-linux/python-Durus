
%define 	module	Durus

Summary:	Durus - a persistent object system for applications written in the Python programming language
Summary(pl):	Durus - system przechowywania obiektów aplikacji napisanych w jêzyku programowania Python
Name:		python-%{module}
Version:	1.2
Release:	3
License:	CNRI
Group:		Libraries/Python
Source0:	http://www.mems-exchange.org/software/files/durus/%{module}-%{version}.tar.gz
# Source0-md5:	5be418d49cb105ccb7b96dfb81520bfc
URL:		http://www.mems-exchange.org/software/durus/
BuildRequires:	python-devel >= 2.3
Requires:	python >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Durus is a system that offers an easy way to use and maintain a
consistent collection of object instances used by one or more
processes. Access and change of a persistent instances is managed
through a cached Connection instance which includes commit() and
abort() methods so that changes are transactional. Durus is best
suited to collections of less than a million instances with relatively
stable state.

%description -l pl
Durus jest system umo¿liwiaj±cym u¿ywanie i zarz±dzanie w ³atwy sposób
kolekcj± obiektów u¿ywanych przez jeden lub wiêcej procesów. Dostêp do
obiektów i ich modyfikacje zarz±dzane s± przy pomocy przechowywanych
stale w pamiêci obiektów po³±czeñ umo¿liwiaj±cych wykonywanie
transakcyjnych operacji na obiektach. Durus najlepiej sprawdza siê
przy bazach, które nie zawieraj± wiêcej ni¿ milion obiektów z
relatywnie stabilnym stanem.

%package -n Durus-utils
Summary:	Utility programs for Durus system
Summary(pl):	Programy narzêdziowe systemu Durus
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Obsoletes:	Durus-client
Obsoletes:	Durus-server

%description -n Durus-utils
This package contains utility programs for Durus system. It contains
simple Python script with both client and server functionality.

%description -n Durus-utils -l pl
Programy nardzêdziowe systemu Durus. Pakiet ten zawiera prosty skrypt
udostêpniaj±cy funkcjonalno¶æ zarówno klienta jaki i serwera systemu
Durus.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{py_sitedir},%{_mandir}/man1}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir} \
	--optimize=2

cp -a doc/durus.1 $RPM_BUILD_ROOT%{_mandir}/man1
find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS.txt CHANGES.txt LICENSE.txt README.txt doc/{FAQ.txt,FAQ.html,default.css}
%{py_sitedir}/durus

%files -n Durus-utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/durus
%{_mandir}/man1/*
