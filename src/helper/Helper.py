import itertools


class Helper:
    def __init__(self):
        pass

    def unique_list_by_key(self, lst):
        for _, grp in itertools.groupby(lst, lambda d: (d['source_api'], d['target_api'])):
            yield list(grp)[0]
