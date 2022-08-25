
dictContact = {

# Using Dictionary
# Names, addresses and phone numbers are only fictitious used for example, if any are the same it's coincidence.

        'mayasulistia'  :   {'No.':'001',
                            'Category':'Mantan Pacar',
                            'Nama':'Maya Sulistia',
                            'Address':'Jln. Bumi Permai no 10',
                            'Phone':'0856090919'},

        'diniamarta'    :   {'No.':'002',
                            'Category':'Mantan Pacar',
                            'Nama':'Dini Amarta',
                            'Address':'Jln. Terang Dona no 11',
                            'Phone':'0852193319'},


        'donisugiarto'  :   {'No.':'004',
                            'Category':'Teman Kampus',
                            'Nama':'Doni Sugiarto',
                            'Address':'Jln. Palem Indah no 99',
                            'Phone':'0856075419'},


        'ibranrahmat'   :   {'No.':'004',
                            'Category':'Teman Kampus',
                            'Nama':'Ibran Rahmat',
                            'Address':'Jln. Kuat Terang no 109',
                            'Phone':'0856123416'},


        'merinhartono'  :   {'No.':'005',
                            'Category':'Mantan Pacar',
                            'Nama':'Merin Hartono',
                            'Address':'Jln. Harapan Puyol  no 32',
                            'Phone':'0878087919'},


        'udinsubagio'   :   {'No.':'006',
                            'Category':'Teman Kantor',
                            'Nama':'Udin Subagio',
                            'Address':'Jln. Tanah Indah no 221',
                            'Phone':'0813033919'}
   
   
    }


def default_contact():
    if len(dictContact) == 0:
        print('Contact not Found')
    else:
        print('='*83)
        print(' ' *30+'CONTACT LIST')
        print('='*83)
        print('No. \t|Category \t|Nama  \t\t|Address  \t\t\t|Phone')
        for key in dictContact.keys():
            print('{} \t|{} \t|{} \t|{} \t|{}\t'.format(dictContact[key]['No.'],dictContact[key]['Category'],dictContact[key]['Nama'],dictContact[key]['Address'],dictContact[key]['Phone']))

def view_contact():
    while len(dictContact) == 0:
        print('Contact not Found')
        break
    else:
        while True:
            pilih_menu = int(input('=====CONTACT MENU===== \n1. View by Category\n2. View All Contacts\n3. Search by Name\n4. Back to Main Menu\n Choose Menu Number: '))
            if pilih_menu == 1:
                pilih_category = int(input('=====CATEGORY LIST=====\n1. Mantan Pacar\n2. Teman Kampus\n3. Teman Kantor\n4. Back to Main Menu\n Choose Category: '))
                if pilih_category == 1:
                    print('='*83)
                    print(' ' *30+'MANTAN PACAR')
                    print('='*83)
                    print('No. \t|Category \t|Nama  \t\t|Address  \t\t\t|Phone')
                    for key in dictContact.keys():
                        if dictContact[key]['Category'] == 'Mantan Pacar':
                            print('{} \t|{} \t|{} \t|{} \t|{}\t'.format(dictContact[key]['No.'],dictContact[key]['Category'],dictContact[key]['Nama'],dictContact[key]['Address'],dictContact[key]['Phone']))
                        else:
                            continue
                elif pilih_category == 2:
                    print('='*83)
                    print(' ' *30+'TEMAN KAMPUS')
                    print('='*83)
                    print('No. \t|Category \t|Nama \t\t\t|Address \t\t|Phone')
                    for key in dictContact.keys():
                        if dictContact[key]['Category'] == 'Teman Kampus':
                            print('{} \t|{} \t|{} \t|{} \t|{}\t'.format(dictContact[key]['No.'],dictContact[key]['Category'],dictContact[key]['Nama'],dictContact[key]['Address'],dictContact[key]['Phone']))
                        else:
                            continue
                elif pilih_category == 3:
                    print('='*83)
                    print(' ' *30+'MANTAN KANTOR')
                    print('='*83)
                    print('No. \t|Category \t|Nama \t\t\t|Address \t\t|Phone')
                    for key in dictContact.keys():
                        if dictContact[key]['Category'] == 'Teman Kantor':
                            print('{} \t|{} \t|{} \t|{} \t|{}\t'.format(dictContact[key]['No.'],dictContact[key]['Category'],dictContact[key]['Nama'],dictContact[key]['Address'],dictContact[key]['Phone']))
                        else:
                            continue
                elif pilih_category == 4:
                    break
                else:
                    print('Sector not Found')
            elif pilih_menu == 2:
                default_contact()
            elif pilih_menu == 3:
                search = input("Search Contact Name: ")
                print('No. \t|Category \t|Nama \t\t\t|Address \t\t|Phone')
                for key in dictContact.keys():
                    if search.lower() in dictContact[key]["Nama"].lower():
                        print('{} \t|{} \t|{} \t|{} \t|{}'.format(dictContact[key]["No."],dictContact[key]["Category"],dictContact[key]["Nama"],dictContact[key]["Address"],dictContact[key]["Phone"]))
                    else:
                        continue
            elif pilih_menu == 4:
                break
            else:
                print('Menu not Found')  

            

