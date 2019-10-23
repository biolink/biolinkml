
""" Metadata filters for test cases -- various tools to remove metadata from output """
import re


def ldcontext_metadata_filter(s: str) -> str:
    """
    Metafilter for jsonld context
    :param s: jsonld context string
    :return: string stripped of metadata
    """
    return re.sub(r'Auto generated from .*? by', 'Auto generated from ... by',
                  re.sub(r'Generation date: .*?\\n', r'Generation date: \\n', s))

def json_metadata_filter(s: str) -> str:
    return re.sub(r'("source_file_date": )".*"', r'\1"Friday Sep 27 12:00:00 2003"',
           re.sub(r'("generation_date": )".*"', r'\1"Friday Sep 27 12:00:00 2003"',
           re.sub(r'("source_file_size": )".*"', r'\1"23600:', s)))


def metadata_filter(s: str) -> str:
    return re.sub(r'(# Auto generated from ).*(\.yaml by pythongen\.py version:) .*', r'\1\2',
                  re.sub(r'(# Generation date:) .*', r'\1', re.sub(r'\r\n', '\n', s)))