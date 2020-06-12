from sanic import Sanic, response

app = Sanic()


@app.route('/api/v1/healthcheck')
async def healthcheck(request):
    return response.json({
        'healty': True
    })


@app.route('/api/v1/users', methods=['POST'])
async def users(request):
    body = request.json

    if 'username' not in body.keys() or 'password' not in body.keys():
        return response.json({
            'error': 'badRequest',
            'message': 'username and password required'
        }, 400)

    user = {
        'username': body['username'],
        'password': body['password']
    }

    return response.json(user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
