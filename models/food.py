class Food:
    info: dict

    def __str__(self):
        return self.info['description']

    def __repr__(self) -> str:
        return self.__str__()
