
from view import View as view
from db_manager import PhoneBook

pb = PhoneBook()

def start():
    while True:
        choise = view.menu()
        match choise:
            case 1:
                if pb.file_not_opened() and not pb.comparison():
                    pb.open_file()
                    view.action_status(choise)
                else:
                    view.action_status(choise-1)
                    if view.confirmation(choise):
                        pb.open_file()
                        view.action_status(choise)
            case 2:
                if pb.comparison():
                    pb.save_file()
                    view.action_status(choise)
                else:
                    view.no_changes()
            case 3:
                get_pb = pb.get()
                answer = pb.file_not_opened()
                if answer:
                    view.file_not_opened(answer)
                else:
                    view.contact_list(get_pb)
            case 4:
                get_pb = pb.get()
                answer = pb.file_not_opened()
                if answer:
                    view.file_not_opened(answer)
                else:
                    view.search_phone_number(get_pb)
            case 5:
                new = view.new_contact_input()
                pb.add(new)
                view.action_status(choise)
            case 6:
                get_pb = pb.get()
                answer = pb.file_not_opened()
                if answer:
                    view.file_not_opened(answer)
                else:
                    view.search_phone_number(get_pb)
                    ind = view.contact_id()
                    new = view.new_contact_input()
                    pb.change_contact(ind, new)
                    view.action_status(choise)
            case 7:
                get_pb = pb.get()
                answer = pb.file_not_opened()
                if answer:
                    view.file_not_opened(answer)
                else:
                    view.search_phone_number(get_pb)
                    ind = view.contact_id()
                    if view.confirmation(choise):
                        pb.delete_contact()
                        view.action_status(choise)
            case 8:
                if pb.comparison():
                    view.file_not_saved()
                    if view.confirmation(choise):
                        view.goodbye()
                        break
                else:
                    view.goodbye()
                    break