import redis

redis_connection = redis.Redis(
    host='localhost',
    port=6379,
    charset='utf-8',
    decode_responses=True
)

data = {
    "shopping": {
        "store": "ICA Maxi",
        "selfscan": True,
        "items": ["milk", "bread", "cookies", "pizza"],
        "expected_cost": 150
    }
}

if __name__ == '__main__':
    print(redis_connection.ping())

    # redis_connection.json().set('shopping_data', '$', data)

    # value = redis_connection.json().get('shopping_data')
    # print(value)
    """
    random_number = 4  # Decided by dice roll

    redis_connection.set('rnum', random_number)

    value = int(redis_connection.get('rnum'))
    print(value)
    print(type(value))
    print(redis_connection.object(infotype='encoding', key='rnum'))
    """

    # mylist = [1, 2, 3, 4, 5]
    #redis_connection.rpush('numbers', *mylist)
    list_data = redis_connection.lrange('numbers', 0, -1)
    print(list_data)
    print('length:', redis_connection.llen('numbers'))
    