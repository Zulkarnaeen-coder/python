student_data = {
    "id1":{
        "name":"Hasan",
         "class":"V",
        "Subject_Interegration":"Math"
    },
    "id2":{
        "name":"Mamunn",
        "class":"V",
        "Subject_Interegration":"English"
    },
    "id23":{
        "name":"Hasan",
        "class":"V",
        "Subject_Interegration":"Math"
    },
    "id4":{
        "name":"Robiul",
        "class":"V",
        "Subject_Interegration":"B.G.S"
    }
}
result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_keys = (details["name"],details["class"],details["Subject_Interegration"])

    if unique_keys not in seen_keys:
        seen_keys.append(unique_keys)
        result[student_id] = details

for k,v in result.items():
    print(k," ",v)