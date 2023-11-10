#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		ffmpegthumbs
Summary:	Ffmpegthumbs
Name:		ka5-%{kaname}
Version:	23.08.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	acdfc912929ba19ede7feb2f03d831b9
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	ffmpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FFmpeg based thumbnail generator for video files.

%description -l pl.UTF-8
Oparty na FFmpeg generator miniaturek plików wideo.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/thumbcreator/ffmpegthumbs.so
%{_datadir}/config.kcfg/ffmpegthumbnailersettings5.kcfg
%{_datadir}/metainfo/org.kde.ffmpegthumbs.metainfo.xml
%{_datadir}/qlogging-categories5/ffmpegthumbs.categories
