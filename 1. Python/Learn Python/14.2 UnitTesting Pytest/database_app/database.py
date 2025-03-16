class CustomerDB:
    def __init__(self):
        self.customers=[]
        self.next_id=1
        self.connection=None

    def connect(self):
        #simulate connecting to a db
        self.connection="DummyConnectionObject"
        print("Connected to the db")

    def insert_customer(self,name,email):
        # insert a new customer into the list
        customer={
            "id":self.next_id,
            "name":name,
            "email":email
        }
        self.customers.append(customer)
        self.next_id+=1
    def get_all_customers(self):
    # retrieve all customers from the list
        return self.customers

    def get_customer_by_name(self,name):
        #Retrieve a customer by name
        for cus in self.customers:
            if cus["name"]==name:
                return cus
        return None

    def clear_customers(self):
        # clear all customers (reset the db)
        self.customers=[]
        self.next_id=1

    def close(self):
        self.connection=None
        print("Database connection closed.")
