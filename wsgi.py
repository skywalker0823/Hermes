from app import create_app
# from app.socketio import socketio

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, host="0.0.0.0")