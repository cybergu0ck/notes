# Sorted Sets

- Sorted set is an ordered collection of unique members.
- they are good for priority queues, low latency leaderboards and secondary indexing.
- they keep the score for all the members from the start.

<br>
<br>
<br>

# Creating a Sorted Set

### `zadd`

- The syntax for zadd is as follows

  ```
  zadd key [NX|XX] [GL|LT] [CH] [INCR] score member [score member ...]
  ```

- In this example, we are creating a sorted sets for avengers with starting score as 0.
  ```cmd
  zadd strongest_avenger 0 "hulk" 0 "ironman" 0 "captain america" 0 "thor"
  ```

<br>
<br>
<br>

# Updating a Sorted Set

### `zincrby`

- The syntax for zincrby is as follows:

  ```
  zincrby key increment member
  ```

- Here, we increment the score for hulk by 20.
  ```cmd
  zincrby strongest_avenger 20 "hulk"
  ```
- If we want to decrement the score, we must use negative value with the zincrby command.

<br>
<br>
<br>

# Reading a Sorted Set

### `zrange`

- zrange shows the set from highest score to lowest score. [official docs](https://redis.io/commands/zrange/)
- The syntax for zrange is

  ```
  ZRANGE key start stop [BYSCORE | BYLEX] [REV] [LIMIT offset count] [WITHSCORES]
  ```

* Here, we want to list top 2 (hence the start and stop is 0 and 1) along with the score values and score values being highest to lowest (hence the REV).

  ```cmd
  zrange strongest_avenger 0  1 REV WITHSCORES

   1)"hulk"
   2) "20"
   3) "thor"
   4) "0"
  ```

<br>

### `zrank`

- The syntax for zrank is as follows:
  ```
  zrank key member
  ```
  <br>

### `zrevrank`

- The syntax for zrevrank is as follows:

  ```
  zrevrank key member
  ```

  <br>

### `zscore`

- The syntax for zscore is as follows:
  ```
  zscore
  ```

<br>
<br>
<br>
