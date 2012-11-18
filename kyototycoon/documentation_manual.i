/*
 * This file is part of the kyototycoon SWIG binding.
 *
 * Copyright(c) Benjamin Schulz (beschulz[the a with the stuff]betabugs.de)
 * https://github.com/beschulz/kyototycoon
 *
 * This file may be licensed under the terms of of the
 * GNU General Public License Version 2 (the ``GPL'').
 *
 * Software distributed under the License is distributed
 * on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
 * express or implied. See the GPL for the specific language
 * governing rights and limitations.
 *
 * You should have received a copy of the GPL along with this
 * program. If not, go to http://www.gnu.org/licenses/gpl.html
 * or write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 */

%feature("docstring", "Close the database connection.

:returns: True on success, False otherwise") kyototycoon::DB::close;



%feature("docstring", "Get the number of records in the database.

:returns: number of records in the database") kyototycoon::DB::count;



%feature("docstring", "Creates a new cursor.

:rtype: :py:class:`kyototycoon.kyototycoon.Cursor`") kyototycoon::DB::cursor;




%feature("docstring", "Get the last error encountered.

:rtype: :py:class:`kyototycoon.kyototycoon.Error`") kyototycoon::DB::error;



%feature("docstring", "Get the last error encountered.

:rtype: :py:class:`kyototycoon.kyototycoon.Error`") kyototycoon::Cursor::error;




%feature("docstring", "Get current database connection expression.

:rtype: string") kyototycoon::DB::expression;



%feature("docstring", "Get current database name.

:rtype: string") kyototycoon::DB::get_target;



%feature("docstring", "Get the max value of long long.

:rtype: long long") kyototycoon::DB::ll_max;


%feature("docstring", "Open the database connection

:param host: hostname or ip address of database host
:param port: the port at which the database server currently runs
:param timeout: connectin timeout in secods

:rtype: bool
:returns: True on success, False otherwise.") kyototycoon::DB::open;



%feature("docstring", "Sets the database name

:param expr: database expression
") kyototycoon::DB::set_target;



%feature("docstring", "Get the size of the current database in bytes

:returns: the databases size in bytes.
") kyototycoon::DB::set_target;


%feature("docstring", "Path of the file

") kyototycoon::FileStatus::path;




%feature("docstring", "Size of the file

") kyototycoon::FileStatus::size;



%feature("docstring", "Time stamp of the file

") kyototycoon::FileStatus::ts;






%feature("docstring", "Base class for all exceptions

") kyototycoon::Error;
