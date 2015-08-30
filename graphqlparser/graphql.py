#!/usr/bin/env python
# Copyright (c) 2015, Gary Roberts.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

from ctypes import *
from .GraphQLParser import *
import inspect

class GraphQLException(Exception):
    pass

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

class Parser():
    def __init__(self):
        self._nodes = []
        self._visted_nodes = []

    def visit_node(self, node):
        self._nodes.append(node)

    def end_visit_node(self):
        a = self._nodes.pop()
        self._visted_nodes.append(a)

    def process_visit_document(self, node, unused):
        self.document = Document(node)
        self.visit_node(self.document)
        return True

    def process_end_visit_document(self, node, unused):
        self._nodes[-1].definitions_size = GraphQLAstDocument_get_definitions_size(node)
        self.end_visit_node()

    def process_visit_operation_definition(self, node, unused):
        self.visit_node(Operation(node, self._nodes[-1]))
        return True

    def process_end_visit_operation_definition(self, node, unused):
        self._nodes[-1].operation = str(GraphQLAstOperationDefinition_get_operation(node))
        name = GraphQLAstOperationDefinition_get_name(node)
        self._nodes[-1].name = str(GraphQLAstName_get_value(name))
        self._nodes[-1].variables_size = GraphQLAstOperationDefinition_get_variable_definitions_size(node)
        self._nodes[-1].directives_size = GraphQLAstOperationDefinition_get_directives_size(node)
        #self._nodes[-1].selection_set = GraphQLAstOperationDefinition_get_selection_set(node)
        self.end_visit_node()

    def process_visit_variable_definition(self, node, unused):
        self.visit_node(Variable(node, self._nodes[-1]))
        return True

    def process_end_visit_variable_definition(self, node, unused):
        if isinstance(self._nodes[-1], Value):
            self._nodes[-3].default_value = self._nodes[-1].value
            self.end_visit_node()
            
        self._nodes[-2].variable = GraphQLAstVariableDefinition_get_variable(node)
        typeT = GraphQLAstVariableDefinition_get_type(node)
        typeName = GraphQLAstNamedType_get_name(typeT)
        self._nodes[-2].type = str(GraphQLAstName_get_value(typeName))
        #self._nodes[-2].default_value = GraphQLAstVariableDefinition_get_default_value(node)
        #print self._nodes[-2].default_value
        self._nodes[-2].variable = self._nodes[-1]
        self.end_visit_node()
        self.end_visit_node()

    def process_visit_selection_set(self, node, unused):
        self.visit_node(SelectionSet(node, self._nodes[-1]))
        return True

    def process_end_visit_selection_set(self, node, unused):
        self._nodes[-1].selection_set_size = GraphQLAstSelectionSet_get_selections_size(node)
        self.end_visit_node()

    def process_visit_field(self, node, unused):
        self.visit_node(Field(node, self._nodes[-1]))
        return True

    def process_end_visit_field(self, node, unused):
        self._nodes[-1].alias = GraphQLAstField_get_alias(node)
        name = GraphQLAstField_get_name(node)
        self._nodes[-1].name = str(GraphQLAstName_get_value(name))
        self._nodes[-1].arguments_size = GraphQLAstField_get_arguments_size(node)
        self._nodes[-1].directives_size = GraphQLAstField_get_directives_size(node)
        #self._nodes[-1].selection_set = GraphQLAstField_get_selection_set(node)
        self.end_visit_node()

    def process_visit_argument(self, node, unused):
        return True

    def process_end_visit_argument(self, node, unused):
        name = GraphQLAstArgument_get_name(node)
        #value = GraphQLAstArgument_get_value(node)
        self._nodes[-2].add_argument(str(GraphQLAstName_get_value(name)), self._nodes[-1])
        self.end_visit_node()

    def process_visit_fragment_spread(self, node, unused):
        name = GraphQLAstFragmentSpread_get_name(node)
        self._nodes[-1].add_frag_usage(str(GraphQLAstName_get_value(name)))
        return False

    def process_end_visit_fragment_spread(self, node, unused):
        pass
        #self.end_visit_node()

    def process_visit_inline_fragment(self, node, unused):
        frag = Fragment(node)
        self._nodes[-1].add_field(frag)
        self.visit_node(frag)
        return True

    def process_end_visit_inline_fragment(self, node, unused):
        condition = GraphQLAstInlineFragment_get_type_condition(node)
        condition_name = GraphQLAstNamedType_get_name(condition)
        self._nodes[-1].condition = str(GraphQLAstName_get_value(condition_name))
        self._nodes[-1].directives_size = GraphQLAstInlineFragment_get_directives_size(node)
        #selection_set = GraphQLAstInlineFragment_get_selection_set(node)
        self.end_visit_node()
        pass

    def process_visit_fragment_definition(self, node, unused):
        frag = Fragment(node)
        name = GraphQLAstFragmentDefinition_get_name(node)
        frag.name = str(GraphQLAstName_get_value(name))
        self._nodes[-1].add_fragment(frag.name, frag)
        self.visit_node(frag)
        return True

    def process_end_visit_fragment_definition(self, node, unused):
        condition = GraphQLAstFragmentDefinition_get_type_condition(node)
        condition_name = GraphQLAstNamedType_get_name(condition)
        self._nodes[-1].condition = str(GraphQLAstName_get_value(condition_name))
        self._nodes[-1].directives_size = GraphQLAstFragmentDefinition_get_directives_size(node)
        #self._nodes[-1].selection_set = GraphQLAstFragmentDefinition_get_selection_set(node)
        self.end_visit_node()

    def process_visit_variable(self, node, unused):
        return True

    def process_end_visit_variable(self, node, unused):
        name = GraphQLAstVariable_get_name(node)
        self.visit_node(VariableUsage(node, str(GraphQLAstName_get_value(name))))

    def process_visit_int_value(self, node, unused):
        return True

    def process_end_visit_int_value(self, node, unused):
        value = GraphQLAstIntValue_get_value(node)
        self.visit_node(Value(int(value)))

    def process_visit_float_value(self, node, unused):
        return True

    def process_end_visit_float_value(self, node, unused):
        value = GraphQLAstFloatValue_get_value(node)
        self.visit_node(Value(float(value)))

    def process_visit_string_value(self, node, unused):
        return True

    def process_end_visit_string_value(self, node, unused):
        value = GraphQLAstStringValue_get_value(node)
        self.visit_node(Value(str(value)))

    def process_visit_boolean_value(self, node, unused):
        return True

    def process_end_visit_boolean_value(self, node, unused):
        value = GraphQLAstBooleanValue_get_value(node)
        self.visit_node(Value(bool(value)))

    def process_visit_enum_value(self, node, unused):
        return True

    def process_end_visit_enum_value(self, node, unused):
        value = GraphQLAstEnumValue_get_value(node)
        self.visit_node(Value(str(value)))

    def process_visit_array_value(self, node, unused):
        return True

    def process_end_visit_array_value(self, node, unused):
        size = GraphQLAstArrayValue_get_values_size(node)
        data = []
        for i in range(size):
            data.append(self._nodes[-1].value)
            self.end_visit_node()
        data.reverse()
        self.visit_node(Value(data))

    def process_visit_object_value(self, node, unused):
        return True

    def process_end_visit_object_value(self, node, unused):
        size = GraphQLAstObjectValue_get_fields_size(node)
        data = {}
        for i in range(size):
            data.update(self._nodes[-1])
            self.end_visit_node()
        self.visit_node(Value(data))

    def process_visit_object_field(self, node, unused):
        return True

    def process_end_visit_object_field(self, node, unused):
        name = GraphQLAstObjectField_get_name(node)
        #value = GraphQLAstObjectField_get_value(node)
        value = self._nodes[-1]
        self.end_visit_node()
        self.visit_node({str(GraphQLAstName_get_value(name)): value.value})

    def process_visit_directive(self, node, unused):
        self.visit_node(Directive(node, self._nodes[-1]))
        return True

    def process_end_visit_directive(self, node, unused):
        name = GraphQLAstDirective_get_name(node)
        self._nodes[-1].name = str(GraphQLAstName_get_value(name))
        self._nodes[-1].argument_size = GraphQLAstDirective_get_arguments_size(node)
        self.end_visit_node()

    def process_visit_named_type(self, node, unused):
        return False

    def process_end_visit_named_type(self, node, unused):
        name = GraphQLAstNamedType_get_name(node)

    def process_visit_list_type(self, node, unused):
        return False

    def process_end_visit_list_type(self, node, unused):
        type = GraphQLAstListType_get_type(node)

    def process_visit_non_null_type(self, node, unused):
        return False

    def process_end_visit_non_null_type(self, node, unused):
        type = GraphQLAstNonNullType_get_type(node)

    def process_visit_name(self, node, unused):
        return False

    def process_end_visit_name(self, node, unused):
        pass


    def parse_query(self, query):
        error = POINTER(c_char)()
        ast = graphql_parse_string(query, byref(error))

        callbacks = GraphQLAstVisitorCallbacks(
            visit_document = visit_document_func(self.process_visit_document),
            end_visit_document = end_visit_document_func(self.process_end_visit_document),
            visit_operation_definition = visit_operation_definition_func(self.process_visit_operation_definition),
            end_visit_operation_definition = end_visit_operation_definition_func(self.process_end_visit_operation_definition),
            visit_variable_definition = visit_variable_definition_func(self.process_visit_variable_definition),
            end_visit_variable_definition = end_visit_variable_definition_func(self.process_end_visit_variable_definition),
            visit_selection_set = visit_selection_set_func(self.process_visit_selection_set),
            end_visit_selection_set = end_visit_selection_set_func(self.process_end_visit_selection_set),
            visit_field = visit_field_func(self.process_visit_field),
            end_visit_field = end_visit_field_func(self.process_end_visit_field),
            visit_argument = visit_argument_func(self.process_visit_argument),
            end_visit_argument = end_visit_argument_func(self.process_end_visit_argument),
            visit_fragment_spread = visit_fragment_spread_func(self.process_visit_fragment_spread),
            end_visit_fragment_spread = end_visit_fragment_spread_func(self.process_end_visit_fragment_spread),
            visit_inline_fragment = visit_inline_fragment_func(self.process_visit_inline_fragment),
            end_visit_inline_fragment = end_visit_inline_fragment_func(self.process_end_visit_inline_fragment),
            visit_fragment_definition = visit_fragment_definition_func(self.process_visit_fragment_definition),
            end_visit_fragment_definition = end_visit_fragment_definition_func(self.process_end_visit_fragment_definition),
            visit_variable = visit_variable_func(self.process_visit_variable),
            end_visit_variable = end_visit_variable_func(self.process_end_visit_variable),
            visit_int_value = visit_int_value_func(self.process_visit_int_value),
            end_visit_int_value = end_visit_int_value_func(self.process_end_visit_int_value),
            visit_float_value = visit_float_value_func(self.process_visit_float_value),
            end_visit_float_value = end_visit_float_value_func(self.process_end_visit_float_value),
            visit_string_value = visit_string_value_func(self.process_visit_string_value),
            end_visit_string_value = end_visit_string_value_func(self.process_end_visit_string_value),
            visit_boolean_value = visit_boolean_value_func(self.process_visit_boolean_value),
            end_visit_boolean_value = end_visit_boolean_value_func(self.process_end_visit_boolean_value),
            visit_enum_value = visit_enum_value_func(self.process_visit_enum_value),
            end_visit_enum_value = end_visit_enum_value_func(self.process_end_visit_enum_value),
            visit_array_value = visit_array_value_func(self.process_visit_array_value),
            end_visit_array_value = end_visit_array_value_func(self.process_end_visit_array_value),
            visit_object_value = visit_object_value_func(self.process_visit_object_value),
            end_visit_object_value = end_visit_object_value_func(self.process_end_visit_object_value),
            visit_object_field = visit_object_field_func(self.process_visit_object_field),
            end_visit_object_field = end_visit_object_field_func(self.process_end_visit_object_field),
            visit_directive = visit_directive_func(self.process_visit_directive),
            end_visit_directive = end_visit_directive_func(self.process_end_visit_directive),
            visit_named_type = visit_named_type_func(self.process_visit_named_type),
            end_visit_named_type = end_visit_named_type_func(self.process_end_visit_named_type),
            visit_list_type = visit_list_type_func(self.process_visit_list_type),
            end_visit_list_type = end_visit_list_type_func(self.process_end_visit_list_type),
            visit_non_null_type = visit_non_null_type_func(self.process_visit_non_null_type),
            end_visit_non_null_type = end_visit_non_null_type_func(self.process_end_visit_non_null_type),
            visit_name = visit_name_func(self.process_visit_name),
            end_visit_name = end_visit_name_func(self.process_end_visit_name)
        )
        graphql_node_visit(ast, pointer(callbacks), None)
        if error:
            raise GraphQLException(string_at(error))

        graphql_node_free(ast)
        return self.document

def main():
    f = open("tests/relay-todo.graphql", 'r')
    query = f.read()
    parser = Parser()
    document = parser.parse_query(query)
    print(document)

if __name__ == '__main__':
    main()
