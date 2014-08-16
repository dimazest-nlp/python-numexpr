%{?scl:%scl_package python-numexpr}
%{!?scl:%global pkg_name %{name}}

%global	module	numexpr

Summary:	Fast numerical array expression evaluator for Python and NumPy
Name:		%{?scl_prefix}python-%{module}
Version:	2.3
Release:	1%{?dist}
Source0:	https://github.com/pydata/numexpr/archive/%{module}-%{version}.tar.gz
License:	MIT
Group:		Development/Languages
URL:		http://numexpr.googlecode.com/

Requires:	%{?scl_prefix}numpy
%{?scl:Requires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}numpy
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  gcc-c++
%{?scl:BuildRequires: %{scl}-build %{scl}-runtime}
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It’s the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

%prep
%setup -q -n %{module}-%{version}

sed -i "s|/usr/bin/env |/usr/bin/|" %{module}/cpuinfo.py

%build
%{?scl:scl enable %{scl} - << \EOF}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
%{?scl:EOF}

%check
libdir=`ls build/|grep lib`
pushd "build/$libdir"
%{?scl:scl enable %{scl} "}
%{__python3} -c 'import numexpr; numexpr.test()'
%{?scl:"}
popd

%install
%{?scl:scl enable %{scl} "}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}
#This could be done more properly ?
chmod 0644 %{buildroot}%{python3_sitearch}/%{module}/cpuinfo.py
chmod 0755 %{buildroot}%{python3_sitearch}/%{module}/*.so


%files
%doc ANNOUNCE.rst LICENSE.txt RELEASE_NOTES.rst README.rst
%{python3_sitearch}/numexpr/
%{python3_sitearch}/numexpr-%{version}-py*.egg-info/

%changelog
* Sat Aug 16 2014 Dmitrijs Milajevs <dimazest@gmail.com> - 2.3-4
- Cleanup and adoptations for Software collections.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Thibault North <tnorth@fedoraproject.org> -2.3-1
- Update to new release 2.3

* Fri Jan 17 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.2-2
- Move requirements to the proper package (#1054683)

* Sun Sep 29 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.2-1
- Update to 2.2.2 (#1013130)

* Mon Sep 09 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.1-1
- Update to 2.2.1

* Thu Sep 05 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2-1
- Update to 2.2
- Add python3-numexpr package

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 8 2012  Thibault North <tnorth@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Sun Nov 27 2011 Thibault North <tnorth@fedoraproject.org> - 2.0-1
- Update to 2.0

* Sun Oct 30 2011 Thibault North <tnorth@fedoraproject.org> - 1.4.2-2
- Add check section
- Fix permissions and remove useless sections

* Thu Oct 20 2011 Thibault North <tnorth@fedoraproject.org> - 1.4.2-1
- Updated to 1.4.2

* Fri Apr 29 2011 Thibault North <tnorth@fedoraproject.org> - 1.4.1-3
- Fix buildroot issue

* Tue Dec 21 2010 Thibault North <tnorth@fedoraproject.org> - 1.4.1-2
- Fixes for the review process

* Fri Nov 05 2010 Thibault North <tnorth@fedoraproject.org> - 1.4.1-1
- Initial package based on Mandriva's one
