# encoding: utf-8
# module scipy.linalg.cython_lapack
# from D:\ProgramData\Anaconda3\lib\site-packages\scipy\linalg\cython_lapack.cp36-win_amd64.pyd
# by generator 1.145
"""
LAPACK functions for Cython
===========================

Usable from Cython via::

    cimport scipy.linalg.cython_lapack

This module provides Cython-level wrappers for all primary routines included
in LAPACK 3.1.0 except for ``zcgesv`` since its interface is not consistent
from LAPACK 3.1.0 to 3.6.0. It also provides some of the
fixed-api auxiliary routines.

These wrappers do not check for alignment of arrays.
Alignment should be checked before these wrappers are used.

Raw function pointers (Fortran-style pointer arguments):

- cbdsqr
- cgbbrd
- cgbcon
- cgbequ
- cgbrfs
- cgbsv
- cgbsvx
- cgbtf2
- cgbtrf
- cgbtrs
- cgebak
- cgebal
- cgebd2
- cgebrd
- cgecon
- cgeequ
- cgees
- cgeesx
- cgeev
- cgeevx
- cgehd2
- cgehrd
- cgelq2
- cgelqf
- cgels
- cgelsd
- cgelss
- cgelsy
- cgeql2
- cgeqlf
- cgeqp3
- cgeqr2
- cgeqrf
- cgerfs
- cgerq2
- cgerqf
- cgesc2
- cgesdd
- cgesv
- cgesvd
- cgesvx
- cgetc2
- cgetf2
- cgetrf
- cgetri
- cgetrs
- cggbak
- cggbal
- cgges
- cggesx
- cggev
- cggevx
- cggglm
- cgghrd
- cgglse
- cggqrf
- cggrqf
- cgtcon
- cgtrfs
- cgtsv
- cgtsvx
- cgttrf
- cgttrs
- cgtts2
- chbev
- chbevd
- chbevx
- chbgst
- chbgv
- chbgvd
- chbgvx
- chbtrd
- checon
- cheev
- cheevd
- cheevr
- cheevx
- chegs2
- chegst
- chegv
- chegvd
- chegvx
- cherfs
- chesv
- chesvx
- chetd2
- chetf2
- chetrd
- chetrf
- chetri
- chetrs
- chgeqz
- chpcon
- chpev
- chpevd
- chpevx
- chpgst
- chpgv
- chpgvd
- chpgvx
- chprfs
- chpsv
- chpsvx
- chptrd
- chptrf
- chptri
- chptrs
- chsein
- chseqr
- clabrd
- clacgv
- clacn2
- clacon
- clacp2
- clacpy
- clacrm
- clacrt
- cladiv
- claed0
- claed7
- claed8
- claein
- claesy
- claev2
- clag2z
- clags2
- clagtm
- clahef
- clahqr
- clahr2
- claic1
- clals0
- clalsa
- clalsd
- clangb
- clange
- clangt
- clanhb
- clanhe
- clanhp
- clanhs
- clanht
- clansb
- clansp
- clansy
- clantb
- clantp
- clantr
- clapll
- clapmt
- claqgb
- claqge
- claqhb
- claqhe
- claqhp
- claqp2
- claqps
- claqr0
- claqr1
- claqr2
- claqr3
- claqr4
- claqr5
- claqsb
- claqsp
- claqsy
- clar1v
- clar2v
- clarcm
- clarf
- clarfb
- clarfg
- clarft
- clarfx
- clargv
- clarnv
- clarrv
- clartg
- clartv
- clarz
- clarzb
- clarzt
- clascl
- claset
- clasr
- classq
- claswp
- clasyf
- clatbs
- clatdf
- clatps
- clatrd
- clatrs
- clatrz
- clauu2
- clauum
- cpbcon
- cpbequ
- cpbrfs
- cpbstf
- cpbsv
- cpbsvx
- cpbtf2
- cpbtrf
- cpbtrs
- cpocon
- cpoequ
- cporfs
- cposv
- cposvx
- cpotf2
- cpotrf
- cpotri
- cpotrs
- cppcon
- cppequ
- cpprfs
- cppsv
- cppsvx
- cpptrf
- cpptri
- cpptrs
- cptcon
- cpteqr
- cptrfs
- cptsv
- cptsvx
- cpttrf
- cpttrs
- cptts2
- crot
- cspcon
- cspmv
- cspr
- csprfs
- cspsv
- cspsvx
- csptrf
- csptri
- csptrs
- csrscl
- cstedc
- cstegr
- cstein
- cstemr
- csteqr
- csycon
- csymv
- csyr
- csyrfs
- csysv
- csysvx
- csytf2
- csytrf
- csytri
- csytrs
- ctbcon
- ctbrfs
- ctbtrs
- ctgevc
- ctgex2
- ctgexc
- ctgsen
- ctgsja
- ctgsna
- ctgsy2
- ctgsyl
- ctpcon
- ctprfs
- ctptri
- ctptrs
- ctrcon
- ctrevc
- ctrexc
- ctrrfs
- ctrsen
- ctrsna
- ctrsyl
- ctrti2
- ctrtri
- ctrtrs
- ctzrzf
- cung2l
- cung2r
- cungbr
- cunghr
- cungl2
- cunglq
- cungql
- cungqr
- cungr2
- cungrq
- cungtr
- cunm2l
- cunm2r
- cunmbr
- cunmhr
- cunml2
- cunmlq
- cunmql
- cunmqr
- cunmr2
- cunmr3
- cunmrq
- cunmrz
- cunmtr
- cupgtr
- cupmtr
- dbdsdc
- dbdsqr
- ddisna
- dgbbrd
- dgbcon
- dgbequ
- dgbrfs
- dgbsv
- dgbsvx
- dgbtf2
- dgbtrf
- dgbtrs
- dgebak
- dgebal
- dgebd2
- dgebrd
- dgecon
- dgeequ
- dgees
- dgeesx
- dgeev
- dgeevx
- dgehd2
- dgehrd
- dgelq2
- dgelqf
- dgels
- dgelsd
- dgelss
- dgelsy
- dgeql2
- dgeqlf
- dgeqp3
- dgeqr2
- dgeqrf
- dgerfs
- dgerq2
- dgerqf
- dgesc2
- dgesdd
- dgesv
- dgesvd
- dgesvx
- dgetc2
- dgetf2
- dgetrf
- dgetri
- dgetrs
- dggbak
- dggbal
- dgges
- dggesx
- dggev
- dggevx
- dggglm
- dgghrd
- dgglse
- dggqrf
- dggrqf
- dgtcon
- dgtrfs
- dgtsv
- dgtsvx
- dgttrf
- dgttrs
- dgtts2
- dhgeqz
- dhsein
- dhseqr
- disnan
- dlabad
- dlabrd
- dlacn2
- dlacon
- dlacpy
- dladiv
- dlae2
- dlaebz
- dlaed0
- dlaed1
- dlaed2
- dlaed3
- dlaed4
- dlaed5
- dlaed6
- dlaed7
- dlaed8
- dlaed9
- dlaeda
- dlaein
- dlaev2
- dlaexc
- dlag2
- dlag2s
- dlags2
- dlagtf
- dlagtm
- dlagts
- dlagv2
- dlahqr
- dlahr2
- dlaic1
- dlaln2
- dlals0
- dlalsa
- dlalsd
- dlamch
- dlamrg
- dlaneg
- dlangb
- dlange
- dlangt
- dlanhs
- dlansb
- dlansp
- dlanst
- dlansy
- dlantb
- dlantp
- dlantr
- dlanv2
- dlapll
- dlapmt
- dlapy2
- dlapy3
- dlaqgb
- dlaqge
- dlaqp2
- dlaqps
- dlaqr0
- dlaqr1
- dlaqr2
- dlaqr3
- dlaqr4
- dlaqr5
- dlaqsb
- dlaqsp
- dlaqsy
- dlaqtr
- dlar1v
- dlar2v
- dlarf
- dlarfb
- dlarfg
- dlarft
- dlarfx
- dlargv
- dlarnv
- dlarra
- dlarrb
- dlarrc
- dlarrd
- dlarre
- dlarrf
- dlarrj
- dlarrk
- dlarrr
- dlarrv
- dlartg
- dlartv
- dlaruv
- dlarz
- dlarzb
- dlarzt
- dlas2
- dlascl
- dlasd0
- dlasd1
- dlasd2
- dlasd3
- dlasd4
- dlasd5
- dlasd6
- dlasd7
- dlasd8
- dlasda
- dlasdq
- dlasdt
- dlaset
- dlasq1
- dlasq2
- dlasq6
- dlasr
- dlasrt
- dlassq
- dlasv2
- dlaswp
- dlasy2
- dlasyf
- dlatbs
- dlatdf
- dlatps
- dlatrd
- dlatrs
- dlatrz
- dlauu2
- dlauum
- dopgtr
- dopmtr
- dorg2l
- dorg2r
- dorgbr
- dorghr
- dorgl2
- dorglq
- dorgql
- dorgqr
- dorgr2
- dorgrq
- dorgtr
- dorm2l
- dorm2r
- dormbr
- dormhr
- dorml2
- dormlq
- dormql
- dormqr
- dormr2
- dormr3
- dormrq
- dormrz
- dormtr
- dpbcon
- dpbequ
- dpbrfs
- dpbstf
- dpbsv
- dpbsvx
- dpbtf2
- dpbtrf
- dpbtrs
- dpocon
- dpoequ
- dporfs
- dposv
- dposvx
- dpotf2
- dpotrf
- dpotri
- dpotrs
- dppcon
- dppequ
- dpprfs
- dppsv
- dppsvx
- dpptrf
- dpptri
- dpptrs
- dptcon
- dpteqr
- dptrfs
- dptsv
- dptsvx
- dpttrf
- dpttrs
- dptts2
- drscl
- dsbev
- dsbevd
- dsbevx
- dsbgst
- dsbgv
- dsbgvd
- dsbgvx
- dsbtrd
- dsgesv
- dspcon
- dspev
- dspevd
- dspevx
- dspgst
- dspgv
- dspgvd
- dspgvx
- dsprfs
- dspsv
- dspsvx
- dsptrd
- dsptrf
- dsptri
- dsptrs
- dstebz
- dstedc
- dstegr
- dstein
- dstemr
- dsteqr
- dsterf
- dstev
- dstevd
- dstevr
- dstevx
- dsycon
- dsyev
- dsyevd
- dsyevr
- dsyevx
- dsygs2
- dsygst
- dsygv
- dsygvd
- dsygvx
- dsyrfs
- dsysv
- dsysvx
- dsytd2
- dsytf2
- dsytrd
- dsytrf
- dsytri
- dsytrs
- dtbcon
- dtbrfs
- dtbtrs
- dtgevc
- dtgex2
- dtgexc
- dtgsen
- dtgsja
- dtgsna
- dtgsy2
- dtgsyl
- dtpcon
- dtprfs
- dtptri
- dtptrs
- dtrcon
- dtrevc
- dtrexc
- dtrrfs
- dtrsen
- dtrsna
- dtrsyl
- dtrti2
- dtrtri
- dtrtrs
- dtzrzf
- dzsum1
- icmax1
- ieeeck
- ilaver
- izmax1
- sbdsdc
- sbdsqr
- scsum1
- sdisna
- sgbbrd
- sgbcon
- sgbequ
- sgbrfs
- sgbsv
- sgbsvx
- sgbtf2
- sgbtrf
- sgbtrs
- sgebak
- sgebal
- sgebd2
- sgebrd
- sgecon
- sgeequ
- sgees
- sgeesx
- sgeev
- sgeevx
- sgehd2
- sgehrd
- sgelq2
- sgelqf
- sgels
- sgelsd
- sgelss
- sgelsy
- sgeql2
- sgeqlf
- sgeqp3
- sgeqr2
- sgeqrf
- sgerfs
- sgerq2
- sgerqf
- sgesc2
- sgesdd
- sgesv
- sgesvd
- sgesvx
- sgetc2
- sgetf2
- sgetrf
- sgetri
- sgetrs
- sggbak
- sggbal
- sgges
- sggesx
- sggev
- sggevx
- sggglm
- sgghrd
- sgglse
- sggqrf
- sggrqf
- sgtcon
- sgtrfs
- sgtsv
- sgtsvx
- sgttrf
- sgttrs
- sgtts2
- shgeqz
- shsein
- shseqr
- slabad
- slabrd
- slacn2
- slacon
- slacpy
- sladiv
- slae2
- slaebz
- slaed0
- slaed1
- slaed2
- slaed3
- slaed4
- slaed5
- slaed6
- slaed7
- slaed8
- slaed9
- slaeda
- slaein
- slaev2
- slaexc
- slag2
- slag2d
- slags2
- slagtf
- slagtm
- slagts
- slagv2
- slahqr
- slahr2
- slaic1
- slaln2
- slals0
- slalsa
- slalsd
- slamch
- slamrg
- slangb
- slange
- slangt
- slanhs
- slansb
- slansp
- slanst
- slansy
- slantb
- slantp
- slantr
- slanv2
- slapll
- slapmt
- slapy2
- slapy3
- slaqgb
- slaqge
- slaqp2
- slaqps
- slaqr0
- slaqr1
- slaqr2
- slaqr3
- slaqr4
- slaqr5
- slaqsb
- slaqsp
- slaqsy
- slaqtr
- slar1v
- slar2v
- slarf
- slarfb
- slarfg
- slarft
- slarfx
- slargv
- slarnv
- slarra
- slarrb
- slarrc
- slarrd
- slarre
- slarrf
- slarrj
- slarrk
- slarrr
- slarrv
- slartg
- slartv
- slaruv
- slarz
- slarzb
- slarzt
- slas2
- slascl
- slasd0
- slasd1
- slasd2
- slasd3
- slasd4
- slasd5
- slasd6
- slasd7
- slasd8
- slasda
- slasdq
- slasdt
- slaset
- slasq1
- slasq2
- slasq6
- slasr
- slasrt
- slassq
- slasv2
- slaswp
- slasy2
- slasyf
- slatbs
- slatdf
- slatps
- slatrd
- slatrs
- slatrz
- slauu2
- slauum
- sopgtr
- sopmtr
- sorg2l
- sorg2r
- sorgbr
- sorghr
- sorgl2
- sorglq
- sorgql
- sorgqr
- sorgr2
- sorgrq
- sorgtr
- sorm2l
- sorm2r
- sormbr
- sormhr
- sorml2
- sormlq
- sormql
- sormqr
- sormr2
- sormr3
- sormrq
- sormrz
- sormtr
- spbcon
- spbequ
- spbrfs
- spbstf
- spbsv
- spbsvx
- spbtf2
- spbtrf
- spbtrs
- spocon
- spoequ
- sporfs
- sposv
- sposvx
- spotf2
- spotrf
- spotri
- spotrs
- sppcon
- sppequ
- spprfs
- sppsv
- sppsvx
- spptrf
- spptri
- spptrs
- sptcon
- spteqr
- sptrfs
- sptsv
- sptsvx
- spttrf
- spttrs
- sptts2
- srscl
- ssbev
- ssbevd
- ssbevx
- ssbgst
- ssbgv
- ssbgvd
- ssbgvx
- ssbtrd
- sspcon
- sspev
- sspevd
- sspevx
- sspgst
- sspgv
- sspgvd
- sspgvx
- ssprfs
- sspsv
- sspsvx
- ssptrd
- ssptrf
- ssptri
- ssptrs
- sstebz
- sstedc
- sstegr
- sstein
- sstemr
- ssteqr
- ssterf
- sstev
- sstevd
- sstevr
- sstevx
- ssycon
- ssyev
- ssyevd
- ssyevr
- ssyevx
- ssygs2
- ssygst
- ssygv
- ssygvd
- ssygvx
- ssyrfs
- ssysv
- ssysvx
- ssytd2
- ssytf2
- ssytrd
- ssytrf
- ssytri
- ssytrs
- stbcon
- stbrfs
- stbtrs
- stgevc
- stgex2
- stgexc
- stgsen
- stgsja
- stgsna
- stgsy2
- stgsyl
- stpcon
- stprfs
- stptri
- stptrs
- strcon
- strevc
- strexc
- strrfs
- strsen
- strsna
- strsyl
- strti2
- strtri
- strtrs
- stzrzf
- zbdsqr
- zdrscl
- zgbbrd
- zgbcon
- zgbequ
- zgbrfs
- zgbsv
- zgbsvx
- zgbtf2
- zgbtrf
- zgbtrs
- zgebak
- zgebal
- zgebd2
- zgebrd
- zgecon
- zgeequ
- zgees
- zgeesx
- zgeev
- zgeevx
- zgehd2
- zgehrd
- zgelq2
- zgelqf
- zgels
- zgelsd
- zgelss
- zgelsy
- zgeql2
- zgeqlf
- zgeqp3
- zgeqr2
- zgeqrf
- zgerfs
- zgerq2
- zgerqf
- zgesc2
- zgesdd
- zgesv
- zgesvd
- zgesvx
- zgetc2
- zgetf2
- zgetrf
- zgetri
- zgetrs
- zggbak
- zggbal
- zgges
- zggesx
- zggev
- zggevx
- zggglm
- zgghrd
- zgglse
- zggqrf
- zggrqf
- zgtcon
- zgtrfs
- zgtsv
- zgtsvx
- zgttrf
- zgttrs
- zgtts2
- zhbev
- zhbevd
- zhbevx
- zhbgst
- zhbgv
- zhbgvd
- zhbgvx
- zhbtrd
- zhecon
- zheev
- zheevd
- zheevr
- zheevx
- zhegs2
- zhegst
- zhegv
- zhegvd
- zhegvx
- zherfs
- zhesv
- zhesvx
- zhetd2
- zhetf2
- zhetrd
- zhetrf
- zhetri
- zhetrs
- zhgeqz
- zhpcon
- zhpev
- zhpevd
- zhpevx
- zhpgst
- zhpgv
- zhpgvd
- zhpgvx
- zhprfs
- zhpsv
- zhpsvx
- zhptrd
- zhptrf
- zhptri
- zhptrs
- zhsein
- zhseqr
- zlabrd
- zlacgv
- zlacn2
- zlacon
- zlacp2
- zlacpy
- zlacrm
- zlacrt
- zladiv
- zlaed0
- zlaed7
- zlaed8
- zlaein
- zlaesy
- zlaev2
- zlag2c
- zlags2
- zlagtm
- zlahef
- zlahqr
- zlahr2
- zlaic1
- zlals0
- zlalsa
- zlalsd
- zlangb
- zlange
- zlangt
- zlanhb
- zlanhe
- zlanhp
- zlanhs
- zlanht
- zlansb
- zlansp
- zlansy
- zlantb
- zlantp
- zlantr
- zlapll
- zlapmt
- zlaqgb
- zlaqge
- zlaqhb
- zlaqhe
- zlaqhp
- zlaqp2
- zlaqps
- zlaqr0
- zlaqr1
- zlaqr2
- zlaqr3
- zlaqr4
- zlaqr5
- zlaqsb
- zlaqsp
- zlaqsy
- zlar1v
- zlar2v
- zlarcm
- zlarf
- zlarfb
- zlarfg
- zlarft
- zlarfx
- zlargv
- zlarnv
- zlarrv
- zlartg
- zlartv
- zlarz
- zlarzb
- zlarzt
- zlascl
- zlaset
- zlasr
- zlassq
- zlaswp
- zlasyf
- zlatbs
- zlatdf
- zlatps
- zlatrd
- zlatrs
- zlatrz
- zlauu2
- zlauum
- zpbcon
- zpbequ
- zpbrfs
- zpbstf
- zpbsv
- zpbsvx
- zpbtf2
- zpbtrf
- zpbtrs
- zpocon
- zpoequ
- zporfs
- zposv
- zposvx
- zpotf2
- zpotrf
- zpotri
- zpotrs
- zppcon
- zppequ
- zpprfs
- zppsv
- zppsvx
- zpptrf
- zpptri
- zpptrs
- zptcon
- zpteqr
- zptrfs
- zptsv
- zptsvx
- zpttrf
- zpttrs
- zptts2
- zrot
- zspcon
- zspmv
- zspr
- zsprfs
- zspsv
- zspsvx
- zsptrf
- zsptri
- zsptrs
- zstedc
- zstegr
- zstein
- zstemr
- zsteqr
- zsycon
- zsymv
- zsyr
- zsyrfs
- zsysv
- zsysvx
- zsytf2
- zsytrf
- zsytri
- zsytrs
- ztbcon
- ztbrfs
- ztbtrs
- ztgevc
- ztgex2
- ztgexc
- ztgsen
- ztgsja
- ztgsna
- ztgsy2
- ztgsyl
- ztpcon
- ztprfs
- ztptri
- ztptrs
- ztrcon
- ztrevc
- ztrexc
- ztrrfs
- ztrsen
- ztrsna
- ztrsyl
- ztrti2
- ztrtri
- ztrtrs
- ztzrzf
- zung2l
- zung2r
- zungbr
- zunghr
- zungl2
- zunglq
- zungql
- zungqr
- zungr2
- zungrq
- zungtr
- zunm2l
- zunm2r
- zunmbr
- zunmhr
- zunml2
- zunmlq
- zunmql
- zunmqr
- zunmr2
- zunmr3
- zunmrq
- zunmrz
- zunmtr
- zupgtr
- zupmtr
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _test_dlamch(*args, **kwargs): # real signature unknown
    pass

def _test_slamch(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'cbdsqr': None, # (!) real value is ''
    'cgbbrd': None, # (!) real value is ''
    'cgbcon': None, # (!) real value is ''
    'cgbequ': None, # (!) real value is ''
    'cgbrfs': None, # (!) real value is ''
    'cgbsv': None, # (!) real value is ''
    'cgbsvx': None, # (!) real value is ''
    'cgbtf2': None, # (!) real value is ''
    'cgbtrf': None, # (!) real value is ''
    'cgbtrs': None, # (!) real value is ''
    'cgebak': None, # (!) real value is ''
    'cgebal': None, # (!) real value is ''
    'cgebd2': None, # (!) real value is ''
    'cgebrd': None, # (!) real value is ''
    'cgecon': None, # (!) real value is ''
    'cgeequ': None, # (!) real value is ''
    'cgees': None, # (!) real value is ''
    'cgeesx': None, # (!) real value is ''
    'cgeev': None, # (!) real value is ''
    'cgeevx': None, # (!) real value is ''
    'cgehd2': None, # (!) real value is ''
    'cgehrd': None, # (!) real value is ''
    'cgelq2': None, # (!) real value is ''
    'cgelqf': None, # (!) real value is ''
    'cgels': None, # (!) real value is ''
    'cgelsd': None, # (!) real value is ''
    'cgelss': None, # (!) real value is ''
    'cgelsy': None, # (!) real value is ''
    'cgeql2': None, # (!) real value is ''
    'cgeqlf': None, # (!) real value is ''
    'cgeqp3': None, # (!) real value is ''
    'cgeqr2': None, # (!) real value is ''
    'cgeqrf': None, # (!) real value is ''
    'cgerfs': None, # (!) real value is ''
    'cgerq2': None, # (!) real value is ''
    'cgerqf': None, # (!) real value is ''
    'cgesc2': None, # (!) real value is ''
    'cgesdd': None, # (!) real value is ''
    'cgesv': None, # (!) real value is ''
    'cgesvd': None, # (!) real value is ''
    'cgesvx': None, # (!) real value is ''
    'cgetc2': None, # (!) real value is ''
    'cgetf2': None, # (!) real value is ''
    'cgetrf': None, # (!) real value is ''
    'cgetri': None, # (!) real value is ''
    'cgetrs': None, # (!) real value is ''
    'cggbak': None, # (!) real value is ''
    'cggbal': None, # (!) real value is ''
    'cgges': None, # (!) real value is ''
    'cggesx': None, # (!) real value is ''
    'cggev': None, # (!) real value is ''
    'cggevx': None, # (!) real value is ''
    'cggglm': None, # (!) real value is ''
    'cgghrd': None, # (!) real value is ''
    'cgglse': None, # (!) real value is ''
    'cggqrf': None, # (!) real value is ''
    'cggrqf': None, # (!) real value is ''
    'cgtcon': None, # (!) real value is ''
    'cgtrfs': None, # (!) real value is ''
    'cgtsv': None, # (!) real value is ''
    'cgtsvx': None, # (!) real value is ''
    'cgttrf': None, # (!) real value is ''
    'cgttrs': None, # (!) real value is ''
    'cgtts2': None, # (!) real value is ''
    'chbev': None, # (!) real value is ''
    'chbevd': None, # (!) real value is ''
    'chbevx': None, # (!) real value is ''
    'chbgst': None, # (!) real value is ''
    'chbgv': None, # (!) real value is ''
    'chbgvd': None, # (!) real value is ''
    'chbgvx': None, # (!) real value is ''
    'chbtrd': None, # (!) real value is ''
    'checon': None, # (!) real value is ''
    'cheev': None, # (!) real value is ''
    'cheevd': None, # (!) real value is ''
    'cheevr': None, # (!) real value is ''
    'cheevx': None, # (!) real value is ''
    'chegs2': None, # (!) real value is ''
    'chegst': None, # (!) real value is ''
    'chegv': None, # (!) real value is ''
    'chegvd': None, # (!) real value is ''
    'chegvx': None, # (!) real value is ''
    'cherfs': None, # (!) real value is ''
    'chesv': None, # (!) real value is ''
    'chesvx': None, # (!) real value is ''
    'chetd2': None, # (!) real value is ''
    'chetf2': None, # (!) real value is ''
    'chetrd': None, # (!) real value is ''
    'chetrf': None, # (!) real value is ''
    'chetri': None, # (!) real value is ''
    'chetrs': None, # (!) real value is ''
    'chgeqz': None, # (!) real value is ''
    'chpcon': None, # (!) real value is ''
    'chpev': None, # (!) real value is ''
    'chpevd': None, # (!) real value is ''
    'chpevx': None, # (!) real value is ''
    'chpgst': None, # (!) real value is ''
    'chpgv': None, # (!) real value is ''
    'chpgvd': None, # (!) real value is ''
    'chpgvx': None, # (!) real value is ''
    'chprfs': None, # (!) real value is ''
    'chpsv': None, # (!) real value is ''
    'chpsvx': None, # (!) real value is ''
    'chptrd': None, # (!) real value is ''
    'chptrf': None, # (!) real value is ''
    'chptri': None, # (!) real value is ''
    'chptrs': None, # (!) real value is ''
    'chsein': None, # (!) real value is ''
    'chseqr': None, # (!) real value is ''
    'clabrd': None, # (!) real value is ''
    'clacgv': None, # (!) real value is ''
    'clacn2': None, # (!) real value is ''
    'clacon': None, # (!) real value is ''
    'clacp2': None, # (!) real value is ''
    'clacpy': None, # (!) real value is ''
    'clacrm': None, # (!) real value is ''
    'clacrt': None, # (!) real value is ''
    'cladiv': None, # (!) real value is ''
    'claed0': None, # (!) real value is ''
    'claed7': None, # (!) real value is ''
    'claed8': None, # (!) real value is ''
    'claein': None, # (!) real value is ''
    'claesy': None, # (!) real value is ''
    'claev2': None, # (!) real value is ''
    'clag2z': None, # (!) real value is ''
    'clags2': None, # (!) real value is ''
    'clagtm': None, # (!) real value is ''
    'clahef': None, # (!) real value is ''
    'clahqr': None, # (!) real value is ''
    'clahr2': None, # (!) real value is ''
    'claic1': None, # (!) real value is ''
    'clals0': None, # (!) real value is ''
    'clalsa': None, # (!) real value is ''
    'clalsd': None, # (!) real value is ''
    'clangb': None, # (!) real value is ''
    'clange': None, # (!) real value is ''
    'clangt': None, # (!) real value is ''
    'clanhb': None, # (!) real value is ''
    'clanhe': None, # (!) real value is ''
    'clanhp': None, # (!) real value is ''
    'clanhs': None, # (!) real value is ''
    'clanht': None, # (!) real value is ''
    'clansb': None, # (!) real value is ''
    'clansp': None, # (!) real value is ''
    'clansy': None, # (!) real value is ''
    'clantb': None, # (!) real value is ''
    'clantp': None, # (!) real value is ''
    'clantr': None, # (!) real value is ''
    'clapll': None, # (!) real value is ''
    'clapmt': None, # (!) real value is ''
    'claqgb': None, # (!) real value is ''
    'claqge': None, # (!) real value is ''
    'claqhb': None, # (!) real value is ''
    'claqhe': None, # (!) real value is ''
    'claqhp': None, # (!) real value is ''
    'claqp2': None, # (!) real value is ''
    'claqps': None, # (!) real value is ''
    'claqr0': None, # (!) real value is ''
    'claqr1': None, # (!) real value is ''
    'claqr2': None, # (!) real value is ''
    'claqr3': None, # (!) real value is ''
    'claqr4': None, # (!) real value is ''
    'claqr5': None, # (!) real value is ''
    'claqsb': None, # (!) real value is ''
    'claqsp': None, # (!) real value is ''
    'claqsy': None, # (!) real value is ''
    'clar1v': None, # (!) real value is ''
    'clar2v': None, # (!) real value is ''
    'clarcm': None, # (!) real value is ''
    'clarf': None, # (!) real value is ''
    'clarfb': None, # (!) real value is ''
    'clarfg': None, # (!) real value is ''
    'clarft': None, # (!) real value is ''
    'clarfx': None, # (!) real value is ''
    'clargv': None, # (!) real value is ''
    'clarnv': None, # (!) real value is ''
    'clarrv': None, # (!) real value is ''
    'clartg': None, # (!) real value is ''
    'clartv': None, # (!) real value is ''
    'clarz': None, # (!) real value is ''
    'clarzb': None, # (!) real value is ''
    'clarzt': None, # (!) real value is ''
    'clascl': None, # (!) real value is ''
    'claset': None, # (!) real value is ''
    'clasr': None, # (!) real value is ''
    'classq': None, # (!) real value is ''
    'claswp': None, # (!) real value is ''
    'clasyf': None, # (!) real value is ''
    'clatbs': None, # (!) real value is ''
    'clatdf': None, # (!) real value is ''
    'clatps': None, # (!) real value is ''
    'clatrd': None, # (!) real value is ''
    'clatrs': None, # (!) real value is ''
    'clatrz': None, # (!) real value is ''
    'clauu2': None, # (!) real value is ''
    'clauum': None, # (!) real value is ''
    'cpbcon': None, # (!) real value is ''
    'cpbequ': None, # (!) real value is ''
    'cpbrfs': None, # (!) real value is ''
    'cpbstf': None, # (!) real value is ''
    'cpbsv': None, # (!) real value is ''
    'cpbsvx': None, # (!) real value is ''
    'cpbtf2': None, # (!) real value is ''
    'cpbtrf': None, # (!) real value is ''
    'cpbtrs': None, # (!) real value is ''
    'cpocon': None, # (!) real value is ''
    'cpoequ': None, # (!) real value is ''
    'cporfs': None, # (!) real value is ''
    'cposv': None, # (!) real value is ''
    'cposvx': None, # (!) real value is ''
    'cpotf2': None, # (!) real value is ''
    'cpotrf': None, # (!) real value is ''
    'cpotri': None, # (!) real value is ''
    'cpotrs': None, # (!) real value is ''
    'cppcon': None, # (!) real value is ''
    'cppequ': None, # (!) real value is ''
    'cpprfs': None, # (!) real value is ''
    'cppsv': None, # (!) real value is ''
    'cppsvx': None, # (!) real value is ''
    'cpptrf': None, # (!) real value is ''
    'cpptri': None, # (!) real value is ''
    'cpptrs': None, # (!) real value is ''
    'cptcon': None, # (!) real value is ''
    'cpteqr': None, # (!) real value is ''
    'cptrfs': None, # (!) real value is ''
    'cptsv': None, # (!) real value is ''
    'cptsvx': None, # (!) real value is ''
    'cpttrf': None, # (!) real value is ''
    'cpttrs': None, # (!) real value is ''
    'cptts2': None, # (!) real value is ''
    'crot': None, # (!) real value is ''
    'cspcon': None, # (!) real value is ''
    'cspmv': None, # (!) real value is ''
    'cspr': None, # (!) real value is ''
    'csprfs': None, # (!) real value is ''
    'cspsv': None, # (!) real value is ''
    'cspsvx': None, # (!) real value is ''
    'csptrf': None, # (!) real value is ''
    'csptri': None, # (!) real value is ''
    'csptrs': None, # (!) real value is ''
    'csrscl': None, # (!) real value is ''
    'cstedc': None, # (!) real value is ''
    'cstegr': None, # (!) real value is ''
    'cstein': None, # (!) real value is ''
    'cstemr': None, # (!) real value is ''
    'csteqr': None, # (!) real value is ''
    'csycon': None, # (!) real value is ''
    'csymv': None, # (!) real value is ''
    'csyr': None, # (!) real value is ''
    'csyrfs': None, # (!) real value is ''
    'csysv': None, # (!) real value is ''
    'csysvx': None, # (!) real value is ''
    'csytf2': None, # (!) real value is ''
    'csytrf': None, # (!) real value is ''
    'csytri': None, # (!) real value is ''
    'csytrs': None, # (!) real value is ''
    'ctbcon': None, # (!) real value is ''
    'ctbrfs': None, # (!) real value is ''
    'ctbtrs': None, # (!) real value is ''
    'ctgevc': None, # (!) real value is ''
    'ctgex2': None, # (!) real value is ''
    'ctgexc': None, # (!) real value is ''
    'ctgsen': None, # (!) real value is ''
    'ctgsja': None, # (!) real value is ''
    'ctgsna': None, # (!) real value is ''
    'ctgsy2': None, # (!) real value is ''
    'ctgsyl': None, # (!) real value is ''
    'ctpcon': None, # (!) real value is ''
    'ctprfs': None, # (!) real value is ''
    'ctptri': None, # (!) real value is ''
    'ctptrs': None, # (!) real value is ''
    'ctrcon': None, # (!) real value is ''
    'ctrevc': None, # (!) real value is ''
    'ctrexc': None, # (!) real value is ''
    'ctrrfs': None, # (!) real value is ''
    'ctrsen': None, # (!) real value is ''
    'ctrsna': None, # (!) real value is ''
    'ctrsyl': None, # (!) real value is ''
    'ctrti2': None, # (!) real value is ''
    'ctrtri': None, # (!) real value is ''
    'ctrtrs': None, # (!) real value is ''
    'ctzrzf': None, # (!) real value is ''
    'cung2l': None, # (!) real value is ''
    'cung2r': None, # (!) real value is ''
    'cungbr': None, # (!) real value is ''
    'cunghr': None, # (!) real value is ''
    'cungl2': None, # (!) real value is ''
    'cunglq': None, # (!) real value is ''
    'cungql': None, # (!) real value is ''
    'cungqr': None, # (!) real value is ''
    'cungr2': None, # (!) real value is ''
    'cungrq': None, # (!) real value is ''
    'cungtr': None, # (!) real value is ''
    'cunm2l': None, # (!) real value is ''
    'cunm2r': None, # (!) real value is ''
    'cunmbr': None, # (!) real value is ''
    'cunmhr': None, # (!) real value is ''
    'cunml2': None, # (!) real value is ''
    'cunmlq': None, # (!) real value is ''
    'cunmql': None, # (!) real value is ''
    'cunmqr': None, # (!) real value is ''
    'cunmr2': None, # (!) real value is ''
    'cunmr3': None, # (!) real value is ''
    'cunmrq': None, # (!) real value is ''
    'cunmrz': None, # (!) real value is ''
    'cunmtr': None, # (!) real value is ''
    'cupgtr': None, # (!) real value is ''
    'cupmtr': None, # (!) real value is ''
    'dbdsdc': None, # (!) real value is ''
    'dbdsqr': None, # (!) real value is ''
    'ddisna': None, # (!) real value is ''
    'dgbbrd': None, # (!) real value is ''
    'dgbcon': None, # (!) real value is ''
    'dgbequ': None, # (!) real value is ''
    'dgbrfs': None, # (!) real value is ''
    'dgbsv': None, # (!) real value is ''
    'dgbsvx': None, # (!) real value is ''
    'dgbtf2': None, # (!) real value is ''
    'dgbtrf': None, # (!) real value is ''
    'dgbtrs': None, # (!) real value is ''
    'dgebak': None, # (!) real value is ''
    'dgebal': None, # (!) real value is ''
    'dgebd2': None, # (!) real value is ''
    'dgebrd': None, # (!) real value is ''
    'dgecon': None, # (!) real value is ''
    'dgeequ': None, # (!) real value is ''
    'dgees': None, # (!) real value is ''
    'dgeesx': None, # (!) real value is ''
    'dgeev': None, # (!) real value is ''
    'dgeevx': None, # (!) real value is ''
    'dgehd2': None, # (!) real value is ''
    'dgehrd': None, # (!) real value is ''
    'dgelq2': None, # (!) real value is ''
    'dgelqf': None, # (!) real value is ''
    'dgels': None, # (!) real value is ''
    'dgelsd': None, # (!) real value is ''
    'dgelss': None, # (!) real value is ''
    'dgelsy': None, # (!) real value is ''
    'dgeql2': None, # (!) real value is ''
    'dgeqlf': None, # (!) real value is ''
    'dgeqp3': None, # (!) real value is ''
    'dgeqr2': None, # (!) real value is ''
    'dgeqrf': None, # (!) real value is ''
    'dgerfs': None, # (!) real value is ''
    'dgerq2': None, # (!) real value is ''
    'dgerqf': None, # (!) real value is ''
    'dgesc2': None, # (!) real value is ''
    'dgesdd': None, # (!) real value is ''
    'dgesv': None, # (!) real value is ''
    'dgesvd': None, # (!) real value is ''
    'dgesvx': None, # (!) real value is ''
    'dgetc2': None, # (!) real value is ''
    'dgetf2': None, # (!) real value is ''
    'dgetrf': None, # (!) real value is ''
    'dgetri': None, # (!) real value is ''
    'dgetrs': None, # (!) real value is ''
    'dggbak': None, # (!) real value is ''
    'dggbal': None, # (!) real value is ''
    'dgges': None, # (!) real value is ''
    'dggesx': None, # (!) real value is ''
    'dggev': None, # (!) real value is ''
    'dggevx': None, # (!) real value is ''
    'dggglm': None, # (!) real value is ''
    'dgghrd': None, # (!) real value is ''
    'dgglse': None, # (!) real value is ''
    'dggqrf': None, # (!) real value is ''
    'dggrqf': None, # (!) real value is ''
    'dgtcon': None, # (!) real value is ''
    'dgtrfs': None, # (!) real value is ''
    'dgtsv': None, # (!) real value is ''
    'dgtsvx': None, # (!) real value is ''
    'dgttrf': None, # (!) real value is ''
    'dgttrs': None, # (!) real value is ''
    'dgtts2': None, # (!) real value is ''
    'dhgeqz': None, # (!) real value is ''
    'dhsein': None, # (!) real value is ''
    'dhseqr': None, # (!) real value is ''
    'disnan': None, # (!) real value is ''
    'dlabad': None, # (!) real value is ''
    'dlabrd': None, # (!) real value is ''
    'dlacn2': None, # (!) real value is ''
    'dlacon': None, # (!) real value is ''
    'dlacpy': None, # (!) real value is ''
    'dladiv': None, # (!) real value is ''
    'dlae2': None, # (!) real value is ''
    'dlaebz': None, # (!) real value is ''
    'dlaed0': None, # (!) real value is ''
    'dlaed1': None, # (!) real value is ''
    'dlaed2': None, # (!) real value is ''
    'dlaed3': None, # (!) real value is ''
    'dlaed4': None, # (!) real value is ''
    'dlaed5': None, # (!) real value is ''
    'dlaed6': None, # (!) real value is ''
    'dlaed7': None, # (!) real value is ''
    'dlaed8': None, # (!) real value is ''
    'dlaed9': None, # (!) real value is ''
    'dlaeda': None, # (!) real value is ''
    'dlaein': None, # (!) real value is ''
    'dlaev2': None, # (!) real value is ''
    'dlaexc': None, # (!) real value is ''
    'dlag2': None, # (!) real value is ''
    'dlag2s': None, # (!) real value is ''
    'dlags2': None, # (!) real value is ''
    'dlagtf': None, # (!) real value is ''
    'dlagtm': None, # (!) real value is ''
    'dlagts': None, # (!) real value is ''
    'dlagv2': None, # (!) real value is ''
    'dlahqr': None, # (!) real value is ''
    'dlahr2': None, # (!) real value is ''
    'dlaic1': None, # (!) real value is ''
    'dlaln2': None, # (!) real value is ''
    'dlals0': None, # (!) real value is ''
    'dlalsa': None, # (!) real value is ''
    'dlalsd': None, # (!) real value is ''
    'dlamch': None, # (!) real value is ''
    'dlamrg': None, # (!) real value is ''
    'dlaneg': None, # (!) real value is ''
    'dlangb': None, # (!) real value is ''
    'dlange': None, # (!) real value is ''
    'dlangt': None, # (!) real value is ''
    'dlanhs': None, # (!) real value is ''
    'dlansb': None, # (!) real value is ''
    'dlansp': None, # (!) real value is ''
    'dlanst': None, # (!) real value is ''
    'dlansy': None, # (!) real value is ''
    'dlantb': None, # (!) real value is ''
    'dlantp': None, # (!) real value is ''
    'dlantr': None, # (!) real value is ''
    'dlanv2': None, # (!) real value is ''
    'dlapll': None, # (!) real value is ''
    'dlapmt': None, # (!) real value is ''
    'dlapy2': None, # (!) real value is ''
    'dlapy3': None, # (!) real value is ''
    'dlaqgb': None, # (!) real value is ''
    'dlaqge': None, # (!) real value is ''
    'dlaqp2': None, # (!) real value is ''
    'dlaqps': None, # (!) real value is ''
    'dlaqr0': None, # (!) real value is ''
    'dlaqr1': None, # (!) real value is ''
    'dlaqr2': None, # (!) real value is ''
    'dlaqr3': None, # (!) real value is ''
    'dlaqr4': None, # (!) real value is ''
    'dlaqr5': None, # (!) real value is ''
    'dlaqsb': None, # (!) real value is ''
    'dlaqsp': None, # (!) real value is ''
    'dlaqsy': None, # (!) real value is ''
    'dlaqtr': None, # (!) real value is ''
    'dlar1v': None, # (!) real value is ''
    'dlar2v': None, # (!) real value is ''
    'dlarf': None, # (!) real value is ''
    'dlarfb': None, # (!) real value is ''
    'dlarfg': None, # (!) real value is ''
    'dlarft': None, # (!) real value is ''
    'dlarfx': None, # (!) real value is ''
    'dlargv': None, # (!) real value is ''
    'dlarnv': None, # (!) real value is ''
    'dlarra': None, # (!) real value is ''
    'dlarrb': None, # (!) real value is ''
    'dlarrc': None, # (!) real value is ''
    'dlarrd': None, # (!) real value is ''
    'dlarre': None, # (!) real value is ''
    'dlarrf': None, # (!) real value is ''
    'dlarrj': None, # (!) real value is ''
    'dlarrk': None, # (!) real value is ''
    'dlarrr': None, # (!) real value is ''
    'dlarrv': None, # (!) real value is ''
    'dlartg': None, # (!) real value is ''
    'dlartv': None, # (!) real value is ''
    'dlaruv': None, # (!) real value is ''
    'dlarz': None, # (!) real value is ''
    'dlarzb': None, # (!) real value is ''
    'dlarzt': None, # (!) real value is ''
    'dlas2': None, # (!) real value is ''
    'dlascl': None, # (!) real value is ''
    'dlasd0': None, # (!) real value is ''
    'dlasd1': None, # (!) real value is ''
    'dlasd2': None, # (!) real value is ''
    'dlasd3': None, # (!) real value is ''
    'dlasd4': None, # (!) real value is ''
    'dlasd5': None, # (!) real value is ''
    'dlasd6': None, # (!) real value is ''
    'dlasd7': None, # (!) real value is ''
    'dlasd8': None, # (!) real value is ''
    'dlasda': None, # (!) real value is ''
    'dlasdq': None, # (!) real value is ''
    'dlasdt': None, # (!) real value is ''
    'dlaset': None, # (!) real value is ''
    'dlasq1': None, # (!) real value is ''
    'dlasq2': None, # (!) real value is ''
    'dlasq6': None, # (!) real value is ''
    'dlasr': None, # (!) real value is ''
    'dlasrt': None, # (!) real value is ''
    'dlassq': None, # (!) real value is ''
    'dlasv2': None, # (!) real value is ''
    'dlaswp': None, # (!) real value is ''
    'dlasy2': None, # (!) real value is ''
    'dlasyf': None, # (!) real value is ''
    'dlatbs': None, # (!) real value is ''
    'dlatdf': None, # (!) real value is ''
    'dlatps': None, # (!) real value is ''
    'dlatrd': None, # (!) real value is ''
    'dlatrs': None, # (!) real value is ''
    'dlatrz': None, # (!) real value is ''
    'dlauu2': None, # (!) real value is ''
    'dlauum': None, # (!) real value is ''
    'dopgtr': None, # (!) real value is ''
    'dopmtr': None, # (!) real value is ''
    'dorg2l': None, # (!) real value is ''
    'dorg2r': None, # (!) real value is ''
    'dorgbr': None, # (!) real value is ''
    'dorghr': None, # (!) real value is ''
    'dorgl2': None, # (!) real value is ''
    'dorglq': None, # (!) real value is ''
    'dorgql': None, # (!) real value is ''
    'dorgqr': None, # (!) real value is ''
    'dorgr2': None, # (!) real value is ''
    'dorgrq': None, # (!) real value is ''
    'dorgtr': None, # (!) real value is ''
    'dorm2l': None, # (!) real value is ''
    'dorm2r': None, # (!) real value is ''
    'dormbr': None, # (!) real value is ''
    'dormhr': None, # (!) real value is ''
    'dorml2': None, # (!) real value is ''
    'dormlq': None, # (!) real value is ''
    'dormql': None, # (!) real value is ''
    'dormqr': None, # (!) real value is ''
    'dormr2': None, # (!) real value is ''
    'dormr3': None, # (!) real value is ''
    'dormrq': None, # (!) real value is ''
    'dormrz': None, # (!) real value is ''
    'dormtr': None, # (!) real value is ''
    'dpbcon': None, # (!) real value is ''
    'dpbequ': None, # (!) real value is ''
    'dpbrfs': None, # (!) real value is ''
    'dpbstf': None, # (!) real value is ''
    'dpbsv': None, # (!) real value is ''
    'dpbsvx': None, # (!) real value is ''
    'dpbtf2': None, # (!) real value is ''
    'dpbtrf': None, # (!) real value is ''
    'dpbtrs': None, # (!) real value is ''
    'dpocon': None, # (!) real value is ''
    'dpoequ': None, # (!) real value is ''
    'dporfs': None, # (!) real value is ''
    'dposv': None, # (!) real value is ''
    'dposvx': None, # (!) real value is ''
    'dpotf2': None, # (!) real value is ''
    'dpotrf': None, # (!) real value is ''
    'dpotri': None, # (!) real value is ''
    'dpotrs': None, # (!) real value is ''
    'dppcon': None, # (!) real value is ''
    'dppequ': None, # (!) real value is ''
    'dpprfs': None, # (!) real value is ''
    'dppsv': None, # (!) real value is ''
    'dppsvx': None, # (!) real value is ''
    'dpptrf': None, # (!) real value is ''
    'dpptri': None, # (!) real value is ''
    'dpptrs': None, # (!) real value is ''
    'dptcon': None, # (!) real value is ''
    'dpteqr': None, # (!) real value is ''
    'dptrfs': None, # (!) real value is ''
    'dptsv': None, # (!) real value is ''
    'dptsvx': None, # (!) real value is ''
    'dpttrf': None, # (!) real value is ''
    'dpttrs': None, # (!) real value is ''
    'dptts2': None, # (!) real value is ''
    'drscl': None, # (!) real value is ''
    'dsbev': None, # (!) real value is ''
    'dsbevd': None, # (!) real value is ''
    'dsbevx': None, # (!) real value is ''
    'dsbgst': None, # (!) real value is ''
    'dsbgv': None, # (!) real value is ''
    'dsbgvd': None, # (!) real value is ''
    'dsbgvx': None, # (!) real value is ''
    'dsbtrd': None, # (!) real value is ''
    'dsgesv': None, # (!) real value is ''
    'dspcon': None, # (!) real value is ''
    'dspev': None, # (!) real value is ''
    'dspevd': None, # (!) real value is ''
    'dspevx': None, # (!) real value is ''
    'dspgst': None, # (!) real value is ''
    'dspgv': None, # (!) real value is ''
    'dspgvd': None, # (!) real value is ''
    'dspgvx': None, # (!) real value is ''
    'dsprfs': None, # (!) real value is ''
    'dspsv': None, # (!) real value is ''
    'dspsvx': None, # (!) real value is ''
    'dsptrd': None, # (!) real value is ''
    'dsptrf': None, # (!) real value is ''
    'dsptri': None, # (!) real value is ''
    'dsptrs': None, # (!) real value is ''
    'dstebz': None, # (!) real value is ''
    'dstedc': None, # (!) real value is ''
    'dstegr': None, # (!) real value is ''
    'dstein': None, # (!) real value is ''
    'dstemr': None, # (!) real value is ''
    'dsteqr': None, # (!) real value is ''
    'dsterf': None, # (!) real value is ''
    'dstev': None, # (!) real value is ''
    'dstevd': None, # (!) real value is ''
    'dstevr': None, # (!) real value is ''
    'dstevx': None, # (!) real value is ''
    'dsycon': None, # (!) real value is ''
    'dsyev': None, # (!) real value is ''
    'dsyevd': None, # (!) real value is ''
    'dsyevr': None, # (!) real value is ''
    'dsyevx': None, # (!) real value is ''
    'dsygs2': None, # (!) real value is ''
    'dsygst': None, # (!) real value is ''
    'dsygv': None, # (!) real value is ''
    'dsygvd': None, # (!) real value is ''
    'dsygvx': None, # (!) real value is ''
    'dsyrfs': None, # (!) real value is ''
    'dsysv': None, # (!) real value is ''
    'dsysvx': None, # (!) real value is ''
    'dsytd2': None, # (!) real value is ''
    'dsytf2': None, # (!) real value is ''
    'dsytrd': None, # (!) real value is ''
    'dsytrf': None, # (!) real value is ''
    'dsytri': None, # (!) real value is ''
    'dsytrs': None, # (!) real value is ''
    'dtbcon': None, # (!) real value is ''
    'dtbrfs': None, # (!) real value is ''
    'dtbtrs': None, # (!) real value is ''
    'dtgevc': None, # (!) real value is ''
    'dtgex2': None, # (!) real value is ''
    'dtgexc': None, # (!) real value is ''
    'dtgsen': None, # (!) real value is ''
    'dtgsja': None, # (!) real value is ''
    'dtgsna': None, # (!) real value is ''
    'dtgsy2': None, # (!) real value is ''
    'dtgsyl': None, # (!) real value is ''
    'dtpcon': None, # (!) real value is ''
    'dtprfs': None, # (!) real value is ''
    'dtptri': None, # (!) real value is ''
    'dtptrs': None, # (!) real value is ''
    'dtrcon': None, # (!) real value is ''
    'dtrevc': None, # (!) real value is ''
    'dtrexc': None, # (!) real value is ''
    'dtrrfs': None, # (!) real value is ''
    'dtrsen': None, # (!) real value is ''
    'dtrsna': None, # (!) real value is ''
    'dtrsyl': None, # (!) real value is ''
    'dtrti2': None, # (!) real value is ''
    'dtrtri': None, # (!) real value is ''
    'dtrtrs': None, # (!) real value is ''
    'dtzrzf': None, # (!) real value is ''
    'dzsum1': None, # (!) real value is ''
    'icmax1': None, # (!) real value is ''
    'ieeeck': None, # (!) real value is ''
    'ilaver': None, # (!) real value is ''
    'izmax1': None, # (!) real value is ''
    'sbdsdc': None, # (!) real value is ''
    'sbdsqr': None, # (!) real value is ''
    'scsum1': None, # (!) real value is ''
    'sdisna': None, # (!) real value is ''
    'sgbbrd': None, # (!) real value is ''
    'sgbcon': None, # (!) real value is ''
    'sgbequ': None, # (!) real value is ''
    'sgbrfs': None, # (!) real value is ''
    'sgbsv': None, # (!) real value is ''
    'sgbsvx': None, # (!) real value is ''
    'sgbtf2': None, # (!) real value is ''
    'sgbtrf': None, # (!) real value is ''
    'sgbtrs': None, # (!) real value is ''
    'sgebak': None, # (!) real value is ''
    'sgebal': None, # (!) real value is ''
    'sgebd2': None, # (!) real value is ''
    'sgebrd': None, # (!) real value is ''
    'sgecon': None, # (!) real value is ''
    'sgeequ': None, # (!) real value is ''
    'sgees': None, # (!) real value is ''
    'sgeesx': None, # (!) real value is ''
    'sgeev': None, # (!) real value is ''
    'sgeevx': None, # (!) real value is ''
    'sgehd2': None, # (!) real value is ''
    'sgehrd': None, # (!) real value is ''
    'sgelq2': None, # (!) real value is ''
    'sgelqf': None, # (!) real value is ''
    'sgels': None, # (!) real value is ''
    'sgelsd': None, # (!) real value is ''
    'sgelss': None, # (!) real value is ''
    'sgelsy': None, # (!) real value is ''
    'sgeql2': None, # (!) real value is ''
    'sgeqlf': None, # (!) real value is ''
    'sgeqp3': None, # (!) real value is ''
    'sgeqr2': None, # (!) real value is ''
    'sgeqrf': None, # (!) real value is ''
    'sgerfs': None, # (!) real value is ''
    'sgerq2': None, # (!) real value is ''
    'sgerqf': None, # (!) real value is ''
    'sgesc2': None, # (!) real value is ''
    'sgesdd': None, # (!) real value is ''
    'sgesv': None, # (!) real value is ''
    'sgesvd': None, # (!) real value is ''
    'sgesvx': None, # (!) real value is ''
    'sgetc2': None, # (!) real value is ''
    'sgetf2': None, # (!) real value is ''
    'sgetrf': None, # (!) real value is ''
    'sgetri': None, # (!) real value is ''
    'sgetrs': None, # (!) real value is ''
    'sggbak': None, # (!) real value is ''
    'sggbal': None, # (!) real value is ''
    'sgges': None, # (!) real value is ''
    'sggesx': None, # (!) real value is ''
    'sggev': None, # (!) real value is ''
    'sggevx': None, # (!) real value is ''
    'sggglm': None, # (!) real value is ''
    'sgghrd': None, # (!) real value is ''
    'sgglse': None, # (!) real value is ''
    'sggqrf': None, # (!) real value is ''
    'sggrqf': None, # (!) real value is ''
    'sgtcon': None, # (!) real value is ''
    'sgtrfs': None, # (!) real value is ''
    'sgtsv': None, # (!) real value is ''
    'sgtsvx': None, # (!) real value is ''
    'sgttrf': None, # (!) real value is ''
    'sgttrs': None, # (!) real value is ''
    'sgtts2': None, # (!) real value is ''
    'shgeqz': None, # (!) real value is ''
    'shsein': None, # (!) real value is ''
    'shseqr': None, # (!) real value is ''
    'slabad': None, # (!) real value is ''
    'slabrd': None, # (!) real value is ''
    'slacn2': None, # (!) real value is ''
    'slacon': None, # (!) real value is ''
    'slacpy': None, # (!) real value is ''
    'sladiv': None, # (!) real value is ''
    'slae2': None, # (!) real value is ''
    'slaebz': None, # (!) real value is ''
    'slaed0': None, # (!) real value is ''
    'slaed1': None, # (!) real value is ''
    'slaed2': None, # (!) real value is ''
    'slaed3': None, # (!) real value is ''
    'slaed4': None, # (!) real value is ''
    'slaed5': None, # (!) real value is ''
    'slaed6': None, # (!) real value is ''
    'slaed7': None, # (!) real value is ''
    'slaed8': None, # (!) real value is ''
    'slaed9': None, # (!) real value is ''
    'slaeda': None, # (!) real value is ''
    'slaein': None, # (!) real value is ''
    'slaev2': None, # (!) real value is ''
    'slaexc': None, # (!) real value is ''
    'slag2': None, # (!) real value is ''
    'slag2d': None, # (!) real value is ''
    'slags2': None, # (!) real value is ''
    'slagtf': None, # (!) real value is ''
    'slagtm': None, # (!) real value is ''
    'slagts': None, # (!) real value is ''
    'slagv2': None, # (!) real value is ''
    'slahqr': None, # (!) real value is ''
    'slahr2': None, # (!) real value is ''
    'slaic1': None, # (!) real value is ''
    'slaln2': None, # (!) real value is ''
    'slals0': None, # (!) real value is ''
    'slalsa': None, # (!) real value is ''
    'slalsd': None, # (!) real value is ''
    'slamch': None, # (!) real value is ''
    'slamrg': None, # (!) real value is ''
    'slangb': None, # (!) real value is ''
    'slange': None, # (!) real value is ''
    'slangt': None, # (!) real value is ''
    'slanhs': None, # (!) real value is ''
    'slansb': None, # (!) real value is ''
    'slansp': None, # (!) real value is ''
    'slanst': None, # (!) real value is ''
    'slansy': None, # (!) real value is ''
    'slantb': None, # (!) real value is ''
    'slantp': None, # (!) real value is ''
    'slantr': None, # (!) real value is ''
    'slanv2': None, # (!) real value is ''
    'slapll': None, # (!) real value is ''
    'slapmt': None, # (!) real value is ''
    'slapy2': None, # (!) real value is ''
    'slapy3': None, # (!) real value is ''
    'slaqgb': None, # (!) real value is ''
    'slaqge': None, # (!) real value is ''
    'slaqp2': None, # (!) real value is ''
    'slaqps': None, # (!) real value is ''
    'slaqr0': None, # (!) real value is ''
    'slaqr1': None, # (!) real value is ''
    'slaqr2': None, # (!) real value is ''
    'slaqr3': None, # (!) real value is ''
    'slaqr4': None, # (!) real value is ''
    'slaqr5': None, # (!) real value is ''
    'slaqsb': None, # (!) real value is ''
    'slaqsp': None, # (!) real value is ''
    'slaqsy': None, # (!) real value is ''
    'slaqtr': None, # (!) real value is ''
    'slar1v': None, # (!) real value is ''
    'slar2v': None, # (!) real value is ''
    'slarf': None, # (!) real value is ''
    'slarfb': None, # (!) real value is ''
    'slarfg': None, # (!) real value is ''
    'slarft': None, # (!) real value is ''
    'slarfx': None, # (!) real value is ''
    'slargv': None, # (!) real value is ''
    'slarnv': None, # (!) real value is ''
    'slarra': None, # (!) real value is ''
    'slarrb': None, # (!) real value is ''
    'slarrc': None, # (!) real value is ''
    'slarrd': None, # (!) real value is ''
    'slarre': None, # (!) real value is ''
    'slarrf': None, # (!) real value is ''
    'slarrj': None, # (!) real value is ''
    'slarrk': None, # (!) real value is ''
    'slarrr': None, # (!) real value is ''
    'slarrv': None, # (!) real value is ''
    'slartg': None, # (!) real value is ''
    'slartv': None, # (!) real value is ''
    'slaruv': None, # (!) real value is ''
    'slarz': None, # (!) real value is ''
    'slarzb': None, # (!) real value is ''
    'slarzt': None, # (!) real value is ''
    'slas2': None, # (!) real value is ''
    'slascl': None, # (!) real value is ''
    'slasd0': None, # (!) real value is ''
    'slasd1': None, # (!) real value is ''
    'slasd2': None, # (!) real value is ''
    'slasd3': None, # (!) real value is ''
    'slasd4': None, # (!) real value is ''
    'slasd5': None, # (!) real value is ''
    'slasd6': None, # (!) real value is ''
    'slasd7': None, # (!) real value is ''
    'slasd8': None, # (!) real value is ''
    'slasda': None, # (!) real value is ''
    'slasdq': None, # (!) real value is ''
    'slasdt': None, # (!) real value is ''
    'slaset': None, # (!) real value is ''
    'slasq1': None, # (!) real value is ''
    'slasq2': None, # (!) real value is ''
    'slasq6': None, # (!) real value is ''
    'slasr': None, # (!) real value is ''
    'slasrt': None, # (!) real value is ''
    'slassq': None, # (!) real value is ''
    'slasv2': None, # (!) real value is ''
    'slaswp': None, # (!) real value is ''
    'slasy2': None, # (!) real value is ''
    'slasyf': None, # (!) real value is ''
    'slatbs': None, # (!) real value is ''
    'slatdf': None, # (!) real value is ''
    'slatps': None, # (!) real value is ''
    'slatrd': None, # (!) real value is ''
    'slatrs': None, # (!) real value is ''
    'slatrz': None, # (!) real value is ''
    'slauu2': None, # (!) real value is ''
    'slauum': None, # (!) real value is ''
    'sopgtr': None, # (!) real value is ''
    'sopmtr': None, # (!) real value is ''
    'sorg2l': None, # (!) real value is ''
    'sorg2r': None, # (!) real value is ''
    'sorgbr': None, # (!) real value is ''
    'sorghr': None, # (!) real value is ''
    'sorgl2': None, # (!) real value is ''
    'sorglq': None, # (!) real value is ''
    'sorgql': None, # (!) real value is ''
    'sorgqr': None, # (!) real value is ''
    'sorgr2': None, # (!) real value is ''
    'sorgrq': None, # (!) real value is ''
    'sorgtr': None, # (!) real value is ''
    'sorm2l': None, # (!) real value is ''
    'sorm2r': None, # (!) real value is ''
    'sormbr': None, # (!) real value is ''
    'sormhr': None, # (!) real value is ''
    'sorml2': None, # (!) real value is ''
    'sormlq': None, # (!) real value is ''
    'sormql': None, # (!) real value is ''
    'sormqr': None, # (!) real value is ''
    'sormr2': None, # (!) real value is ''
    'sormr3': None, # (!) real value is ''
    'sormrq': None, # (!) real value is ''
    'sormrz': None, # (!) real value is ''
    'sormtr': None, # (!) real value is ''
    'spbcon': None, # (!) real value is ''
    'spbequ': None, # (!) real value is ''
    'spbrfs': None, # (!) real value is ''
    'spbstf': None, # (!) real value is ''
    'spbsv': None, # (!) real value is ''
    'spbsvx': None, # (!) real value is ''
    'spbtf2': None, # (!) real value is ''
    'spbtrf': None, # (!) real value is ''
    'spbtrs': None, # (!) real value is ''
    'spocon': None, # (!) real value is ''
    'spoequ': None, # (!) real value is ''
    'sporfs': None, # (!) real value is ''
    'sposv': None, # (!) real value is ''
    'sposvx': None, # (!) real value is ''
    'spotf2': None, # (!) real value is ''
    'spotrf': None, # (!) real value is ''
    'spotri': None, # (!) real value is ''
    'spotrs': None, # (!) real value is ''
    'sppcon': None, # (!) real value is ''
    'sppequ': None, # (!) real value is ''
    'spprfs': None, # (!) real value is ''
    'sppsv': None, # (!) real value is ''
    'sppsvx': None, # (!) real value is ''
    'spptrf': None, # (!) real value is ''
    'spptri': None, # (!) real value is ''
    'spptrs': None, # (!) real value is ''
    'sptcon': None, # (!) real value is ''
    'spteqr': None, # (!) real value is ''
    'sptrfs': None, # (!) real value is ''
    'sptsv': None, # (!) real value is ''
    'sptsvx': None, # (!) real value is ''
    'spttrf': None, # (!) real value is ''
    'spttrs': None, # (!) real value is ''
    'sptts2': None, # (!) real value is ''
    'srscl': None, # (!) real value is ''
    'ssbev': None, # (!) real value is ''
    'ssbevd': None, # (!) real value is ''
    'ssbevx': None, # (!) real value is ''
    'ssbgst': None, # (!) real value is ''
    'ssbgv': None, # (!) real value is ''
    'ssbgvd': None, # (!) real value is ''
    'ssbgvx': None, # (!) real value is ''
    'ssbtrd': None, # (!) real value is ''
    'sspcon': None, # (!) real value is ''
    'sspev': None, # (!) real value is ''
    'sspevd': None, # (!) real value is ''
    'sspevx': None, # (!) real value is ''
    'sspgst': None, # (!) real value is ''
    'sspgv': None, # (!) real value is ''
    'sspgvd': None, # (!) real value is ''
    'sspgvx': None, # (!) real value is ''
    'ssprfs': None, # (!) real value is ''
    'sspsv': None, # (!) real value is ''
    'sspsvx': None, # (!) real value is ''
    'ssptrd': None, # (!) real value is ''
    'ssptrf': None, # (!) real value is ''
    'ssptri': None, # (!) real value is ''
    'ssptrs': None, # (!) real value is ''
    'sstebz': None, # (!) real value is ''
    'sstedc': None, # (!) real value is ''
    'sstegr': None, # (!) real value is ''
    'sstein': None, # (!) real value is ''
    'sstemr': None, # (!) real value is ''
    'ssteqr': None, # (!) real value is ''
    'ssterf': None, # (!) real value is ''
    'sstev': None, # (!) real value is ''
    'sstevd': None, # (!) real value is ''
    'sstevr': None, # (!) real value is ''
    'sstevx': None, # (!) real value is ''
    'ssycon': None, # (!) real value is ''
    'ssyev': None, # (!) real value is ''
    'ssyevd': None, # (!) real value is ''
    'ssyevr': None, # (!) real value is ''
    'ssyevx': None, # (!) real value is ''
    'ssygs2': None, # (!) real value is ''
    'ssygst': None, # (!) real value is ''
    'ssygv': None, # (!) real value is ''
    'ssygvd': None, # (!) real value is ''
    'ssygvx': None, # (!) real value is ''
    'ssyrfs': None, # (!) real value is ''
    'ssysv': None, # (!) real value is ''
    'ssysvx': None, # (!) real value is ''
    'ssytd2': None, # (!) real value is ''
    'ssytf2': None, # (!) real value is ''
    'ssytrd': None, # (!) real value is ''
    'ssytrf': None, # (!) real value is ''
    'ssytri': None, # (!) real value is ''
    'ssytrs': None, # (!) real value is ''
    'stbcon': None, # (!) real value is ''
    'stbrfs': None, # (!) real value is ''
    'stbtrs': None, # (!) real value is ''
    'stgevc': None, # (!) real value is ''
    'stgex2': None, # (!) real value is ''
    'stgexc': None, # (!) real value is ''
    'stgsen': None, # (!) real value is ''
    'stgsja': None, # (!) real value is ''
    'stgsna': None, # (!) real value is ''
    'stgsy2': None, # (!) real value is ''
    'stgsyl': None, # (!) real value is ''
    'stpcon': None, # (!) real value is ''
    'stprfs': None, # (!) real value is ''
    'stptri': None, # (!) real value is ''
    'stptrs': None, # (!) real value is ''
    'strcon': None, # (!) real value is ''
    'strevc': None, # (!) real value is ''
    'strexc': None, # (!) real value is ''
    'strrfs': None, # (!) real value is ''
    'strsen': None, # (!) real value is ''
    'strsna': None, # (!) real value is ''
    'strsyl': None, # (!) real value is ''
    'strti2': None, # (!) real value is ''
    'strtri': None, # (!) real value is ''
    'strtrs': None, # (!) real value is ''
    'stzrzf': None, # (!) real value is ''
    'zbdsqr': None, # (!) real value is ''
    'zdrscl': None, # (!) real value is ''
    'zgbbrd': None, # (!) real value is ''
    'zgbcon': None, # (!) real value is ''
    'zgbequ': None, # (!) real value is ''
    'zgbrfs': None, # (!) real value is ''
    'zgbsv': None, # (!) real value is ''
    'zgbsvx': None, # (!) real value is ''
    'zgbtf2': None, # (!) real value is ''
    'zgbtrf': None, # (!) real value is ''
    'zgbtrs': None, # (!) real value is ''
    'zgebak': None, # (!) real value is ''
    'zgebal': None, # (!) real value is ''
    'zgebd2': None, # (!) real value is ''
    'zgebrd': None, # (!) real value is ''
    'zgecon': None, # (!) real value is ''
    'zgeequ': None, # (!) real value is ''
    'zgees': None, # (!) real value is ''
    'zgeesx': None, # (!) real value is ''
    'zgeev': None, # (!) real value is ''
    'zgeevx': None, # (!) real value is ''
    'zgehd2': None, # (!) real value is ''
    'zgehrd': None, # (!) real value is ''
    'zgelq2': None, # (!) real value is ''
    'zgelqf': None, # (!) real value is ''
    'zgels': None, # (!) real value is ''
    'zgelsd': None, # (!) real value is ''
    'zgelss': None, # (!) real value is ''
    'zgelsy': None, # (!) real value is ''
    'zgeql2': None, # (!) real value is ''
    'zgeqlf': None, # (!) real value is ''
    'zgeqp3': None, # (!) real value is ''
    'zgeqr2': None, # (!) real value is ''
    'zgeqrf': None, # (!) real value is ''
    'zgerfs': None, # (!) real value is ''
    'zgerq2': None, # (!) real value is ''
    'zgerqf': None, # (!) real value is ''
    'zgesc2': None, # (!) real value is ''
    'zgesdd': None, # (!) real value is ''
    'zgesv': None, # (!) real value is ''
    'zgesvd': None, # (!) real value is ''
    'zgesvx': None, # (!) real value is ''
    'zgetc2': None, # (!) real value is ''
    'zgetf2': None, # (!) real value is ''
    'zgetrf': None, # (!) real value is ''
    'zgetri': None, # (!) real value is ''
    'zgetrs': None, # (!) real value is ''
    'zggbak': None, # (!) real value is ''
    'zggbal': None, # (!) real value is ''
    'zgges': None, # (!) real value is ''
    'zggesx': None, # (!) real value is ''
    'zggev': None, # (!) real value is ''
    'zggevx': None, # (!) real value is ''
    'zggglm': None, # (!) real value is ''
    'zgghrd': None, # (!) real value is ''
    'zgglse': None, # (!) real value is ''
    'zggqrf': None, # (!) real value is ''
    'zggrqf': None, # (!) real value is ''
    'zgtcon': None, # (!) real value is ''
    'zgtrfs': None, # (!) real value is ''
    'zgtsv': None, # (!) real value is ''
    'zgtsvx': None, # (!) real value is ''
    'zgttrf': None, # (!) real value is ''
    'zgttrs': None, # (!) real value is ''
    'zgtts2': None, # (!) real value is ''
    'zhbev': None, # (!) real value is ''
    'zhbevd': None, # (!) real value is ''
    'zhbevx': None, # (!) real value is ''
    'zhbgst': None, # (!) real value is ''
    'zhbgv': None, # (!) real value is ''
    'zhbgvd': None, # (!) real value is ''
    'zhbgvx': None, # (!) real value is ''
    'zhbtrd': None, # (!) real value is ''
    'zhecon': None, # (!) real value is ''
    'zheev': None, # (!) real value is ''
    'zheevd': None, # (!) real value is ''
    'zheevr': None, # (!) real value is ''
    'zheevx': None, # (!) real value is ''
    'zhegs2': None, # (!) real value is ''
    'zhegst': None, # (!) real value is ''
    'zhegv': None, # (!) real value is ''
    'zhegvd': None, # (!) real value is ''
    'zhegvx': None, # (!) real value is ''
    'zherfs': None, # (!) real value is ''
    'zhesv': None, # (!) real value is ''
    'zhesvx': None, # (!) real value is ''
    'zhetd2': None, # (!) real value is ''
    'zhetf2': None, # (!) real value is ''
    'zhetrd': None, # (!) real value is ''
    'zhetrf': None, # (!) real value is ''
    'zhetri': None, # (!) real value is ''
    'zhetrs': None, # (!) real value is ''
    'zhgeqz': None, # (!) real value is ''
    'zhpcon': None, # (!) real value is ''
    'zhpev': None, # (!) real value is ''
    'zhpevd': None, # (!) real value is ''
    'zhpevx': None, # (!) real value is ''
    'zhpgst': None, # (!) real value is ''
    'zhpgv': None, # (!) real value is ''
    'zhpgvd': None, # (!) real value is ''
    'zhpgvx': None, # (!) real value is ''
    'zhprfs': None, # (!) real value is ''
    'zhpsv': None, # (!) real value is ''
    'zhpsvx': None, # (!) real value is ''
    'zhptrd': None, # (!) real value is ''
    'zhptrf': None, # (!) real value is ''
    'zhptri': None, # (!) real value is ''
    'zhptrs': None, # (!) real value is ''
    'zhsein': None, # (!) real value is ''
    'zhseqr': None, # (!) real value is ''
    'zlabrd': None, # (!) real value is ''
    'zlacgv': None, # (!) real value is ''
    'zlacn2': None, # (!) real value is ''
    'zlacon': None, # (!) real value is ''
    'zlacp2': None, # (!) real value is ''
    'zlacpy': None, # (!) real value is ''
    'zlacrm': None, # (!) real value is ''
    'zlacrt': None, # (!) real value is ''
    'zladiv': None, # (!) real value is ''
    'zlaed0': None, # (!) real value is ''
    'zlaed7': None, # (!) real value is ''
    'zlaed8': None, # (!) real value is ''
    'zlaein': None, # (!) real value is ''
    'zlaesy': None, # (!) real value is ''
    'zlaev2': None, # (!) real value is ''
    'zlag2c': None, # (!) real value is ''
    'zlags2': None, # (!) real value is ''
    'zlagtm': None, # (!) real value is ''
    'zlahef': None, # (!) real value is ''
    'zlahqr': None, # (!) real value is ''
    'zlahr2': None, # (!) real value is ''
    'zlaic1': None, # (!) real value is ''
    'zlals0': None, # (!) real value is ''
    'zlalsa': None, # (!) real value is ''
    'zlalsd': None, # (!) real value is ''
    'zlangb': None, # (!) real value is ''
    'zlange': None, # (!) real value is ''
    'zlangt': None, # (!) real value is ''
    'zlanhb': None, # (!) real value is ''
    'zlanhe': None, # (!) real value is ''
    'zlanhp': None, # (!) real value is ''
    'zlanhs': None, # (!) real value is ''
    'zlanht': None, # (!) real value is ''
    'zlansb': None, # (!) real value is ''
    'zlansp': None, # (!) real value is ''
    'zlansy': None, # (!) real value is ''
    'zlantb': None, # (!) real value is ''
    'zlantp': None, # (!) real value is ''
    'zlantr': None, # (!) real value is ''
    'zlapll': None, # (!) real value is ''
    'zlapmt': None, # (!) real value is ''
    'zlaqgb': None, # (!) real value is ''
    'zlaqge': None, # (!) real value is ''
    'zlaqhb': None, # (!) real value is ''
    'zlaqhe': None, # (!) real value is ''
    'zlaqhp': None, # (!) real value is ''
    'zlaqp2': None, # (!) real value is ''
    'zlaqps': None, # (!) real value is ''
    'zlaqr0': None, # (!) real value is ''
    'zlaqr1': None, # (!) real value is ''
    'zlaqr2': None, # (!) real value is ''
    'zlaqr3': None, # (!) real value is ''
    'zlaqr4': None, # (!) real value is ''
    'zlaqr5': None, # (!) real value is ''
    'zlaqsb': None, # (!) real value is ''
    'zlaqsp': None, # (!) real value is ''
    'zlaqsy': None, # (!) real value is ''
    'zlar1v': None, # (!) real value is ''
    'zlar2v': None, # (!) real value is ''
    'zlarcm': None, # (!) real value is ''
    'zlarf': None, # (!) real value is ''
    'zlarfb': None, # (!) real value is ''
    'zlarfg': None, # (!) real value is ''
    'zlarft': None, # (!) real value is ''
    'zlarfx': None, # (!) real value is ''
    'zlargv': None, # (!) real value is ''
    'zlarnv': None, # (!) real value is ''
    'zlarrv': None, # (!) real value is ''
    'zlartg': None, # (!) real value is ''
    'zlartv': None, # (!) real value is ''
    'zlarz': None, # (!) real value is ''
    'zlarzb': None, # (!) real value is ''
    'zlarzt': None, # (!) real value is ''
    'zlascl': None, # (!) real value is ''
    'zlaset': None, # (!) real value is ''
    'zlasr': None, # (!) real value is ''
    'zlassq': None, # (!) real value is ''
    'zlaswp': None, # (!) real value is ''
    'zlasyf': None, # (!) real value is ''
    'zlatbs': None, # (!) real value is ''
    'zlatdf': None, # (!) real value is ''
    'zlatps': None, # (!) real value is ''
    'zlatrd': None, # (!) real value is ''
    'zlatrs': None, # (!) real value is ''
    'zlatrz': None, # (!) real value is ''
    'zlauu2': None, # (!) real value is ''
    'zlauum': None, # (!) real value is ''
    'zpbcon': None, # (!) real value is ''
    'zpbequ': None, # (!) real value is ''
    'zpbrfs': None, # (!) real value is ''
    'zpbstf': None, # (!) real value is ''
    'zpbsv': None, # (!) real value is ''
    'zpbsvx': None, # (!) real value is ''
    'zpbtf2': None, # (!) real value is ''
    'zpbtrf': None, # (!) real value is ''
    'zpbtrs': None, # (!) real value is ''
    'zpocon': None, # (!) real value is ''
    'zpoequ': None, # (!) real value is ''
    'zporfs': None, # (!) real value is ''
    'zposv': None, # (!) real value is ''
    'zposvx': None, # (!) real value is ''
    'zpotf2': None, # (!) real value is ''
    'zpotrf': None, # (!) real value is ''
    'zpotri': None, # (!) real value is ''
    'zpotrs': None, # (!) real value is ''
    'zppcon': None, # (!) real value is ''
    'zppequ': None, # (!) real value is ''
    'zpprfs': None, # (!) real value is ''
    'zppsv': None, # (!) real value is ''
    'zppsvx': None, # (!) real value is ''
    'zpptrf': None, # (!) real value is ''
    'zpptri': None, # (!) real value is ''
    'zpptrs': None, # (!) real value is ''
    'zptcon': None, # (!) real value is ''
    'zpteqr': None, # (!) real value is ''
    'zptrfs': None, # (!) real value is ''
    'zptsv': None, # (!) real value is ''
    'zptsvx': None, # (!) real value is ''
    'zpttrf': None, # (!) real value is ''
    'zpttrs': None, # (!) real value is ''
    'zptts2': None, # (!) real value is ''
    'zrot': None, # (!) real value is ''
    'zspcon': None, # (!) real value is ''
    'zspmv': None, # (!) real value is ''
    'zspr': None, # (!) real value is ''
    'zsprfs': None, # (!) real value is ''
    'zspsv': None, # (!) real value is ''
    'zspsvx': None, # (!) real value is ''
    'zsptrf': None, # (!) real value is ''
    'zsptri': None, # (!) real value is ''
    'zsptrs': None, # (!) real value is ''
    'zstedc': None, # (!) real value is ''
    'zstegr': None, # (!) real value is ''
    'zstein': None, # (!) real value is ''
    'zstemr': None, # (!) real value is ''
    'zsteqr': None, # (!) real value is ''
    'zsycon': None, # (!) real value is ''
    'zsymv': None, # (!) real value is ''
    'zsyr': None, # (!) real value is ''
    'zsyrfs': None, # (!) real value is ''
    'zsysv': None, # (!) real value is ''
    'zsysvx': None, # (!) real value is ''
    'zsytf2': None, # (!) real value is ''
    'zsytrf': None, # (!) real value is ''
    'zsytri': None, # (!) real value is ''
    'zsytrs': None, # (!) real value is ''
    'ztbcon': None, # (!) real value is ''
    'ztbrfs': None, # (!) real value is ''
    'ztbtrs': None, # (!) real value is ''
    'ztgevc': None, # (!) real value is ''
    'ztgex2': None, # (!) real value is ''
    'ztgexc': None, # (!) real value is ''
    'ztgsen': None, # (!) real value is ''
    'ztgsja': None, # (!) real value is ''
    'ztgsna': None, # (!) real value is ''
    'ztgsy2': None, # (!) real value is ''
    'ztgsyl': None, # (!) real value is ''
    'ztpcon': None, # (!) real value is ''
    'ztprfs': None, # (!) real value is ''
    'ztptri': None, # (!) real value is ''
    'ztptrs': None, # (!) real value is ''
    'ztrcon': None, # (!) real value is ''
    'ztrevc': None, # (!) real value is ''
    'ztrexc': None, # (!) real value is ''
    'ztrrfs': None, # (!) real value is ''
    'ztrsen': None, # (!) real value is ''
    'ztrsna': None, # (!) real value is ''
    'ztrsyl': None, # (!) real value is ''
    'ztrti2': None, # (!) real value is ''
    'ztrtri': None, # (!) real value is ''
    'ztrtrs': None, # (!) real value is ''
    'ztzrzf': None, # (!) real value is ''
    'zung2l': None, # (!) real value is ''
    'zung2r': None, # (!) real value is ''
    'zungbr': None, # (!) real value is ''
    'zunghr': None, # (!) real value is ''
    'zungl2': None, # (!) real value is ''
    'zunglq': None, # (!) real value is ''
    'zungql': None, # (!) real value is ''
    'zungqr': None, # (!) real value is ''
    'zungr2': None, # (!) real value is ''
    'zungrq': None, # (!) real value is ''
    'zungtr': None, # (!) real value is ''
    'zunm2l': None, # (!) real value is ''
    'zunm2r': None, # (!) real value is ''
    'zunmbr': None, # (!) real value is ''
    'zunmhr': None, # (!) real value is ''
    'zunml2': None, # (!) real value is ''
    'zunmlq': None, # (!) real value is ''
    'zunmql': None, # (!) real value is ''
    'zunmqr': None, # (!) real value is ''
    'zunmr2': None, # (!) real value is ''
    'zunmr3': None, # (!) real value is ''
    'zunmrq': None, # (!) real value is ''
    'zunmrz': None, # (!) real value is ''
    'zunmtr': None, # (!) real value is ''
    'zupgtr': None, # (!) real value is ''
    'zupmtr': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

