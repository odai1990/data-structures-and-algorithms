from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import AnimalShelter,Cat,Dog

def test_version():
    assert __version__ == '0.1.0'


def test_adding_to_shelter():
    '''
    testing enqueue is working fine
    '''
    shelter=AnimalShelter()
    cat1=Cat('jojo')
    assert shelter.enqueue(cat1)!="You can't add other animal than dogs or cats"

def test_adding_to_shelter_multi_dogs_and_cats():
    '''
    testing enqueue is working fine with adding multi dogs and cats opjects
    '''
    shelter=AnimalShelter()
    cat1=Cat('smoor')
    cat2=Cat('tota')
    dog1=Dog('toto')
    dog2=Dog('smer')
    assert shelter.enqueue(cat1)!="You can't add other animal than dogs or cats"
    assert shelter.enqueue(cat2)!="You can't add other animal than dogs or cats"
    assert shelter.enqueue(dog1)!="You can't add other animal than dogs or cats"
    assert shelter.enqueue(dog2)!="You can't add other animal than dogs or cats"

def test_dequeue_from_shelter_dog_or_cat():
    '''
    testing dequeue is handel remove and return dogs or cats objects
    '''
    shelter=AnimalShelter()
    cat1=Cat('smoor')
    dog1=Dog('toto')
    cat2=Cat('tota')    
    dog2=Dog('smer')
    shelter.enqueue(cat1)
    shelter.enqueue(dog1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog2)
    assert isinstance(shelter.dequeue('dog'), Dog)  
    assert shelter.dequeue('cat') != None     
    assert isinstance(shelter.dequeue('cat'), Cat) 
    assert isinstance(shelter.dequeue('dog'), Dog)


def test_dequeue_from_shelter_another_animal():
    '''
    testing dequeue is handel returning another animal
    '''
    shelter=AnimalShelter()
    cat1=Cat('smoor')
    dog1=Dog('toto')
    cat2=Cat('tota')    
    dog2=Dog('smer')
    shelter.dequeue('hamster')
    assert shelter.dequeue('hamster') == None     
 