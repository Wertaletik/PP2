import csv
from connect import get_connection

def insert_contact(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(
            "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Contact added.")
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    
    cur.close()
    conn.close()


def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()
    
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                cur.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
            except:
                print(f"Skipped duplicate: {row}")
    
    conn.commit()
    cur.close()
    conn.close()
    print("CSV import completed.")


def query_contacts(filter_type=None, value=None):
    conn = get_connection()
    cur = conn.cursor()
    
    if filter_type == "name":
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", ('%' + value + '%',))
    elif filter_type == "phone":
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (value + '%',))
    else:
        cur.execute("SELECT * FROM contacts")
    
    rows = cur.fetchall()
    if not rows:
        print("No contacts found")
        return
    
    space1=max(len(str(row[0])) for row in rows)
    space2=max(len(row[1]) for row in rows)
    for row in rows:
        space11=space1-len(str(row[0]))
        space22=space2-len(row[1])
        print(f"ID: {row[0]}"+ " "*space11 +
              f" | Name: {row[1]}"+ " "*space22 +
              f" | Phone: {row[2]}"
            )
    
    cur.close()
    conn.close()


def update_contact(old_value, new_name=None, new_phone=None):
    conn = get_connection()
    cur = conn.cursor()
    
    if new_name:
        cur.execute(
            "UPDATE contacts SET name=%s WHERE name=%s OR phone=%s",
            (new_name, old_value, old_value)
        )
    
    if new_phone:
        cur.execute(
            "UPDATE contacts SET phone=%s WHERE name=%s OR phone=%s",
            (new_phone, old_value, old_value)
        )
    
    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated.")


def delete_contact(value):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute(
        "DELETE FROM contacts WHERE name=%s OR phone=%s",
        (value, value)
    )
    
    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted.")


def menu():
    while True:
        print("\n1. Add contact")
        print("2. Import from CSV")
        print("3. Show all contacts")
        print("4. Search")
        print("5. Update")
        print("6. Delete")
        print("0. Exit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)
        
        elif choice == "2":
            insert_from_csv(r"C:\Study\PP2\practice7\contacts.csv")
        
        elif choice == "3":
            query_contacts()
        
        elif choice == "4":
            f = input("Filter (name/phone): ")
            v = input("Value: ")
            query_contacts(f, v)
        
        elif choice == "5":
            old = input("Enter name or phone to update: ")
            new_name = input("New name (or Enter to skip): ")
            new_phone = input("New phone (or Enter to skip): ")
            
            update_contact(old,
                           new_name if new_name else None,
                           new_phone if new_phone else None)
        
        elif choice == "6":
            value = input("Enter name or phone to delete: ")
            delete_contact(value)
        
        elif choice == "0":
            break


if __name__ == "__main__":
    menu()