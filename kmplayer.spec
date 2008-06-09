
%define unstable 0
%{?_with_unstable: %global unstable 1}

%if %unstable
%define dont_strip 1
%endif

%define name kmplayer
%define betaver rc4

Name: %name
Version: 0.11.0
Release: %mkrel -c %betaver 2
Summary: A multimedia mplayer/phonon frontend for KDE
License: GPLv2+
Group: Video
Url: http://kmplayer.kde.org/
Source:	http://kmplayer.kde.org/pkgs/%{name}-%{version}-%{betaver}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: libnspr-devel
BuildRequires: gtk2-devel
BuildRequires: dbus-glib-devel

Obsoletes:     kde4-%name < 0.11.0-0.rc2.5
Provides:      kde4-%name

%description
KMPlayer can play all the audio/video supported by mplayer/phonon from local
file or url, be embedded inside Konqueror and KHTML and play DVD's.

%post
%{update_menus}
%if %mdkversion < 200900
/sbin/ldconfig
%endif

%postun
%{clean_menus}
%if %mdkversion < 200900
/sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog README
%{_kde_bindir}/kmplayer
%{_kde_bindir}/kphononplayer
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/kde4/services/*.desktop
%{_kde_libdir}/*.so
%{_kde_libdir}/kde4/*.so
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%package npplayer
Group: Video
Summary: Kmplayer netscape plugin player
Requires: %name

%description npplayer
Kmplayer netscape plugin player.

%files npplayer
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%_kde_bindir/knpplayer

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-%{betaver}

%build
LDFLAGS="$LDFLAGS -Wl,--as-needed -Wl,--no-undefined"; export LDFLAGS ;
%cmake_kde4
%make

%install
rm -rf %buildroot
cd build
%makeinstall_std
cd -

rm -fr %buildroot%_kde_datadir/doc/HTML/en/doc/
# icons/oxygen/*. conflicts with oxygen-icon-theme
rm -f %buildroot%_kde_iconsdir/oxygen/*/apps/%name.*

%{find_lang} %{name} --with-html

%clean
rm -rf $RPM_BUILD_ROOT
