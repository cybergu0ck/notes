# Introduction

- Redis is an open-source in-memory data structure store that can be used as a database, cache, and message broker.

- Redis is designed to be fast, efficient, and scalable, making it a popular choice for high-performance applications.


<br/>
<br/>

# Redis rudimentary commands

| Operation | Syntax | Example | 
|----------|----------|----|
| select a db | `select <db>` | `select 1` |
| set a key:value | `set <key> <value>` | `set name sally` |
| get the value for a key | `get <key>` | `get name` |
| flush current db entirely | `flushdb` |

<br/>
<br/>


# Strings

| Operation | Syntax | Example | 
|----------|----------|----|
| Get length of a key's value |  `strlen <key>`  | |
| Get the specified value of range | `getrange <key> <start> <end>` | |
| Append to key's value | `append <key> <value>` | |
| Increment by 1 integer value of a key | `incr <key>` | |
| Increment by specific value for a integer value of a key | `incrby <key><value>` | |



<br/>
<br/>

# Hashes

- hashes are like strings. The important difference is that they provide an extra level of indirection: a field.


    | Operation | Syntax | Example | 
    |----------|----------|----|
    | Set a field and value for a key|  `hset <key> <field> <value>` |  `hset user:goku power 999`  |
    | Set multiple fields and values | `hmset <key> <field> <value> [<field> <value>...]` | `hmset user:goku race saiyan age 737` | 
    | Get value for a field of a key | `hget <key> <field>` | | 
    | Get values for multiple fields of a key | `hmget <key> <field> [<field>...]` | | 
    | List all the fields of a key | `hkeys <key>` | |
    | delete a specific field of a key | `hdel <field>` | |


<br/>
<br/>

# Lists

- Lists let you store and manipulate an array of values for a given key.
- Lists maintain their order and have efficient index-based operations.

    | Operation | Syntax | Example | 
    |----------|----------|----|
    | push a value to a key from left-side|  `lpush <key> <value>`|    |
