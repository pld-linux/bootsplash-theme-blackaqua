
%define	theme	blackaqua

Summary:	Bootsplash - PLD blackaqua theme
Summary(pl.UTF-8):	Bootsplash - Motyw PLD blackaqua 
Name:		bootsplash-theme-%{theme}
Version:	1.0
Release:	1
Epoch:		0
License:	GPL v2
Group:		Themes
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	94a42ab7e2fb881961001b5669705e9a
URL:		http://cvs.pld-linux.org/cgi-bin/cvsweb/pld-artwork/bootsplash/blackaqua/
Requires:	bootsplash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blackaqua PLD theme for bootsplash.

%description -l pl.UTF-8
Motyw PLD Blackaqua do bootsplasha.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/bootsplash/themes/%{theme}
install -d $THEME_DIR/{config,images}
install %{theme}/config/*.cfg $THEME_DIR/config
install %{theme}/images/*.jpg $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/bootsplash/themes/%{theme}
