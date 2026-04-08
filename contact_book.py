# contact_book.py - Contact Book Application
# Store, view, search, update, and delete contacts using a dictionary.

# ── Data Storage ───────────────────────────────────────────────────────────────

# contacts is a dict keyed by lowercase name for easy lookup.
# Each value is another dict with the contact's details.
# Example: {"alice": {"name": "Alice", "phone": "...", "email": "...", "address": "..."}}
contacts = {}


# ── Display Helper ─────────────────────────────────────────────────────────────

def print_contact(contact):
    """Print a single contact's details in a neat format."""
    print("  " + "-" * 38)
    print(f"  Name    : {contact['name']}")
    print(f"  Phone   : {contact['phone']}")
    print(f"  Email   : {contact['email']}")
    print(f"  Address : {contact['address']}")
    print("  " + "-" * 38)


# ── Operations ─────────────────────────────────────────────────────────────────

def add_contact():
    """Add a new contact after collecting all required details."""
    print("\n[ Add New Contact ]")

    name = input("  Name    : ").strip()
    if not name:
        print("  Error: Name cannot be empty.")
        return

    key = name.lower()
    if key in contacts:
        print(f"  Error: A contact named '{name}' already exists.")
        return

    phone   = input("  Phone   : ").strip()
    email   = input("  Email   : ").strip()
    address = input("  Address : ").strip()

    contacts[key] = {
        "name":    name,
        "phone":   phone,
        "email":   email,
        "address": address,
    }
    print(f"\n  Contact '{name}' added successfully.")


def view_contacts():
    """Display all saved contacts."""
    print("\n[ All Contacts ]")

    if not contacts:
        print("  No contacts saved yet.")
        return

    print(f"  {len(contacts)} contact(s) found:\n")
    for contact in contacts.values():
        print_contact(contact)


def search_contact():
    """Search for a contact by name or phone number (partial match)."""
    print("\n[ Search Contact ]")

    query = input("  Enter name or phone to search: ").strip().lower()
    if not query:
        print("  Error: Search term cannot be empty.")
        return

    # Collect all contacts where name or phone contains the query string
    results = [
        c for c in contacts.values()
        if query in c["name"].lower() or query in c["phone"].lower()
    ]

    if not results:
        print(f"  No contacts found matching '{query}'.")
    else:
        print(f"\n  {len(results)} result(s) found:")
        for contact in results:
            print_contact(contact)


def update_contact():
    """Update one or more fields of an existing contact."""
    print("\n[ Update Contact ]")

    name = input("  Enter the name of the contact to update: ").strip()
    key  = name.lower()

    if key not in contacts:
        print(f"  Error: No contact named '{name}' found.")
        return

    contact = contacts[key]
    print("\n  Leave a field blank to keep the current value.")
    print_contact(contact)

    # For each field, only update if the user typed something new
    new_name    = input(f"  New Name    [{contact['name']}]   : ").strip()
    new_phone   = input(f"  New Phone   [{contact['phone']}]  : ").strip()
    new_email   = input(f"  New Email   [{contact['email']}]  : ").strip()
    new_address = input(f"  New Address [{contact['address']}]: ").strip()

    # Handle name change — requires updating the dict key too
    if new_name and new_name.lower() != key:
        new_key = new_name.lower()
        if new_key in contacts:
            print(f"  Error: A contact named '{new_name}' already exists.")
            return
        contact["name"] = new_name
        contacts[new_key] = contacts.pop(key)   # move to new key
    elif new_name:
        contact["name"] = new_name

    if new_phone:   contact["phone"]   = new_phone
    if new_email:   contact["email"]   = new_email
    if new_address: contact["address"] = new_address

    print(f"\n  Contact updated successfully.")


def delete_contact():
    """Delete a contact by name after confirmation."""
    print("\n[ Delete Contact ]")

    name = input("  Enter the name of the contact to delete: ").strip()
    key  = name.lower()

    if key not in contacts:
        print(f"  Error: No contact named '{name}' found.")
        return

    confirm = input(f"  Are you sure you want to delete '{contacts[key]['name']}'? (yes/no): ").strip().lower()
    if confirm in {"yes", "y"}:
        del contacts[key]
        print(f"  Contact '{name}' deleted successfully.")
    else:
        print("  Deletion cancelled.")


# ── Menu ───────────────────────────────────────────────────────────────────────

def show_menu():
    """Print the main menu options."""
    print("\n" + "=" * 42)
    print("          Contact Book — Main Menu")
    print("=" * 42)
    print("  1. Add a new contact")
    print("  2. View all contacts")
    print("  3. Search for a contact")
    print("  4. Update a contact")
    print("  5. Delete a contact")
    print("  6. Exit")
    print("=" * 42)


# ── Main Loop ──────────────────────────────────────────────────────────────────

def main():
    print("=" * 42)
    print("       Welcome to your Contact Book")
    print("=" * 42)

    # Map menu choices to their functions
    actions = {
        "1": add_contact,
        "2": view_contacts,
        "3": search_contact,
        "4": update_contact,
        "5": delete_contact,
    }

    while True:
        show_menu()
        choice = input("  Choose an option (1-6): ").strip()

        if choice == "6":
            print("\n  Goodbye! Your contacts are saved for this session.")
            break
        elif choice in actions:
            actions[choice]()        # call the matching function
        else:
            print(f"  '{choice}' is not a valid option. Please choose 1-6.")


# ── Entry Point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
