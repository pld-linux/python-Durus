
%define 	module	Durus

Summary:	Durus - a persistent object system for applications written in the Python programming language
Summary(pl):	Durus - system przechowywania obiektów aplikacji napisanych w jêzyku programowania Python
Name:		python-%{module}
Version:	1.1
Release:	1
License:	CNRI
Group:		Libraries/Python
Source0:	http://www.mems-exchange.org/software/files/durus/%{module}-%{version}.tar.gz
# Source0-md5:	6b829032403eecd4a3f0e5107a755c21
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

%package -n Durus-server
Summary:	Server program for Durus object system
Summary(pl):	Program serwera systemu Durus
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description -n Durus-server
This package contains server program for Durus object system.

%description -n Durus-server -l pl
Program serwera systemu Durus.

%package -n Durus-client
Summary:	Client program for Durus object system
Summary(pl):	Program klienta systemu Durus
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description -n Durus-client
This package contains client program for Durus object system.

%description -n Durus-client -l pl
Program klienta systemu Durus.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{py_sitedir}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir} \
	--optimize=2

# rename the client program to omit possible conflicts with name
mv $RPM_BUILD_ROOT%{_bindir}/client.py $RPM_BUILD_ROOT%{_bindir}/durus-client.py

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS.txt LICENSE.txt README.txt
%{py_sitedir}/durus

%files -n Durus-server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/run_durus.py

%files -n Durus-client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/durus-client.py
