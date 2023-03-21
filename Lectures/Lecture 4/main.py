import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    charset='utf-8',
    decode_responses=True
)

if __name__ == '__main__':
    output = r.ping()
    print(output)

    value = r.get('name')
    print(value)

    response = r.set('age', 38)
    print(response)

    response2 = r.mset({
        'Sweden': 'Stockholm',
        'Denmark': 'Copenhagen'
    })
    print(response2)

    value2 = r.get('Finland')
    print(value2)

    print(r.keys())

    response3 = r.set('prices', [1,2,3,4,5,6])
    print(response3)
    