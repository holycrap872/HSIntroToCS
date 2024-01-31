# Python Recursion Worksheet

Instructions:
1.	Log into Grok
2.	Go to https://groklearning.com/learn/python-turtle-playground/1/0/
3.	Read the directions for each task very carefully before you begin working on it.
4.	Every time the directions say "take a screenshot" of something, do it and then copy it into the proper space _in this document_.

---

## Problem 1

First, we’re going to experiment with the shape produced by the `shape_one()`
function.

### Predict

1. How is `shape_one()` recursive?
   ```
   
   
   ```
2. Sketch your best guess of what will happen for a call to `shape_one()` that
   results in no levels of recursion (aka, the base case):
   ```
   

   

   ```
3. Sketch your best guess of what will happen for a call to `shape_one()` that
   results in one level of recursion:
   ```



   
   ```
4. Based on your sketches, what do you think `shape_one()` is creating?
   ```

   ```

### Run

1. Sketch the result that comes from running `shape_one()`:
   ```




   ```

### Investigate

1. What is the role of each parameter in the `shape_one()` function? How do
   they influence the shape that is output?
   ```


   ```
2. How does the number of levels of recursion affect the shape? What happens
   as you increase or decrease the levels?
   ```


   ```
3. How is the size of each branch determined relative to its parent branch?
   What would happen if you change the scaling factor?
   ```


   ```

### Modify

1. Alter the code so there are only right angle turns. Run the code and then sketch
   the result:
   ```




   ```
2. Alter the code so that there is a third (recursive) call to `shape_one()`
   within each recursion level. Make sure that the result is symmetrical. Run
   the code and then sketch the result:
   ```




   ```
3. Alter the code so that the base case draws a small circle. Run the code and
   then sketch the result:
   ```




   ```

## Shape Two

Now, we’re going to experiment with the shape produced by the `shape_two()`
function. Make sure that `shape_one()` is commented out and `shape_two()` is
uncommented.

### Predict

1. How is `shape_two()` recursive?
   ```


   ```
2. Sketch your best guess of what will happen for a call to `shape_two()` that
   results in no levels of recursion (aka, the base case):
   ```




   ```
3. Sketch your best guess of what will happen for a call to `shape_two()` that
   results in one level of recursion:
   ```



 
   ```
4. Based on your sketches, what do you think `shape_two()` is creating?
   ```

 
   ```

### Run

1. Sketch the result that comes from running `shape_two()`:
   ```




   ```

### Investigate

1. Analyze how the function uses division (`/`). What is the rule for
   division, and how does it create the resulting shape?
   ```


   ```
2. How does the base case determine the most detailed level of the shape?
   ```


   ```

### Modify

1. Add code so that the resulting shape is a closed circle/figure. Run the code
   and then sketch the result:
    ```





    ```
2. Alter the code so there only right angle turns. Run the code and then sketch
   the result:
    ```





    ```

## Shape Three

Now it's your turn to `make`. In the space below, sketch a self-similar pattern.
Then, create a function called `shape_three()` to try and recreate it via a
turtle.