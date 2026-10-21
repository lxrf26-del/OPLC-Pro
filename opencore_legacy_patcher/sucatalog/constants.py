"""
constants.py: Enumerations for sucatalog-py
"""

from enum import StrEnum


class SeedType(StrEnum):
    """
    Enum for catalog types

    Variants:
        DeveloperSeed:  Developer Beta (Part of the Apple Developer Program)
        PublicSeed:     Public Beta
        CustomerSeed:   AppleSeed Program (Generally mirrors DeveloperSeed)
        PublicRelease:  Public Release
    """
    DeveloperSeed: str = "seed"
    PublicSeed:    str = "beta"
    CustomerSeed:  str = "customerseed"
    PublicRelease: str = ""


class CatalogVersion(StrEnum):
    """
    Enum for macOS versions

    GOLDEN_GATE     str = "27"
    TAHOE:          str = "26"
    SEQUOIA:        str = "15"
    SONOMA:         str = "14"
    VENTURA:        str = "13"
    MONTEREY:       str = "12"
   

class CatalogExtension(StrEnum):
    """
    Enum for catalog extensions

    Used for generating sucatalog URLs
    """
    PLIST: str = ".sucatalog"
    GZIP:  str = ".sucatalog.gz"
