Name:		bwidget
Version:	1.9.2
Release:	%mkrel 1
Summary:	Extended widget set for Tk
Group:		System/Libraries
License:	BSD
URL:		http://tcllib.sourceforge.net/
Source0:	http://downloads.sourceforge.net/tcllib/BWidget-%{version}.tar.gz
#Requires:      tcl(abi) = 8.5 tk
Requires:	tcl
Requires:	tk
BuildRequires:	tcl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
An extended widget set for Tcl/Tk.

%prep
%setup -q -n BWidget-%{version}
%{__sed} -i 's/\r//' LICENSE.txt BWman/*.html

%build

%install
%{__rm} -rf %{buildroot}
# Don't bother with the included configure script and Makefile.  They
# are missing a lot of pieces and won't work at all.  Installation is
# pretty simple, so we can just do it here manually.
%{__mkdir_p} %{buildroot}%{tcl_sitelib}/%{name}%{version}/
%{__mkdir_p} %{buildroot}%{tcl_sitelib}/%{name}%{version}/lang
%{__mkdir_p} %{buildroot}%{tcl_sitelib}/%{name}%{version}/images

%{__install} -m 0644 -pD *.tcl %{buildroot}%{tcl_sitelib}/%{name}%{version}/
%{__install} -m 0644 -pD lang/*.rc %{buildroot}%{tcl_sitelib}/%{name}%{version}/lang/
%{__install} -m 0644 -pD images/*.gif images/*.xbm %{buildroot}%{tcl_sitelib}/%{name}%{version}/images/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0644,root,root,0755)
%doc README.txt LICENSE.txt
%doc BWman/*.html
%defattr(-,root,root,0755)
%{tcl_sitelib}/%{name}%{version}


%changelog
* Tue Mar 15 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.9.2-1mdv2011.0
+ Revision: 645050
- update to new version 1.9.2

* Mon Feb 15 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.9.0-1mdv2011.0
+ Revision: 506073
- Update to 1.9.0
- Clean spec to fix warnings

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.8.0-6mdv2010.0
+ Revision: 436907
- rebuild

* Fri Dec 05 2008 Adam Williamson <awilliamson@mandriva.org> 1.8.0-5mdv2009.1
+ Revision: 310802
- buildrequires tcl-devel (for the macros)
- rebuild with new tcl
- drop the now unneeded defines

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.8.0-4mdv2009.0
+ Revision: 243378
- rebuild

* Wed Jan 09 2008 David Walluck <walluck@mandriva.org> 1.8.0-2mdv2008.1
+ Revision: 147396
- add macros
- fix tcl Requires

* Mon Jan 07 2008 David Walluck <walluck@mandriva.org> 1.8.0-1mdv2008.1
+ Revision: 146191
- hardcode tcl version
- import bwidget


* Fri Jan  3 2008 Marcela Maslanova <mmaslano@redhat.com> 1.8.0-3
- rebuild with new tcl8.5, changed abi in spec

* Wed Aug 22 2007 Wart <wart at kobold.org> 1.8.0-2
- License tag clarification
- Move files to a tcl-specific directory for faster loading

* Thu Oct 19 2006 Wart <wart at kobold.org> 1.8.0-1
- Update to 1.8.0
- Remove patch that was accepted upstream

* Mon Aug 28 2006 Wart <wart at kobold.org> 1.7.0-4
- Rebuild for Fedora Extras

* Fri Aug 11 2006 Wart <wart at kobold.org> 1.7.0-3
- Add patch for adding a color selector to the font dialog

* Sat Dec 10 2005 Wart <wart at kobold.org> 1.7.0-2
- added dist tag to release tag.

* Sat Dec 10 2005 Wart <wart at kobold.org> 1.7.0-1
- Initial spec file.
