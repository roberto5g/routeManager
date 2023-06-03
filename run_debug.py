from app.app import app


def run_flask():
    app.run(debug=True)


if __name__ == '__main__':
    run_flask()
