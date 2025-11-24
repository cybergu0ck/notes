# Debian package managers

<br>
<br>
<br>

## Apt

<br>
<br>

### Update and upgrade

```bash
sudo apt update
```

```bash
sudo apt upgrade
```

<br>
<br>

### Installing a package

```bash
sudo apt install <package>
```

<br>

#### Installing a deb file

1. Give execute permission

	```bash
	chmod +x ./<debfile.deb>
	```

1. Install the deb file. Ensure `./` is used explicitly.

	```bash
	sudo apt install ./<debfile.deb>
	```


<br>
<br>

### Uninstalling a package

* Remove the package

	```bash
	sudo apt remove <package>
	```

* Purge the program to remove program related files.

	```bash
	sudo apt purge <package_name>
	```

- Remove Orphaned Dependencies

	```bash
	sudo apt autoremove
	```

- Delete user configuration (if any)

	```bash
	rm -rf ~/.config/<package_name>
	rm -rf ~/.cache/<package_name>
	rm -rf ~/.local/share/<package_name>
	```


<br>
<br>

