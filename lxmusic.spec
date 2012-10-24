Summary:	Lightweight XMMS2 GUI frontend
Name:     	lxmusic
Version:	0.4.5
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://www.lxde.org/
BuildRequires:	gtk+2-devel >= 2.0
Buildrequires:	xmms2-devel >= 0.8
BuildRequires:	intltool
Requires:	xmms2 >= 0.8

%description
LXMusic is a simple GUI XMMS2 client with minimal functionality.
It can do nothing more than playing music files.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%{find_lang} %{name}

%files -f %{name}.lang
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
