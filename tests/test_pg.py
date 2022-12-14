import sys
sys.path.insert(1, 'src/simcode')
from point_generator import point_generator

def test_PassingTest_List():
    assert point_generator(2,[[0,0,0],[1,1,1]]) == {'0':[0,0,0],'1':[1,1,1]}
    
def test_PassingTest_ListSquare():
    assert point_generator(2,[[0,0,0],[0,1,0],[1,0,0],[1,1,0]]) == point_generator(4,'square')

def test_PassingTest_Line():
    assert point_generator(2,'line') == {'0':[0,0,0],'1':[0,0,1]}
    
def test_PassingTest_Square():
    assert point_generator(4,'square') == {'0':[0,0,0],'1':[0,1,0],'2':[1,0,0],'3':[1,1,0]}

def test_FailingTest_ListDim():
    try:
        point_generator(2,[[0,0,0],[1,1]])
        assert False
    except TypeError:
        assert True

def test_FailingTest_UndefInit():
    try:
        point_generator(2,'undef')
        assert False
    except TypeError:
        assert True
