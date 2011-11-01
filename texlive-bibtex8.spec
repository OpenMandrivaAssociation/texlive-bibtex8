Name:		texlive-bibtex8
Version:	3.71
Release:	1
Summary:	A fully 8-bit adaptation of BibTeX 0.99
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/8-bit
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex8.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex8.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-bibtex8.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
An enhanced, portable C version of BibTeX. Enhanced by
conversion to "big" (32-bit) capacity, addition of run-time
selectable capacity and 8-bit support extensions. National
character set and sorting order are controlled by an external
configuration file. Various examples are included.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%doc %{_texmfdir}/doc/bibtex8/00readme.txt
%doc %{_texmfdir}/doc/bibtex8/HISTORY
%doc %{_texmfdir}/doc/bibtex8/csfile.txt
%doc %{_texmfdir}/doc/bibtex8/file_id.diz

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
