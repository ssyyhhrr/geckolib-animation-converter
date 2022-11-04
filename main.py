import sys
import json

with open(sys.argv[1]) as f:
    d = json.load(f)
    for i in d["animations"]:
        for j in d["animations"][i]["bones"]:
            for k in d["animations"][i]["bones"][j]:
                for l in d["animations"][i]["bones"][j][k]:
                    if l != "vector" and not isinstance(d["animations"][i]["bones"][j][k][l], (list, int)) and not d["animations"][i]["bones"][j][k][l].get("post") is None:
                        d["animations"][i]["bones"][j][k][l] = d["animations"][i]["bones"][j][k][l]["post"]
    with open(sys.argv[2], "a+") as g:
        json.dump(d, g)
