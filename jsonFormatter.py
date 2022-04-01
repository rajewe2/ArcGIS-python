#input malformed json from file and output formatted json
import json

#load json file
with open("input.json") as myJson:
    data = json.load(myJson)
    
#dump to new file
with open("outputFile.json", w+) as outFile:
    json.dump(data, outfile, indent=4)