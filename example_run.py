#!/usr/bin/env python

from graphqlparser import Parser

def main():
    f = open("tests/relay-todo.graphql", 'r')
    query = f.read()
    parser = Parser()
    document = parser.parse_query(query)
    print(document)

if __name__ == '__main__':
    main()
