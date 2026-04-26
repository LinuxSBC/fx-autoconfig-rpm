Name: fx-autoconfig
Version: 1.0.0
Release: 1
Summary: Firefox userChrome.js manager

License: MPL-2.0
Distribution: user
Group: user
Packager: user

%description
Firefox userChrome.js manager

%files
/usr/lib64/firefox/defaults/pref/config-prefs.js
/usr/lib64/firefox/config.js

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib64/firefox/
cp -r ./fx-autoconfig/program/defaults $RPM_BUILD_ROOT/usr/lib64/firefox/
cp ./fx-autoconfig/program/config.js $RPM_BUILD_ROOT/usr/lib64/firefox/

%post
if [ -d /usr/lib64/firefox/defaults/pref ]; then
    echo "userChrome.js manager installed successfully."
else
    echo "Failed to install userChrome.js manager."
fi

%clean
rm -rf $RPM_BUILD_ROOT
