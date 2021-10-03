import json

def module_amount(mydict):
    key_list = mydict.keys()
    modules_list = []
    for k in key_list:
        module_json = {"name": k, "amount": mydict[k]}
        modules_list.append(module_json)
    my_json = json.dumps(modules_list)
    with open('./returns/data.json', 'w', encoding='utf-8') as f:
        json.dump(my_json, f, ensure_ascii=False, indent=4)