import PointGenerator

def PassingTest_List():
    assert PointGenerator(2,[[0,0,0],[1,1,1]]) == {'0':[0,0,0],'1':[1,1,1]}
    
def PassingTest_ListSquare():
    assert PointGenerator(2,[[0,0,0],[0,1,0],[1,0,0],[1,1,0]]) == PointGenerator(4,'square')

def PassingTest_Line():
    assert PointGenerator(2,'line') == {'0':[0,0,0],'1':[0,0,1]}
    
def PassingTest_Square():
    assert PointGenerator(4,'square') == {'0':[0,0,0],'1':[0,1,0],'2':[1,0,0],'3':[1,1,0]}

def FailingTest_ListDim():
    try:
        PointGenerator(2,[[0,0,0],[1,1]])
        assert False
    except TypeError:
        assert True

def FailingTest_UndefInit():
    try:
        PointGenerator(2,'undef')
        assert False
    except SyntaxError:
        assert True
