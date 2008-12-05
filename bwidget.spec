Name:           bwidget
Version:        1.8.0
Release:        %mkrel 5
Summary:        Extended widget set for Tk
Group:          System/Libraries
License:        BSD
URL:            http://tcllib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/tcllib/BWidget-%{version}.tar.gz
#Requires:      tcl(abi) = 8.5 tk
Requires:       tcl
Requires:       tk
BuildRequires:  tcl-devel
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
