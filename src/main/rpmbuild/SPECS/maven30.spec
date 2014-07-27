Name:           %{_name}
Version:        %{_version}
Release:        %{_release}
Summary:        Apache Maven 3.x Compat
License:        None
BuildArch:      %{_arch}
Source0:        apache-maven-%{_version}-bin.tar.gz
AutoReqProv:	no

%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

%description
Software project management and comprehension tool

%prep
%setup -q -c

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}/usr/local/apache-maven
cp -r apache-maven-%{version} %{buildroot}/usr/local/apache-maven

%files
%defattr(-,root,root,-)
/usr/local/apache-maven/apache-maven-%{_version}

%changelog
* Sun Jul 27 2014 Eduardo ito <ed@fghijk.local> - 3.0.5-1
- Initial release
