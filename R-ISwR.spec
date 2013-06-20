%global packname  ISwR
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.0_6
Release:          2
Summary:          Introductory Statistics with R
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-6.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-survival 
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex 
BuildRequires:    R-survival 
BuildRequires:    pkgconfig(lapack)

%description
Data sets and scripts for text examples and exercises in P. Dalgaard
(2008), `Introductory Statistics with R', 2nd ed., Springer Verlag, ISBN

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/rawdata
%{rlibdir}/%{packname}/scripts


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0_5-1
+ Revision: 776269
- Import R-ISwR
- Import R-ISwR

