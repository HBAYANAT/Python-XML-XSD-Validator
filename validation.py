import xmlschema
import logging
import datetime
import sys

# Sys. Argv[0] returns the PY file name you are running & the others 1 2 ...  are what you add as arguments after the command that runs the Py app
xml_file_path = sys.argv[1]
xsd_file_path = sys.argv[2]


schema = xmlschema.XMLSchema(xsd_file_path)

try:
    schema.validate(xml_file_path)
    print("XML File Validation Success")  # display OK

except xmlschema.XMLSchemaValidationError as error:
    # I log the error in the file log.txt, this is an appending method to keep all data in
    logging.basicConfig(filename="log.txt", level=logging.DEBUG)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("{0} Validation error: {1}".format(now, error))
    # format the error code saved in the logs are similar to the one displayed on the console output.
    logging.debug("{0} Validation error: {1}".format(now, error))
