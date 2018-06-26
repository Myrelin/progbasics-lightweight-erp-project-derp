# Do not modify this file
# run this program (the ERP software) from the terminal from thd root directory of this project


import sys
import ui  # User Interface
# Store module
from store import store
# Human Resources module
from hr import hr
# Tool manager module
from inventory import inventory
# Accounting module
from accounting import accounting
# Sales module
from sales import sales
# Customer Relationship Management (CRM) module
from crm import crm


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        store.start_module()
    elif option == "2":
        hr.start_module()
    elif option == "3":
        inventory.start_module()
    elif option == "4":
        accounting.start_module()
    elif option == "5":
        sales.start_module()
    elif option == "6":
        crm.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["(1) Store manager ",
               "(2) Human resources manager ",
               "(3) Inventory manager ",
               "(4) Accounting manager ",
               "(5) Sales manager ",
               "(6) Customer Relationship Management (CRM)"]

    ui.print_menu("Main menu ", options, "\nExit program\n")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()
