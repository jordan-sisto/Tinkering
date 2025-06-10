
from core_builder_module import ExtendedWarbandRoster
from trench_data import all_factions_data

def choose_faction():
    print("Available factions:")
    for idx, name in enumerate(all_factions_data.keys()):
        print(f"{idx + 1}. {name}")
    choice = int(input("Enter faction number: ")) - 1
    faction_name = list(all_factions_data.keys())[choice]
    return faction_name, all_factions_data[faction_name]

def main():
    print("=== Trench Crusade Warband Builder CLI ===")
    faction_name, data = choose_faction()
    roster = ExtendedWarbandRoster(data)

    while True:
        print(f"
Faction: {faction_name} | Ducats Left: {roster.remaining_ducats}")
        print("Options: [1] Add Unit [2] Add Weapon [3] Add Gear [4] Add Power [5] Summary [6] Validate [0] Exit")
        cmd = input("Select option: ")

        if cmd == "1":
            for cat, units in roster.units.items():
                print(f"{cat.title()}:")
                for name, cost in units.items():
                    print(f"  {name} ({cost} ducats)")
            name = input("Enter unit name to add: ")
            print(roster.add_unit(name))

        elif cmd == "2":
            for w in roster.ranged_weapons + roster.melee_weapons:
                print(f"{w['name']} ({w['cost']}) — {w.get('notes','')}")
            name = input("Enter weapon name to add: ")
            print(roster.add_weapon(name))

        elif cmd == "3":
            for g in roster.gear:
                print(f"{g['name']} ({g['cost']})")
            name = input("Enter gear name to add: ")
            print(roster.add_gear(name))

        elif cmd == "4":
            for p in roster.powers:
                print(f"{p['name']} ({p['cost']})")
            name = input("Enter Goetic Power to add: ")
            print(roster.add_power(name))

        elif cmd == "5":
            summary = roster.summary()
            print(f"Total Ducats: {summary['Total Ducats']}, Remaining: {summary['Remaining Ducats']}")
            for cat in ['Units', 'Weapons', 'Gear', 'Powers']:
                print(f"{cat}:")
                for name, cost in summary[cat]:
                    print(f"  {name} ({cost})")

        elif cmd == "6":
            for line in roster.validate():
                print("-", line)

        elif cmd == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
