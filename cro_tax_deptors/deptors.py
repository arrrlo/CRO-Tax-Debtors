class Deptors:

    def __init__(self, spider, save_handler, screen, category_data):
        self._spider = spider
        self._screen = screen
        self._save_handler = save_handler
        self._category_data = category_data

    def run(self, print_in_terminal=True):
        for item in self._spider.parse():

            # save deptor
            name, dept = self._save_handler.save(item.data)

            # print everything on terminal
            if print_in_terminal:
                self._screen(self._category_data['title'], name, dept,
                             self._category_data['toplist_limit'],
                             self._category_data['color'])


class Item:

    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

    def __eq__(self, other):
        return len(self.data.keys()) > 0


class CategoryDone(Exception):
    pass
