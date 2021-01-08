import dropbox
class uploadmyfiles:
    def __init__(self,dbxtoken):
        self.dbxtoken = dbxtoken
    def uploadFile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.dbxtoken)
        file = open(file_from,'rb')
        dbx.files_upload(file.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
def main():
    token = 'sl.Ao_1knHyXwOWoB7-JFCi8vsEUY1nqnRGLyL0-KdLQ21gXcfTzIl2gx6sI9Y09GulkKRhL9OsqMlliBh_gcdIM3kMY0U95NOhusIvvJaSyebrptc9oCYEG1JG-X-BwVD1KdOm954'
    td = uploadmyfiles(token)   
    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the full path to upload to the dropbox: ")
    td.uploadFile(file_from,file_to)
    print('file has Uploaded to your server storage')
main()