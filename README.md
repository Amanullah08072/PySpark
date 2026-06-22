# PySpark

Sort merge join shuffles BOTH tables across executors so matching keys land together. Broadcast copies the small table to every executor — the big table never moves. One entire shuffle just disappears.
