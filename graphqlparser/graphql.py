# Copyright (c) 2015, Gary Roberts.
# All rights reserved.

class Document():
    def __init__(self, node):
        self.node = node
        self.definitions = []
        self.fragments = {}

    def add_definition(self, definition):
        self.definitions.append(definition)
    
    def add_fragment(self, frag_name, frag):
        self.definitions.append(frag)
        self.fragments[frag_name] = frag

class Definition():
    def __init__(self, node, parent):
        self.node = node
        self.directives = {}
        parent.add_definition(self)

    def is_definition(self):
        return True

    def add_directive(self, k, args):
        self.directives[k] = args

    def set_selection_set(self, s):
        self.selection_set = s

class Operation(Definition):
    def __init__(self, node, parent):
        self.node = node
        self.directives = {}
        self.definitions = []
        parent.add_definition(self)

    def add_definition(self, definition):
        self.definitions.append(definition)

class Selection():
    def __init__(self):
        self.directives = []
        self.selection_set = None

    def is_selection(self):
        return True

    def add_directive(self, k):
        self.directives.append(k)

    def set_selection_set(self, s):
        self.selection_set = s

class SelectionSet(Selection):
    def __init__(self, node, parent):
        self.node = node
        self.fields = []
        self.frags = []
        self.directives = []
        parent.set_selection_set(self)

    def add_field(self, field):
        self.fields.append(field)
        
    def add_frag_usage(self, fragname):
        self.frags.append(fragname)

class Field(Selection):
    def __init__(self, node, parent):
        self.node = node
        self.selections = []
        self.arguments = {}
        self.directives = []
        parent.add_field(self)

    def add_argument(self, name, value):
        self.arguments[name] = value.value


class Fragment(Selection):
    def __init__(self, node):
        self.node = node
        self.directives = []

class Variable(Definition):
    def __init__(self, node, parent):
        self.node = node
        parent.add_definition(self)

class VariableUsage():
    def __init__(self, node, value):
        self.node = node
        self.value = value

class Directive():
    def __init__(self, node, parent):
        self.node = node
        self.arguments = {}
        parent.add_directive(self)

    def add_argument(self, name, value):
        self.arguments[name] = value.value

class Value():
    def __init__(self, value):
        self.value = value

    def is_value(self):
        return True

class Scalar():
    def is_scalar(self):
        return True
