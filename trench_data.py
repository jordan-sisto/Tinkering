
import json

# This data should be generated from the spreadsheet and rules files via parsing scripts.
# The following is a placeholder stub.

all_factions_data = {
    "Heretic Legion": {
        "faction": "Heretic Legion",
        "units": {
            "core": {
                "1 Heretic Priest": 150,
                "Heretic Trooper": 50,
                "Heretic Gunner": 65
            },
            "special": {
                "Heretic Butcher": 90,
                "Heretic Flametrooper": 85
            }
        },
        "ranged_weapons": [
            {"name": "Trench Carbine", "cost": 25, "notes": "Reliable"},
            {"name": "Rifle", "cost": 30, "notes": ""}
        ],
        "melee_weapons": [
            {"name": "Bayonet", "cost": 10, "notes": ""},
            {"name": "Butcher Blade", "cost": 20, "notes": "Lethal"}
        ],
        "gear": [
            {"name": "Gas Mask", "cost": 15},
            {"name": "Satchel Charge", "cost": 25}
        ],
        "powers": [
            {"name": "INFILTRATOR", "cost": 30},
            {"name": "Tank Palanquin", "cost": 50}
        ]
    }
}
