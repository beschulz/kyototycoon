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

#include "./wrapper.hpp"

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

	bool Cursor::set_value(const string& value, const long long xt, const bool step)
	{
		return pimpl->set_value_str(value, xt, step);
	}
	
	bool Cursor::remove()
	{
		return pimpl->remove();
	}

	string Cursor::get_key(const bool step) throw(Error)
	{
		string ret;
		if (!pimpl->get_key(&ret, step)) Error::translate( pimpl->error() );
		return ret;
	}

	string Cursor::get_value(const bool step) throw(Error)
	{
		string ret;
		if (!pimpl->get_value(&ret, step)) Error::translate( pimpl->error() );
		return ret;
	}

	bool Cursor::jump(const string key)
	{
		if (key.empty()) return pimpl->jump();
		else             return pimpl->jump(key);
	}

	bool Cursor::jump_back(const string key)
	{
		if (key.empty()) return pimpl->jump_back();
		else             return pimpl->jump_back(key);
	}

	bool Cursor::step()
	{
		return pimpl->step();
	}
	
	bool Cursor::step_back()
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

	bool DB::open(const string& host, const long long port, const double timeout)
	{
		return pimpl->open(host, (int32_t)port, timeout);
	}

	bool DB::close()
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

	bool DB::tune_replication(const string& host, const int32_t port, const long long ts, const double iv)
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
	
	bool DB::ulog_remove(const long long ts)
	{
		return pimpl->ulog_remove(ts);
	}
	
	Map DB::status() throw(Error)
	{
		Map ret;
		if (!pimpl->status(&ret)) Error::translate( pimpl->error() );
		return ret;
	}
	
	bool DB::clear()
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

	bool DB::set(const string& key, const string& value, const long long xt)
	{
		return pimpl->set(key, value, xt);
	}

	bool DB::add(const string& key, const string& value, const long long xt)
	{
		return pimpl->add(key, value, xt);
	}

	bool DB::replace(const string& key, const string& value, const long long xt)
	{
		return pimpl->replace(key, value, xt);
	}

	bool DB::append(const string& key, const string& value, const long long xt)
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

	bool DB::cas(const string& key, const string& oval, const string& nval, const long long xt)
	{
		return pimpl->cas(key.c_str(), key.size(),
            		oval.empty()?0:oval.c_str(), oval.size(),
					nval.empty()?0:nval.c_str(), nval.size(), xt);
		//return pimpl->cas(key, oval, nval, xt);
	}

	bool DB::remove(const string& key)
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

	bool DB::vacuum(const long long steps)
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

	List DB::match_similar(const string origin, const long long range, const bool utf, const long long max) throw(Error)
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