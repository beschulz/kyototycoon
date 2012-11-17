%feature("docstring", "Close the database connection.

:returns: True on success, False otherwise") kyototycoon::DB::close;



%feature("docstring", "Get the number of records in the database.

:returns: number of records in the database") kyototycoon::DB::count;



%feature("docstring", "Creates a new cursor.

:returns: the new cursor") kyototycoon::DB::cursor;




%feature("docstring", "Get the last error encountered.

:rtype: :py:class:`Error`") kyototycoon::DB::error;




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
