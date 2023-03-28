import os
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)

    def upload_file(self, file_from, file_to):
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    self.dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode('overwrite'))

def main():
    access_token = 'access-token'
    file_from = input("Enter the path of the file to be uploaded: ")
    file_to = input("Enter the full path to upload the file to, also the desired name: ")

    transfer_data = TransferData(access_token)
    transfer_data.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
