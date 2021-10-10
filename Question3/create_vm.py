"""
file:           create_vm.py
created:        07/10/2021 11:57
author:         ciaran mcdevitt
version:        v1.0.0
licensing:      (c) 2021 Ciaran McDevitt, LYIT
                available under the GNU Public License (GPL)
description:
credits:

"""
import random
import time


class VirtualMachine:
    """
    Class to create new VirtualMachine objects

    Parameters required:
    argument1 (str): unique_name
    argument1 (str): created_date
    argument1 (str): requester
    argument1 (str): shutdown_date
    argument1 (str): operating_system
    argument1 (str): required_ram
    argument1 (str): storage_capacity
    """
    def __init__(self, unique_name, created_date, requester, shutdown_date,
                 operating_system, required_ram, storage_capacity):
        self.unique_name = unique_name
        self.created_date = created_date
        self.requester = requester
        self.shutdown_date = shutdown_date
        self.operating_system = operating_system
        self.required_ram = required_ram
        self.storage_capacity = storage_capacity

    def print_vm_details(self):
        """
        Method to print a newly generated VM's details

        Output:
        Neat table featuring all the values passed when the VM was created

        """
        print(f"---------------------------------------\n"
              f" ~New VM: {self.unique_name} created~\n"
              f"---------------------------------------\n"
              f"Owner:            {self.requester}\n"
              f"Creation date:    {self.created_date}\n"
              f"Operating System: {self.operating_system}\n"
              f"RAM:              {self.required_ram}\n"
              f"Storage:          {self.storage_capacity}\n"
              f"Shutdown date:    {self.shutdown_date}\n\n")


def get_operating_system():
    """
    Method to offer a user a choice of 1 of three available operating systems,
    Linux, Windows or MacOs.  Bad input is handle so that a user cannot proceed until they have
    made a valid selection

    :return:
    :argument (str) operating system
    """
    operating_system = ""
    os_choice_not_made_yet = True
    while os_choice_not_made_yet:
        choice = input("Press (1) Linux\n      (2) Windows\n      (3) MacOS\n")
        if choice in ("1", "2", "3"):
            if choice == "1":
                operating_system = "Linux"
                os_choice_not_made_yet = False
            elif choice == "2":
                operating_system = "Windows"
                os_choice_not_made_yet = False
            else:
                operating_system = "MacOS"
                os_choice_not_made_yet = False
        else:
            print("Please check your input\n")

    return operating_system


def get_ram_details():
    """
    Method to allow a user a choice the required RAM for the VM,
    Input is validated the closest possible RAM size above what they need.
    Any request for above 32gb are given the max RAM size of 32gb
    Bad input is handled so that a user cannot proceed until they have
    made a valid selection

    :return:
    :argument (str) ram_size (the value of the required RAM for the new VM)
    """
    ram = ""
    not_valid_ram_details = True
    while not_valid_ram_details:
        ram_size = input("Please select the amount of RAM required (32gb is the largest available)\n")
        ram_size = ram_size.upper()
        ram_size.replace("GB", "")
        if ram_size.isdigit():
            ram_size = int(ram_size)
            not_valid_ram_details = False
            if ram_size > 32:
                ram = "32gb"
                print(f"* Assigning {ram} of RAM as it's the largest amount available\n")
            elif ram_size > 16:
                ram = "32gb"
                print(f"* Bumping you up to {ram} of RAM\n")
            elif 16 > ram_size > 8:
                ram = "16gb"
                print(f"* Bumping you up to {ram} of RAM\n")
            elif 8 > ram_size > 4:
                ram = "8gb"
                print(f"* Bumping you up to {ram} of RAM\n")
            elif 4 > ram_size > 2:
                ram = "4gb"
                print(f"* Bumping you up to {ram} of RAM\n")
            elif 2 > ram_size > 1:
                ram = "2gb"
                print(f"* Bumping you up to {ram} of RAM\n")
            else:
                ram = "1gb"
                print(f"Assigning you the default {ram} of RAM\n")
        else:
            print("Please enter RAM size in format: 32gb, 16gb\n")

    return ram


def get_storage_capacity():
    """
    Method to allow a user to choose the required storage needed for the VM,
    Users must select from a range of options in a printed menu.
    Bad input is handled so that a user cannot proceed until they have
    made a valid selection

    :return:
    :argument (str) storage_capacity (the amount of storage required for the new VM)
    """
    storage_capacity = ""
    not_valid_storage_capacity = True

    while not_valid_storage_capacity:
        choice = input("How much storage does your VM need?\n"
                       "(1)\t\t1gb\n"
                       "(2)\t\t2gb\n"
                       "(3)\t\t5gb\n"
                       "(4)\t\t10gb\n"
                       "(5)\t\t20gb\n"
                       "(6)\t\t60gb\n"
                       "(7)\t\t120gb\n"
                       "(8)\t\t240gb\n"
                       "(9)\t\t480gb\n\n")

        if choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            not_valid_storage_capacity = False
            if choice == "1":
                storage_capacity = "1gb"
            elif choice == "2":
                storage_capacity = "2gb"
            elif choice == "3":
                storage_capacity = "5gb"
            elif choice == "4":
                storage_capacity = "10gb"
            elif choice == "5":
                storage_capacity = "20gb"
            elif choice == "6":
                storage_capacity = "60gb"
            elif choice == "7":
                storage_capacity = "120gb"
            elif choice == "8":
                storage_capacity = "240gb"
            elif choice == "9":
                storage_capacity = "480gb"
        else:
            print("Please check your input, invalid selection made\n")

    return storage_capacity


def create_unique_vm_name():
    """
    Method to generate a unique name for the VM

    :return:
    :argument (str) unique_name (a unique name is generated at random)
    """
    unique_num = random.randint(1, 10000)
    unique_name = f"vm_{unique_num}"
    return unique_name


def create_new_vm():
    """
    Method to gather the required information to create

    :return:
    :argument (str) ram_size (the value of the required RAM for the new VM)
    """
    print("Please complete this questionnaire so we can get your VM provisioned...\n")
    unique_name = create_unique_vm_name()
    requester_name = input("What is your full name?\n")
    created_date = input("When do you need the VM?\n")
    shutdown_date = input('When can we shut down the VM again?\n')
    operating_system = get_operating_system()
    required_ram = get_ram_details()
    storage_capacity = get_storage_capacity()

    name = create_unique_vm_name()
    name = VirtualMachine(unique_name=unique_name,  created_date=created_date, requester=requester_name,
                          shutdown_date=shutdown_date, operating_system=operating_system,
                          required_ram=required_ram, storage_capacity=storage_capacity)

    return name


if __name__ == '__main__':
    '''
    Main method of application
    
    Linear programming only presented here demo of lists

    Parameters:
    None    
    '''

    while True:
        create_a_new_vm = input("\nDo you wish to create a new VM? (y / any other key)\n")
        if create_a_new_vm.upper() == "Y":
            new_vm = create_new_vm()
        else:
            print("Goodbye...")
            time.sleep(5)
            exit()
        new_vm.print_vm_details()
