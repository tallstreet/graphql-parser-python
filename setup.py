#!/usr/bin/env python

import os
import graphqlparser

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = ['graphql-parser']

parser = Extension('parser',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
                    include_dirs = ['/usr/local/include'],
                    libraries = [''],
                    library_dirs = ['/usr/local/lib'],
                    sources = [
                    'libgraphqlparser/Ast.cpp',
                    'libgraphqlparser/JsonVisitor.cpp Ast.h AstVisitor.h',
                    'libgraphqlparser/c/GraphQLAst.h',
                    'libgraphqlparser/c/GraphQLAst.cpp',
                    'libgraphqlparser/c/GraphQLAstNode.cpp',
                    'libgraphqlparser/c/GraphQLAstForEachConcreteType.h',
                    'libgraphqlparser/c/GraphQLAstVisitor.h',
                    'libgraphqlparser/c/GraphQLAstVisitor.cpp',
                    'libgraphqlparser/c/GraphQLParser.cpp',
                    'libgraphqlparser/parser.tab.cpp parser.tab.hpp',
                    'libgraphqlparser/lexer.cpp',
                    'libgraphqlparser/GraphQLParser.cpp'])

setup(
    name='graphqlparser',
    version=graphqlparser.__version__,
    description='graphql-parser: Parser for latest GraphQL specification',
    long_description=open('README.md').read(),
    author='Gary Roberts',
    author_email='contact@tallstreet.com',
    url='https://github.com/tallstreet/graphql-parser-python/',
    packages=packages,
    license=open('LICENSE').read(),
    zip_safe=False,
    ext_modules = [parser],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ),
)

del os.environ['PYTHONDONTWRITEBYTECODE']
