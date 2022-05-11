import ssl

from quart import make_response, Quart, render_template, url_for

app = Quart(__name__)

@app.route('/stack_colors')
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
    app.run(
        host='0.0.0.0', 
        port=5000, 
        certfile='cert.pem', 
        keyfile='key.pem',
    )
