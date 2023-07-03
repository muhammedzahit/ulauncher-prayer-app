import os

def create_city_folders():
    with open('sorted_cities.txt', 'r') as f:
        line = f.readline()
        while line != "":
            city, value = line.split(':')[0].strip(), line.split(':')[1].strip()

            current_file_path = os.path.abspath(__file__)
            print("Current file Path", current_file_path)
            parent_file_path = os.path.dirname(current_file_path)
            print("Parent path", parent_file_path) 

            os.makedirs(parent_file_path + "/cities/" + city + "/", exist_ok=True)
            with open("./cities/" + city + "/" + "value.txt", "w") as file:
                file.write(value)

            line = f.readline()

#create_city_folders()