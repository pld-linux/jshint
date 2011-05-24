# TODO
# - add something to run it with, bindir wrapper
%define		subver	2011-04-16
%define		ver		%(echo %{subver} | tr -d -)
Summary:	JSHint, A JavaScript Code Quality Tool
Name:		jshint
Version:	%{ver}
Release:	1
License:	MIT
Group:		Development/Tools
URL:		http://www.jshint.com/
Source0:	https://github.com/jshint/jshint/tarball/%{subver}#/%{name}-%{version}.tgz
# Source0-md5:	5bfdc95c06e0ceefd9f185e421432424
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
JSHint is a community-driven tool to detect errors and potential
problems in JavaScript code and to enforce your team's coding
conventions. It is very flexible so you can easily adjust it to your
particular coding guidelines and the environment you expect your code
to execute in.

%prep
%setup -qc
mv *-jshint-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
install -p jshint.js $RPM_BUILD_ROOT%{_appdir}
cp -a env $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown CHANGELOG
%{_appdir}
