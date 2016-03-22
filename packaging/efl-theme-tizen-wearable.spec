Name:          efl-theme-tizen-wearable
Summary:       Tizen theme files
Version:       1.1.0
Release:       1
Group:         TO_BE/FILLED_IN
License:       BSD 2-clause and Flora-1.1
Source0:       %{name}-%{version}.tar.gz
BuildRequires: model-build-features
BuildRequires: edje-bin
%define _unpackaged_files_terminate_build 0

%description
Tizen theme for EFL

%prep
%setup -q

%build
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"

%if "%{?model_build_feature_formfactor}" == "wearable"
    export TARGET=wearable
%else
    export TARGET=wearable-circle
%endif

make

%install
%if "%{?model_build_feature_formfactor}" == "wearable"
    export TARGET=wearable
%else
    export TARGET=wearable-circle
%endif

make install prefix=%{_prefix} DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/*.edj
%{_datadir}/license/%{name}
%manifest %{name}.manifest
