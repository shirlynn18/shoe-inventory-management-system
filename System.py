def main_menu():
    while True:
        print('----------------------------------\n'
              '             KJ SPORTS             \n'
              'Shoe Inventory Management System\n'
              '----------------------------------\n'
              '[1]  Add a new product\n'
              '[2]  Update product details\n'
              '[3]  Add a new supplier\n'
              '[4]  Place an order\n'
              '[5]  View inventory\n'
              '[6]  Generate reports\n'
              '[7]  Exit\n'
              '----------------------------------\n')

        try:
            option = int(input('Select an Option (1-7): '))

            match option:
                case 1:
                    add_products()
                case 2:
                    update_products()
                case 3:
                    add_suppliers()
                case 4:
                    place_orders()
                case 5:
                    view_inventory()
                case 6:
                    generate_reports()
                case 7:
                    print('Goodbye!')
                    break
                case _:
                    print('ERROR: Invalid Option')

        except ValueError as e:
            print(e)
            print('Please enter an integer.')


# add a new product
def add_products():
    import re  # splitting a string based on a pattern

    while True:
        # strip() removes leading and trailing whitespace to avoid error
        product_id = input('Enter Product ID: ').strip()

        if (len(product_id) != 5 or
                not product_id[0] == 'S' or
                not product_id[1:].isdigit()):
            print("ERROR: Invalid Product ID")
        else:
            break  # break the loop if Product ID is entered correctly

    while True:
        product_name = input('Enter Product Name: ').strip()

        if not product_name.strip():
            print('ERROR: Please enter a valid product name.')
        else:
            break  # break the loop if Product Name is entered correctly

    description = input('Enter Description: ').strip()

    while True:
        stock = input('Enter Stock: ').strip()

        if not stock.isdigit():
            print('ERROR: Please enter an integer.')
        else:
            break  # break the loop if Stock is entered correctly

    while True:
        price = input('Enter Price (RM): ').strip()

        try:  # convert to float and format to two decimal places
            price = f'{float(price):.2f}'
            break  # break the loop if Price is entered correctly
        except ValueError as e:
            print(e)
            print('ERROR: Please enter a valid number for price.')

    try:
        with open("products.txt", "r") as f:
            # start reading from the second line as the first line is header
            content = f.readlines()[1:]
    except IOError as e:
        print(e)
        print('Cannot read from file!')

    # check if the product already exists in the file
    product_exists = False
    for lines in content:
        # split each line into a list when there are two or more spaces
        product_info = re.split(r'\s{2,}', lines.strip())

        if product_info[0] == product_id:
            product_exists = True  # product exists
            break

    if product_exists:
        print('The product already exists.')
    else:  # convert the new data entered into a list
        product_list = []
        product_list.append((product_id, product_name, description,
                             stock, price))

        try:
            with open("products.txt", "a") as f:
                for i in product_list:  # format and write the product details
                    f.write("{:<13} {:<15} {:<20} {:<8} {:<15}\n".format(*i))
        except IOError as e:
            print(e)
            print('Cannot write to file!')
        print('Product added successfully!')


# update product details
def update_products():
    import re  # splitting a string based on a pattern

    while True:
        product_id = input('Enter the Product ID to update: ').strip()

        if (len(product_id) != 5 or
                not product_id[0] == 'S' or
                not product_id[1:].isdigit()):
            print("ERROR: Invalid Product ID")
        else:
            break  # break the loop if Product ID is entered correctly

    try:
        with open("products.txt", "r") as f:
            content = f.readlines()  # reads all lines from the file
    except IOError as e:
        print(e)
        print('Cannot read from file!')

    updated_info = []  # store updated data
    product_exists = False  # check if the product exists

    for lines in content:
        product_info = re.split(r'\s{2,}', lines.strip())

        if product_info[0] == product_id:
            product_exists = True  # product exists
            print('Product found.')

            while True:
                new_name = input('Enter new Product Name: ').strip()
                if not new_name.strip():
                    print('ERROR: Please enter a valid product name.')
                else:
                    break

            new_description = input('Enter Description: ').strip()

            while True:
                new_stock = input('Enter new Stock: ').strip()
                if not new_stock.isdigit():
                    print('ERROR: Please enter an integer.')
                else:
                    break

            while True:
                new_price = input('Enter new Price (RM): ').strip()
                try:
                    new_price = f'{float(new_price):.2f}'
                    break
                except ValueError as e:
                    print(e)
                    print('ERROR: Please enter a valid number for price.')

            # append the updated product info as a list of strings
            updated_info.append([product_id, new_name, new_description,
                                 new_stock, new_price])

        else:
            # append the unchanged product info as a list of strings
            updated_info.append(product_info)

    if not product_exists:  # product does not exists
        print('ERROR: Product not found.')
        return

    # write the updated product info back to the file
    try:
        with open("products.txt", "w") as f:
            for i in updated_info:
                f.write("{:<13} {:<15} {:<20} {:<8} {:<15}\n".format(*i))
            print('Product details updated successfully!')
    except IOError as e:
        print(e)
        print('Cannot write to file!')


