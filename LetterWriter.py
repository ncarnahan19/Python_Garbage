print("Class (AACC):")
AnneArundel = input()
print("Class (Liberty):")
LibertyClass = input()
print("Reason class should be substituted: \"This class is a \":")
reason = input()
print("Do we have a syllabus:")
gotIt = input()

if gotIt == 'yes':
    haveASyllabus = 'a course Syllabus, '
else:
    haveASyllabus = ''


letterContents = '''Good Evening Mr. Donahoo, 
     I am requesting a substitution for my required class, ''' + LibertyClass +  '''.  The class which I am requesting count as a substitution, 
     ''' + AnneArundel +  ''' taken at Anne Arundel Community College, ''' + reason + ''' Attached is a ''' + haveASyllabus +  '''substitution request form and a course description.  Thank you for your consideration!
Best Regards,
Nicholas Carnahan
'''
print(letterContents)
print("Are you happy with the output?")
response = input()

if response.lower() == 'y':
    # Write contents to file

    fileName = LibertyClass + '_SubstitutionRequestLetter' 


    letterWordDoc = open(fileName, 'w')

    letterWordDoc.write(letterContents) 

    letterWordDoc.close()
else:
    print("End Process")

'''>>> baconFile = open('bacon.txt', 'w')
>>> baconFile.write('Hello world!\n')
13
>>> baconFile.close()
'''
