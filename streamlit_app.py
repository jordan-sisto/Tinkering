
import streamlit as st
from core_builder_module import ExtendedWarbandRoster
from trench_data import all_factions_data

# App Title
st.title("⚔️ Trench Crusade Warband Builder")

# Faction selection
factions = list(all_factions_data.keys())
faction_name = st.selectbox("Choose your faction", factions)
data = all_factions_data[faction_name]
builder = ExtendedWarbandRoster(data)

st.subheader(f"Faction: {faction_name} — Budget: {builder.ducat_limit} ducats")

# Unit selection
with st.expander("Add Units"):
    for cat in builder.units:
        st.markdown(f"**{cat.title()}**")
        for name, cost in builder.units[cat].items():
            if st.button(f"Add {name} ({cost} ducats)", key=f"unit_{name}"):
                st.success(builder.add_unit(name))

# Weapon selection
with st.expander("Add Weapons"):
    for w in builder.ranged_weapons + builder.melee_weapons:
        label = f"{w['name']} ({w['cost']} ducats) — {w.get('notes','')}"
        if st.button(label, key=f"weapon_{w['name']}"):
            st.success(builder.add_weapon(w['name']))

# Gear selection
with st.expander("Add Gear"):
    for g in builder.gear:
        label = f"{g['name']} ({g['cost']} ducats)"
        if st.button(label, key=f"gear_{g['name']}"):
            st.success(builder.add_gear(g['name']))

# Powers selection
with st.expander("Add Goetic Powers"):
    for p in builder.powers:
        label = f"{p['name']} ({p['cost']} ducats)"
        if st.button(label, key=f"power_{p['name']}"):
            st.success(builder.add_power(p['name']))

# Summary and Validation
st.subheader("📋 Warband Summary")
sum_data = builder.summary()
st.write(f"**Remaining Ducats:** {sum_data['Remaining Ducats']} / {sum_data['Total Ducats']}")
st.write("**Units:**", sum_data["Units"])
st.write("**Weapons:**", sum_data["Weapons"])
st.write("**Gear:**", sum_data["Gear"])
st.write("**Powers:**", sum_data["Powers"])

if st.button("✅ Validate Warband"):
    validation = builder.validate()
    for result in validation:
        if result.startswith("✅"):
            st.success(result)
        else:
            st.error(result)
