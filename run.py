from app.app import app
import threading
import webview


def run_flask():
    app.run()


if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    webview.create_window("Router Manager", "http://127.0.0.1:5000/app")
    webview.start()
