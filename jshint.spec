# TODO
# - add something to run it with, bindir wrapper
Summary:	JSHint, A JavaScript Code Quality Tool
Name:		jshint
Version:	20110219
Release:	1
License:	MIT
Group:		Development/Tools
URL:		http://www.jshint.com/
Source0:	http://www.jshint.com/%{name}.js
# Source0-md5:	69b2644418640ee42ed093c11a361eea
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
JSHint is a community-driven tool to detect errors and potential
problems in JavaScript code and to enforce your team's coding
conventions. It is very flexible so you can easily adjust it to your
particular coding guidelines and the environment you expect your code
to execute in.

%prep
%setup -qcT
cp -p %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
install -p jshint.js $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
