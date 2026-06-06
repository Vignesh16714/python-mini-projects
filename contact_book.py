# ============================================
# DAY 1 — Mini Project: CLI Contact Book
# ============================================
import os

FILENAME = "contacts.txt"

# Load contacts from file
def load_contacts():
    contacts = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name},{phone}\n")

# Add a contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    if name in contacts:
        print(f"⚠️  {name} already exists!")
    else:
        contacts[name] = phone
        save_contacts(contacts)
        print(f"✅ {name} added successfully!")

# Search a contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"📞 {name}: {contacts[name]}")
    else:
        print(f"❌ {name} not found!")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️  {name} deleted successfully!")
    else:
        print(f"❌ {name} not found!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found!")
    else:
        print("\n--- 📒 All Contacts ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print("----------------------")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\n====== Contact Book ======")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")
        print("==========================")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            view_contacts(contacts)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️  Invalid option! Choose 1-5.")

main()