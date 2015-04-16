import json

arr = []
k = 0
for line in open("obesity.csv"):
    if k == 0:
        k = 1
        continue
    spline = line.replace("\n", "").split(",")
    if len(spline) == 3 and spline[2] != "":
        (state, county, percent) = spline
        arr.append({"state": state, "county": county, "percent": percent})

open("obesity.json", "w").write(json.dumps(arr))
print arr