# add a new supplier
def add_suppliers():
    import re  # splitting a string based on a pattern

    while True:
        # strip() removes leading and trailing whitespace to avoid error
        supplier_id = input('Enter Supplier ID: ').strip()

        if (len(supplier_id) != 5 or
                not supplier_id[0] == 'P' or
                not supplier_id[1:].isdigit()):
            print("ERROR: Invalid Supplier ID")
        else:
            break  # break the loop if Supplier ID is entered correctly

    while True:
        supplier_name = input('Enter Supplier Name: ').strip()

        if not supplier_name.strip():
            print('ERROR: Please enter a supplier name.')
        else:
            break  # break the loop if Supplier Name is entered correctly

    while True:
        supplier_contact = input('Enter Supplier Contact Details: ').strip()

        if (not supplier_contact.isdigit() or
            not supplier_contact.startswith('01') or
                len(supplier_contact) >= 11):
            print('Phone number must start with "01" and up to 11 digits.')
        else:
            break  # break the loop if Contact Details are entered correctly

    try:
        with open("suppliers.txt", "r") as f:
            content = f.readlines()[1:]  # start reading from the second line
    except IOError as e:
        print(e)
        print('Cannot read from file!')

    # check if the supplier already exists in the file
    supplier_exists = False
    for lines in content:
        # split each line into a list when there are two or more spaces
        supplier_info = re.split(r'\s{2,}', lines.strip())

        if supplier_info[0] == supplier_id:
            supplier_exists = True
            break

    if supplier_exists:
        print('The supplier already exists.')
    else:  # convert the new data entered into a list
        supplier_list = []
        supplier_list.append((supplier_id, supplier_name, supplier_contact))

        try:
            with open("suppliers.txt", "a") as f:
                for i in supplier_list:  # format and write the supplier info
                    f.write("{:<13} {:<15} {:<8}\n".format(*i))
        except IOError as e:
            print(e)
            print('Cannot write to file!')
        print('Supplier added successfully!')


# place an order
def place_orders():
    from datetime import datetime  # format the date
    import re  # splitting a string based on a pattern

    while True:
        # strip() removes leading and trailing whitespace to avoid error
        order_id = input('Enter Order ID: ').strip()

        if (len(order_id) != 5 or
                not order_id[0] == 'R' or
                not order_id[1:].isdigit()):
            print("ERROR: Invalid Order ID")
        else:
            break  # break the loop if Order ID is entered correctly

    while True:
        product_id = input('Enter the Product ID to order: ').strip()

        if (len(product_id) != 5 or
                not product_id[0] == 'S' or
                not product_id[1:].isdigit()):
            print("ERROR: Invalid Product ID")
        else:
            break  # break the loop if Product ID is entered correctly

    while True:
        quantity = input('Enter Quantity: ').strip()

        if not quantity.isdigit():
            print('ERROR: Please enter an integer.')
        else:
            break  # break the loop if Quantity is entered correctly

    while True:
        order_date = input('Enter Order Date (YYYY-MM-DD): ').strip()

        try:
            datetime.strptime(order_date, "%Y-%m-%d")
            break  # break the loop if Order Date is entered correctly
        except ValueError as e:
            print(e)
            print('Order Date must be in YYYY-MM-DD format')

    # read the products file
    try:
        with open("products.txt", "r") as f:
            content = f.readlines()[1:]  # start reading from the second line
    except IOError as e:
        print(e)
        print('Cannot read from file!')

    # check if the product to order exists in the products file
    product_exists = False
    for lines in content:
        # split each line into a list when there are two or more spaces
        product_info = re.split(r'\s{2,}', lines.strip())

        if product_info[0] == product_id:
            product_exists = True  # product exists
            break

    if product_exists:  # convert the order info entered into a list
        order_list = []
        order_list.append((order_id, product_id, quantity, order_date))

        try:
            with open("orders.txt", "a") as f:
                for i in order_list:  # format and write the order details
                    f.write("{:<11} {:<12} {:<11} {:<8}\n".format(*i))
        except IOError as e:
            print(e)
            print('Cannot write to file!')
        print('Order placed successfully!')

    else:
        print('ERROR: Product does not exist.')


