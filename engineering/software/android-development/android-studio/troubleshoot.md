# Troubleshoot

## App data not getting deleted even after uninstall

While developping the app, every change in the db schema breaks the app. Unistalling and relaunching the app via Android studio should work but sometimes doesn't. Run the following command in Android Studio's terminal to delete the app’s stored data.

```bash
cd "$env:LOCALAPPDATA\Android\Sdk\platform-tools" .\adb.exe shell pm clear com.example.vyan
```
