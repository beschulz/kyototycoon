%module kyototycoon
%{
/* Includes the header in the wrapper code */
#include "wrapper.hpp"
%}

%include <typemaps.i>
%include <std_string.i>
%include <std_vector.i>
%include <std_map.i>
%include <std_pair.i>
%include <exception.i>

#define SWIG_SHARED_PTR_SUBNAMESPACE tr1
%include <std_shared_ptr.i>
%shared_ptr(kyototycoon::Cursor)

namespace std {
	%template() vector<FileStatus>;
	%template() vector<string>;
	%template() map<string, string>;
	%template() pair<string, string>;
}

%extend kyototycoon::DB
{
	%pythoncode
	%{
		__swig_getmethods__["db"] = get_target
		__swig_setmethods__["db"] = set_target
		if _newclass: db = property(get_target, set_target)
	%}
};

%feature("autodoc", "1");
%include "documentation.i"
%include "documentation_manual.i"

/* Parse the header file to generate wrappers */
%include "wrapper.hpp"

%nodefaultctor Error;
%nodefaultctor NoError;
%nodefaultctor NotImplementedError;
%nodefaultctor InvalidError;
%nodefaultctor LogicError;
%nodefaultctor TimeoutError;
%nodefaultctor InternalError;
%nodefaultctor NetworkError;
%nodefaultctor MiscError;

%nodefaultctor Cursor;
%pythoncode %{
	''' compatibility alias '''
	KyotoTycoon = DB
%}
