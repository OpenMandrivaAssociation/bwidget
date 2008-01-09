%define tcl_version 8.5
%define tcl_sitelib %{_datadir}/tcl%{tcl_version}

Name:           bwidget
Version:        1.8.0
Release:        %mkrel 1
Summary:        Extended widget set for Tk

Group:          System/Libraries
License:        BSD
URL:            http://tcllib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/tcllib/BWidget-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
#Requires:       tcl(abi) = 8.5 tk
Requires:       tcl
Requires:       tk
BuildRequires:  tcl

%description
An extended widget set for Tcl/Tk.

%prep
%setup -q -n BWidget-%{version}
%{__sed} -i 's/\r//' LICENSE.txt BWman/*.html

%build

%install
rm -rf $RPM_BUILD_ROOT
# Don't bother with the included configure script and Makefile.  They
# are missing a lot of pieces and won't work at all.  Installation is
# pretty simple, so we can just do it here manually.
mkdir -p $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/
mkdir $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/lang
mkdir $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/images

install -m 0644 -pD *.tcl $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/
install -m 0644 -pD lang/*.rc $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/lang/
install -m 0644 -pD images/*.gif images/*.xbm $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/images/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(0644,root,root,0755)
%doc README.txt LICENSE.txt
%doc BWman/*.html
%defattr(-,root,root,0755)
%{tcl_sitelib}/%{name}%{version}
