import kyototycoon

db = kyototycoon.DB()
print dir(kyototycoon)

db.open()


db['a'] = 'assasasa'

print db['a']