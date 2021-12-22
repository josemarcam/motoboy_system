def PaginationFilter(request_data):
        
        page = None
        per_page = None
        request_data = ({} if request_data == None or type(request_data) != dict else request_data )
        
        if "page" in request_data:
            page = int(request_data['page'])
            request_data.pop("page")

        if "per_page" in request_data:
            per_page = int(request_data['per_page'])
            request_data.pop("per_page")
        
        return page, per_page, request_data