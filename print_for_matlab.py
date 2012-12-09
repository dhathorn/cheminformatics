#!/usr/bin/python
class print_for_matlab(object):
    def __init__(self):
        self.headers = False

    def print_to_file(self, data, f):
        if not self.headers:
            self.print_matlab_headers(data, f)
            self.headers = True
        self.print_out(data, f)

    def print_matlab_headers(self, data, f):
        for d in data:
            f.write("%s%s," % (d[0], d[1]))
        f.write('\n')

    def print_out(self, data, f):
        for d in data:
            f.write("%s," % (d[2]))
        f.write('\n')
