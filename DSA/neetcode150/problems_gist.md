|Title|Link/Description|Topics|TC|SC|Hints|
|---|---|---|---|---|---|
|Contains Duplicate|https://leetcode.com/problems/contains-duplicate/description/|sets|O(N)|O(N)|Initialize set - iterate thro' arr - if already in set - return|
|Valid Anagram|https://leetcode.com/problems/valid-anagram/|dictionary|O(N)|O(1)|compare dictionaries|
|Two Sum|https://leetcode.com/problems/two-sum/description/|dictionary|O(N)|O(N)|initialize dict - loop arr - validate if complement in dict - add num:index|
|Group Anagrams|https://leetcode.com/problems/group-anagrams/|dictionary,ascii char|O(N)|O(N)|initialize alphabet list - ord(char) word add list - group keys|
|Top K Frequent Elements|https://leetcode.com/problems/top-k-frequent-elements/description/|BucketSort|O(N)|O(N)|count ele freq - create [[],[]] till arr len - loop dict append to bucket - reverse loop|
|Encode and Decode Strings| Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.| |O(N)|O(N)|encode:len(word)+char+word - Decode:extract len-increment after char - move window from len to len - append output|
|Product of Array except self|https://leetcode.com/problems/product-of-array-except-self/description/|2pointers - separate run| O(N)|O(N)|fill arr left multiply - right multiply existing ans arr|
|Valid Sudoku|https://leetcode.com/problems/valid-sudoku/description/|
|Longest Consecutive Seq|https://leetcode.com/problems/longest-consecutive-sequence/description/|sets,arrays|O(N)| O(N)|prep set-if prev num not in set --> start - with every next num incre streak|
|Valid Palindrome|https://leetcode.com/problems/valid-palindrome/description/|2pointers,string manipulation|O(n)|O(1)|not alphanumeric incre/decrement pointers - compare chars|
|Two Sum 2| Input arr is sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/| two pointers|O(n)|O(1)|start pointers opp end, based on target range - incre/decre|
|Binary Search|https://leetcode.com/problems/binary-search/description/|Iterative| O(log n)|O(1)|divide arr based on mid point & target|
|Valid Parentheses|https://leetcode.com/problems/valid-parentheses/description/|dictionaries,stack|O(n)|O(n)|create parentheses dict - if char in dict - pop first ele-compare-return/append|
|Best time to buy and sell|https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/|DP,2-pointers|O(n)|O(1)|initialize maxp=0 - minbuy-first ele - calculate current profit-compare max profit - update min buy to current ele|
|3sum|https://leetcode.com/problems/3sum/description/|2-pointers(keep one static)|O(n2)|O(m) m for storing results|fix i - iterate j&k - once end of arr reached-increment i & start again - if eles same increment j,k till new ele reached|
|ContainerWithMostWater|https://leetcode.com/problems/container-with-most-water/description/|2-pointers(opp side)|O(n)|O(1)|opp side - follow formula for width,height and area calculation|
|Trapping rain water|https://leetcode.com/problems/trapping-rain-water/description/ |2pointer(opp side)|O(n)|O(1)|max left or right = compare b/w max height & current value ; total water capacity is always maximum height - current value|
|Search in 2D Matrix| https://leetcode.com/problems/search-a-2d-matrix/description/| binary search|O(log(m*n))|O(1)|calculate ele (row,col) by float div, remainder div at each step|
|Koko eating bananas|https://leetcode.com/problems/koko-eating-bananas/description/|binary search|O(n*log(max_pile))|O(1)|for every ele, take the ciel and update the hrs. based on hrs added, update pointers|
|Min ele in sorted rotated array|https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/|binary search|O(log n)|O(1)|find the sorted arr - left/right/entire arr and binary search|