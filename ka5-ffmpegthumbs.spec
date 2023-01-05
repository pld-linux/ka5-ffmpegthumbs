#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		ffmpegthumbs
Summary:	Ffmpegthumbs
Name:		ka5-%{kaname}
Version:	22.12.0
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	8358083300e2c279e5627064ee79b4fc
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
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
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/ffmpegthumbs.so
%{_datadir}/kservices5/ffmpegthumbs.desktop
%{_datadir}/config.kcfg/ffmpegthumbnailersettings5.kcfg
%{_datadir}/metainfo/org.kde.ffmpegthumbs.metainfo.xml
%{_datadir}/qlogging-categories5/ffmpegthumbs.categories
