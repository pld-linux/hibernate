Name:		hibernate
Summary:	Software suspend 2 hibernate script
Version:	0.97
Release:	1
License:	GPL
Group:		Applications/System
URL:		http://softwaresuspend.berlios.de/
Source0:	http://dagobah.ucc.asn.au/swsusp/script2/%{name}-script-%{version}.tar.gz
# Source0-md5:	74f98f5953c2e58e12ab056ba1a352a4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hibernate is a shell script that handles the process of getting ready
to suspend to disk and to resume from disk. It requires the Software
Suspend 2 patches available at http://softwaresuspend.berlios.de/
After installing you will want to run 'hibernate -h' to see available
options and modify your /etc/hibernate/hibernate.conf to set them.

%prep
%setup -q -n %{name}-script-%{version}

%install
rm -rf $RPM_BUILD_ROOT

BASE_DIR=$RPM_BUILD_ROOT \
PREFIX=%{_prefix} \
MAN_DIR=$RPM_BUILD_ROOT%{_mandir} \
sh ./install.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG COPYING TODO SCRIPTLET-API
%attr(755,root,root) %{_sbindir}/hibernate
%{_datadir}/hibernate
%dir /etc/hibernate
%config(noreplace) %verify(not md5 size mtime) /etc/hibernate/*
%{_mandir}/man?/*
