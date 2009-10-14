Name:		mutrace
Version:	0.2
Release:	%mkrel 1
Summary:	Mutex Tracer
Group:		Development/Other
License:	LGPLv3+ and GPLv2+
URL:		http://git.0pointer.de/?p=mutrace.git
Source0:	http://0pointer.de/public/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	util-linux-ng
BuildRequires:	binutils-devel

%description
mutrace is a mutex profiler. It may be used to track down contended mutexes in
multi-threaded applications.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/mutrace
%{_bindir}/matrace
%{_libdir}/libmutrace.so
%{_libdir}/libmatrace.so
%{_libdir}/libmutrace-backtrace-symbols.so

