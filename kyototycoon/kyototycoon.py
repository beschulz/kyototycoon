# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_kyototycoon', [dirname(__file__)])
        except ImportError:
            import _kyototycoon
            return _kyototycoon
        if fp is not None:
            try:
                _mod = imp.load_module('_kyototycoon', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _kyototycoon = swig_import_helper()
    del swig_import_helper
else:
    import _kyototycoon
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _kyototycoon.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _kyototycoon.SwigPyIterator_value(self)
    def incr(self, n = 1): return _kyototycoon.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _kyototycoon.SwigPyIterator_decr(self, n)
    def distance(self, *args, **kwargs): return _kyototycoon.SwigPyIterator_distance(self, *args, **kwargs)
    def equal(self, *args, **kwargs): return _kyototycoon.SwigPyIterator_equal(self, *args, **kwargs)
    def copy(self): return _kyototycoon.SwigPyIterator_copy(self)
    def next(self): return _kyototycoon.SwigPyIterator_next(self)
    def __next__(self): return _kyototycoon.SwigPyIterator___next__(self)
    def previous(self): return _kyototycoon.SwigPyIterator_previous(self)
    def advance(self, *args, **kwargs): return _kyototycoon.SwigPyIterator_advance(self, *args, **kwargs)
    def __eq__(self, *args, **kwargs): return _kyototycoon.SwigPyIterator___eq__(self, *args, **kwargs)
    def __ne__(self, *args, **kwargs): return _kyototycoon.SwigPyIterator___ne__(self, *args, **kwargs)
    def __iadd__(self, *args, **kwargs): return _kyototycoon.SwigPyIterator___iadd__(self, *args, **kwargs)
    def __isub__(self, *args, **kwargs): return _kyototycoon.SwigPyIterator___isub__(self, *args, **kwargs)
    def __add__(self, *args, **kwargs): return _kyototycoon.SwigPyIterator___add__(self, *args, **kwargs)
    def __sub__(self, *args): return _kyototycoon.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _kyototycoon.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _kyototycoon.SHARED_PTR_DISOWN
class Error(Exception):
    """
    Base class for all exceptions


    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Error, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Error, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SUCCESS = _kyototycoon.Error_SUCCESS
    NOIMPL = _kyototycoon.Error_NOIMPL
    INVALID = _kyototycoon.Error_INVALID
    LOGIC = _kyototycoon.Error_LOGIC
    TIMEOUT = _kyototycoon.Error_TIMEOUT
    INTERNAL = _kyototycoon.Error_INTERNAL
    NETWORK = _kyototycoon.Error_NETWORK
    EMISC = _kyototycoon.Error_EMISC
    def code(self):
        """code(self) -> Code"""
        return _kyototycoon.Error_code(self)

    def name(self):
        """name(self) -> string"""
        return _kyototycoon.Error_name(self)

    def message(self):
        """message(self) -> string"""
        return _kyototycoon.Error_message(self)

    def __str__(self):
        """__str__(self) -> string"""
        return _kyototycoon.Error___str__(self)

    __swig_destroy__ = _kyototycoon.delete_Error
    __del__ = lambda self : None;
Error_swigregister = _kyototycoon.Error_swigregister
Error_swigregister(Error)

class NoError(Error):
    """Proxy of C++ kyototycoon::NoError class"""
    __swig_setmethods__ = {}
    for _s in [Error]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NoError, name, value)
    __swig_getmethods__ = {}
    for _s in [Error]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, NoError, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _kyototycoon.delete_NoError
    __del__ = lambda self : None;
NoError_swigregister = _kyototycoon.NoError_swigregister
NoError_swigregister(NoError)

class NotImplementedError(Error):
    """Proxy of C++ kyototycoon::NotImplementedError class"""
    __swig_setmethods__ = {}
    for _s in [Error]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NotImplementedError, name, value)
    __swig_getmethods__ = {}
    for _s in [Error]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, NotImplementedError, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _kyototycoon.delete_NotImplementedError
    __del__ = lambda self : None;
NotImplementedError_swigregister = _kyototycoon.NotImplementedError_swigregister
NotImplementedError_swigregister(NotImplementedError)

class InvalidError(Error):
    """Proxy of C++ kyototycoon::InvalidError class"""
    __swig_setmethods__ = {}
    for _s in [Error]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, InvalidError, name, value)
    __swig_getmethods__ = {}
    for _s in [Error]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, InvalidError, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _kyototycoon.delete_InvalidError
    __del__ = lambda self : None;
InvalidError_swigregister = _kyototycoon.InvalidError_swigregister
InvalidError_swigregister(InvalidError)

class LogicError(Error):
    """Proxy of C++ kyototycoon::LogicError class"""
    __swig_setmethods__ = {}
    for _s in [Error]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, LogicError, name, value)
    __swig_getmethods__ = {}
    for _s in [Error]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, LogicError, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _kyototycoon.delete_LogicError
    __del__ = lambda self : None;
LogicError_swigregister = _kyototycoon.LogicError_swigregister
LogicError_swigregister(LogicError)

class TimeoutError(Error):
    """Proxy of C++ kyototycoon::TimeoutError class"""
    __swig_setmethods__ = {}
    for _s in [Error]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TimeoutError, name, value)
    __swig_getmethods__ = {}
    for _s in [Error]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, TimeoutError, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _kyototycoon.delete_TimeoutError
    __del__ = lambda self : None;
TimeoutError_swigregister = _kyototycoon.TimeoutError_swigregister
TimeoutError_swigregister(TimeoutError)

class InternalError(Error):
    """Proxy of C++ kyototycoon::InternalError class"""
    __swig_setmethods__ = {}
    for _s in [Error]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, InternalError, name, value)
    __swig_getmethods__ = {}
    for _s in [Error]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, InternalError, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _kyototycoon.delete_InternalError
    __del__ = lambda self : None;
InternalError_swigregister = _kyototycoon.InternalError_swigregister
InternalError_swigregister(InternalError)

class NetworkError(Error):
    """Proxy of C++ kyototycoon::NetworkError class"""
    __swig_setmethods__ = {}
    for _s in [Error]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NetworkError, name, value)
    __swig_getmethods__ = {}
    for _s in [Error]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, NetworkError, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _kyototycoon.delete_NetworkError
    __del__ = lambda self : None;
NetworkError_swigregister = _kyototycoon.NetworkError_swigregister
NetworkError_swigregister(NetworkError)

class MiscError(Error):
    """Proxy of C++ kyototycoon::MiscError class"""
    __swig_setmethods__ = {}
    for _s in [Error]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MiscError, name, value)
    __swig_getmethods__ = {}
    for _s in [Error]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, MiscError, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _kyototycoon.delete_MiscError
    __del__ = lambda self : None;
MiscError_swigregister = _kyototycoon.MiscError_swigregister
MiscError_swigregister(MiscError)

class Cursor(_object):
    """Proxy of C++ kyototycoon::Cursor class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Cursor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Cursor, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def set_value(self, *args, **kwargs):
        """
        set_value(self, string value, long long xt = max_ts, bool step = False) -> bool

        Set the value of the current record.

        :param value: the value of the record.
        :param step: (optional) to move the cursor to the next record. If it is omitted, the cursor stays at the current record.
        :param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
        """
        return _kyototycoon.Cursor_set_value(self, *args, **kwargs)

    def remove(self):
        """
        remove(self) -> bool

        Remove the current record.

        """
        return _kyototycoon.Cursor_remove(self)

    def get_key(self, step = False):
        """
        get_key(self, bool step = False) -> string

        Get the key of the current record.

        :param step: (optional) to move the cursor to the next record. If it is omitted, the cursor stays at the current record.
        """
        return _kyototycoon.Cursor_get_key(self, step)

    def get_value(self, step = False):
        """
        get_value(self, bool step = False) -> string

        Get the value of the current record.

        :param step: (optional) to move the cursor to the next record. If it is omitted, the cursor stays at the current record.
        """
        return _kyototycoon.Cursor_get_value(self, step)

    def jump(self, key = ""):
        """
        jump(self, string key = "") -> bool

        Jump the cursor to the first record for forward scan.

        :param key: (optional) the key of the destination record. If it is omitted, the first record is specified.
        """
        return _kyototycoon.Cursor_jump(self, key)

    def jump_back(self, key = ""):
        """
        jump_back(self, string key = "") -> bool

        Jump the cursor to a record for forward scan.

        :param key: (optional) the key of the destination record. If it is omitted, the last record is specified.
        """
        return _kyototycoon.Cursor_jump_back(self, key)

    def step(self):
        """
        step(self) -> bool

        Step the cursor to the next record.

        """
        return _kyototycoon.Cursor_step(self)

    def step_back(self):
        """
        step_back(self) -> bool

        Step the cursor to the previous record.

        """
        return _kyototycoon.Cursor_step_back(self)

    def error(self):
        """
        error(self) -> Error

        Get the last error encountered.

        :rtype: :py:class:`kyototycoon.kyototycoon.Error`
        """
        return _kyototycoon.Cursor_error(self)

    def get(self, step = False):
        """
        get(self, bool step = False) -> __dummy_5__

        Get a pair of the key and the value of the current record.

        :param step: (optional) to move the cursor to the next record. If it is omitted, the cursor stays at the current record.
        :returns: tuple (key, value) of the current record
        """
        return _kyototycoon.Cursor_get(self, step)

    __swig_destroy__ = _kyototycoon.delete_Cursor
    __del__ = lambda self : None;
Cursor_swigregister = _kyototycoon.Cursor_swigregister
Cursor_swigregister(Cursor)
cvar = _kyototycoon.cvar
max_ts = cvar.max_ts

class FileStatus(_object):
    """Proxy of C++ kyototycoon::FileStatus class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileStatus, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FileStatus, name)
    __repr__ = _swig_repr
    __swig_setmethods__["path"] = _kyototycoon.FileStatus_path_set
    __swig_getmethods__["path"] = _kyototycoon.FileStatus_path_get
    if _newclass:path = _swig_property(_kyototycoon.FileStatus_path_get, _kyototycoon.FileStatus_path_set)
    __swig_setmethods__["size"] = _kyototycoon.FileStatus_size_set
    __swig_getmethods__["size"] = _kyototycoon.FileStatus_size_get
    if _newclass:size = _swig_property(_kyototycoon.FileStatus_size_get, _kyototycoon.FileStatus_size_set)
    __swig_setmethods__["ts"] = _kyototycoon.FileStatus_ts_set
    __swig_getmethods__["ts"] = _kyototycoon.FileStatus_ts_get
    if _newclass:ts = _swig_property(_kyototycoon.FileStatus_ts_get, _kyototycoon.FileStatus_ts_set)
    def __init__(self): 
        """__init__(self) -> FileStatus"""
        this = _kyototycoon.new_FileStatus()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _kyototycoon.delete_FileStatus
    __del__ = lambda self : None;
FileStatus_swigregister = _kyototycoon.FileStatus_swigregister
FileStatus_swigregister(FileStatus)

class DB(_object):
    """Proxy of C++ kyototycoon::DB class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DB, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DB, name)
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, string database = kyototycoon::string("")) -> DB"""
        this = _kyototycoon.new_DB(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _kyototycoon.delete_DB
    __del__ = lambda self : None;
    def error(self):
        """
        error(self) -> Error

        Get the last error encountered.

        :rtype: :py:class:`kyototycoon.kyototycoon.Error`
        """
        return _kyototycoon.DB_error(self)

    def open(self, *args, **kwargs):
        """
        open(self, string host = "", long long port = 1978, double timeout = -1.0) -> bool

        Open the database connection

        :param host: hostname or ip address of database host
        :param port: the port at which the database server currently runs
        :param timeout: connectin timeout in secods

        :rtype: bool
        :returns: True on success, False otherwise.
        """
        return _kyototycoon.DB_open(self, *args, **kwargs)

    def close(self):
        """
        close(self) -> bool

        Close the database connection.

        :returns: True on success, False otherwise
        """
        return _kyototycoon.DB_close(self)

    def report(self):
        """
        report(self) -> Map

        Get the report of the server information.

        :returns: (optional) arbitrary records.
        """
        return _kyototycoon.DB_report(self)

    def play_script(self, *args, **kwargs):
        """
        play_script(self, string name, Map args) -> Map

        Call a procedure of the script language extension.

        :param name: the name of the procedure to call.
        :param args: arguments to the script
        :returns: (optional) arbitrary keys which trail the character "_".
        """
        return _kyototycoon.DB_play_script(self, *args, **kwargs)

    def tune_replication(self, *args, **kwargs):
        """
        tune_replication(self, string host = "", int32_t port = 1978, long long ts = max_ts, 
            double iv = -1) -> bool

        Set the replication configuration.

        :param host: (optional) the name or the address of the master server. If it is omitted, replication is disabled.
        :param port: (optional) the port numger of the server. If it is omitted, the default port is specified.
        :param ts: (optional) the maximum time stamp of already read logs. If it is omitted, the current setting is not modified. If it is "now", the current time is specified.
        :param iv: (optional) the interval of each replication operation in milliseconds. If it is omitted, the current setting is not modified.
        """
        return _kyototycoon.DB_tune_replication(self, *args, **kwargs)

    def ulog_list(self):
        """ulog_list(self) -> FileStatusList"""
        return _kyototycoon.DB_ulog_list(self)

    def ulog_remove(self, *args, **kwargs):
        """ulog_remove(self, long long ts = max_ts) -> bool"""
        return _kyototycoon.DB_ulog_remove(self, *args, **kwargs)

    def status(self):
        """
        status(self) -> Map

        Get the miscellaneous status information of a database.

        :returns: count: the number of records.
        :returns: size: the size of the database file.
        :returns: (optional) arbitrary records for other information.
        """
        return _kyototycoon.DB_status(self)

    def clear(self):
        """
        clear(self) -> bool

        Remove all records in a database.

        """
        return _kyototycoon.DB_clear(self)

    def count(self):
        """
        count(self) -> long long

        Get the number of records in the database.

        :returns: number of records in the database
        """
        return _kyototycoon.DB_count(self)

    def size(self):
        """size(self) -> long long"""
        return _kyototycoon.DB_size(self)

    def set(self, *args, **kwargs):
        """
        set(self, string key, string value, long long xt = max_ts) -> bool

        Set the value of a record.

        :param key: the key of the record.
        :param value: the value of the record.
        :param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
        """
        return _kyototycoon.DB_set(self, *args, **kwargs)

    def add(self, *args, **kwargs):
        """
        add(self, string key, string value, long long xt = max_ts) -> bool

        Add a record.

        :param key: the key of the record.
        :param value: the value of the record.
        :param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
        """
        return _kyototycoon.DB_add(self, *args, **kwargs)

    def replace(self, *args, **kwargs):
        """
        replace(self, string key, string value, long long xt = max_ts) -> bool

        Replace the value of a record.

        :param key: the key of the record.
        :param value: the value of the record.
        :param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
        """
        return _kyototycoon.DB_replace(self, *args, **kwargs)

    def append(self, *args, **kwargs):
        """
        append(self, string key, string value, long long xt = max_ts) -> bool

        Append the value of a record.

        :param key: the key of the record.
        :param value: the value of the record.
        :param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
        """
        return _kyototycoon.DB_append(self, *args, **kwargs)

    def increment(self, *args, **kwargs):
        """
        increment(self, string key, long long num = 1, long long orig = 0, 
            long long xt = max_ts) -> long long

        Add a number to the numeric integer value of a record.

        :param key: the key of the record.
        :param num: the additional number.
        :param orig: (optional) the origin number. If it is omitted, 0 is specified. "try" means INT64MIN. "set" means INT64MAX.
        :param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
        :returns: num: the result value.
        """
        return _kyototycoon.DB_increment(self, *args, **kwargs)

    def increment_double(self, *args, **kwargs):
        """
        increment_double(self, string key, double num = 1.0, double orig = 0.0, long long xt = max_ts) -> double

        Add a number to the numeric double value of a record.

        :param key: the key of the record.
        :param num: the additional number.
        :param orig: (optional) the origin number. If it is omitted, 0 is specified. "try" means negative infinity. "set" means positive infinity.
        :param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
        :returns: num: the result value.
        """
        return _kyototycoon.DB_increment_double(self, *args, **kwargs)

    def cas(self, *args, **kwargs):
        """
        cas(self, string key, string oval = "", string nval = "", long long xt = max_ts) -> bool

        Perform compare-and-swap.

        :param key: the key of the record.
        :param oval: (optional) the old value. If it is omittted, no record is meant.
        :param nval: (optional) the new value. If it is omittted, the record is removed.
        :param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
        """
        return _kyototycoon.DB_cas(self, *args, **kwargs)

    def remove(self, *args, **kwargs):
        """
        remove(self, string key) -> bool

        Remove a record.

        :param key: the key of the record.
        """
        return _kyototycoon.DB_remove(self, *args, **kwargs)

    def get(self, *args, **kwargs):
        """
        get(self, string key) -> string

        Retrieve the value of a record.

        :param key: the key of the record.
        :returns: value: (optional) the value of the record.
        :returns: the value of the record
        """
        return _kyototycoon.DB_get(self, *args, **kwargs)

    def seize(self, *args, **kwargs):
        """
        seize(self, string key) -> string

        Retrieve the value of a record and remove it atomically.

        :param key: the key of the record.
        :returns: value: (optional) the value of the record.
        :returns: xt: (optional) the absolute expiration time. If it is omitted, there is no expiration time.
        """
        return _kyototycoon.DB_seize(self, *args, **kwargs)

    def set_bulk(self, *args, **kwargs):
        """
        set_bulk(self, Map recs, long long xt = max_ts, bool atomic = True) -> long long

        Store records at once.

        :param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
        :param atomic: (optional) to perform all operations atomically. If it is omitted, non-atomic operations are performed.
        :param recs: dictionary (key=>value) of records to set
        :returns: num: the number of stored reocrds.
        """
        return _kyototycoon.DB_set_bulk(self, *args, **kwargs)

    def remove_bulk(self, *args, **kwargs):
        """
        remove_bulk(self, List keys, bool atomic = True) -> long long

        Store records at once.

        :param atomic: (optional) to perform all operations atomically. If it is omitted, non-atomic operations are performed.
        :param keys: list of keys of the records to remove
        :returns: num: the number of removed reocrds.
        """
        return _kyototycoon.DB_remove_bulk(self, *args, **kwargs)

    def get_bulk(self, *args, **kwargs):
        """
        get_bulk(self, List keys, bool atomic = True) -> Map

        Retrieve records at once.

        :param atomic: (optional) to perform all operations atomically. If it is omitted, non-atomic operations are performed.
        :param keys: list of keys of the records to retrieve
        :returns: num: the number of retrieved reocrds.
        :returns: dictionary (key=>value) of records
        """
        return _kyototycoon.DB_get_bulk(self, *args, **kwargs)

    def vacuum(self, *args, **kwargs):
        """
        vacuum(self, long long steps) -> bool

        Scan the database and eliminate regions of expired records.

        :param step: (optional) the number of steps. If it is omitted or not more than 0, the whole region is scanned.
        """
        return _kyototycoon.DB_vacuum(self, *args, **kwargs)

    def match_prefix(self, *args, **kwargs):
        """
        match_prefix(self, string prefix, long long max = -1) -> List

        Get keys matching a prefix string.

        :param prefix: the prefix string.
        :param max: (optional) the maximum number to retrieve. If it is omitted or negative, no limit is specified.
        :returns: num: the number of retrieved keys.
        :returns: (optional) arbitrary keys which trail the character "_". Each value specifies the order of the key.
        """
        return _kyototycoon.DB_match_prefix(self, *args, **kwargs)

    def match_regex(self, *args, **kwargs):
        """
        match_regex(self, string regex, long long max = -1) -> List

        Get keys matching a ragular expression string.

        :param regex: the regular expression string.
        :param max: (optional) the maximum number to retrieve. If it is omitted or negative, no limit is specified.
        :returns: num: the number of retrieved keys.
        :returns: (optional) arbitrary keys which trail the character "_". Each value specifies the order of the key.
        """
        return _kyototycoon.DB_match_regex(self, *args, **kwargs)

    def match_similar(self, *args, **kwargs):
        """
        match_similar(self, string origin, long long range, bool utf, long long max = -1) -> List

        Get keys similar to a string in terms of the levenshtein distance.

        :param origin: the origin string.
        :param range: (optional) the maximum distance of keys to adopt. If it is omitted or negative, 1 is specified.
        :param utf: (optional) flag to treat keys as UTF-8 strings. If it is omitted, false is specified.
        :param max: (optional) the maximum number to retrieve. If it is omitted or negative, no limit is specified.
        :returns: num: the number of retrieved keys.
        :returns: (optional) arbitrary keys which trail the character "_". Each value specifies the order of the key.
        """
        return _kyototycoon.DB_match_similar(self, *args, **kwargs)

    def set_target(self, *args, **kwargs):
        """
        set_target(self, string expr)

        Get the size of the current database in bytes

        :returns: the databases size in bytes.

        """
        return _kyototycoon.DB_set_target(self, *args, **kwargs)

    def expression(self):
        """
        expression(self) -> string

        Get current database connection expression.

        :rtype: string
        """
        return _kyototycoon.DB_expression(self)

    def cursor(self):
        """
        cursor(self) -> ptr

        Creates a new cursor.

        :rtype: :py:class:`kyototycoon.kyototycoon.Cursor`
        """
        return _kyototycoon.DB_cursor(self)

    def __getitem__(self, *args, **kwargs):
        """__getitem__(self, string key) -> string"""
        return _kyototycoon.DB___getitem__(self, *args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        """__setitem__(self, string key, string value)"""
        return _kyototycoon.DB___setitem__(self, *args, **kwargs)

    def ll_max():
        """
        ll_max() -> long long

        Get the max value of long long.

        :rtype: long long
        """
        return _kyototycoon.DB_ll_max()

    if _newclass:ll_max = staticmethod(ll_max)
    __swig_getmethods__["ll_max"] = lambda x: ll_max
    def get_target(self):
        """
        get_target(self) -> string

        Get current database name.

        :rtype: string
        """
        return _kyototycoon.DB_get_target(self)

    __swig_getmethods__["db"] = get_target
    __swig_setmethods__["db"] = set_target
    if _newclass: db = property(get_target, set_target)

DB_swigregister = _kyototycoon.DB_swigregister
DB_swigregister(DB)

def DB_ll_max():
  """
    DB_ll_max() -> long long

    Get the max value of long long.

    :rtype: long long
    """
  return _kyototycoon.DB_ll_max()

''' compatibility alias '''
KyotoTycoon = DB

# This file is compatible with both classic and new-style classes.

