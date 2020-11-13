


class Enumerati:
    def __instancecheck__(self, instance: str) -> bool:
        return instance in self.permissible_values

    def __str__(self):
        return sel

