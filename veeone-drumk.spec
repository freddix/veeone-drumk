%define		rname	drumkv1

Summary:	Old-school all-digital drum-kit sampler synthesizer with stereo fx
Name:		veeone-drumk
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/%{rname}/%{rname}-%{version}.tar.gz
# Source0-md5:	9a0a9ff41e53b973c7567af9de189403
URL:		http://drumkv1.sourceforge.net
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsndfile-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	jack-audio-connection-kit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
drumkv1 is (yet) an(other) s an old-school all-digital drum-kit
sampler synthesizer with stereo fx.

%prep
%setup -qn %{rname}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{rname}_jack
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/%{rname}.png

%dir %{_libdir}/lv2/%{rname}.lv2
%attr(755,root,root) %{_libdir}/lv2/%{rname}.lv2/*.so
%{_libdir}/lv2/%{rname}.lv2/*.ttl

