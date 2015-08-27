'''Wrapper for GraphQLAst.h

Generated with:
/usr/local/bin/ctypesgen.py ../c/GraphQLAst.h ../c/GraphQLAstForEachConcreteType.h ../c/GraphQLAstNode.h ../c/GraphQLAstVisitor.h ../c/GraphQLParser.h -o GraphQLParser.py -l graphqlparser -L ..

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = ['..']

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs(['..'])

# Begin libraries

_libs["graphqlparser"] = load_library("graphqlparser")

# 1 libraries
# End libraries

# No modules

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 18
class struct_GraphQLAstDefinition(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 20
class struct_GraphQLAstDocument(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 21
if hasattr(_libs['graphqlparser'], 'GraphQLAstDocument_get_definitions_size'):
    GraphQLAstDocument_get_definitions_size = _libs['graphqlparser'].GraphQLAstDocument_get_definitions_size
    GraphQLAstDocument_get_definitions_size.argtypes = [POINTER(struct_GraphQLAstDocument)]
    GraphQLAstDocument_get_definitions_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 23
class struct_GraphQLAstOperationDefinition(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 24
if hasattr(_libs['graphqlparser'], 'GraphQLAstOperationDefinition_get_operation'):
    GraphQLAstOperationDefinition_get_operation = _libs['graphqlparser'].GraphQLAstOperationDefinition_get_operation
    GraphQLAstOperationDefinition_get_operation.argtypes = [POINTER(struct_GraphQLAstOperationDefinition)]
    if sizeof(c_int) == sizeof(c_void_p):
        GraphQLAstOperationDefinition_get_operation.restype = ReturnString
    else:
        GraphQLAstOperationDefinition_get_operation.restype = String
        GraphQLAstOperationDefinition_get_operation.errcheck = ReturnString

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 25
class struct_GraphQLAstName(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 25
if hasattr(_libs['graphqlparser'], 'GraphQLAstOperationDefinition_get_name'):
    GraphQLAstOperationDefinition_get_name = _libs['graphqlparser'].GraphQLAstOperationDefinition_get_name
    GraphQLAstOperationDefinition_get_name.argtypes = [POINTER(struct_GraphQLAstOperationDefinition)]
    GraphQLAstOperationDefinition_get_name.restype = POINTER(struct_GraphQLAstName)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 26
if hasattr(_libs['graphqlparser'], 'GraphQLAstOperationDefinition_get_variable_definitions_size'):
    GraphQLAstOperationDefinition_get_variable_definitions_size = _libs['graphqlparser'].GraphQLAstOperationDefinition_get_variable_definitions_size
    GraphQLAstOperationDefinition_get_variable_definitions_size.argtypes = [POINTER(struct_GraphQLAstOperationDefinition)]
    GraphQLAstOperationDefinition_get_variable_definitions_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 27
if hasattr(_libs['graphqlparser'], 'GraphQLAstOperationDefinition_get_directives_size'):
    GraphQLAstOperationDefinition_get_directives_size = _libs['graphqlparser'].GraphQLAstOperationDefinition_get_directives_size
    GraphQLAstOperationDefinition_get_directives_size.argtypes = [POINTER(struct_GraphQLAstOperationDefinition)]
    GraphQLAstOperationDefinition_get_directives_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 28
class struct_GraphQLAstSelectionSet(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 28
if hasattr(_libs['graphqlparser'], 'GraphQLAstOperationDefinition_get_selection_set'):
    GraphQLAstOperationDefinition_get_selection_set = _libs['graphqlparser'].GraphQLAstOperationDefinition_get_selection_set
    GraphQLAstOperationDefinition_get_selection_set.argtypes = [POINTER(struct_GraphQLAstOperationDefinition)]
    GraphQLAstOperationDefinition_get_selection_set.restype = POINTER(struct_GraphQLAstSelectionSet)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 30
class struct_GraphQLAstVariableDefinition(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 31
class struct_GraphQLAstVariable(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 31
if hasattr(_libs['graphqlparser'], 'GraphQLAstVariableDefinition_get_variable'):
    GraphQLAstVariableDefinition_get_variable = _libs['graphqlparser'].GraphQLAstVariableDefinition_get_variable
    GraphQLAstVariableDefinition_get_variable.argtypes = [POINTER(struct_GraphQLAstVariableDefinition)]
    GraphQLAstVariableDefinition_get_variable.restype = POINTER(struct_GraphQLAstVariable)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 32
class struct_GraphQLAstType(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 32
if hasattr(_libs['graphqlparser'], 'GraphQLAstVariableDefinition_get_type'):
    GraphQLAstVariableDefinition_get_type = _libs['graphqlparser'].GraphQLAstVariableDefinition_get_type
    GraphQLAstVariableDefinition_get_type.argtypes = [POINTER(struct_GraphQLAstVariableDefinition)]
    GraphQLAstVariableDefinition_get_type.restype = POINTER(struct_GraphQLAstType)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 33
class struct_GraphQLAstValue(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 33
if hasattr(_libs['graphqlparser'], 'GraphQLAstVariableDefinition_get_default_value'):
    GraphQLAstVariableDefinition_get_default_value = _libs['graphqlparser'].GraphQLAstVariableDefinition_get_default_value
    GraphQLAstVariableDefinition_get_default_value.argtypes = [POINTER(struct_GraphQLAstVariableDefinition)]
    GraphQLAstVariableDefinition_get_default_value.restype = POINTER(struct_GraphQLAstValue)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 36
if hasattr(_libs['graphqlparser'], 'GraphQLAstSelectionSet_get_selections_size'):
    GraphQLAstSelectionSet_get_selections_size = _libs['graphqlparser'].GraphQLAstSelectionSet_get_selections_size
    GraphQLAstSelectionSet_get_selections_size.argtypes = [POINTER(struct_GraphQLAstSelectionSet)]
    GraphQLAstSelectionSet_get_selections_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 38
class struct_GraphQLAstSelection(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 40
class struct_GraphQLAstField(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 41
if hasattr(_libs['graphqlparser'], 'GraphQLAstField_get_alias'):
    GraphQLAstField_get_alias = _libs['graphqlparser'].GraphQLAstField_get_alias
    GraphQLAstField_get_alias.argtypes = [POINTER(struct_GraphQLAstField)]
    GraphQLAstField_get_alias.restype = POINTER(struct_GraphQLAstName)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 42
if hasattr(_libs['graphqlparser'], 'GraphQLAstField_get_name'):
    GraphQLAstField_get_name = _libs['graphqlparser'].GraphQLAstField_get_name
    GraphQLAstField_get_name.argtypes = [POINTER(struct_GraphQLAstField)]
    GraphQLAstField_get_name.restype = POINTER(struct_GraphQLAstName)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 43
if hasattr(_libs['graphqlparser'], 'GraphQLAstField_get_arguments_size'):
    GraphQLAstField_get_arguments_size = _libs['graphqlparser'].GraphQLAstField_get_arguments_size
    GraphQLAstField_get_arguments_size.argtypes = [POINTER(struct_GraphQLAstField)]
    GraphQLAstField_get_arguments_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 44
if hasattr(_libs['graphqlparser'], 'GraphQLAstField_get_directives_size'):
    GraphQLAstField_get_directives_size = _libs['graphqlparser'].GraphQLAstField_get_directives_size
    GraphQLAstField_get_directives_size.argtypes = [POINTER(struct_GraphQLAstField)]
    GraphQLAstField_get_directives_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 45
if hasattr(_libs['graphqlparser'], 'GraphQLAstField_get_selection_set'):
    GraphQLAstField_get_selection_set = _libs['graphqlparser'].GraphQLAstField_get_selection_set
    GraphQLAstField_get_selection_set.argtypes = [POINTER(struct_GraphQLAstField)]
    GraphQLAstField_get_selection_set.restype = POINTER(struct_GraphQLAstSelectionSet)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 47
class struct_GraphQLAstArgument(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 48
if hasattr(_libs['graphqlparser'], 'GraphQLAstArgument_get_name'):
    GraphQLAstArgument_get_name = _libs['graphqlparser'].GraphQLAstArgument_get_name
    GraphQLAstArgument_get_name.argtypes = [POINTER(struct_GraphQLAstArgument)]
    GraphQLAstArgument_get_name.restype = POINTER(struct_GraphQLAstName)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 49
if hasattr(_libs['graphqlparser'], 'GraphQLAstArgument_get_value'):
    GraphQLAstArgument_get_value = _libs['graphqlparser'].GraphQLAstArgument_get_value
    GraphQLAstArgument_get_value.argtypes = [POINTER(struct_GraphQLAstArgument)]
    GraphQLAstArgument_get_value.restype = POINTER(struct_GraphQLAstValue)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 51
class struct_GraphQLAstFragmentSpread(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 52
if hasattr(_libs['graphqlparser'], 'GraphQLAstFragmentSpread_get_name'):
    GraphQLAstFragmentSpread_get_name = _libs['graphqlparser'].GraphQLAstFragmentSpread_get_name
    GraphQLAstFragmentSpread_get_name.argtypes = [POINTER(struct_GraphQLAstFragmentSpread)]
    GraphQLAstFragmentSpread_get_name.restype = POINTER(struct_GraphQLAstName)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 53
if hasattr(_libs['graphqlparser'], 'GraphQLAstFragmentSpread_get_directives_size'):
    GraphQLAstFragmentSpread_get_directives_size = _libs['graphqlparser'].GraphQLAstFragmentSpread_get_directives_size
    GraphQLAstFragmentSpread_get_directives_size.argtypes = [POINTER(struct_GraphQLAstFragmentSpread)]
    GraphQLAstFragmentSpread_get_directives_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 55
class struct_GraphQLAstInlineFragment(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 56
class struct_GraphQLAstNamedType(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 56
if hasattr(_libs['graphqlparser'], 'GraphQLAstInlineFragment_get_type_condition'):
    GraphQLAstInlineFragment_get_type_condition = _libs['graphqlparser'].GraphQLAstInlineFragment_get_type_condition
    GraphQLAstInlineFragment_get_type_condition.argtypes = [POINTER(struct_GraphQLAstInlineFragment)]
    GraphQLAstInlineFragment_get_type_condition.restype = POINTER(struct_GraphQLAstNamedType)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 57
if hasattr(_libs['graphqlparser'], 'GraphQLAstInlineFragment_get_directives_size'):
    GraphQLAstInlineFragment_get_directives_size = _libs['graphqlparser'].GraphQLAstInlineFragment_get_directives_size
    GraphQLAstInlineFragment_get_directives_size.argtypes = [POINTER(struct_GraphQLAstInlineFragment)]
    GraphQLAstInlineFragment_get_directives_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 58
if hasattr(_libs['graphqlparser'], 'GraphQLAstInlineFragment_get_selection_set'):
    GraphQLAstInlineFragment_get_selection_set = _libs['graphqlparser'].GraphQLAstInlineFragment_get_selection_set
    GraphQLAstInlineFragment_get_selection_set.argtypes = [POINTER(struct_GraphQLAstInlineFragment)]
    GraphQLAstInlineFragment_get_selection_set.restype = POINTER(struct_GraphQLAstSelectionSet)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 60
class struct_GraphQLAstFragmentDefinition(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 61
if hasattr(_libs['graphqlparser'], 'GraphQLAstFragmentDefinition_get_name'):
    GraphQLAstFragmentDefinition_get_name = _libs['graphqlparser'].GraphQLAstFragmentDefinition_get_name
    GraphQLAstFragmentDefinition_get_name.argtypes = [POINTER(struct_GraphQLAstFragmentDefinition)]
    GraphQLAstFragmentDefinition_get_name.restype = POINTER(struct_GraphQLAstName)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 62
if hasattr(_libs['graphqlparser'], 'GraphQLAstFragmentDefinition_get_type_condition'):
    GraphQLAstFragmentDefinition_get_type_condition = _libs['graphqlparser'].GraphQLAstFragmentDefinition_get_type_condition
    GraphQLAstFragmentDefinition_get_type_condition.argtypes = [POINTER(struct_GraphQLAstFragmentDefinition)]
    GraphQLAstFragmentDefinition_get_type_condition.restype = POINTER(struct_GraphQLAstNamedType)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 63
if hasattr(_libs['graphqlparser'], 'GraphQLAstFragmentDefinition_get_directives_size'):
    GraphQLAstFragmentDefinition_get_directives_size = _libs['graphqlparser'].GraphQLAstFragmentDefinition_get_directives_size
    GraphQLAstFragmentDefinition_get_directives_size.argtypes = [POINTER(struct_GraphQLAstFragmentDefinition)]
    GraphQLAstFragmentDefinition_get_directives_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 64
if hasattr(_libs['graphqlparser'], 'GraphQLAstFragmentDefinition_get_selection_set'):
    GraphQLAstFragmentDefinition_get_selection_set = _libs['graphqlparser'].GraphQLAstFragmentDefinition_get_selection_set
    GraphQLAstFragmentDefinition_get_selection_set.argtypes = [POINTER(struct_GraphQLAstFragmentDefinition)]
    GraphQLAstFragmentDefinition_get_selection_set.restype = POINTER(struct_GraphQLAstSelectionSet)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 69
if hasattr(_libs['graphqlparser'], 'GraphQLAstVariable_get_name'):
    GraphQLAstVariable_get_name = _libs['graphqlparser'].GraphQLAstVariable_get_name
    GraphQLAstVariable_get_name.argtypes = [POINTER(struct_GraphQLAstVariable)]
    GraphQLAstVariable_get_name.restype = POINTER(struct_GraphQLAstName)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 71
class struct_GraphQLAstIntValue(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 72
if hasattr(_libs['graphqlparser'], 'GraphQLAstIntValue_get_value'):
    GraphQLAstIntValue_get_value = _libs['graphqlparser'].GraphQLAstIntValue_get_value
    GraphQLAstIntValue_get_value.argtypes = [POINTER(struct_GraphQLAstIntValue)]
    if sizeof(c_int) == sizeof(c_void_p):
        GraphQLAstIntValue_get_value.restype = ReturnString
    else:
        GraphQLAstIntValue_get_value.restype = String
        GraphQLAstIntValue_get_value.errcheck = ReturnString

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 74
class struct_GraphQLAstFloatValue(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 75
if hasattr(_libs['graphqlparser'], 'GraphQLAstFloatValue_get_value'):
    GraphQLAstFloatValue_get_value = _libs['graphqlparser'].GraphQLAstFloatValue_get_value
    GraphQLAstFloatValue_get_value.argtypes = [POINTER(struct_GraphQLAstFloatValue)]
    if sizeof(c_int) == sizeof(c_void_p):
        GraphQLAstFloatValue_get_value.restype = ReturnString
    else:
        GraphQLAstFloatValue_get_value.restype = String
        GraphQLAstFloatValue_get_value.errcheck = ReturnString

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 77
class struct_GraphQLAstStringValue(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 78
if hasattr(_libs['graphqlparser'], 'GraphQLAstStringValue_get_value'):
    GraphQLAstStringValue_get_value = _libs['graphqlparser'].GraphQLAstStringValue_get_value
    GraphQLAstStringValue_get_value.argtypes = [POINTER(struct_GraphQLAstStringValue)]
    if sizeof(c_int) == sizeof(c_void_p):
        GraphQLAstStringValue_get_value.restype = ReturnString
    else:
        GraphQLAstStringValue_get_value.restype = String
        GraphQLAstStringValue_get_value.errcheck = ReturnString

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 80
class struct_GraphQLAstBooleanValue(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 81
if hasattr(_libs['graphqlparser'], 'GraphQLAstBooleanValue_get_value'):
    GraphQLAstBooleanValue_get_value = _libs['graphqlparser'].GraphQLAstBooleanValue_get_value
    GraphQLAstBooleanValue_get_value.argtypes = [POINTER(struct_GraphQLAstBooleanValue)]
    GraphQLAstBooleanValue_get_value.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 83
class struct_GraphQLAstEnumValue(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 84
if hasattr(_libs['graphqlparser'], 'GraphQLAstEnumValue_get_value'):
    GraphQLAstEnumValue_get_value = _libs['graphqlparser'].GraphQLAstEnumValue_get_value
    GraphQLAstEnumValue_get_value.argtypes = [POINTER(struct_GraphQLAstEnumValue)]
    if sizeof(c_int) == sizeof(c_void_p):
        GraphQLAstEnumValue_get_value.restype = ReturnString
    else:
        GraphQLAstEnumValue_get_value.restype = String
        GraphQLAstEnumValue_get_value.errcheck = ReturnString

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 86
class struct_GraphQLAstArrayValue(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 87
if hasattr(_libs['graphqlparser'], 'GraphQLAstArrayValue_get_values_size'):
    GraphQLAstArrayValue_get_values_size = _libs['graphqlparser'].GraphQLAstArrayValue_get_values_size
    GraphQLAstArrayValue_get_values_size.argtypes = [POINTER(struct_GraphQLAstArrayValue)]
    GraphQLAstArrayValue_get_values_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 89
class struct_GraphQLAstObjectValue(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 90
if hasattr(_libs['graphqlparser'], 'GraphQLAstObjectValue_get_fields_size'):
    GraphQLAstObjectValue_get_fields_size = _libs['graphqlparser'].GraphQLAstObjectValue_get_fields_size
    GraphQLAstObjectValue_get_fields_size.argtypes = [POINTER(struct_GraphQLAstObjectValue)]
    GraphQLAstObjectValue_get_fields_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 92
class struct_GraphQLAstObjectField(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 93
if hasattr(_libs['graphqlparser'], 'GraphQLAstObjectField_get_name'):
    GraphQLAstObjectField_get_name = _libs['graphqlparser'].GraphQLAstObjectField_get_name
    GraphQLAstObjectField_get_name.argtypes = [POINTER(struct_GraphQLAstObjectField)]
    GraphQLAstObjectField_get_name.restype = POINTER(struct_GraphQLAstName)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 94
if hasattr(_libs['graphqlparser'], 'GraphQLAstObjectField_get_value'):
    GraphQLAstObjectField_get_value = _libs['graphqlparser'].GraphQLAstObjectField_get_value
    GraphQLAstObjectField_get_value.argtypes = [POINTER(struct_GraphQLAstObjectField)]
    GraphQLAstObjectField_get_value.restype = POINTER(struct_GraphQLAstValue)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 96
class struct_GraphQLAstDirective(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 97
if hasattr(_libs['graphqlparser'], 'GraphQLAstDirective_get_name'):
    GraphQLAstDirective_get_name = _libs['graphqlparser'].GraphQLAstDirective_get_name
    GraphQLAstDirective_get_name.argtypes = [POINTER(struct_GraphQLAstDirective)]
    GraphQLAstDirective_get_name.restype = POINTER(struct_GraphQLAstName)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 98
if hasattr(_libs['graphqlparser'], 'GraphQLAstDirective_get_arguments_size'):
    GraphQLAstDirective_get_arguments_size = _libs['graphqlparser'].GraphQLAstDirective_get_arguments_size
    GraphQLAstDirective_get_arguments_size.argtypes = [POINTER(struct_GraphQLAstDirective)]
    GraphQLAstDirective_get_arguments_size.restype = c_int

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 103
if hasattr(_libs['graphqlparser'], 'GraphQLAstNamedType_get_name'):
    GraphQLAstNamedType_get_name = _libs['graphqlparser'].GraphQLAstNamedType_get_name
    GraphQLAstNamedType_get_name.argtypes = [POINTER(struct_GraphQLAstNamedType)]
    GraphQLAstNamedType_get_name.restype = POINTER(struct_GraphQLAstName)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 105
class struct_GraphQLAstListType(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 106
if hasattr(_libs['graphqlparser'], 'GraphQLAstListType_get_type'):
    GraphQLAstListType_get_type = _libs['graphqlparser'].GraphQLAstListType_get_type
    GraphQLAstListType_get_type.argtypes = [POINTER(struct_GraphQLAstListType)]
    GraphQLAstListType_get_type.restype = POINTER(struct_GraphQLAstType)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 108
class struct_GraphQLAstNonNullType(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 109
if hasattr(_libs['graphqlparser'], 'GraphQLAstNonNullType_get_type'):
    GraphQLAstNonNullType_get_type = _libs['graphqlparser'].GraphQLAstNonNullType_get_type
    GraphQLAstNonNullType_get_type.argtypes = [POINTER(struct_GraphQLAstNonNullType)]
    GraphQLAstNonNullType_get_type.restype = POINTER(struct_GraphQLAstType)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 112
if hasattr(_libs['graphqlparser'], 'GraphQLAstName_get_value'):
    GraphQLAstName_get_value = _libs['graphqlparser'].GraphQLAstName_get_value
    GraphQLAstName_get_value.argtypes = [POINTER(struct_GraphQLAstName)]
    if sizeof(c_int) == sizeof(c_void_p):
        GraphQLAstName_get_value.restype = ReturnString
    else:
        GraphQLAstName_get_value.restype = String
        GraphQLAstName_get_value.errcheck = ReturnString

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstNode.h: 17
class struct_GraphQLAstNode(Structure):
    pass

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstNode.h: 20
class struct_GraphQLAstLocation(Structure):
    pass

struct_GraphQLAstLocation.__slots__ = [
    'beginLine',
    'beginColumn',
    'endLine',
    'endColumn',
]
struct_GraphQLAstLocation._fields_ = [
    ('beginLine', c_uint),
    ('beginColumn', c_uint),
    ('endLine', c_uint),
    ('endColumn', c_uint),
]

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstNode.h: 28
if hasattr(_libs['graphqlparser'], 'graphql_node_get_location'):
    graphql_node_get_location = _libs['graphqlparser'].graphql_node_get_location
    graphql_node_get_location.argtypes = [POINTER(struct_GraphQLAstNode), POINTER(struct_GraphQLAstLocation)]
    graphql_node_get_location.restype = None

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstNode.h: 31
if hasattr(_libs['graphqlparser'], 'graphql_node_free'):
    graphql_node_free = _libs['graphqlparser'].graphql_node_free
    graphql_node_free.argtypes = [POINTER(struct_GraphQLAstNode)]
    graphql_node_free.restype = None

visit_document_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstDocument), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_document_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstDocument), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_operation_definition_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstOperationDefinition), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_operation_definition_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstOperationDefinition), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_variable_definition_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstVariableDefinition), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_variable_definition_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstVariableDefinition), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_selection_set_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstSelectionSet), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_selection_set_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstSelectionSet), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_field_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstField), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_field_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstField), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_argument_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstArgument), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_argument_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstArgument), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_fragment_spread_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstFragmentSpread), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_fragment_spread_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstFragmentSpread), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_inline_fragment_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstInlineFragment), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_inline_fragment_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstInlineFragment), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_fragment_definition_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstFragmentDefinition), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_fragment_definition_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstFragmentDefinition), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_variable_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstVariable), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_variable_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstVariable), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_int_value_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstIntValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_int_value_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstIntValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_float_value_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstFloatValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_float_value_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstFloatValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_string_value_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstStringValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_string_value_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstStringValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_boolean_value_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstBooleanValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_boolean_value_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstBooleanValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_enum_value_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstEnumValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_enum_value_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstEnumValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_array_value_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstArrayValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_array_value_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstArrayValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_object_value_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstObjectValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_object_value_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstObjectValue), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_object_field_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstObjectField), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_object_field_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstObjectField), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_directive_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstDirective), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_directive_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstDirective), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_named_type_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstNamedType), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_named_type_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstNamedType), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_list_type_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstListType), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_list_type_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstListType), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_non_null_type_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstNonNullType), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_non_null_type_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstNonNullType), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

visit_name_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_GraphQLAstName), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

end_visit_name_func = CFUNCTYPE(UNCHECKED(None), POINTER(struct_GraphQLAstName), POINTER(None)) # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 23

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 37
class struct_GraphQLAstVisitorCallbacks(Structure):
    pass

struct_GraphQLAstVisitorCallbacks.__slots__ = [
    'visit_document',
    'end_visit_document',
    'visit_operation_definition',
    'end_visit_operation_definition',
    'visit_variable_definition',
    'end_visit_variable_definition',
    'visit_selection_set',
    'end_visit_selection_set',
    'visit_field',
    'end_visit_field',
    'visit_argument',
    'end_visit_argument',
    'visit_fragment_spread',
    'end_visit_fragment_spread',
    'visit_inline_fragment',
    'end_visit_inline_fragment',
    'visit_fragment_definition',
    'end_visit_fragment_definition',
    'visit_variable',
    'end_visit_variable',
    'visit_int_value',
    'end_visit_int_value',
    'visit_float_value',
    'end_visit_float_value',
    'visit_string_value',
    'end_visit_string_value',
    'visit_boolean_value',
    'end_visit_boolean_value',
    'visit_enum_value',
    'end_visit_enum_value',
    'visit_array_value',
    'end_visit_array_value',
    'visit_object_value',
    'end_visit_object_value',
    'visit_object_field',
    'end_visit_object_field',
    'visit_directive',
    'end_visit_directive',
    'visit_named_type',
    'end_visit_named_type',
    'visit_list_type',
    'end_visit_list_type',
    'visit_non_null_type',
    'end_visit_non_null_type',
    'visit_name',
    'end_visit_name',
]
struct_GraphQLAstVisitorCallbacks._fields_ = [
    ('visit_document', visit_document_func),
    ('end_visit_document', end_visit_document_func),
    ('visit_operation_definition', visit_operation_definition_func),
    ('end_visit_operation_definition', end_visit_operation_definition_func),
    ('visit_variable_definition', visit_variable_definition_func),
    ('end_visit_variable_definition', end_visit_variable_definition_func),
    ('visit_selection_set', visit_selection_set_func),
    ('end_visit_selection_set', end_visit_selection_set_func),
    ('visit_field', visit_field_func),
    ('end_visit_field', end_visit_field_func),
    ('visit_argument', visit_argument_func),
    ('end_visit_argument', end_visit_argument_func),
    ('visit_fragment_spread', visit_fragment_spread_func),
    ('end_visit_fragment_spread', end_visit_fragment_spread_func),
    ('visit_inline_fragment', visit_inline_fragment_func),
    ('end_visit_inline_fragment', end_visit_inline_fragment_func),
    ('visit_fragment_definition', visit_fragment_definition_func),
    ('end_visit_fragment_definition', end_visit_fragment_definition_func),
    ('visit_variable', visit_variable_func),
    ('end_visit_variable', end_visit_variable_func),
    ('visit_int_value', visit_int_value_func),
    ('end_visit_int_value', end_visit_int_value_func),
    ('visit_float_value', visit_float_value_func),
    ('end_visit_float_value', end_visit_float_value_func),
    ('visit_string_value', visit_string_value_func),
    ('end_visit_string_value', end_visit_string_value_func),
    ('visit_boolean_value', visit_boolean_value_func),
    ('end_visit_boolean_value', end_visit_boolean_value_func),
    ('visit_enum_value', visit_enum_value_func),
    ('end_visit_enum_value', end_visit_enum_value_func),
    ('visit_array_value', visit_array_value_func),
    ('end_visit_array_value', end_visit_array_value_func),
    ('visit_object_value', visit_object_value_func),
    ('end_visit_object_value', end_visit_object_value_func),
    ('visit_object_field', visit_object_field_func),
    ('end_visit_object_field', end_visit_object_field_func),
    ('visit_directive', visit_directive_func),
    ('end_visit_directive', end_visit_directive_func),
    ('visit_named_type', visit_named_type_func),
    ('end_visit_named_type', end_visit_named_type_func),
    ('visit_list_type', visit_list_type_func),
    ('end_visit_list_type', end_visit_list_type_func),
    ('visit_non_null_type', visit_non_null_type_func),
    ('end_visit_non_null_type', end_visit_non_null_type_func),
    ('visit_name', visit_name_func),
    ('end_visit_name', end_visit_name_func),
]

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 48
if hasattr(_libs['graphqlparser'], 'graphql_node_visit'):
    graphql_node_visit = _libs['graphqlparser'].graphql_node_visit
    graphql_node_visit.argtypes = [POINTER(struct_GraphQLAstNode), POINTER(struct_GraphQLAstVisitorCallbacks), POINTER(None)]
    graphql_node_visit.restype = None

__int64_t = c_longlong # /Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include/i386/_types.h: 46

__darwin_off_t = __int64_t # /Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include/sys/_types.h: 71

fpos_t = __darwin_off_t # /Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include/stdio.h: 77

# /Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include/stdio.h: 88
class struct___sbuf(Structure):
    pass

struct___sbuf.__slots__ = [
    '_base',
    '_size',
]
struct___sbuf._fields_ = [
    ('_base', POINTER(c_ubyte)),
    ('_size', c_int),
]

# /Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include/stdio.h: 94
class struct___sFILEX(Structure):
    pass

# /Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include/stdio.h: 153
class struct___sFILE(Structure):
    pass

struct___sFILE.__slots__ = [
    '_p',
    '_r',
    '_w',
    '_flags',
    '_file',
    '_bf',
    '_lbfsize',
    '_cookie',
    '_close',
    '_read',
    '_seek',
    '_write',
    '_ub',
    '_extra',
    '_ur',
    '_ubuf',
    '_nbuf',
    '_lb',
    '_blksize',
    '_offset',
]
struct___sFILE._fields_ = [
    ('_p', POINTER(c_ubyte)),
    ('_r', c_int),
    ('_w', c_int),
    ('_flags', c_short),
    ('_file', c_short),
    ('_bf', struct___sbuf),
    ('_lbfsize', c_int),
    ('_cookie', POINTER(None)),
    ('_close', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
    ('_read', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), String, c_int)),
    ('_seek', CFUNCTYPE(UNCHECKED(fpos_t), POINTER(None), fpos_t, c_int)),
    ('_write', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), String, c_int)),
    ('_ub', struct___sbuf),
    ('_extra', POINTER(struct___sFILEX)),
    ('_ur', c_int),
    ('_ubuf', c_ubyte * 3),
    ('_nbuf', c_ubyte * 1),
    ('_lb', struct___sbuf),
    ('_blksize', c_int),
    ('_offset', fpos_t),
]

FILE = struct___sFILE # /Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include/stdio.h: 153

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLParser.h: 31
if hasattr(_libs['graphqlparser'], 'graphql_parse_string'):
    graphql_parse_string = _libs['graphqlparser'].graphql_parse_string
    graphql_parse_string.argtypes = [String, POINTER(POINTER(c_char))]
    graphql_parse_string.restype = POINTER(struct_GraphQLAstNode)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLParser.h: 41
if hasattr(_libs['graphqlparser'], 'graphql_parse_file'):
    graphql_parse_file = _libs['graphqlparser'].graphql_parse_file
    graphql_parse_file.argtypes = [POINTER(FILE), POINTER(POINTER(c_char))]
    graphql_parse_file.restype = POINTER(struct_GraphQLAstNode)

# /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLParser.h: 46
if hasattr(_libs['graphqlparser'], 'graphql_error_free'):
    graphql_error_free = _libs['graphqlparser'].graphql_error_free
    graphql_error_free.argtypes = [String]
    graphql_error_free.restype = None

GraphQLAstDefinition = struct_GraphQLAstDefinition # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 18

GraphQLAstDocument = struct_GraphQLAstDocument # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 20

GraphQLAstOperationDefinition = struct_GraphQLAstOperationDefinition # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 23

GraphQLAstName = struct_GraphQLAstName # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 25

GraphQLAstSelectionSet = struct_GraphQLAstSelectionSet # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 28

GraphQLAstVariableDefinition = struct_GraphQLAstVariableDefinition # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 30

GraphQLAstVariable = struct_GraphQLAstVariable # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 31

GraphQLAstType = struct_GraphQLAstType # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 32

GraphQLAstValue = struct_GraphQLAstValue # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 33

GraphQLAstSelection = struct_GraphQLAstSelection # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 38

GraphQLAstField = struct_GraphQLAstField # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 40

GraphQLAstArgument = struct_GraphQLAstArgument # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 47

GraphQLAstFragmentSpread = struct_GraphQLAstFragmentSpread # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 51

GraphQLAstInlineFragment = struct_GraphQLAstInlineFragment # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 55

GraphQLAstNamedType = struct_GraphQLAstNamedType # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 56

GraphQLAstFragmentDefinition = struct_GraphQLAstFragmentDefinition # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 60

GraphQLAstIntValue = struct_GraphQLAstIntValue # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 71

GraphQLAstFloatValue = struct_GraphQLAstFloatValue # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 74

GraphQLAstStringValue = struct_GraphQLAstStringValue # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 77

GraphQLAstBooleanValue = struct_GraphQLAstBooleanValue # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 80

GraphQLAstEnumValue = struct_GraphQLAstEnumValue # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 83

GraphQLAstArrayValue = struct_GraphQLAstArrayValue # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 86

GraphQLAstObjectValue = struct_GraphQLAstObjectValue # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 89

GraphQLAstObjectField = struct_GraphQLAstObjectField # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 92

GraphQLAstDirective = struct_GraphQLAstDirective # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 96

GraphQLAstListType = struct_GraphQLAstListType # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 105

GraphQLAstNonNullType = struct_GraphQLAstNonNullType # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAst.h: 108

GraphQLAstNode = struct_GraphQLAstNode # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstNode.h: 17

GraphQLAstLocation = struct_GraphQLAstLocation # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstNode.h: 20

GraphQLAstVisitorCallbacks = struct_GraphQLAstVisitorCallbacks # /Users/gary.roberts/Development/go/src/github.com/tallstreet/graphql/libgraphqlparser/c/GraphQLAstVisitor.h: 37

# No inserted files

