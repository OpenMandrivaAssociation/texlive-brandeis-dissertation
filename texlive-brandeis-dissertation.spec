Name:		texlive-brandeis-dissertation
Version:	61215
Release:	2
Summary:	Class for Brandeis University dissertations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/brandeis-dissertation
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-dissertation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-dissertation.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-dissertation.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/brandeis-dissertation
%doc %{_texmfdistdir}/doc/latex/brandeis-dissertation
#- source
%doc %{_texmfdistdir}/source/latex/brandeis-dissertation

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
