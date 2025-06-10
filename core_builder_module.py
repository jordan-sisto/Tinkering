
class ExtendedWarbandRoster:
    def __init__(self, faction_data, ducat_limit=700):
        self.faction = faction_data["faction"]
        self.ducat_limit = ducat_limit
        self.remaining_ducats = ducat_limit
        self.units = faction_data["units"]
        self.ranged_weapons = faction_data["ranged_weapons"]
        self.melee_weapons = faction_data["melee_weapons"]
        self.gear = faction_data["gear"]
        self.powers = faction_data.get("powers", [])

        self.selected_units = []
        self.selected_weapons = []
        self.selected_gear = []
        self.selected_powers = []

    def add_unit(self, name):
        for cat in self.units:
            if name in self.units[cat]:
                cost = float(self.units[cat][name])
                if self.remaining_ducats < cost:
                    return f"❌ Not enough ducats to add {name} (needs {cost}, have {self.remaining_ducats})"
                self.selected_units.append((name, cost))
                self.remaining_ducats -= cost
                return f"✅ Added unit: {name} ({cost} ducats)"
        return f"❌ Unit '{name}' not found"

    def remove_unit(self, name):
        for i, (unit, cost) in enumerate(self.selected_units):
            if unit == name:
                self.selected_units.pop(i)
                self.remaining_ducats += cost
                return f"✅ Removed unit: {name}"
        return f"❌ Unit '{name}' not in roster"

    def add_weapon(self, name):
        for w in self.ranged_weapons + self.melee_weapons:
            if w["name"] == name:
                cost = float(w["cost"])
                if self.remaining_ducats < cost:
                    return f"❌ Not enough ducats to add {name} (needs {cost}, have {self.remaining_ducats})"
                self.selected_weapons.append((name, cost))
                self.remaining_ducats -= cost
                return f"✅ Added weapon: {name} ({cost} ducats)"
        return f"❌ Weapon '{name}' not found"

    def add_gear(self, name):
        for g in self.gear:
            if g["name"] == name:
                cost = float(g["cost"])
                if self.remaining_ducats < cost:
                    return f"❌ Not enough ducats to add {name} (needs {cost}, have {self.remaining_ducats})"
                self.selected_gear.append((name, cost))
                self.remaining_ducats -= cost
                return f"✅ Added gear: {name} ({cost} ducats)"
        return f"❌ Gear '{name}' not found"

    def add_power(self, name):
        for p in self.powers:
            if p["name"] == name:
                cost = p.get("cost", 0)
                if cost == '' or cost is None:
                    return f"❌ No cost listed for '{name}'"
                cost = float(cost)
                if self.remaining_ducats < cost:
                    return f"❌ Not enough ducats to add {name} (needs {cost}, have {self.remaining_ducats})"
                self.selected_powers.append((name, cost))
                self.remaining_ducats -= cost
                return f"✅ Added Goetic Power: {name} ({cost} ducats)"
        return f"❌ Goetic Power '{name}' not found"

    def summary(self):
        return {
            "Faction": self.faction,
            "Total Ducats": self.ducat_limit,
            "Remaining Ducats": self.remaining_ducats,
            "Units": self.selected_units,
            "Weapons": self.selected_weapons,
            "Gear": self.selected_gear,
            "Powers": self.selected_powers
        }

    def validate(self):
        messages = []
        if len(self.selected_units) == 0:
            messages.append("❌ No units selected")
        else:
            messages.append("✅ At least one unit present")
        if self.remaining_ducats < 0:
            messages.append("❌ Budget exceeded")
        else:
            messages.append("✅ Budget respected")
        return messages
