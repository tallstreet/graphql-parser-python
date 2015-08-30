# graphql for Python

 This uses the python bindings for [libgraphqlparser](https://github.com/graphql/libgraphqlparser) to generate a GraphQL parser which generates a python data-structure 

# Usage  

```
git clone https://github.com/tallstreet/graphql-parser-python.git
cd graphql-parser-python
git submodule init
git submodule update
cd libgraphqlparser
cmake .
make
cp libgraphqlparser.* ..
./example_run.py
export PYTHONPATH=$PYTHONPATH:.
python test/graphql_test.py
```
