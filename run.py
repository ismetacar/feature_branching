from sanic import Sanic, response

app = Sanic()


@app.route('/api/v1/healthcheck')
async def healthcheck(request):
    return response.json({
        'healty': True
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
    