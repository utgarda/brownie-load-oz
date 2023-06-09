from brownie import config, project
from pathlib import Path


project.load(Path.home() / ".brownie" / "packages" / config["dependencies"][0])
# The only thing we want from non-upgradeable OZ, or else we need to put it in our repo
ERC1967Proxy = project.OpenzeppelinContracts491Project.ERC1967Proxy

def main():
    # deployer = accounts.load('deployer')
    # logic = MyContract.deploy(
        # {'from': deployer},
        # publish_source = True,
    # )
    # init_data = logic.initialize.encode_input(...)
    # my_contract_proxied = ERC1967Proxy.deploy(
        # logic,
        # init_data,
        # {'from': deployer},
        # publish_source = True
    # )
    print('all done')
