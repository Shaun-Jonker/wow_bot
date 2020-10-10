import csv


class Writer:

    def write_to_file(self, raid_list):

        with open(f'raid_list.csv', "w", newline='', encoding="utf-8") as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in raid_list:
                writer.writerow(item)
        print(f"=====Writing to file complete=====\n")

    def append (self, raid_list):

        with open(f'raid_list.csv', "a+", newline='', encoding="utf-8") as the_file:
            csv.register_dialect("custom", delimiter=",")
            writer = csv.writer(the_file, dialect="custom")
            for item in raid_list:
                writer.writerow(item)
        print(f"=====Writing to file complete=====\n")

