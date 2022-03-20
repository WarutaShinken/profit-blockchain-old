from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": "profit_harvester profit_timelord_launcher profit_timelord profit_farmer profit_full_node profit_wallet".split(),
    "node": "profit_full_node".split(),
    "harvester": "profit_harvester".split(),
    "farmer": "profit_harvester profit_farmer profit_full_node profit_wallet".split(),
    "farmer-no-wallet": "profit_harvester profit_farmer profit_full_node".split(),
    "farmer-only": "profit_farmer".split(),
    "timelord": "profit_timelord_launcher profit_timelord profit_full_node".split(),
    "timelord-only": "profit_timelord".split(),
    "timelord-launcher-only": "profit_timelord_launcher".split(),
    "wallet": "profit_wallet profit_full_node".split(),
    "wallet-only": "profit_wallet".split(),
    "introducer": "profit_introducer".split(),
    "simulator": "profit_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
