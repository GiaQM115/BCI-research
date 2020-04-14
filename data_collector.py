import requests as req
import os

if __name__ == "__main__":
    url_root = "https://archive.physionet.org/pn4/eegmmidb/"

    # get list of records
    res = req.get(url_root + "RECORDS")
    records = res.text.split()
    cwd = os.getcwd()
    print("Files will be saved to " + cwd + "/data")
    open(cwd + "/data/records", 'w+').write(res.text)
    failed = []

    # get each record
    for record in records:
        print("Attempting to retrieve " + record)
        res = req.get(url_root + record)
        if res.status_code != 200:
            failed.append(record)
        else:
            # if new subject, mkdir
            subject = record[0:4]
            if subject not in os.listdir(cwd + "/data/"):
                os.mkdir(cwd + "/data/" + subject[0:5])

            # write binary to file
            open(cwd + "/data/" + record, 'wb').write(res.content)

    print("All record downloads attempted")
    print("Failed downloads:")
    print(failed)

