Good Advice I Got From LeetCode:
A common question when first joining LeetCode is: "Where should I start?"
No two software engineers take the exact same journey. 
We all learn different skills at different times and, therefore should distribute our time and attention differently in order to maximize our studies.

------------

Time Complexity: Measures how the time to run an algorithm
Space Complexity: Measures how the memory usage of an algorithm

For any for loop:
When calculating the per iteration time complexity, we consider the operations inside the loop body.

For any while loop:
When calculating the per iteration time complexity, we consider all operations that occur within each while loop iteration, including the condition evaluation.
The condition evaluation happens every time before the loop body executes, so it contributes to the per iteration time.

O(1)
- defining a function
- initializing a variable
- adding two value

------------

Array (data structure)
Arrays are a simple **data structure** for storing lots of **similar** items. 
When we create an Array, we need to **initialize the n**, which is the number of value that the Array can hold. This is called the **capacity** which cannot be changed later.
    simple example of why we need to initialize:
    same as it is for the physical box of DVDs. Do you really want to find a box that could hold 1000000 DVDs when you currently only have 15 DVDs 
    If you make an Array with 1000000 spaces, the computer will reserve memory to hold 1000000 DVDs, even if you only put 15 DVDs into it. 

------------

when using .remove, better use i to track the index
for more details please refer to question 27

------------

**For Me To Revise Again**
498 Diagonal Traverse
941 Valid Mountain Array
1089 Duplicate Zeros Array
1299 (need to take more time to think on it)
1346 Check If N and Its Double Exist

**Very Confuse Question** will have chinese explanation
561