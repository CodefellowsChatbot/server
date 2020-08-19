import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from resources.info import Info
import json

def main():
    info = Info()
    # print(info.courses["javascript"])

    output = {"intents": []}
    with open("chat_bot/greeting.json", "r") as data:
        greetings = json.load(data)
        for el in greetings['intents']:
            output['intents'].append(el)

    def walk_json(json_obj, last=""):
        for key in json_obj:
            if isinstance(json_obj[key], str):
                output["intents"].append(
                    {
                        "patterns": [f"{last} {key}"],
                        "responses": [json_obj[key]],
                        "tag": f"{last} {json_obj[key]}",
                    }
                )
            elif isinstance(json_obj[key], list):
                output["intents"].append(
                    {
                        "patterns": [f"{last} {key}"],
                        "responses": json_obj[key],
                        "tag": f"{last} {json_obj[key]}",
                    }
                )
            elif hasattr(json_obj[key], "__iter__"):
                walk_json(json_obj[key], f"{last} {key}")
            else:
                print(last, json_obj[key])
                pass


    walk_json(info.courses)
    walk_json(info.events)
    walk_json(info.apply)
    walk_json(info.employment)
    walk_json(info.financing)
    walk_json(info.calendar)
    final_out = json.dumps(output)
    # print(final_out)

    ## put file in right place
    with open('./chat_bot/intents.json', 'w') as writer:
        writer.write(final_out)

if __name__ == "__main__":
    main()