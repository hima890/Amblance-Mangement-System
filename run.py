from app import create_app

# Create the app instance
app = create_app()

# Run the app
if __name__ == '__main__':
    app.run(
        port = 5000,
        debug = True,
    )