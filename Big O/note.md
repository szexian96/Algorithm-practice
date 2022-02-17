# 6.Big O (Algorithm)

## Analogy

- Small file: use email, ftp
- Large file: 1TB( it can took maybe 1 day)　 ⇒ take flight?
- how much faster to transfer a file with physical transfer or electronic transfer

## Time Complexity

Concept of asymptotic runtime aka big O time

### Electronics Transfer O(s)

- the time to transfer the file increase linearly with size

### Airplane Transfer O(1)

- size of file increase but it won't take any longer to get the file to your friend
- time is constant

<img src="https://miro.medium.com/max/1200/1*yiyfZodqXNwMouC0-B0Wlg.png" width="400"/>

※O(1)=Airplane Transfer O(1) Electronics Transfer O(s)

### Multiple runtimes

- O(log N)
- O(N log N)
- O(N)
- O($N^2$)
- O($2^N$)
- no fixed possible runtime
  - Time to paint a fence $w$ meter wide $h$ meters high
    - O($wh$)
  - $p$ layers of paint
    - Time = O($whp$)

### Best Case, Worse Case and Expected Case

Describe our runtime for an algorithm in 3 different ways

・ Perspective of Quick Sort

1. Quick Sort picks a random element as a pivot
2. Swaps value in the array that element less that pivot or greater than pivot => Partial sort
3. Recursively sort left and right using similar process.

- Best Case

  - all elements are equal
  - quick sort will on average traverse the array once
  - $O(N)$ :run very quickly on a sorted array

- Worst Case

  - pivot is the biggest element in the array
  - pivot is the first element in subarray
  - array is sorted in reverse order
  - recursion cannot divide the array in half and recurse on each half
  - shrinks the subarray by 1 element
  - $O(N^2)$ runtime

- Expected Case
  - pivot will be very low or very high, but it won't happen over and over
  - $O(N log N)$ runtime

## Space Complexity

- the amount of memory or space required by an algorithm
- parallel concept to time complexity
  - create an array of size n, this will require O(n)space
  - 2D array of size nxn, require $O(N^2)$ space.

Code like this would take $O(n)$ time and $O(n)$ space

[CODE HERE](stackSpace.py)

Each call is added to the call stack and take up actually memory

```
sum(4)
	-> sum(3)
		-> sum(2)
			-> sum(1)
				->sum(0)
```

n calls total doesnot mean it take $O(n)$ space<br>
Below function, which adds adjacent elements between 0 and n(把 0 和 n 加起來):

[CODE HERE](pairSumSequence.py)

$O(n)$ calls to pairSum. call does not exist simultaneously on the call stack so only need $O(1)$ space.

## Drop The Constant

- possible for o(N)code to run faster that O(1) / specific inputs
- Big O describe rate of increase
- $O(2N)$ = $O(N)$??
- Big O allow us to express how the runtime scales.
- $O(N)$ not always better that $O(N^2)$

1. $O(N)$ for loop (min and max)
   [CODE HERE](minmaxV1.py)
2. $O(N^2)$ 2 for loop (min and max) (HERE WIN)
   [CODE HERE](minmaxV2.py)

## Drop the Non-Dominant Terms

- 丢掉那些没用的