from application import create_app

app = create_app()

#Running the app
if __name__ == '__main__':
    app.run(debug=True) 