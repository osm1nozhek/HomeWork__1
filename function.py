def Parse(query: str) -> dict:
    if "?" in query:
        dict1={}
        query=query[query.rfind("?")+1:].replace("&"," ").split(" ")
        for el in query:
            if el =="":
                query.remove(el)
            else:
                el = el.replace("=", " ", 1).split(" ")
                dict1[el[0]] = el[-1]
        return dict1
    else:
        return {}

def parse_cookie(query: str) -> dict:
    dict1={}
    query=query.replace(";"," ").split()
    for el in query :
        el=el.replace("="," ",1).split()
        dict1[el[0]]=el[-1]
    return dict1