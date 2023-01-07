
Android Studio is the official Integrated Development Environment (IDE), for Android app development built and distributed by Google. It is a specialized workshop with tools to make it easy for software developers to use to design, build, run, and test apps for the Android platform. 

Android Studio uses IntelliJ IDEA as its foundation and includes the Android plugin pre-installed along with some tweaks specifically for the Android platform, so it will feel very familiar to you.



#### Basic Workflow
---
- To create a new project, start Android Studio, click **+ Start a new Android Studio project**, name your project, choose a template, and fill in the details.
- To create an Android virtual device (an emulator) to run your app, choose **Tools > DeviceManager** and then use the[Device Manager](http://developer.android.com/tools/devices/managing-avds.html) to select a hardware device and system image.
- To run your app on a virtual device, make sure you have created a device, select the device from the toolbar dropdown menu, and then run your app by clicking the **Run** icon on the toolbar.
- To find your project files, in the **Project** window, select **Project Source Files** from the dropdown.


### Testing
---
Testing, in the context of software, is a structured method of checking your software to make sure it works correctly. Automated testing is actual code that checks to ensure that another piece of code you wrote is working correctly.

Testing software is advantageous because it lets you weed out bugs before you release your code into the wild; it's essential to a positive user experience.

While manual testing almost always has a place, testing in Android can often be automated. Throughout the Android Basics in Kotlin course, you focus on automated tests to test the app code and the functional requirements of the app itself. In this codelab, you learn the very basics of testing in Android. In later codelabs, you learn more advanced practices of testing Android apps.

As you become familiar with Android development and testing Android apps, you should make it a regular practice to write tests alongside your app code. Creating a test every time you create a new feature in your app reduces your workload later as your app grows. It also provides a convenient way for you to make sure your app works properly without spending too much time manually testing your app.