import ssl

from quart import make_response, Quart, render_template, url_for

app = Quart(__name__)

@app.route('/')
async def index():
    result = await render_template('index.html')
    response = await make_response(result)
    response.push_promises.update([
        url_for('static', filename='css/bootstrap.min.css'),
        url_for('static', filename='js/bootstrap.min.js'),
        url_for('static', filename='js/jquery.min.js'),
    ])
    return response


if __name__ == '__main__':
    ssl_context = ssl.create_default_context(
        ssl.Purpose.CLIENT_AUTH,
    )
    ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    ssl_context.set_ciphers('ECDHE+AESGCM')
    ssl_context.load_cert_chain(
        certfile='cert.pem', keyfile='key.pem',
    )
    ssl_context.set_alpn_protocols(['h2', 'http/1.1'])
    app.run(host='localhost', port=5000, ssl=ssl_context)
