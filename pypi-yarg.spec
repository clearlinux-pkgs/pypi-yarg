#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-yarg
Version  : 0.1.9
Release  : 5
URL      : https://files.pythonhosted.org/packages/d4/c8/cc640404a0981e6c14e2044fc64e43b4c1ddf69e7dddc8f2a02638ba5ae8/yarg-0.1.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/d4/c8/cc640404a0981e6c14e2044fc64e43b4c1ddf69e7dddc8f2a02638ba5ae8/yarg-0.1.9.tar.gz
Summary  : A semi hard Cornish cheese, also queries PyPI (PyPI client)
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-yarg-license = %{version}-%{release}
Requires: pypi-yarg-python = %{version}-%{release}
Requires: pypi-yarg-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(requests)

%description
========================================================

%package license
Summary: license components for the pypi-yarg package.
Group: Default

%description license
license components for the pypi-yarg package.


%package python
Summary: python components for the pypi-yarg package.
Group: Default
Requires: pypi-yarg-python3 = %{version}-%{release}

%description python
python components for the pypi-yarg package.


%package python3
Summary: python3 components for the pypi-yarg package.
Group: Default
Requires: python3-core
Provides: pypi(yarg)
Requires: pypi(requests)

%description python3
python3 components for the pypi-yarg package.


%prep
%setup -q -n yarg-0.1.9
cd %{_builddir}/yarg-0.1.9
pushd ..
cp -a yarg-0.1.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653004544
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-yarg
cp %{_builddir}/yarg-0.1.9/LICENSE %{buildroot}/usr/share/package-licenses/pypi-yarg/7fb776523625a73facb05491ab93ca479279a26e
cp %{_builddir}/yarg-0.1.9/LICENSE-REQUESTS %{buildroot}/usr/share/package-licenses/pypi-yarg/65075425649cfd8ff9e8bae57dea27249239ea6a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/tests/__init__.py
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/tests/__pycache__/__init__.cpython-*.pyc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-yarg/65075425649cfd8ff9e8bae57dea27249239ea6a
/usr/share/package-licenses/pypi-yarg/7fb776523625a73facb05491ab93ca479279a26e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
