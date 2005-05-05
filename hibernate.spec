Summary:	Software suspend 2 hibernate script
Summary(pl):	Skrypt hibernuj±cy dla Software suspend 2
Name:		hibernate
Version:	1.07
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://suspend2.net/downloads/all/%{name}-script-%{version}.tar.gz
# Source0-md5:	0ceb0ec40065cdcf07a6c0ed51de95ac
URL:		http://www.suspend2.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hibernate is a shell script that handles the process of getting ready
to suspend to disk and to resume from disk. It requires the Software
Suspend 2 patches available at <http://www.suspend2.net/>.
After installing you will want to run 'hibernate -h' to see available
options and modify your /etc/hibernate/hibernate.conf to set them.

%description -l pl
hibernate to skrypt pow³oki obs³uguj±cy proces przygotowania do
zachowania stanu na dysku (suspend to disk) i obudzenia z dysku.
Wymaga ³at Software Suspend 2 dostêpnych pod
<http://www.suspend2.net/>. Po zainstalowaniu 'hibernate -h' poka¿e
dostêpne opcje, które mo¿na ustawiæ w /etc/hibernate/hibernate.conf .

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hibernate
%{_mandir}/man?/*
