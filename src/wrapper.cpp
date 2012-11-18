#include "wrapper.hpp"

namespace kyototycoon
{

	//----------------------------------------------------------------
	// error information
	//----------------------------------------------------------------
	Error::Error(const RemoteDB::Error& o)
	:pimpl(o) {}

	Error::Code Error::code() const
	{
		return Error::Code( pimpl.code() );
	}

	string Error::name() const
	{
		return pimpl.name();
	}

	string Error::message() const
	{
		return pimpl.message();
	}

	string Error::type() const
	{
		switch(code())
		{
			case SUCCESS : return "NoError";
			case NOIMPL  : return "NotImplementedError";
			case INVALID : return "InvalidError";
			case LOGIC   : return "LogicError";
			case TIMEOUT : return "TimeoutError";
			case INTERNAL: return "InternalError";
			case NETWORK : return "NetworkError";
			case EMISC   : return "MiscError";
			default : return "Error";
		}
	}

	void Error::translate(RemoteDB::Error e)
	{
		switch(e.code())
		{
			//case SUCCESS : return "NoError";
			case NOIMPL  : throw NotImplementedError(e);
			case INVALID : throw InvalidError(e);
			case LOGIC   : throw LogicError(e);
			case TIMEOUT : throw TimeoutError(e);
			case INTERNAL: throw InternalError(e);
			case NETWORK : throw NetworkError(e);
			case EMISC   : throw MiscError(e);
			default      : throw Error(e);
		}
	}


	//----------------------------------------------------------------
	// cursor
	//----------------------------------------------------------------
	Cursor::Cursor( RemoteDB::Cursor* o )
	:pimpl(o)
	{}

	boolean Cursor::set_value(const string& value, const long long xt, const boolean step)
	{
		return pimpl->set_value_str(value, xt, step);
	}
	
	boolean Cursor::remove()
	{
		return pimpl->remove();
	}

	string Cursor::get_key(const boolean step) throw(Error)
	{
		string ret;
		if (!pimpl->get_key(&ret, step)) Error::translate( pimpl->error() );
		return ret;
	}

	string Cursor::get_value(const boolean step) throw(Error)
	{
		string ret;
		if (!pimpl->get_value(&ret, step)) Error::translate( pimpl->error() );
		return ret;
	}

	boolean Cursor::jump(const string key)
	{
		if (key.empty()) return pimpl->jump();
		else             return pimpl->jump(key);
	}

	boolean Cursor::jump_back(const string key)
	{
		if (key.empty()) return pimpl->jump_back();
		else             return pimpl->jump_back(key);
	}

	boolean Cursor::step()
	{
		return pimpl->step();
	}
	
	boolean Cursor::step_back()
	{
		return pimpl->step_back();
	}
	
	/*DB Cursor::db()
	{
		//return pimpl->
	}*/

	Error Cursor::error()
	{
		return Error(pimpl->error());
	}


	//DB::DB() :pimpl( new RemoteDB() ) {}

	DB::DB(const string& database)
	:pimpl( new RemoteDB() )
	{
		this->set_target(database);
	}

	DB::~DB()
	{

	}

	Error DB::error()
	{
		return Error( pimpl->error() );
	}

	boolean DB::open(const string& host, const int32_t port, const double timeout)
	{
		return pimpl->open(host, port, timeout);
	}

	boolean DB::close()
	{
		return pimpl->close();
	}

	Map DB::report() throw(Error)
	{
		Map ret;
		if (!pimpl->report(&ret)) Error::translate( pimpl->error() );
		return ret;
	}

	Map DB::play_script(const string& name, const Map& args) throw(Error)
	{
		Map result;
		if (!pimpl->play_script(name, args, &result)) Error::translate( pimpl->error() );
		return result;
	}

	boolean DB::tune_replication(const string& host, const int32_t port, const long long ts, const double iv)
	{
		return pimpl->tune_replication(host, port, ts, iv);
	}

