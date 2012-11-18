%feature("docstring", "Echo back the input data as the output data, just for testing.

:param (optional) arbitrary records.
:returns: (optional) corresponding records to the input data.") kyototycoon::DB::echo;



%feature("docstring", "Get the report of the server information.

:returns: (optional) arbitrary records.") kyototycoon::DB::report;



%feature("docstring", "Call a procedure of the script language extension.

:param name: the name of the procedure to call.
:param args: arguments to the script
:returns: (optional) arbitrary keys which trail the character \"_\".") kyototycoon::DB::play_script;



%feature("docstring", "Set the replication configuration.

:param host: (optional) the name or the address of the master server. If it is omitted, replication is disabled.
:param port: (optional) the port numger of the server. If it is omitted, the default port is specified.
:param ts: (optional) the maximum time stamp of already read logs. If it is omitted, the current setting is not modified. If it is \"now\", the current time is specified.
:param iv: (optional) the interval of each replication operation in milliseconds. If it is omitted, the current setting is not modified.") kyototycoon::DB::tune_replication;



%feature("docstring", "Get the miscellaneous status information of a database.

:returns: count: the number of records.
:returns: size: the size of the database file.
:returns: (optional) arbitrary records for other information.") kyototycoon::DB::status;



%feature("docstring", "Remove all records in a database.
") kyototycoon::DB::clear;



%feature("docstring", "Synchronize updated contents with the file and the device.

:param hard: (optional) for physical synchronization with the device.
:param command: (optional) the command name to process the database file.") kyototycoon::DB::synchronize;



%feature("docstring", "Set the value of a record.

:param key: the key of the record.
:param value: the value of the record.
:param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.") kyototycoon::DB::set;



%feature("docstring", "Add a record.

:param key: the key of the record.
:param value: the value of the record.
:param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.") kyototycoon::DB::add;



%feature("docstring", "Replace the value of a record.

:param key: the key of the record.
:param value: the value of the record.
:param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.") kyototycoon::DB::replace;



%feature("docstring", "Append the value of a record.

:param key: the key of the record.
:param value: the value of the record.
:param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.") kyototycoon::DB::append;



%feature("docstring", "Add a number to the numeric integer value of a record.

:param key: the key of the record.
:param num: the additional number.
:param orig: (optional) the origin number. If it is omitted, 0 is specified. \"try\" means INT64MIN. \"set\" means INT64MAX.
:param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
:returns: num: the result value.") kyototycoon::DB::increment;



%feature("docstring", "Add a number to the numeric double value of a record.

:param key: the key of the record.
:param num: the additional number.
:param orig: (optional) the origin number. If it is omitted, 0 is specified. \"try\" means negative infinity. \"set\" means positive infinity.
:param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
:returns: num: the result value.") kyototycoon::DB::increment_double;



%feature("docstring", "Perform compare-and-swap.

:param key: the key of the record.
:param oval: (optional) the old value. If it is omittted, no record is meant.
:param nval: (optional) the new value. If it is omittted, the record is removed.
:param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.") kyototycoon::DB::cas;



%feature("docstring", "Remove a record.

:param key: the key of the record.") kyototycoon::DB::remove;



%feature("docstring", "Retrieve the value of a record.

:param key: the key of the record.
:returns: value: (optional) the value of the record.
:returns: the value of the record") kyototycoon::DB::get;



%feature("docstring", "Check the existence of a record.

:param key: the key of the record.
:returns: vsiz: (optional) the size of the value of the record.
:returns: xt: (optional) the absolute expiration time. If it is omitted, there is no expiration time.") kyototycoon::DB::check;



%feature("docstring", "Retrieve the value of a record and remove it atomically.

:param key: the key of the record.
:returns: value: (optional) the value of the record.
:returns: xt: (optional) the absolute expiration time. If it is omitted, there is no expiration time.") kyototycoon::DB::seize;



%feature("docstring", "Store records at once.

:param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.
:param atomic: (optional) to perform all operations atomically. If it is omitted, non-atomic operations are performed.
:param recs: dictionary (key=>value) of records to set
:returns: num: the number of stored reocrds.") kyototycoon::DB::set_bulk;



%feature("docstring", "Store records at once.

:param atomic: (optional) to perform all operations atomically. If it is omitted, non-atomic operations are performed.
:param keys: list of keys of the records to remove
:returns: num: the number of removed reocrds.") kyototycoon::DB::remove_bulk;



%feature("docstring", "Retrieve records at once.

:param atomic: (optional) to perform all operations atomically. If it is omitted, non-atomic operations are performed.
:param keys: list of keys of the records to retrieve
:returns: num: the number of retrieved reocrds.
:returns: dictionary (key=>value) of records") kyototycoon::DB::get_bulk;



%feature("docstring", "Scan the database and eliminate regions of expired records.

:param step: (optional) the number of steps. If it is omitted or not more than 0, the whole region is scanned.") kyototycoon::DB::vacuum;



%feature("docstring", "Get keys matching a prefix string.

:param prefix: the prefix string.
:param max: (optional) the maximum number to retrieve. If it is omitted or negative, no limit is specified.
:returns: num: the number of retrieved keys.
:returns: (optional) arbitrary keys which trail the character \"_\". Each value specifies the order of the key.") kyototycoon::DB::match_prefix;



%feature("docstring", "Get keys matching a ragular expression string.

:param regex: the regular expression string.
:param max: (optional) the maximum number to retrieve. If it is omitted or negative, no limit is specified.
:returns: num: the number of retrieved keys.
:returns: (optional) arbitrary keys which trail the character \"_\". Each value specifies the order of the key.") kyototycoon::DB::match_regex;



%feature("docstring", "Get keys similar to a string in terms of the levenshtein distance.

:param origin: the origin string.
:param range: (optional) the maximum distance of keys to adopt. If it is omitted or negative, 1 is specified.
:param utf: (optional) flag to treat keys as UTF-8 strings. If it is omitted, false is specified.
:param max: (optional) the maximum number to retrieve. If it is omitted or negative, no limit is specified.
:returns: num: the number of retrieved keys.
:returns: (optional) arbitrary keys which trail the character \"_\". Each value specifies the order of the key.") kyototycoon::DB::match_similar;



%feature("docstring", "Jump the cursor to the first record for forward scan.

:param key: (optional) the key of the destination record. If it is omitted, the first record is specified.") kyototycoon::Cursor::jump;



%feature("docstring", "Jump the cursor to a record for forward scan.

:param key: (optional) the key of the destination record. If it is omitted, the last record is specified.") kyototycoon::Cursor::jump_back;



%feature("docstring", "Step the cursor to the next record.
") kyototycoon::Cursor::step;



%feature("docstring", "Step the cursor to the previous record.
") kyototycoon::Cursor::step_back;



%feature("docstring", "Set the value of the current record.

:param value: the value of the record.
:param step: (optional) to move the cursor to the next record. If it is omitted, the cursor stays at the current record.
:param xt: (optional) the expiration time from now in seconds. If it is negative, the absolute value is treated as the epoch time. If it is omitted, no expiration time is specified.") kyototycoon::Cursor::set_value;



%feature("docstring", "Remove the current record.
") kyototycoon::Cursor::remove;



%feature("docstring", "Get the key of the current record.

:param step: (optional) to move the cursor to the next record. If it is omitted, the cursor stays at the current record.") kyototycoon::Cursor::get_key;



%feature("docstring", "Get the value of the current record.

:param step: (optional) to move the cursor to the next record. If it is omitted, the cursor stays at the current record.") kyototycoon::Cursor::get_value;



%feature("docstring", "Get a pair of the key and the value of the current record.

:param step: (optional) to move the cursor to the next record. If it is omitted, the cursor stays at the current record.
:returns: tuple (key, value) of the current record") kyototycoon::Cursor::get;



%feature("docstring", "Get a pair of the key and the value of the current record and remove it atomically.

:returns: xt: (optional) the absolute expiration time. If it is omitted, there is no expiration time.") kyototycoon::Cursor::seize;



