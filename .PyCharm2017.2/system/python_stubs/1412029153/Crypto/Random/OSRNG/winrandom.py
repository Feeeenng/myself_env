# encoding: utf-8
# module Crypto.Random.OSRNG.winrandom
# from D:\ProgramData\Anaconda3\lib\site-packages\Crypto\Random\OSRNG\winrandom.cp36-win_amd64.pyd
# by generator 1.145
# no doc
# no imports

# Variables with simple values

INTEL_DEF_PROV = 'Intel Hardware Cryptographic Service Provider'

MS_DEF_DSS_DH_PROV = 'Microsoft Base DSS and Diffie-Hellman Cryptographic Provider'

MS_DEF_DSS_PROV = 'Microsoft Base DSS Cryptographic Provider'

MS_DEF_PROV = 'Microsoft Base Cryptographic Provider v1.0'

MS_DEF_RSA_SCHANNEL_PROV = 'Microsoft RSA SChannel Cryptographic Provider'

MS_DEF_RSA_SIG_PROV = 'Microsoft RSA Signature Cryptographic Provider'

MS_ENHANCED_PROV = 'Microsoft Enhanced Cryptographic Provider v1.0'

PROV_DSS = 3

PROV_DSS_DH = 13

PROV_EC_ECDSA_FULL = 16
PROV_EC_ECDSA_SIG = 14

PROV_EC_ECNRA_FULL = 17
PROV_EC_ECNRA_SIG = 15

PROV_FORTEZZA = 4

PROV_INTEL_SEC = 22

PROV_MS_EXCHANGE = 5

PROV_RSA_FULL = 1
PROV_RSA_SCHANNEL = 12
PROV_RSA_SIG = 2

PROV_SPYRUS_LYNKS = 20

PROV_SSL = 6

# functions

def new(provider=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    new([provider], [provtype]): Returns an object handle to Windows
    CryptoAPI that can be used to access a cryptographically strong
    pseudo-random generator that uses OS-gathered entropy.
    Provider is a string that specifies the Cryptographic Service Provider
    to use, default is the default OS CSP.
    provtype is an integer specifying the provider type to use, default
    is 1 (PROV_RSA_FULL)
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

