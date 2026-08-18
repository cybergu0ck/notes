# Keys

- keys are unique
- keys are binary safe (they can be "foo", 12, 69.96, 0xff88 ) and hence keynames are case sensitive.
- Within a logical database a sigle flat key space exists.
- logical database has default "Database Zero", within a logical database keynames are unique, however they can exist same keynames in different logical databases.
- colon can be used as seperator in keynames. example : 'user:1000:followers'

<br>
<br>

# Creating Keys

### SET command

- SET command is used to set the values for keys.

  ```
  SET key value [EX seconds] [PX milliseconds] [NX | XX]
  ```

  ```cmd
  set customer:1 fred
  ```

* NX can be used to explicitely set the values for non-existing keys, If the key exists and we use NX, then the command will not SET the value for that key!

  ```
  set inventory 150 NX
  ```

- XX can be used to explicitely set the values for existing key's. Although set without XX will modify the value with the new value if the key exists.

- EX can be used to cache the value for the key, cached data are served instantly. the following key will be cached for 7200 seconds, after 7200 seconds redis will delete the key.

  ```
  SET usage:63 '{ "name": Hari, "is_cool": true}' EX 7200
  ```

<br>

### TTL command

- Using TTL command tells the expiration time for a key

  ```
  TTL key
  ```

<br>
<br>

# Getting Values

### GET command

- GET command is used to retrieve the value for the key.

  ```
  GET key
  ```

  ```cmd
  get customer:1000
  ```

<br>
<br>

# Checking if Key Exists

### EXISTS command

- To check if the key exists, EXISTS command returns 1 if key exists else returns 0.

  ```
  EXISTS key [key ...]
  ```

<br>
<br>

# Getting Keys

- There are 2 ways of getting existing key names "KEYS" and "SCAN". Their differences are listed here

  | keys                                                      | scan                                                 |
  | --------------------------------------------------------- | ---------------------------------------------------- |
  | blocks the use of database until the process is completed | iterates using a cursor and returns a slot reference |
  | Not a good idea to use in production                      | Safe for Production                                  |
  | Useful for debugging locally                              |                                                      |
  | `KEYS pattern`                                            | `SCAN slot [MATCH pattern][COUNT count]`             |

* Suppose we want to find all the customers whose id begin with a 1,

  - using keys,
    ```
    keys customer:1*
    ```
  - using scan,
    ```
    scan 0 MATCH customer:1* COUNT 1000
    ```

<br>
<br>

# Deleting Keys

- Removing keys can be done in 2 ways: DEL command and UNLINK command.

<br>

### DEL command

- using DEL command, the DEL command will remove the key and the memory associated with it. This is blocking (will block the use of database until completion)

  ```
  DEL key [key ...]
  ```

<br>

### UNLINK command

- using UNLINK command, this will unlink the key and the memory associated with it is reclaimed by an asynchronous process. THis is non-blocking command

  ```
  UNLINK key [key ...]
  ```

<br>
<br>
