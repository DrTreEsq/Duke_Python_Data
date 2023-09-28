def include(d, *keys):
    return {k: d[k] for k in keys if k in d}


def omit(d, *keys):
    return {k: d[k] for k in d if k not in keys}


class NamedList(dict):
    def add(self, name, **entry):
        self[name] = dict(name=name, **entry)

    def pick(self, *keys):
        return [include(entry, *keys) for entry in self.to_list()]

    def omit(self, *keys):
        return [omit(entry, *keys) for entry in self.to_list()]

    def from_list(self, entries):
        for entry in entries:
            self.add(**entry)

    def to_list(self):
        return [{k: v for k, v in entry.items() if v is not None} for entry in list(self.values())]