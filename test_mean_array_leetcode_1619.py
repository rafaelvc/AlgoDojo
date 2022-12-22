from  mean_array_leetcode_1619 import mean_after_removing_some


def test_mean_after_removing_some():

    arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
    assert(mean_after_removing_some(arr) == 2.0)
      
    arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
    assert(mean_after_removing_some(arr) == 4.0)
      
    arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
    assert(mean_after_removing_some(arr) == 4.777777777777778)

    arr = [8, 8, 8, 7, 9]
    assert(mean_after_removing_some(arr, 20) == 8.0)
