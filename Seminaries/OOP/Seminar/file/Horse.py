class Horse():
   is_horse = True


class Donkey():
   is_donkey = True


class Mule(Horse, Donkey):
    pass


mule = Mule()
print(mule.is_horse)
print(mule.is_donkey)
