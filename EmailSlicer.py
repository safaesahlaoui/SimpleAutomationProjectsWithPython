# collect email from user
#split the email using the @ , the first part as the user name , the second one gonna be saved as domain
# split domain using . ,
def splitfun():
    print ('Welcome to the email slicer')
    print('')
    email_input=input('Input the email adress :')

    (username,domain)=email_input.split("@")
    (domain,extention)=domain.split(".")
    print('Username :',username)
    print('Domein : ',domain)
    print('Extention :',extention)

splitfun()