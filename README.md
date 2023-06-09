# brownie-load-oz
Illustrates a problem loading OZ 4.9.1 with Brownie 1.9.3

### Run proxy deploy script
```shell
python --version
Python 3.10.12


brownie --version
Brownie v1.19.3 - Python development framework for Ethereum


brownie run scripts/deploy_proxy.py
```

... and face the consequences
```
Brownie v1.19.3 - Python development framework for Ethereum

BrownieLoadOzProject is the active project.

Launching 'ganache-cli --chain.vmErrorsOnRPCResponse true --wallet.totalAccounts 10 --hardfork istanbul --miner.blockGasLimit 12000000 --wallet.mnemonic brownie --server.port 8545'...
Compiling contracts...
  Solc version: 0.8.20
  Optimizer: Enabled  Runs: 200
  EVM Version: Istanbul
Generating build data...
  File "brownie/_cli/run.py", line 51, in main
    return_value, frame = run(
  File "brownie/project/scripts.py", line 60, in run
    module = _import_from_path(script)
  File "brownie/project/scripts.py", line 156, in _import_from_path
    _import_cache[import_str] = importlib.import_module(import_str)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen, line line, in in
  File "<frozen, line line, in in
  File "<frozen, line line, in in
  File "<frozen, line line, in in
  File "<frozen, line line, in in
  File "<frozen, line line, in in
  File "./scripts/deploy_proxy.py", line 5, in <module>
    project.load(Path.home() / ".brownie" / "packages" / config["dependencies"][0])
  File "brownie/project/main.py", line 780, in load
    return Project(name, project_path)
  File "brownie/project/main.py", line 188, in __init__
    self.load()
  File "brownie/project/main.py", line 257, in load
    self._compile(changed, self._compiler_config, False)
  File "brownie/project/main.py", line 100, in _compile
    build_json = compiler.compile_and_format(
  File "brownie/project/compiler/__init__.py", line 142, in compile_and_format
    build_json.update(generate_build_json(input_json, output_json, compiler_data, silent))
  File "brownie/project/compiler/__init__.py", line 287, in generate_build_json
    source_nodes, statement_nodes, branch_nodes = solidity._get_nodes(output_json)
  File "brownie/project/compiler/solidity.py", line 606, in _get_nodes
    source_nodes = solcast.from_standard_output(output_json)
  File "solcast/main.py", line 33, in from_standard_output
    source_nodes = set_dependencies(source_nodes)
  File "solcast/dependencies.py", line 18, in set_dependencies
    contract.libraries = dict(
  File "solcast/dependencies.py", line 19, in <genexpr>
    (_get_type_name(i.typeName), i.libraryName.name)
AttributeError: 'UsingForDirective' object has no attribute 'typeName'
Terminating local RPC client...
```
