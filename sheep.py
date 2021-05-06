import json
import sys

input = json.load(sys.stdin)
with open("input.txt", "w") as file:
    json.dump(input, file, indent=4)

count = 1
try:
    for c in input["result"]["contexts"]:
        if c["name"] == "sheep":
            count = int(c["parameters"]["count"])
except KeyError:
    pass

text = ""
for i in range(10):
    text += u"羊が" + str(count) + u"匹。"
    count += 1

print("Content-type: application/json\n\n")

output = {
   "speech": text,
   "contextOut": [
      {
         "name": "sheep",
         "lifespan": 1,
         "parameters": {
              "count": count
         }
      }
    ]
}

json.dump(output, sys.stdout)
