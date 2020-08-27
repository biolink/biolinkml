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
#ifndef LIEF_VDEX_PARSER_H_
#define LIEF_VDEX_PARSER_H_


#include <memory>

#include "LIEF/visibility.h"

#include "LIEF/BinaryStream/VectorStream.hpp"

#include "LIEF/VDEX/File.hpp"


namespace LIEF {
namespace VDEX {

//! @brief Class which parse an VDEX file and transform into a VDEX::File object
class LIEF_API Parser {
  public:
    static std::unique_ptr<File> parse(const std::string& file);
    static std::unique_ptr<File> parse(const std::vector<uint8_t>& data, const std::string& name = "");

    Parser& operator=(const Parser& copy) = delete;
    Parser(const Parser& copy)            = delete;

  private:
    Parser(void);
    Parser(const std::string& file);
    Parser(const std::vector<uint8_t>& data, const std::string& name);
    virtual ~Parser(void);

    void init(const std::string& name, vdex_version_t version);

    template<typename VDEX_T>
    void parse_file(void);

    template<typename VDEX_T>
    void parse_header(void);

    template<typename VDEX_T>
    void parse_checksums(void);

    template<typename VDEX_T>
    void parse_dex_files(void);

    template<typename VDEX_T>
    void parse_verifier_deps(void);

    template<typename VDEX_T>
    void parse_quickening_info(void);

    LIEF::VDEX::File* file_;
    std::unique_ptr<VectorStream> stream_;
};




} // namespace VDEX
} // namespace LIEF
#endif
