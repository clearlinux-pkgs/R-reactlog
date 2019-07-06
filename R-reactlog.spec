#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reactlog
Version  : 1.0.0
Release  : 4
URL      : https://cran.r-project.org/src/contrib/reactlog_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/reactlog_1.0.0.tar.gz
Summary  : Reactivity Visualizer for 'shiny'
Group    : Development/Tools
License  : GPL-3.0
Requires: R-jsonlite
Requires: R-shiny
BuildRequires : R-jsonlite
BuildRequires : R-shiny
BuildRequires : buildreq-R

%description
# reactlog
[![Travis Build Status](https://travis-ci.org/rstudio/reactlog.svg?branch=master)](https://travis-ci.org/rstudio/reactlog)
[![CRAN version](http://www.r-pkg.org/badges/version/reactlog)](https://cran.r-project.org/package=reactlog)
[![reactlog downloads per month](http://cranlogs.r-pkg.org/badges/reactlog)](http://www.rpackages.io/package/reactlog)
[![DOI](https://zenodo.org/badge/137799634.svg)](https://zenodo.org/badge/latestdoi/137799634)

%prep
%setup -q -c -n reactlog

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555960284

%install
export SOURCE_DATE_EPOCH=1555960284
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reactlog
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reactlog
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reactlog
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc reactlog || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/reactlog/DESCRIPTION
/usr/lib64/R/library/reactlog/INDEX
/usr/lib64/R/library/reactlog/Meta/Rd.rds
/usr/lib64/R/library/reactlog/Meta/features.rds
/usr/lib64/R/library/reactlog/Meta/hsearch.rds
/usr/lib64/R/library/reactlog/Meta/links.rds
/usr/lib64/R/library/reactlog/Meta/nsInfo.rds
/usr/lib64/R/library/reactlog/Meta/package.rds
/usr/lib64/R/library/reactlog/Meta/vignette.rds
/usr/lib64/R/library/reactlog/NAMESPACE
/usr/lib64/R/library/reactlog/NEWS.md
/usr/lib64/R/library/reactlog/R/reactlog
/usr/lib64/R/library/reactlog/R/reactlog.rdb
/usr/lib64/R/library/reactlog/R/reactlog.rdx
/usr/lib64/R/library/reactlog/doc/index.html
/usr/lib64/R/library/reactlog/doc/reactlog.R
/usr/lib64/R/library/reactlog/doc/reactlog.Rmd
/usr/lib64/R/library/reactlog/doc/reactlog.html
/usr/lib64/R/library/reactlog/help/AnIndex
/usr/lib64/R/library/reactlog/help/aliases.rds
/usr/lib64/R/library/reactlog/help/paths.rds
/usr/lib64/R/library/reactlog/help/reactlog.rdb
/usr/lib64/R/library/reactlog/help/reactlog.rdx
/usr/lib64/R/library/reactlog/html/00Index.html
/usr/lib64/R/library/reactlog/html/R.css
/usr/lib64/R/library/reactlog/reactlog/defaultLog.js
/usr/lib64/R/library/reactlog/reactlog/reactlog.html
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/fira-mono_source-sans-pro_latin-ext.css
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/iconSearch.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/next-end.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/next-idle.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/next-mark.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/next-output-calc.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/next-step.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/prev-idle.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/prev-mark.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/prev-output-calc.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/prev-start.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/images/prev-step.svg
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/reactlog.css
/usr/lib64/R/library/reactlog/reactlog/reactlogAsset/reactlog.js
