import json

data = json.load(open("obesity.json"))
dic = {}

regions = {
    "New England": ["ME", "NH", "MA", "CT", "RI", "VT"],
    "Mideast": ["NY", "PA", "DE", "MD", "MJ"],
    "Southeast": ["WV", "VA", "NC", "KY", "TN", "SC", "GA", "AL", "MS", "AR", "LA", "FL"],
    "Southwest": ["OK", "TX", "NM", "AZ"],
    "Great Lakes": ["OH", "MI", "IN", "IL", "WI"],
    "Plains": ["MN", "IA", "MO", "KS", "NE", "SD", "ND"],
    "Rocky Mountain": ["MT", "WY", "CO", "UT", "ID"],
    "West": ["WA", "OR", "NV", "CA"],
    "Non-Continental": ["AK", "HI"]
}

allvals = []
for obj in data:
    state = obj["state"]
    if state not in dic:
        dic[state] = []
    try:
        val = float(obj["percent"])
        count = obj["county"]
        allvals.append(val)
        dic[state].append({"name": count, "value": val, "rate": val}) 
    except e:
        pass


avg_for_state = {}
for state in dic:
    vals = [c["value"] for c in dic[state]]
    avg_for_state[state] = sum(vals)/len(vals)

last = {"name": "Obesity in U.S.A", "children": [], "rate": sum(allvals)/len(allvals)}
for state in dic:
    last["children"].append({"name": state, "children": dic[state], "rate": avg_for_state[state]}) 

#for reg in final:
#    last["children"].append({"name": reg, "children": final[reg]})

open("cleanobesity.json", "w").write(json.dumps(last))