def add_contact():
    while True:
        default_contact()
        input_nama = input('Enter name: ')
        new_name_input = input_nama.replace(' ','')
        if new_name_input.lower() not in dictContact.keys():
            print('Please fill in the new contact information')
            input_new_name = input('Enter Name: ')
            input_noid = input('Enter No.: ')
            input_category = input('Enter Category: ')
            input_address = input('Enter Address: ')
            input_phone = input('Enter Phone: ')
            confirm11 = input(f'Are you sure you want to add this all information = {input_new_name},{input_noid},{input_category},{input_address},{input_phone} Yes/No: ')
            if confirm11 != 'Yes':
                print('Contact is cancel to add')
                break
            else:
                dictContact[new_name_input.lower()]={'No.' : input_noid, 'Category': input_category,'Nama': input_new_name,'Address': input_address,'Phone': input_phone}
                default_contact()
                print('Contact added to list')
                break
        else:
            print('Contact Name already listed')
            break

def update_contact():
    update_contact = int(input('=====CONTACT UPDATE=====\n1. Update by Name\n2. Back to Main Menu\nEnter menu number: '))
    if update_contact == 1: 
        default_contact()
        update_contact = input('Enter name to update: ')
        new_update = update_contact.replace(' ','')
        while new_update.lower() in dictContact.keys():
            pilih_update = int(input('=====UPDATE CONTACT INFORMATION===== \nWhat would you like to update? :\n1. Nama\n2. No.\n3. Category\n4. Address\n5. Phone\n6. Back to Main Menu\nEnter number: '))
            if pilih_update == 1:    
                update_name = input('Enter new name: ')
                new_name_update = update_name.replace(' ','')
                while new_name_update.lower() in dictContact.keys():
                    print('Name already exist')
                    update_name = input('Enter new name: ')
                    new_name_update = update_name.replace(' ','')
                confirm12= input('Are you sure want update? Yes/No: ')
                if confirm12 != 'Yes':
                    break
                else:
                    dictContact[new_name_update] = dictContact[new_update.lower()]
                    del dictContact[new_update.lower()]
                    dictContact[new_name_update]['Nama'] = update_name
                    default_contact()
                    print('Name updated')
                    break
            elif pilih_update == 2:
                new_noid_update = input('Enter new id number: ')
                confirm13= input('Are you sure want update? Yes/No: ')
                if confirm13 != 'Yes':
                    break
                else:
                    dictContact[new_update.lower()]['No.'] = new_noid_update
                    default_contact()
                    print('No. updated')
                    break
            elif pilih_update == 3:
                new_category_update = input('Enter new category: ')
                confirm14= input('Are you sure want update? Yes/No: ')
                if confirm14 != 'Yes':
                    break
                else:
                    dictContact[new_update.lower()]['Category'] = new_category_update
                    default_contact()
                    print('Category updated')
                    break
            elif pilih_update == 4:
                new_address_update = input('Enter new address: ')
                confirm15= input('Are you sure want update? Yes/No: ')
                if confirm15 != 'Yes':
                    break
                else:
                    dictContact[new_update.lower()]['Address'] = new_address_update
                    default_contact()
                    print('Address updated')
                    break   
            elif pilih_update == 5:
                new_phone_update = input('Enter new id number: ')
                confirm16= input('Are you sure want update? Yes/No: ')
                if confirm16 != 'Yes':
                    break
                else:
                    dictContact[new_update.lower()]['Phone'] = new_phone_update
                    default_contact()
                    print('Phone updated')
                    break
            else:
                break
        else:
            print('Contact name doesnt exist')
     
def delete_contact():
    default_contact()
    delete_contact = input('Enter contact name you want to delete: ')
    new_delete_contact = delete_contact.replace(' ','')
    while new_delete_contact.lower() not in dictContact.keys():
        print('Contact not Found')
        break
    else:
        check6 = input(f'Are you sure want to delete {delete_contact} ? Yes/No: ')
        while check6 != 'Yes':
            print('Contact not deleted')
            break
        else:
            del dictContact[new_delete_contact.lower()]
            default_contact()
            print('Contact deleted')



while True:
    pilih_menu = int(input('''
    MAIN MENU:
    1. View contacts
    2. Add a contact
    3. Update contact
    4. Delete contact
    0. Exit program
    
    Please enter menu number: '''))

    if pilih_menu == 1:
        view_contact()
    elif pilih_menu == 2:
        add_contact()
    elif pilih_menu == 3:
        update_contact()
    elif pilih_menu == 4:
        delete_contact()
    elif pilih_menu == 0:
        quit()
    else:
        print('Menu not Found')