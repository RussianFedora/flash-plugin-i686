Summary:	Adobe Flash Player 10.3
Name:		flash-plugin-i686
Version:	10.3.181.14
Release:	1
Epoch:		6

Group:		Applications/Internet
License:	Commercial
URL:		http://www.adobe.com
Source0:	http://fpdownload.macromedia.com/get/flashplayer/current/install_flash_player_10_linux.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch:	i686

%description
Adobe Flash Player for i686

%package -n flash-plugin
Summary:	Adobe Flash Player 10.3
Group:		Applications/Internet
License:	Commercial
ExclusiveArch:	i686

%description -n flash-plugin
Adobe Flash Player 10.3 for i686

%prep
%setup -q -c -T -a 0

%build

%install
rm -rf %{buildroot}
install -dD  %{buildroot}%{_libdir}/mozilla/plugins/
install -dD  %{buildroot}%{_libdir}/flash-plugin/

install -m 644 libflashplayer.so \
        %{buildroot}%{_libdir}/flash-plugin/libflashplayer.so

cd %{buildroot}%{_libdir}/mozilla/plugins/
ln -s ../../flash-plugin/libflashplayer.so

%clean
rm -rf %{buildroot}

%files -n flash-plugin
%defattr(-, root, root)
%{_libdir}/flash-plugin/*
%{_libdir}/mozilla/plugins/*.so

%changelog
* Sun May 15 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 10.3.181.14-1
- update to 10.3.181.14

* Fri Apr  8 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 10.2.153.1-1
- update to 10.2.153.1

* Mon Aug  3 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.32.18-1
- update to 10.0.32.18

* Fri Feb 27 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.22.87-1
- update to 10.0.22.87

* Mon Dec 22 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.d21.1-1
- we switched to Adobe x86_64 beta flash
- bump epoch
- Obsoletes flash-plugin

* Fri Dec 19 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.15.3-1
- update to 10.0.15.3

* Mon Nov 17 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.12.36-2
- remove depends on libflashsupport

* Wed Oct 15 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.12.36-1
- update to 10.0.12.36

* Thu May 22 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.0.124.0-1
- try to do everything for x86_64
