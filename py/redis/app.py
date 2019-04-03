import redis
import json
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
key1 = ''.join(['foo', 'bar'])
value = {
  'foo': {
    'bar': ['baz']
  }
}
r.set(key1, json.dumps(value, indent=2))
print(r.get(key1))
print(r.get('foo'))
print(r.dump(key1))