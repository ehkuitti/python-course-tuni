# Kuinka kopioida tekstitiedosto toiseen tekstitiedostoon Pythonilla

from_file = open("originat_file.txt", mode="r")
to_file = open("target_file.txt", mode="w")

to_file.writelines(from_file.readlines())

from_file.close()
to_file.close()
