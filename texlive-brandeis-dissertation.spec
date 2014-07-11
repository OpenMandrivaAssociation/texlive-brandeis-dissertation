# revision 32047
# category Package
# catalog-ctan /macros/latex/contrib/brandeis-dissertation
# catalog-date 2013-10-31 19:22:02 +0100
# catalog-license lppl1.2
# catalog-version 2.0
Name:		texlive-brandeis-dissertation
Version:	2.0
Release:	7
Summary:	Class for Brandeis University dissertations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/brandeis-dissertation
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-dissertation.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-dissertation.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-dissertation.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class will enable the user to typeset a dissertation which
adheres to the formatting guidelines of Brandeis University
Graduate School of Arts and Sciences (GSAS).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/brandeis-dissertation/brandeis-dissertation.cls
%doc %{_texmfdistdir}/doc/latex/brandeis-dissertation/README
%doc %{_texmfdistdir}/doc/latex/brandeis-dissertation/brandeis-dissertation.pdf
%doc %{_texmfdistdir}/doc/latex/brandeis-dissertation/brandeis-dissertation.tex
#- source
%doc %{_texmfdistdir}/source/latex/brandeis-dissertation/brandeis-dissertation.dtx
%doc %{_texmfdistdir}/source/latex/brandeis-dissertation/brandeis-dissertation.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
