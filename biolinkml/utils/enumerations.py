from biolinkml.meta import EnumDefinition


class EnumerationHandler(EnumDefinition):

    def __contains__(self, item):
        return item in self.permissible_values
