# encoding: utf-8
# module matplotlib._png
# from D:\ProgramData\Anaconda3\lib\site-packages\matplotlib\_png.cp36-win_amd64.pyd
# by generator 1.145
# no doc
# no imports

# Variables with simple values

PNG_FILTER_AVG = 64
PNG_FILTER_NONE = 8
PNG_FILTER_PAETH = 128
PNG_FILTER_SUB = 16
PNG_FILTER_UP = 32

# functions

def read_png(file): # real signature unknown; restored from __doc__
    """
    read_png(file)
    
    Read in a PNG file, converting values to floating-point doubles
    in the range (0, 1)
    
    Alias for read_png_float()
    
    Parameters
    ----------
    file : str path or file-like object
    """
    pass

def read_png_float(file): # real signature unknown; restored from __doc__
    """
    read_png_float(file)
    
    Read in a PNG file, converting values to floating-point doubles
    in the range (0, 1)
    
    Parameters
    ----------
    file : str path or file-like object
    """
    pass

def read_png_int(file): # real signature unknown; restored from __doc__
    """
    read_png_int(file)
    
    Read in a PNG file with original integer values.
    
    Parameters
    ----------
    file : str path or file-like object
    """
    pass

def write_png(buffer, file, dpi=0, compression=6, filter=None): # real signature unknown; restored from __doc__
    """
    write_png(buffer, file, dpi=0, compression=6, filter=auto)
    
    Parameters
    ----------
    buffer : numpy array of image data
        Must be an MxNxD array of dtype uint8.
        - if D is 1, the image is greyscale
        - if D is 3, the image is RGB
        - if D is 4, the image is RGBA
    
    file : str path, file-like object or None
        - If a str, must be a file path
        - If a file-like object, must write bytes
        - If None, a byte string containing the PNG data will be returned
    
    dpi : float
        The dpi to store in the file metadata.
    
    compression : int
        The level of lossless zlib compression to apply.  0 indicates no
        compression.  Values 1-9 indicate low/fast through high/slow
        compression.  Default is 6.
    
    filter : int
        Filter to apply.  Must be one of the constants: PNG_FILTER_NONE,
        PNG_FILTER_SUB, PNG_FILTER_UP, PNG_FILTER_AVG, PNG_FILTER_PAETH.
        See the PNG standard for more information.
        If not provided, libpng will try to automatically determine the
        best filter on a line-by-line basis.
    
    Returns
    -------
    buffer : bytes or None
        Byte string containing the PNG content if None was passed in for
        file, otherwise None is returned.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

