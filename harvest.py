############
# Part 1   #
############
import sys

path = sys.argv[1] 

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
            self.code = code
            self.first_harvest = first_harvest
            self.color = color
            self.is_seedless = is_seedless
            self.is_bestseller = is_bestseller
            self.name = name

            self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    # [ <__main__.MelonType object at 0x7f11c95767b8>, 
    # <__main__.MelonType object at 0x7f11c95767f0>, 
    # <__main__.MelonType object at 0x7f11c9576828>, 
    # <__main__.MelonType object at 0x7f11c9576860> ]


    all_melon_types = []

    #Instantiation
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    #appending to a list
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, None, 'Casaba')
    cas.add_pairing('strawberry')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, None, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print("{} pairs well with".format(melon.name))

        for pair in melon.pairings:
            print("-{}".format(pair))

    #OLDER CODE
    # for i in melon_types:

    #     melon_name = (make_melon_types(melon_types)[i][5])
    #     melon_pairs = (make_melon_types(melon_types)[i][0]).pairings
    
    #     print(f'{melon_name} pairs with - {melon_pairs}')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    melon_types = make_melon_types()

    for melon in melon_types:
        #creating a dictionary
        melon_dict[melon.code] = melon

    return melon_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rtg, color_rtg, field, harvester):
        self.melon_type = melon_type
        self.shape_rtg = shape_rtg
        self.color_rtg = color_rtg
        self.field = field
        self.harvester = harvester

    def is_sellable(self):

        if self.shape_rtg > 5 and self.color_rtg > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    harvested_melons = []
    melons_by_id = make_melon_type_lookup(melon_types)

    melon1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    harvested_melons.append(melon1)

    melon2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    harvested_melons.append(melon2)

    melon3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    harvested_melons.append(melon3)

    melon4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    harvested_melons.append(melon4)

    melon5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    harvested_melons.append(melon5)

    melon6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    harvested_melons.append(melon6)

    melon7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    harvested_melons.append(melon7)

    melon8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    harvested_melons.append(melon8)

    melon9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    harvested_melons.append(melon9)

    return harvested_melons

melons = make_melons(make_melon_types())

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:

        print(f'Harvested by {melon.harvester} from field {melon.field}')

        if melon.is_sellable():
            print(f'(CAN BE SOLD)')
        else:
            print(f'(NOT SELLABLE)')


def record_new_harvest():

    harvested_melons = []
    melons_by_id = make_melon_type_lookup(make_melon_types())

    file = open(path)
    i = 0

    for line in file:

        line = line.strip().split(" ")

        shape_rtg = line[1]
        color_rtg = line[3]
        code = line[5]
        harvester = line[8]
        field = line[11]
        i += 1


        for key in melons_by_id:

            if key == code:
                harvested_melons.append(melons_by_id[key])

    
    return (harvested_melons)

