# view inventory
def view_inventory():
    try:
        with open('products.txt', 'r') as f:
            content = f.readlines()

            for lines in content:
                print(lines.strip())
    except IOError as e:
        print(e)
        print('Cannot read from file!')


# generate reports
def generate_reports():
    while True:
        print('----------------------------\n'
              '     Generating Reports     \n'
              '----------------------------\n'
              '[1]  Low stock items\n'
              '[2]  Product sales\n'
              '[3]  Supplier orders\n'
              '[4]  Main Menu\n'
              '----------------------------\n')

        try:
            option = int(input('Select an Option (1-4): '))

            match option:
                case 1:
                    low_stock_report()
                case 2:
                    sales_report()
                case 3:
                    supplier_report()
                case 4:
                    return
                case _:
                    print('ERROR: Invalid Option')

        except ValueError as e:
            print(e)
            print('Please enter an integer.')


# generate low stock report
def low_stock_report():
    import re  # splitting a string based on a pattern
    low_stock_threshold = 10  # define low stock threshold
    low_stock_items = []  # store each product with low stock

    # read from products file
    try:
        with open("products.txt", "r") as f:
            # start reading from the second line as the first line is header
            content = f.readlines()[1:]
    except IOError as e:
        print(e)
        print('Cannot read from file!')

    # check for low stock items
    for lines in content:
        product_info = re.split(r'\s{2,}', lines.strip())

        if int(product_info[3]) < low_stock_threshold:
            low_stock_items.append([product_info[0], product_info[1],
                                    product_info[3]])

    # generate low stock report
    if low_stock_items:
        print('Low Stock Items Report:\n')
        print(f"{'PRODUCT_ID':<13} {'PRODUCT_NAME':<15} {'STOCK':<8}")
        for i in low_stock_items:
            print(f"{i[0]:<13} {i[1]:<15} {i[2]:<8}")
    else:
        print('No low stock items!')


# generate product sales report
def sales_report():
    import re  # splitting a string based on a pattern
    product_sales = []  # store each sold product and its data

    # read from products file
    try:
        with open("products.txt", "r") as f:
            # start reading from the second line as the first line is header
            content1 = f.readlines()[1:]
    except IOError as e:
        print(e)
        print('Cannot read from file!')

    # extract data for product ID, name, and price
    for lines1 in content1:
        product_info = re.split(r'\s{2,}', lines1.strip())
        product_sales.append({
            'product_id': product_info[0],
            'product_name': product_info[1],
            'price': float(product_info[4]),
            'quantity_sold': 0,  # initialize quantity sold
            'revenue': 0  # initialize revenue
        })

    # read from orders file
    try:
        with open("orders.txt", "r") as f:
            # start reading from the second line as the first line is header
            content2 = f.readlines()[1:]
    except IOError as e:
        print(e)
        print('Cannot read from file!')

    # extract data for quantity from order files to determine quantity sold
    for lines2 in content2:
        order_info = re.split(r'\s{2,}', lines2.strip())

        # search the product by ID and update quantity sold
        for i in product_sales:
            if order_info[1] == i['product_id']:
                i['quantity_sold'] += int(order_info[2])

    # calculate total revenue for each product
    for i in product_sales:
        i['revenue'] = i['price'] * i['quantity_sold']

    # generate product sales report
    if product_sales:
        print('Product Sales Report:\n')
        print(f"{'PRODUCT_ID':<13} {'PRODUCT_NAME':<15} "
              f"{'PRICE':<10} {'QUANTITY':<10} {'REVENUE (RM)':<8}")

        for i in product_sales:
            print(f"{i['product_id']:<13} {i['product_name']:<15} "
                  f"{i['price']:<10} {i['quantity_sold']:<10} "
                  f"{i['revenue']:<8.2f}")
    else:
        print('No products sold!')


# generate supplier report
def supplier_report():
    try:
        with open('suppliers.txt', 'r') as f:
            content = f.readlines()

            for lines in content:
                print(lines.strip())
    except IOError as e:
        print(e)
        print('Cannot read from file!')


# call the main menu function
main_menu()
