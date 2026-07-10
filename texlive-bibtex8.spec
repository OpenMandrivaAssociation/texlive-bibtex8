%global tl_name bibtex8
%global tl_revision 75712

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	BibTeX variant supporting 8-bit encodings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/bibtex-x
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex8.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex8.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(bibtex8.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An enhanced, portable C version of BibTeX. Enhanced by conversion to
larger (32-bit) capacity, addition of run-time selectable capacity and
8-bit support extensions. National character set and sorting order are
controlled by an external configuration file. Various examples are
included. Originally written by Niel Kempson and Alejandro Aguilar-
Sierra, it is now maintained as part of TeX Live.

