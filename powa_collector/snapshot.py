def get_snapshot_functions():
    # XXX should we ignore entries without query_src?
    return """SELECT query_source, function_name
              FROM powa_functions
              WHERE operation = 'snapshot' AND enabled
              AND srvid = %s
              ORDER BY priority"""


def get_src_query(src_fct, srvid):
    return ("SELECT %(srvid)d, * FROM %(fname)s(0)" %
            {'fname': src_fct, 'srvid': srvid})


def get_tmp_name(src_fct):
    return "%s_tmp" % src_fct
