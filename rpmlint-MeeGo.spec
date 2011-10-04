#
# spec file for package rpmlint-Factory (Version 1.0)
#
# Copyright (c) 2008 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           rpmlint-MeeGo
Requires:       rpmlint-mini
Summary:        Rpm correctness checker - Factory configuration
Version:        1.0
Release:        45.5
Url:            http://rpmlint.zarb.org/
License:        GPL v2 or later
Group:          System/Packages
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source1:        COPYING
Source2:        config
Obsoletes:	rpmlint-Moblin

%description
Rpmlint is a tool to check common errors on rpm packages. This package
provides the configuration specific for SUSE Factory.



Authors:
--------
    Frederic Lepied <flepied@mandriva.com>
    Gwenole Beauchesne <gbeauchesne@mandriva.com>

%prep
cp %{SOURCE1} .

%build

%install
install -m 644 -D %{SOURCE2} $RPM_BUILD_ROOT/etc/rpmlint/factory.config

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc COPYING
%dir /etc/rpmlint
%config /etc/rpmlint/factory.config

