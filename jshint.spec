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
Source1:	%{name}.sh
# Source0-md5:	5bfdc95c06e0ceefd9f185e421432424
Patch0:		path.patch
Requires:	java-rhino
Requires:	jpackage-utils
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
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p jshint.js $RPM_BUILD_ROOT%{_appdir}
cp -a env $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown CHANGELOG
%attr(755,root,root) %{_bindir}/jshint
%{_appdir}
