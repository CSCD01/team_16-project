import matplotlib.text as txt
import matplotlib.pyplot as plt
import numpy as np


def test_kwargs_order():
    '''
    The issue was that setting Text properties and then setting the fontproperties
    would overwrite the original Text properties. For example,
    plt.xlabel("value", fontproperties='SimHei',size=20) <- This would set size correctly
    plt.ylabel("counts",size=20, fontproperties='SimHei') <- This would not
    
    These tests ensure that this issue was fixed
    '''
    
    #General case
    text = txt.Text(size=20, fontproperties="SimHei") 
    assert text.get_size() == 20
    
    #Data for tests
    data = np.random.randn(10000)
    plt.hist(data, bins=40, facecolor="blue", edgecolor="black", alpha=0.5)
    
    #Case from bug report
    fp_first = plt.xlabel("value", fontproperties='SimHei',size=20)
    size_first = plt.ylabel("counts",size=20, fontproperties='SimHei')
    assert fp_first.get_size() == 20
    assert size_first.get_size() == 20
    
    #Test with multiple properties
    original = plt.xlabel("value", fontproperties="Comic Sans MS", weight="bold", size=16)
    changed = plt.xlabel("value", weight="bold", size=16, fontproperties="Comic Sans MS")
    assert original.get_size() == changed.get_size() 
    assert original.get_weight() == changed.get_weight()
    assert original.get_fontproperties() == changed.get_fontproperties()
      
    #Test on text update
    text = txt.Text()
    kwargs = {"fontproperties": "Times New Roman", "size": 30, "weight": "bold"}
    text.update(kwargs)
    assert text.get_size() == 30
    assert text.get_weight() == "bold"
    
    #Acceptance Test
    plt.xlabel("value", fontproperties='SimHei',size=20, style="italic")
    plt.ylabel("counts",size=20, style="italic", fontproperties='SimHei')
    plt.title("Test Graph", weight="bold", size=30, fontproperties="DejaVu Sans")
    plt.show()

if __name__== "__main__":
    test_kwargs_order()
    print ("All tests passed")
