# git snapshot
#global snapshot 1
%if 0%{?snapshot}
	%global commit		e61107ccad2c3a1c80641ed1696e1ee9fd8e66b5
	%global commitdate	20240817
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	Lightweight XMMS2 GUI frontend
Name:     	lxmusic
Version:	0.4.8
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		https://www.lxde.org/
#Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/lxmusic/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:  intltool
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(xmms2-client)
BuildRequires:  pkgconfig(xmms2-client-glib)
BuildRequires:  pkgconfig(libnotify)

Requires:	xmms2 >= 0.8

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

LXMusic is a simple GUI XMMS2 client with minimal functionality.
It can do nothing more than playing music files.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1.*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	--enable-gtk3 \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name}

