Summary:	Gtk+ audio player
Summary(hu.UTF-8):	Gtk+ audio lejátszó
Name:		mesk
Version:	0.3.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://mesk.nicfit.net/releases/%{name}-%{version}.tgz
# Source0-md5:	089a99436fd85239a9ce58e6f22205f8
URL:		http://mesk.nicfit.net/
BuildRequires:	eject
BuildRequires:	gstreamer-audiosink-alsa
BuildRequires:	gstreamer-cdio
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-gnomevfs
BuildRequires:	gstreamer-mad
BuildRequires:	gstreamer-vorbis
BuildRequires:	librsvg
BuildRequires:	python-CDDB
BuildRequires:	python-dbus
BuildRequires:	python-eyeD3
BuildRequires:	python-gstreamer-devel
BuildRequires:	python-pygtk-gtk
BuildRequires:	python-pyvorbis
Requires:	/usr/bin/eject
Requires:	python-CDDB
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk+ audio player.

%description -l hu.UTF-8
Gtk+ audio lejátszó.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/mesk
%{_libdir}/mesk
%{_desktopdir}/mesk.desktop
%{_iconsdir}/hicolor/*/*/mesk.png
%{_mandir}/man1/mesk.1*
%{_pixmapsdir}/mesk.svg
%{py_sitescriptdir}/mesk
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif
