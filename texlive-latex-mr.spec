Name:		texlive-latex-mr
Version:	55475
Release:	1
Summary:	A practical guide to LaTeX and Polyglossia for Marathi and other Indian languages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex-mr
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-mr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-mr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a short guide to LaTeX and specifically to
the polyglossia package. This document aims to introduce LaTeX
and polyglossia for Indian languages. Though the document often
discusses the language Marathi, the discussion applies to other
India languages also, with some minute changes which are
described in Section 1.2. We assume that the user of this
document knows basic (La)TeX or has, at least, tried her hand
on it. This document is not very suitable for first time users.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/latex-mr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
