
  

# Configuration
---

#### Setting up username and password :
---
```bash
git config --global user.name "your user name"
```

```shell
git config --global user.email "your email id"
```

#### Checking :
---
```bash
git config --global user.name
```

```shell
git config --global user.email
```
  
  

# Pushing Local Repo to Remote Repo
---

#### 1. Creating a Local Repo
---
```bash
git init -b main
```

 
#### 2. Staging all modfications and commiting
---
```bash
git add . && git commit -m "first commit"
```


#### 3. Create a Remote Repo on github and get the remote URL
---
```bash
git remote add origin <REMOTE_URL>    # Sets the new remote

git remote -v # Verifies the new remote URL
```


#### 4. Push it to the remote repo
---
```bash
git branch -M main

git push -u origin main
```