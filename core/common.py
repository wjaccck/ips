__author__ = 'jinhongjun'
import logging
logger = logging.getLogger("ips")
import httplib,json
def req_post(host,port,path,data):
    conn = httplib.HTTPConnection(host, port)
    header={"X-Api-Key": "P0ZZLMZMB5DRIFDRSOS6CGQ50RT3FW87", "Content-Type": "application/x-www-form-urlencoded","X-department":"ops"}
    conn.connect()
    content = json.dumps(data)
    conn.request('POST', path, content, header)
    result = conn.getresponse()
    # if result.status==200:
    #     code={"retcode":0,"message":"done"}
    # else:
    #     code={"retcode":1,"message":result.read()}
    # conn.close()
    return (result.status,result.read())

def get_result(status,content):
    if status==0:
        result={
                "retcode":0,
                "stdout":content,
                "stderr":''
                }
    else:
        result={
                "retcode":status,
                "stdout":'',
                "stderr":content
                }
    return result
