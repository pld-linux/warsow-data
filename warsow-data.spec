#
Summary:	Warsow - data files for game
Summary(pl.UTF-8):	Warsow - pliki danych dla gry
Name:		warsow-data
Version:	0.6
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.zcdn.org/dl/warsow_%{version}_unified.zip
# Source0-md5:	0b17543fb7fbd65ffe607293116cc376
Patch0:		%{name}-paths.patch
URL:		http://www.warsow.net/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Warsow data files.

%description -l pl.UTF-8
Pliki danych dla gry Warsow.

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/warsow}

install warsow wsw_server wswtv_server $RPM_BUILD_ROOT%{_bindir}
cp -a basewsw $RPM_BUILD_ROOT%{_datadir}/warsow

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/warsow
%{_datadir}/warsow/basewsw
