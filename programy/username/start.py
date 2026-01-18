import app
import check
import sys

fixedUsername = app.sanitise(sys.argv[1])

print("uzytkownik: {} czyli jest {}".format(fixedUsername, check.isValid(fixedUsername)))