from connect import get_connection


def call_search(pattern):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM search_contacts(%s::TEXT)",
        (pattern,)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def call_pagination(limit, offset):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s::INT, %s::INT)",
        (limit, offset)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def call_upsert(name, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL upsert_contact(%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


def call_delete(value):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL delete_contact_proc(%s)",
        (value,)
    )

    conn.commit()
    cur.close()
    conn.close()


def call_bulk_insert():
    conn = get_connection()
    cur = conn.cursor()

    names = ["Alice", "Bob", "Charlie"]
    phones = ["12345", "abc", "987654"]

    # ВАЖНО: без третьего аргумента
    cur.execute(
        "CALL bulk_insert_contacts(%s, %s)",
        (names, phones)
    )

    conn.commit()
    cur.close()
    conn.close()


def menu():
    while True:
        print("\n1. Search")
        print("2. Pagination")
        print("3. Upsert")
        print("4. Delete")
        print("5. Bulk insert")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            p = input("Pattern: ")
            call_search(p)

        elif choice == "2":
            lim = int(input("Limit: "))
            off = int(input("Offset: "))
            call_pagination(lim, off)

        elif choice == "3":
            name = input("Name: ")
            phone = input("Phone: ")
            call_upsert(name, phone)

        elif choice == "4":
            val = input("Name or phone: ")
            call_delete(val)

        elif choice == "5":
            call_bulk_insert()

        elif choice == "0":
            break


if __name__ == "__main__":
    menu()