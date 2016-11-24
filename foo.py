import requests_unixsocket
prefix = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
s = requests_unixsocket.Session()
r = s.get(prefix + "/events")
events = r.iter_lines()
next(events)
next(events)
next(events)
next(events)


"""
[{'Action': 'create',
  'Actor': {'Attributes': {'image': 'python:3.6.0b2', 'name': 'test'},
  'ID': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01'},
  'Type': 'container',
  'from': 'python:3.6.0b2',
  'id': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01',
  'status': 'create',
  'time': 1479926693,
  'timeNano': 1479926693041840744},
{'Action': 'attach',
    'Actor': {'Attributes': {'image': 'python:3.6.0b2', 'name': 'test'},
        'ID': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01'},
    'Type': 'container',
    'from': 'python:3.6.0b2',
    'id': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01',
    'status': 'attach',
    'time': 1479926693,
    'timeNano': 1479926693055584882},
{'Action': 'connect',
    'Actor': {'Attributes': {'container': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01',
        'name': 'bridge',
        'type': 'bridge'},
    'ID': '6ed2fce2dddde3cd0b4d0f4fe545a4f27667236ff7f019958101f24aceafdd26'},
    'Type': 'network',
    'time': 1479926693,
    'timeNano': 1479926693173800819},
{'Action': 'start',
    'Actor': {'Attributes': {'image': 'python:3.6.0b2', 'name': 'test'},
        'ID': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01'},
    'Type': 'container',
    'from': 'python:3.6.0b2',
    'id': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01',
    'status': 'start',
    'time': 1479926693,
    'timeNano': 1479926693521368063},
{'Action': 'resize',
    'Actor': {'Attributes': {'height': '59',
        'image': 'python:3.6.0b2',
        'name': 'test',
        'width': '157'},
    'ID': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01'},
    'Type': 'container',
    'from': 'python:3.6.0b2',
    'id': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01',
    'status': 'resize',
    'time': 1479926693,
    'timeNano': 1479926693526105094},
{'Action': 'die',
    'Actor': {'Attributes': {'exitCode': '0',
        'image': 'python:3.6.0b2',
        'name': 'test'},
    'ID': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01'},
    'Type': 'container',
    'from': 'python:3.6.0b2',
    'id': '343aaf89b2d6dc0e38c3a6bc6f44f96e50235f442970891586d87cd06230ac01',
    'status': 'die',
    'time': 1479926703,
    'timeNano': 1479926703099251006}]
"""
