class AndroidWunderlistTestBase:
    # class attribute
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'LLD-AL10',
                    'appPackage': 'com.wunderkinder.wunderlistandroid'}
    # Since the app is already installed launching it using package and activity name
