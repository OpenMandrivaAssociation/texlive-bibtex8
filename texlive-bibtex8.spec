# revision 29725
# category TLCore
# catalog-ctan /biblio/bibtex/8-bit
# catalog-date 2012-04-27 15:08:24 +0200
# catalog-license gpl
# catalog-version 3.71
Name:		texlive-bibtex8
Version:	3.71
Release:	7
Summary:	A fully 8-bit adaptation of BibTeX 0.99
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/8-bit
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex8.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex8.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-bibtex8.bin

%description
An enhanced, portable C version of BibTeX. Enhanced by
conversion to "big" (32-bit) capacity, addition of run-time
selectable capacity and 8-bit support extensions. National
character set and sorting order are controlled by an external
configuration file. Various examples are included.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/csf/base/88591lat.csf
%{_texmfdistdir}/bibtex/csf/base/88591sca.csf
%{_texmfdistdir}/bibtex/csf/base/README.TEXLIVE
%{_texmfdistdir}/bibtex/csf/base/ascii.csf
%{_texmfdistdir}/bibtex/csf/base/cp437lat.csf
%{_texmfdistdir}/bibtex/csf/base/cp850lat.csf
%{_texmfdistdir}/bibtex/csf/base/cp850sca.csf
%{_texmfdistdir}/bibtex/csf/base/cp866rus.csf
%{_texmfdistdir}/bibtex/csf/base/csfile.txt
%{_texmfdistdir}/bibtex/csf/polish-csf/88592pl.csf
%{_texmfdistdir}/bibtex/csf/polish-csf/cp1250pl.csf
%{_texmfdistdir}/bibtex/csf/polish-csf/cp852pl.csf
%{_texmfdistdir}/bibtex/csf/polish-csf/iso8859-7.csf
%doc %{_texmfdistdir}/doc/bibtex8/00readme.txt
%doc %{_texmfdistdir}/doc/bibtex8/HISTORY
%doc %{_texmfdistdir}/doc/bibtex8/csfile.txt
%doc %{_texmfdistdir}/doc/bibtex8/file_id.diz

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
