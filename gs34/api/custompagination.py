from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class customPage(PageNumberPagination):
    page_size = 2
    # page_query_param = "p"# normally in querrry parameter it page=somting but we will writ ep=somethig
    # page_size_query_param = 'records'   #THIS IS FOR WE FIVE A WILL TO CLIENT THAT HE MAKE HIS CHOICE IF RECORDS PER PAGE
    # # max_page_size = 7 #no one mean cline tcan abuse the size
    # last_page_strings = 'end'   #bydefault it is last

class customLimitOffset(LimitOffsetPagination):
    default_limit=5
    # limit_query_param = 'mylimit'
    # offset_query_param = 'myoffset'
    # max_limit = 6   #from this a clien tcan exceed


class customCursorPagination(CursorPagination):
    page_size=4
    ordering = 'name'
    # cursor_query_param = 'cu'