def query_parameters_to_dict(request) -> dict:
    args = request.args
    request_data = {}
    for k, v in args.items():
        request_data[k] = v

    return request_data