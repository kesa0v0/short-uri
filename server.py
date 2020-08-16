import generator

def get_request(res):
    try:
        data = generator.db.select(res)
        print(data)
        if data:
            return response('302', data[1])
        else:
            return responese(404)
