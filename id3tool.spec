%define	subver	a
Summary:	Command line utility for easy manipulation of the ID3 tags present in MPEG Layer 3 audio files
Name:		id3tool
Version:	1.2
Release:	0.%{subver}.1
License:	GPL
Group:		Applications/Sound
Source0:	http://nekohako.xware.cx/id3tool/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	061185562c0d0e6327406d9fc2f194b2
URL:		http://nekohako.xware.cx/id3tool/
#BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line utility for easy manipulation of the ID3 tags present in
MPEG Layer 3 audio files.

%prep
%setup -q -n %{name}-%{version}%{subver}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
