/* Copyright 2017 R. Thomas
 * Copyright 2017 Quarkslab
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#ifndef LIEF_OAT_VISITOR_JSONS_H_
#define LIEF_OAT_VISITOR_JSONS_H_

#include "LIEF/config.h"

#ifdef LIEF_JSON_SUPPORT

#include "LIEF/visibility.h"
#include "LIEF/visitors/json.hpp"
#include "LIEF/OAT.hpp"

namespace LIEF {
namespace OAT {

LIEF_API json to_json(const Object& v);
LIEF_API std::string to_json_str(const Object& v);


class LIEF_API JsonVisitor : public LIEF::JsonVisitor {
  public:
  using LIEF::JsonVisitor::JsonVisitor;

  public:
  virtual void visit(const Binary& binary)        override;
  virtual void visit(const Header& header)        override;
  virtual void visit(const DexFile& dex_file)     override;
  virtual void visit(const Class& cls)            override;
  virtual void visit(const Method& method)        override;
};

}
}

#endif // LIEF_JSON_SUPPORT

#endif
