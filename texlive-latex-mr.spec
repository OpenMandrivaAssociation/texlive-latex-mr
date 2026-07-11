%global tl_name latex-mr
%global tl_revision 55475

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A practical guide to LaTeX and Polyglossia for Marathi and other Indian langu...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex-mr
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-mr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-mr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a short guide to LaTeX and specifically to the
polyglossia package. This document aims to introduce LaTeX and
polyglossia for Indian languages. Though the document often discusses
the language Marathi, the discussion applies to other India languages
also, with some minute changes which are described in Section 1.2. We
assume that the user of this document knows basic (La)TeX or has, at
least, tried her hand on it. This document is not very suitable for
first time users.

