from biolinkml.meta import EnumDefinition


class EnumerationHandler(EnumDefinition):
    """
    This is the abstract API for Enumeration processing.  The default handler is intended to handle the case where the
    enumerations have explicit permissible values and, as such, it is not necessary to refer to a code_set to determine
    the permissible values or their mappings.
    """

    def __contains__(self, item):
        return item in self.permissible_values
