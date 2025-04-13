from app.main import app as application

# This is needed for AWS Elastic Beanstalk
if __name__ == "__main__":
    application.run()
