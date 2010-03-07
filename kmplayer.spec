Name:		kmplayer
Version:	0.11.2
Release:	%mkrel 1
Summary:	A multimedia mplayer/phonon frontend for KDE
License:	GPLv2+
Group:		Video
Url:		http://kmplayer.kde.org/
Source:		http://kmplayer.kde.org/pkgs/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:	libnspr-devel
BuildRequires:	gtk2-devel
BuildRequires:	dbus-glib-devel

Obsoletes:	kde4-%name < 0.11.0-0.rc2.5
Provides:	kde4-%name

%description
KMPlayer can play all the audio/video supported by mplayer/phonon from local
file or url, be embedded inside Konqueror and KHTML and play DVD's.

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog README
%{_kde_bindir}/kmplayer
%{_kde_bindir}/kphononplayer
%{_kde_datadir}/apps/%{name}
%{_kde_services}/*.desktop
%{_kde_configdir}/%{name}rc
%{_kde_libdir}/*.so
%{_kde_libdir}/kde4/*.so
%{_kde_iconsdir}/*/*/*/*
%{_kde_applicationsdir}/*

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
%setup -q -n %{name}-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

# icons/oxygen/*. conflicts with oxygen-icon-theme
rm -f %buildroot%_kde_iconsdir/oxygen/*/apps/%name.*

%{find_lang} %{name} --with-html

%clean
rm -rf $RPM_BUILD_ROOT
