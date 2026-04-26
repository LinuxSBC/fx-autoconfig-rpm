Name: fx-autoconfig
Version: 1.0.0
Release: 1
Summary: Firefox userChrome.js manager

License: MPL-2.0
URL: https://github.com/MrOtherGuy/fx-autoconfig
Source0: https://github.com/MrOtherGuy/fx-autoconfig/archive/master.tar.gz
Requires: firefox

%define debug_package %{nil}

%description
Firefox userChrome.js manager

%prep
# -n tells RPM the actual name of the folder inside the tarball
%autosetup -n fx-autoconfig-master

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/firefox

cp -p program/config.js %{buildroot}%{_libdir}/firefox/
cp -pr program/defaults %{buildroot}%{_libdir}/firefox/defaults

%files
%{_libdir}/firefox/config.js
%{_libdir}/firefox/defaults/

%post
echo "Firefox userChrome.js manager (fx-autoconfig) installed."
%changelog
* Sun Apr 26 2026 Anna Simmons <anna@simmons.ovh> - 1.0.0-1
- Initial package build
