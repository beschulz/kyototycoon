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

#include <string>
#include <vector>
#include <map>
#include <tr1/memory>
#ifdef __APPLE__
#       include <tr1/boost_shared_ptr.h>
#else
#       include <tr1/shared_ptr.h>
#endif /* __APPLE__ */
#include <unistd.h>
#include <ktremotedb.h>
//#	include "../myconf.h"

template <typename T>
struct pimpl_ptr
{
#if __cplusplus > 199711L
	typedef std::unique_ptr<T> type;
#else
	typedef std::auto_ptr<T> type;
#endif
};

/**
 * namespace of Kyoto Tycoon
 */
namespace kyototycoon {
	//----------------------------------------------------------------
	// prediction
	//----------------------------------------------------------------
	//class List;
	//class Map;
	class Error;
	class Cursor;
	class DB;

	typedef std::string string;
	//typedef bool bool;

	//----------------------------------------------------------------
	// list of strings (substituted by the native mechanism)
	//----------------------------------------------------------------
	/*class List {
		string get(const long index);
	};*/
	typedef std::vector<string> List;
	//----------------------------------------------------------------
	// map of strings (substituted by the native mechanism)
	//----------------------------------------------------------------
	/*class Map {
		string get(const string key);
	};*/
	typedef std::map<string, string> Map;
	//----------------------------------------------------------------
	// error information
	//----------------------------------------------------------------
	class Error
	{
		protected:
			RemoteDB::Error pimpl;
			friend class DB;
			friend class Cursor;
			Error(const RemoteDB::Error& o);
			string type() const;
			static void translate(RemoteDB::Error e);
		public:
			enum Code
			{
				SUCCESS = 0,
				NOIMPL = 1,
				INVALID  = 2,
				LOGIC = 3,
				TIMEOUT = 4,
				INTERNAL = 5,
				NETWORK = 6,
				EMISC = 15
			};
			Code code() const;
			string name() const;
			string message() const;

			string __str__()
			{
				return "<" + type() + ":" + name() + ":" + message() + ">";
			}
	};

	class NoError : public Error
	{
		friend class Error;
		NoError(const RemoteDB::Error& o) : Error(o){};
	};

	class NotImplementedError : public Error
	{
		friend class Error;
		NotImplementedError(const RemoteDB::Error& o) : Error(o){};
	};

	class InvalidError : public Error
	{
		friend class Error;
		InvalidError(const RemoteDB::Error& o) : Error(o){};
	};

	class LogicError : public Error
	{
		friend class Error;
		LogicError(const RemoteDB::Error& o) : Error(o){};
	};

	class TimeoutError : public Error
	{
		friend class Error;
		TimeoutError(const RemoteDB::Error& o) : Error(o){};
	};

	class InternalError : public Error
	{
		friend class Error;
		InternalError(const RemoteDB::Error& o) : Error(o){};
	};

	class NetworkError : public Error
	{
		friend class Error;
		NetworkError(const RemoteDB::Error& o) : Error(o){};
	};

	class MiscError : public Error
	{
		friend class Error;
		MiscError(const RemoteDB::Error& o) : Error(o){};
	};


	static const long long max_ts = std::numeric_limits<long long>::max();
	//----------------------------------------------------------------
	// cursor
	//----------------------------------------------------------------
	class Cursor
	{
			friend class DB;

			pimpl_ptr<RemoteDB::Cursor>::type pimpl;
			Cursor( RemoteDB::Cursor* o );
		public:
			typedef std::tr1::shared_ptr<Cursor> ptr;

			bool set_value(const string& value, const long long xt=max_ts, const bool step=false);
			bool remove();
			string get_key(const bool step=false) throw(Error);
			string get_value(const bool step=false) throw(Error);
			bool jump(const string key="");
			bool jump_back(const string key="");
			bool step();
			bool step_back();
			//DB db();
			Error error();

			//extensions
			std::pair<string, string> get(bool step=false)
			{
				return std::make_pair(get_key(step), get_value(false));
			}
	};

	struct FileStatus
	{
		std::string path;                    ///< path
		uint64_t size;                       ///< file size
		uint64_t ts;                         ///< maximum time stamp
	};

	typedef std::vector<FileStatus> FileStatusList;

	//----------------------------------------------------------------
	// common database operations
	//----------------------------------------------------------------
	class DB
	{
			pimpl_ptr<RemoteDB>::type pimpl;
			string dbexpr_;
		public:
			//DB();
			explicit DB(const string& database=string(""));
			~DB();

			Error error();
			bool open(const string& host="", const long long port=1978, const double timeout=-1.0);
			bool close();
			Map report() throw(Error);
			Map play_script(const string& name, const Map& args) throw(Error);
			bool tune_replication(
				const string& host="",
				const int32_t port=1978,
				const long long ts=max_ts,
				const double iv=-1);
			FileStatusList ulog_list() throw(Error);
			bool ulog_remove(const long long ts=max_ts);
			Map status() throw(Error);
			bool clear();
			long long count();
			long long size();
			bool set(const string& key, const string& value, const long long xt=max_ts);
			bool add(const string& key, const string& value, const long long xt=max_ts);
			bool replace(const string& key, const string& value, const long long xt=max_ts);
			bool append(const string& key, const string& value, const long long xt=max_ts);
			long long increment(const string& key, const long long num=1, const long long orig=0, const long long xt=max_ts);
			double increment_double(const string& key, const double num=1.0, const double orig=0.0, const long long xt=max_ts);
			bool cas(const string& key, const string& oval="", const string& nval="", const long long xt=max_ts);
			bool remove(const string& key);
			string get(const string& key) throw(Error);;
			string seize(const string& key) throw(Error);;
			long long set_bulk(const Map& recs, const long long xt=max_ts, bool atomic=true);
			long long remove_bulk(const List keys, bool atomic=true);
			Map get_bulk(const List& keys, bool atomic=true) throw(Error);
			bool vacuum(const long long steps);
			List match_prefix(const string prefix, const long long max=-1) throw(Error);
			List match_regex(const string regex, const long long max=-1) throw(Error);
			List match_similar(const string origin, const long long range, const bool utf, const long long max=-1) throw(Error);
			void set_target(const string expr);
			string expression();
			Cursor::ptr cursor();

			/*string operator [] (const string& key)
			{
				return get(key);
			}*/

			string __getitem__(const string& key)
			{
				return get(key);
			}

			void __setitem__(const string& key, const std::string& value)
			{
				set(key, value);
			}

			static long long ll_max()
			{
				return max_ts;
			}

			string get_target()
			{
				return dbexpr_;
			}
	};
}



/* END OF FILE */
