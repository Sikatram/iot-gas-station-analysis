import csv
from datetime import datetime


class Methods:

    def greaterThanASecond(csv_file_name):

        print("Devices greater than a second: \n")
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            i = 0
            j = 0
            for line in csv_reader:
                if i != 0:
                    date_1 = str(line[1]).strip()
                    date_2 = str(line[2]).strip()
                    date_format_str = '%Y-%m-%d %H:%M:%S'
                    start = datetime.strptime(date_1, date_format_str)
                    end = datetime.strptime(date_2, date_format_str)
                    diff = end - start

                    seconds = int(diff.total_seconds())

                    if seconds >= 1:
                        j = j + 1

                        if str(line[0]) == "N/A":
                            print("Device " + str(i))

                        else:
                            print(str(line[0]))

                i = i + 1

            percentage = j/i * 100
            print(j)
            print(i)
            print("\n" + str(round(percentage, 1)) +
                  "% of devices were a second or more")

    def greaterThanThirtySeconds(csv_file_name):

        print("Devices greater than thirty seconds: \n")
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            i = 0
            j = 0
            for line in csv_reader:
                if i != 0:
                    date_1 = str(line[1]).strip()
                    date_2 = str(line[2]).strip()
                    date_format_str = '%Y-%m-%d %H:%M:%S'
                    start = datetime.strptime(date_1, date_format_str)
                    end = datetime.strptime(date_2, date_format_str)
                    diff = end - start

                    seconds = int(diff.total_seconds())

                    if seconds >= 30:
                        j = j + 1

                        if str(line[0]) == "N/A":
                            print("Device " + str(i))

                        else:
                            print(str(line[0]))

                i = i + 1

            percentage = j/i * 100
            print("\n" + str(round(percentage, 1)) +
                  "% of devices were a thirty seconds or more")

    def greaterThanAMinute(csv_file_name):

        print("Devices greater than a minute: \n")
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            i = 0
            j = 0
            for line in csv_reader:
                if i != 0:
                    date_1 = str(line[1]).strip()
                    date_2 = str(line[2]).strip()
                    date_format_str = '%Y-%m-%d %H:%M:%S'
                    start = datetime.strptime(date_1, date_format_str)
                    end = datetime.strptime(date_2, date_format_str)
                    diff = end - start

                    seconds = int(diff.total_seconds())

                    if seconds >= 60:
                        j = j + 1

                        if str(line[0]) == "N/A":
                            print("Device " + str(i))

                        else:
                            print(str(line[0]))

                i = i + 1

            percentage = j/i * 100
            print("\n" + str(round(percentage, 1)) +
                  "% of devices were a minute or more")

    def greaterThanFifteenMinutes(csv_file_name):

        print("Devices greater than fifteen minutes: \n")
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            i = 0
            j = 0
            for line in csv_reader:
                if i != 0:
                    date_1 = str(line[1]).strip()
                    date_2 = str(line[2]).strip()
                    date_format_str = '%Y-%m-%d %H:%M:%S'
                    start = datetime.strptime(date_1, date_format_str)
                    end = datetime.strptime(date_2, date_format_str)
                    diff = end - start

                    seconds = int(diff.total_seconds())

                    if seconds >= 900:
                        j = j + 1

                        if str(line[0]) == "N/A":
                            print("Device " + str(i))

                        else:
                            print(str(line[0]))

                i = i + 1

            percentage = j/i * 100
            print("\n" + str(round(percentage, 1)) +
                  "% of devices were fifteen minutes or more")

            print("Total Number of Devices Detected: " + str(i))
