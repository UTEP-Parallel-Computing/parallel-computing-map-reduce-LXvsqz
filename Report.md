Map Reduce Lab Report

During this lab assignment I had many more problems than I did in the matrix multiply lab. One of the biggest issues I had was figuring out what it was that I should parallelize. I started the lab by creating a serial version then went step by step to parallelize it. For a couple of hours, I could not figure out to make each thread grab a file, and when using iterate each thread would simply traverse to the end of the array of files and would count occurrences for file 8 (8 times). These results were not accurate, and I used the serial version to compare accuracy of results. Eventually I was able to get each thread to grab its own file and from there I was able to add the number of occurrences to a shared dictionary. When adding to the shared dictionary I made sure to lock the dictionary until the thread was done with it so that a race condition would not occur. Another big problem was the way I timed each program. Since each thread was responsible for doing some function for its own file, I am unsure if my timing is right for time it took to “load” each file. The overall time is right as I used the same ideology as I did in the matrix multiply. I don’t think this is a bug though I thought it was something I should mention. The assignment took me a solid 6 hours to complete. A lot of this time was simply trial and error when trying to parallel various parts of the serial version. Eventually I concluded that the best solution for me would be to iterate over files. Listed below are the timing results I gathered:

•	1 Thread:
o	Overall Time: 19.2691s
o	Average Time reading 1 file: 2.4042s
•	2 Threads:
o	Overall Time: 18.5675s
o	Average Time reading 1 file: 2.0645s
•	4 Threads:
o	Overall Time: 12.7006s
o	Average Time reading 1 file: 1.2594s
•	8 Threads:
o	Overall Time: 11.4954s
o	Average Time reading 1 file: .115658


These are the times I believe Dr. Pruitt told me to list for my results via email. Though the jump is not as clear as in the matrix multiply, we can see a gradual decline in time the more threads that we add. Though our machine is limited, if each thread can handle their own file and gather occurrences at the same time as other threads, we will see a decline in time. The jump may not be big because at the end of the day we are adding to the same shared dictionary so each thread must wait for the lock to release before it can access the dictionary. Since this would cause a race condition, I do not believe there is a way around it and therefore performance may be slower than expected.

One comment I had on the lab was Is perhaps having a larger data size would show a greater jump in performance times (for the better). I did consider having 2 shared dictionaries though I did not trust that the parallel sections would act in the way I thought they would. This is a question I will be asking Mr. Pruitt. 

CPU INFORMATION
model name      : Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz
      4      36     216
 
