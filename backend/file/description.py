describe_upload = """
负责接收上传的文件(单个文件)
参数说明: 
    需要携带cookies
    文件需要有后缀
返回文件上传任务是否已经加入队列
"""

describe_queryUpload = """
上传文件进度, 
参数说明: 
    websocket连接所需参数: 明文(?后)参数token, hashed_token, 和id(用户的id)
    单次查询所需参数: taskId: 上传任务的id
返回上传文件已写入的比特数
"""

describe_queryAllUpload = """
当前用户上传的所有文件的进度, 
参数说明: 
    websocket连接所需参数: 明文(?后)参数token, hashed_token, 和id(用户的id)
    单次查询所需参数为空
返回一个字典, 里面是上传文件的比特数
"""