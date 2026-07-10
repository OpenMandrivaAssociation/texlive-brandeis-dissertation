%global tl_name brandeis-dissertation
%global tl_revision 67935

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.14
Release:	%{tl_revision}.1
Summary:	Class for Brandeis University dissertations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/brandeis-dissertation
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-dissertation.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-dissertation.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-dissertation.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class will enable the user to typeset a dissertation which adheres
to the formatting guidelines of Brandeis University Graduate School of
Arts and Sciences (GSAS).

