# Quick Sort

`ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left`

Array Example:
```[8,4,23,42,16,15]```
 <br><br>
 Pass 1:
 - Original:
 | 8 | 4 | 23 | 16 | 15 |<br>
 |---|---|----|----|----|<br>
 | 0 | 1 | 2  | 3  | 4  |
<br><br>
- After pass:
 | 4 | 8 |      23 | 16 | 15 |<br>
 |---|---|     ----|----|----|<br>
 | 0 | 1 |      0  | 1  | 2  |  
<br><br><br><br>
 Pass 2:
- Original:
 | 4 | 8 |      23 | 16 | 15 |<br>
 |---|---|     ----|----|----|<br>
 | 0 | 1 |      0  | 1  | 2  |  
<br><br>
- After pass:
 | 4 |      8 |      23 | 16 | 15 |<br>
 |---|     ---|     ----|----|----|<br>
 | 0 |      0 |      0  | 1  | 2  |  
<br><br><br><br>
 Pass 3:
- Original:
 | 4 |      8 |      23 | 16 | 15 |<br>
 |---|     ---|     ----|----|----|<br>
 | 0 |      0 |      0  | 1  | 2  |  
<br><br>
- After pass: Marges the 1st split back in sorted order 
 | 4 | 8 |      23 | 16 | 15 |<br>
 |---|---|     ----|----|----|<br>
 | 0 | 1 |      0  | 1  | 2  |  
<br><br><br><br>
 Pass 4:
- Original:
 | 4 | 8 |      23 | 16 | 15 |<br>
 |---|---|     ----|----|----|<br>
 | 0 | 1 |      0  | 1  | 2  |  
<br><br>
- After pass:
 | 4 | 8 |      23 |      16 | 15 |<br>
 |---|---|     ----|     ----|----|<br>
 | 0 | 1 |      0  |      0  | 1  |  

  <br><br><br><br>
  
Pass 5:
- Original:
 | 4 | 8 |      23 |      16 | 15 |<br>
 |---|---|     ----|     ----|----|<br>
 | 0 | 1 |      0  |      0  | 1  |    
<br><br>
- After pass:
 | 4 | 8 |      23 |      16 |      15 |<br>
 |---|---|     ----|     ----|     ----|<br>
 | 0 | 1 |      0  |      0  |      0  |  

Pass 6:
- Original:
 | 4 | 8 |      23 |      16 |      15 |<br>
 |---|---|     ----|     ----|     ----|<br>
 | 0 | 1 |      0  |      0  |      0  |  
<br><br>
- After pass:
 | 4 | 8 |      16 | 23 |      15 |<br>
 |---|---|     ----|----|     ----|<br>
 | 0 | 1 |      0  | 1  |      0  |  

Pass 7:
- Original:
 | 4 | 8 |      16 | 23 |      15 |<br>
 |---|---|     ----|----|     ----|<br>
 | 0 | 1 |      0  | 1  |      0  |  
<br><br>
- After pass:
 | 4 | 8 |      15 | 16 | 23 |<br>
 |---|---|     ----|----|----|<br>
 | 0 | 1 |      0  | 1  | 2  |  

Pass 8
- Original:
 | 4 | 8 |      16 | 23 |      15 |<br>
 |---|---|     ----|----|     ----|<br>
 | 0 | 1 |      0  | 1  |      0  |  
<br><br>
- After pass:
 | 4 | 8 | 15 | 16 | 23 |<br>
 |---|---|----|----|----|<br>
 | 0 | 1 | 2  | 3  | 4  |