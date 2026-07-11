from game import Game, items

def test_init():
    g = Game()
    assert g.room == "hallway"
    assert sum(g.prog.values()) == 0

def test_done_condition():
    g = Game()
    assert not g.done()
    
    # Fast-forward progress to max for all items
    for k in g.prog:
        g.prog[k] = len(items[k]) - 1
        
    assert g.done()