	FileStatusList DB::ulog_list() throw(Error)
	{
		std::vector<UpdateLogger::FileStatus> tmp;
		if (!pimpl->ulog_list(&tmp)) Error::translate( pimpl->error() );

		FileStatusList ret;
		for (std::vector<UpdateLogger::FileStatus>::const_iterator i = tmp.begin(); i != tmp.end(); ++i)
		{
			FileStatus fs;
			fs.path = i->path;
			fs.size = i->size;
			fs.ts = i->ts;
			ret.push_back(fs);
		}
		return ret;
	}
	
	boolean DB::ulog_remove(const long long ts)
	{
		return pimpl->ulog_remove(ts);
	}
	
	Map DB::status() throw(Error)
	{
		Map ret;
		if (!pimpl->status(&ret)) Error::translate( pimpl->error() );
		return ret;
	}
	
	boolean DB::clear()
	{
		return pimpl->clear();
	}
	
	long long DB::count()
	{
		return pimpl->count();
	}
	
	long long DB::size()
	{
		return pimpl->size();
	}

	boolean DB::set(const string& key, const string& value, const long long xt)
	{
		return pimpl->set(key, value, xt);
	}

	boolean DB::add(const string& key, const string& value, const long long xt)
	{
		return pimpl->add(key, value, xt);
	}

	boolean DB::replace(const string& key, const string& value, const long long xt)
	{
		return pimpl->replace(key, value, xt);
	}

	boolean DB::append(const string& key, const string& value, const long long xt)
	{
		return pimpl->append(key, value, xt);
	}

	long long DB::increment(const string& key, const long long num, const long long orig, const long long xt)
	{
		return pimpl->increment(key, num, orig, xt);
	}

	double DB::increment_double(const string& key, const double num, const double orig, const long long xt)
	{
		return pimpl->increment_double(key, num, orig, xt);
	}

	boolean DB::cas(const string& key, const string& oval, const string& nval, const long long xt)
	{
		return pimpl->cas(key.c_str(), key.size(),
            		oval.empty()?0:oval.c_str(), oval.size(),
					nval.empty()?0:nval.c_str(), nval.size(), xt);
		//return pimpl->cas(key, oval, nval, xt);
	}

	boolean DB::remove(const string& key)
	{
		return pimpl->remove(key);
	}

	string DB::get(const string& key) throw(Error)
	{
		string ret;
		if (!pimpl->get(key, &ret)) Error::translate( pimpl->error() );
		return ret;
	}

	string DB::seize(const string& key) throw(Error)
	{
		string ret;
		if (!pimpl->seize(key, &ret)) Error::translate( pimpl->error() );
		return ret;
	}

	long long DB::set_bulk(const Map& recs, const long long xt, bool atomic)
	{
		return pimpl->set_bulk(recs, xt, atomic);
	}

	long long DB::remove_bulk(const List keys, bool atomic)
	{
		return pimpl->remove_bulk(keys, atomic);
	}

	Map DB::get_bulk(const List& keys, bool atomic) throw(Error)
	{
		Map ret;
		pimpl->get_bulk(keys, &ret, atomic);
		return ret;
	}

	boolean DB::vacuum(const long long steps)
	{
		return pimpl->vacuum(steps);
	}

	List DB::match_prefix(const string prefix, const long long max) throw(Error)
	{
		List ret;
		pimpl->match_prefix(prefix, &ret, max);
		return ret;
	}

	List DB::match_regex(const string regex, const long long max) throw(Error)
	{
		List ret;
		pimpl->match_regex(regex, &ret, max);
		return ret;
	}

	List DB::match_similar(const string origin, const long long range, const boolean utf, const long long max) throw(Error)
	{
		List ret;
		pimpl->match_similar(origin, range, utf, &ret, max);
		return ret;
	}

	void DB::set_target(const string expr)
	{
		dbexpr_ = expr;
		return pimpl->set_target(expr);
	}

	string DB::expression()
	{
		return pimpl->expression();
	}

	Cursor::ptr DB::cursor()
	{
		return Cursor::ptr( new Cursor(pimpl->cursor()) );
	}
}