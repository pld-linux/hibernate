Summary:	Software suspend 2 hibernate script
Summary(pl):	Skrypt hibernuj±cy dla Software suspend 2
Name:		hibernate
Version:	1.02
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dagobah.ucc.asn.au/swsusp/script2/%{name}-script-%{version}.tar.gz
# Source0-md5:	5f0fee0d6f8be9817b03e997dffe5bb9
URL:		http://softwaresuspend.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hibernate is a shell script that handles the process of getting ready
to suspend to disk and to resume from disk. It requires the Software
Suspend 2 patches available at http://softwaresuspend.berlios.de/ .
After installing you will want to run 'hibernate -h' to see available
options and modify your /etc/hibernate/hibernate.conf to set them.

%description -l pl
hibernate to skrypt pow³oki obs³uguj±cy proces przygotowania do
zachowania stanu na dysku (suspend to disk) i obudzenia z dysku.
Wymaga ³at Software Suspend 2 dostêpnych pod
http://softwaresuspend.berlios.de/ . Po zainstalowaniu 'hibernate -h'
poka¿e dostêpne opcje, które mo¿na ustawiæ w
/etc/hibernate/hibernate.conf .

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
