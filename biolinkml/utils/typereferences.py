from dataclasses import dataclass
from typing import Set, cast

from biolinkml.meta import ClassDefinitionName, SlotDefinitionName, TypeDefinitionName, SubsetDefinitionName, ElementName
from biolinkml.utils.metamodelcore import empty_set


@dataclass(repr=False, frozen=True)
class RefType:
    name: str

    def __repr__(self):
        return self.name


ClassType = RefType('Class')
TypeType = RefType('Type')
SlotType = RefType('Slot')
SubsetType = RefType('Subset')


@dataclass
class References:
    """
    Summary of references to a given class. The reference class is the key to the dictionary carrying classrefs
    """
    classrefs: Set[ClassDefinitionName] = empty_set()     # Refs of type class
    slotrefs: Set[SlotDefinitionName] = empty_set()       # Refs of type slot
    typerefs: Set[TypeDefinitionName] = empty_set()       # Refs of type type
    subsetrefs: Set[SubsetDefinitionName] = empty_set()   # Refs of type subset

    def addref(self, fromtype: RefType, fromname: ElementName) -> None:
        if fromtype is ClassType:
            self.classrefs.add(cast(ClassDefinitionName, fromname))
        elif fromtype is TypeType:
            self.typerefs.add(cast(TypeDefinitionName, fromname))
        elif fromtype is SlotType:
            self.slotrefs.add(cast(SlotDefinitionName, fromname))
        elif fromtype is SubsetType:
            self.subsetrefs.add(cast(SubsetDefinitionName, fromname))
        else:
            raise TypeError(f"Unknown typ: {fromtype}")

    def update(self, other: "References") -> None:
        self.classrefs.update(other.classrefs)
        self.slotrefs.update(other.slotrefs)
        self.typerefs.update(other.typerefs)
        self.subsetrefs.union(other.subsetrefs)

    def __bool__(self):
        return bool(self.classrefs) or bool(self.slotrefs) or bool(self.typerefs) or bool(self.subsetrefs)
