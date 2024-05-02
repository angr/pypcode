/* ###
 * IP: GHIDRA
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/// \file error.hh
/// \brief Base class for error handling facilities
///
/// This is also doubles as a place to list the common include files

#ifndef __ERROR_HH__
#define __ERROR_HH__

#include "types.h"
#include <sstream>
#include <fstream>
#include <iomanip>
#include <map>
#include <set>
#include <list>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cctype>

namespace ghidra {

using std::string;
using std::map;
using std::set;
using std::list;
using std::vector;
using std::pair;
using std::make_pair;
using std::ostream;
using std::istream;
using std::ifstream;
using std::ofstream;
using std::istringstream;
using std::ostringstream;
using std::ios;
using std::dec;
using std::hex;
using std::oct;
using std::setfill;
using std::fixed;
using std::setprecision;
using std::setw;
using std::endl;
using std::ws;
using std::min;
using std::max;
using std::to_string;
using std::piecewise_construct;
using std::forward_as_tuple;


/// \brief The lowest level error generated by the decompiler
///
/// This is the base error for all exceptions thrown by the
/// decompiler.  This underived form is thrown for very low
/// level errors that immediately abort decompilation (usually
/// for just a single function).
struct LowlevelError {
  string explain;		///< Explanatory string
  /// Initialize the error with an explanatory string
  LowlevelError(const string &s) { explain = s; }

  const char *what() { return explain.c_str(); }
};

/// \brief A generic recoverable error
///
/// This error is the most basic form of recoverable error,
/// meaning there is some problem that the user did not take
/// into account.
struct RecovError : public LowlevelError {
  /// Initialize the error with an explanatory string
  RecovError(const string &s) : LowlevelError(s) {}
};

/// \brief An error generated while parsing a command or language
///
/// This error is generated when parsing character data of some
/// form, as in a user command from the console or when parsing
/// C syntax.
struct ParseError : public LowlevelError { // Parsing error
  /// Initialize the error with an explanatory string
  ParseError(const string &s) : LowlevelError(s) {}
};

} // End namespace ghidra
#endif
