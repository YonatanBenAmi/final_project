from listener_to_topic import listen_kafka

class DivisionData:

    def get_list_data(self)->list:
        print("listening...")
        all_metadata = listen_kafka()
        print("OK: The information is extracted.")
        list_all_data = []
        try:
            for message in all_metadata:
                print("Enter")
                print(message.value)
                list_all_data.append(message.value)
            print("No")
            return list_all_data
        except KeyboardInterrupt:
            print("stopt thre lesenir")

    
    def get_metadata_parts(self, all_data: list)->list:
        my_list = []
        for message in all_data:
            a = message.pop("Path", None)
            print(a)
            my_list.append(message)
        return my_list

            
