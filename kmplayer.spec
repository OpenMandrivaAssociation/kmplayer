%define gitdate 20201207

Name:		kmplayer
Version:	0.12.0b
Release:	1.%{gitdate}.0
Summary:	A multimedia mplayer/phonon frontend for KDE
License:	GPLv2+
Group:		Video
Url:		http://kmplayer.kde.org/
#Source0:	http://download.kde.org/stable/kmplayer/0.12/kmplayer-%{version}.tar.bz2
# Upstream releases is inactive from while, so lets use latest git
Source0:  https://invent.kde.org/multimedia/kmplayer/-/archive/master/kmplayer-master.tar.bz2


BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtd42-xml
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	gettext
# Kf5 BuildRequires
BuildRequires:  cmake
BuildRequires:  cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5MediaPlayer)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5WidgetsAddons)
# Qt5 BuildRequires
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(phonon4qt5)

Obsoletes:	kde4-%{name} < 0.11.0-0.rc2.5
Suggests:	mplayer

%description
KMPlayer can play all the audio/video supported by mplayer/phonon from local
file or url, be embedded inside Konqueror and KHTML and play DVD's.

%files -f %{name}.lang
%doc ChangeLog README
%{_kde5_bindir}/%{name}
%{_kde5_bindir}/kphononplayer
%{_kde5_datadir}/%{name}/
%{_kde5_services}/*.desktop
%{_kde5_datadir}/kxmlgui5/%{name}/
%{_kde5_libdir}/*.so
%{_qt5_plugindir}/*.so
%{_kde5_iconsdir}/hicolor/*/*/*
%{_kde5_applicationsdir}/%{name}.desktop
%config(noreplace) %{_kde5_sysconfdir}/xdg/%{name}rc

#--------------------------------------------------------------------

%package	npplayer
Group:		Video
Summary:	Kmplayer netscape plugin player
Requires:	%{name}

%description	npplayer
Kmplayer netscape plugin player.

%files npplayer
%doc AUTHORS ChangeLog README
%{_kde5_bindir}/knpplayer
#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-master

%build
#export CC=gcc
#export CXX=g++
%cmake_kde5
%ninja 

%install
%ninja_install -C build

%find_lang %{name} --with-html

