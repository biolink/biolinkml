from dataclasses import fields
from typing import Union

from biolinkml.utils.metamodelcore import Curie


class EnumDefinitionMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._addvals()

    def __getitem__(cls, item):
        return cls.__dict__[item]

    def __setitem__(cls, key, value):
        if key in cls.__dict__:
            raise ValueError(f"{cls.__name__} - {key} already assigned")
        cls.__dict__[key] = value

    def __contains__(cls, item) -> bool:
        return item in cls.__dict__


class EnumDefinitionImpl(metaclass=EnumDefinitionMeta):
    def __init__(self, code: Union[str, Curie, "PermissibleValue"]) -> None:
        from biolinkml.meta import PermissibleValue
        if isinstance(code, PermissibleValue):
            key = code.text
        elif isinstance(code, Curie):
            key = '.'.join(str(self.code).split(':', 1))
        else:
            key = code

        if key not in self.__class__:
            # TODO: This is where we create a new PermissibleValue if the definition includes a code_set
            raise ValueError(f"Unknown {self.__class__.__name__} enumeration code: {key}")
        if isinstance(code, PermissibleValue):
            if getattr(self, 'code', None):
                if self.code != code:
                    raise ValueError(f"Enumeration: {self.__class__.__name__} - "
                                     f"Cannot change an existing permissible value entry for {code}")
            else:
                self.code = code
        else:
            self.code = self.__class__[key]

    @classmethod
    def _addvals(cls):
        """ Override this to add non-python compatible values """
        pass

    def __str__(self) -> str:
        return f'{self.code.text}: {self.code.description or ""}'

    def __repr__(self) -> str:
        rlist = [(f.name, getattr(self.code, f.name)) for f in fields(self.code)]
        return '(' + ', '.join([f"{f[0]}={repr(f[1])}" for f in rlist if f[1]]) + ')'
