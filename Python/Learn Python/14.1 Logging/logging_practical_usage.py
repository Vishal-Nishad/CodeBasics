import logging


logging.basicConfig(
    filename='web_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'

)

def login(username):
    logging.info(f"user {username} logged in")

def process_data(data):
    try:
        if data=="bad_data":
            raise ValueError('Invalid data')
        logging.info(f'Data processed: {data}')
    except ValueError as e:
        logging.error(f"Error data: {e}",exc_info=True)

def logout(username):
    logging.info(f"user {username} logged out.")

if __name__=="__main__":
    user_name='vishal'
    login(user_name)
    process_data("bad_data")
    logout(user_name)